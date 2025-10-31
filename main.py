
import sys
import os
import socket
import threading
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget,
                               QVBoxLayout, QLabel, QPushButton, QMessageBox)
from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QPixmap, QPainter, QColor


# 通讯管理器
# class CommunicationManager:
#     """通讯管理器"""
#
#     @staticmethod
#     def bytes2int(bytes_data):
#         """字节转整数"""
#         try:
#             result = 0
#             for byte in bytes_data:
#                 result = result * 256 + int(byte)
#             return result
#         except Exception as e:
#             print(f"字节转换错误: {e}")
#             return 0
#
#     def __init__(self):
#         self.tcp_client_socket = None   # TCP socket对象
#         self.is_connected = False       # 是否已连接
#         self.receive_thread = None      # 接收数据线程
#         self.should_receive = False     # 接收控制标志是否继续运行
#
#     def connect_to_device(self, ip, port):
#         """连接到设备"""
#         try:
#             # 创建socket
#             self.tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#             # 设置超时时间
#             self.tcp_client_socket.settimeout(5)
#             # 连接设备
#             self.tcp_client_socket.connect((ip, port))
#             self.is_connected = True
#
#             # 启动数据接收线程
#             self.should_receive = True      # 允许接收线程运行
#             self.receive_thread = threading.Thread(target=self._receive_data)  # 新线程的目标函数是_receive_data
#             self.receive_thread.daemon = True  # 主程序退出时自动结束
#             self.receive_thread.start()
#
#             return True, "连接成功"
#
#         except socket.timeout:
#             return False, "连接超时"
#         except ConnectionRefusedError:
#             return False, "连接被拒绝"
#         except Exception as e:
#             return False, f"连接错误: {str(e)}"
#
#     def _receive_data(self):  # _为内部方法
#         """接收数据的线程函数"""
#         while self.should_receive and self.is_connected:
#             try:   # 循环条件：需要接收且处于连接状态
#                 recv_data = self.tcp_client_socket.recv(1024)  # 最多接收1024字节
#                 if recv_data:
#                     res_data = list(recv_data)
#                     print(f"接收到数据: {res_data}")
#
#                     # self.tcp_client_socket.send(recv_data)
#                     # 预留：回声功能
#                 else:  # 连接断开就退出
#                     self.is_connected = False
#                     break
#             except Exception as e:
#                 if self.should_receive:
#                     print(f"数据接收错误: {e}")
#                 break
#
#     def send_data(self, data):
#         """发送数据到设备"""
#         if self.is_connected and self.tcp_client_socket:
#             try:
#                 self.tcp_client_socket.send(data)
#                 return True
#             except Exception as e:
#                 print(f"发送数据错误: {e}")
#                 self.is_connected = False
#                 return False
#         return False
#
#     def disconnect(self):
#         """断开连接"""
#         self.should_receive = False
#         self.is_connected = False
#
#         if self.tcp_client_socket:
#             try:
#                 self.tcp_client_socket.close()
#             except:
#                 pass
#             self.tcp_client_socket = None


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # 初始化UI
        from uipy.mainui import Ui_MainWindow
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # 初始化变量
        self.industrial_window = None
        self.current_active_button = None

        # 初始化通讯管理器
        # self.ind_communication = CommunicationManager()  # 工业相机通讯
        # self.plc_communication = CommunicationManager()  # PLC通讯

        # 初始化界面
        self.init_ui()

        # 连接信号槽
        self.connect_signals()

    def init_ui(self):
        """初始化界面设置"""
        # 设置默认显示initialPage页面
        self.ui.stackedWidget.setCurrentIndex(0)

        # 初始化所有按钮为默认颜色
        self.reset_all_buttons_style()

        # # 初始化LED状态
        # self.update_led_status(self.ui.led1, False)
        # self.update_led_status(self.ui.led2, False)
        #
        # # 设置默认IP和端口
        # self.ui.IndIP.setText("192.168.0.10")
        # self.ui.IndPort.setText("2000")
        # self.ui.PLCIP.setText("192.168.0.11")
        # self.ui.PLCPort.setText("2000")

    def connect_signals(self):
        """连接信号和槽"""
        try:
            # 左侧按钮点击事件
            self.ui.industrialC.clicked.connect(self.open_industrial_camera)
            self.ui.hyperspectralC.clicked.connect(
                lambda: self.on_feature_button_clicked(self.ui.hyperspectralC, "高光谱相机"))
            self.ui.connect.clicked.connect(self.switch_to_connect_page)

            self.ui.F1.clicked.connect(lambda: self.on_feature_button_clicked(self.ui.F1, "F1功能"))
            self.ui.F2.clicked.connect(lambda: self.on_feature_button_clicked(self.ui.F2, "F2功能"))
            self.ui.F3.clicked.connect(lambda: self.on_feature_button_clicked(self.ui.F3, "F3功能"))

            # 通讯按钮点击
            # self.ui.IndCon.clicked.connect(self.connect_industrial_camera)
            # self.ui.InfoCon2.clicked.connect(self.connect_plc)

            # 底部控制按钮
            self.ui.Start.clicked.connect(lambda: self.show_not_implemented("启动功能"))
            self.ui.Stop.clicked.connect(lambda: self.show_not_implemented("停止功能"))
            self.ui.Pause.clicked.connect(lambda: self.show_not_implemented("暂停功能"))
            self.ui.Reset.clicked.connect(lambda: self.show_not_implemented("重置功能"))

        except Exception as e:
            print(f"信号连接错误: {e}")

    # 更新LED状态
    # def update_led_status(self, led_label, is_connected):
    #     """更新LED状态"""
    #     color = QColor(0, 255, 0) if is_connected else QColor(255, 0, 0)  # 绿色或红色
    #
    #     # 创建圆形LED
    #     pixmap = QPixmap(20, 20)
    #     pixmap.fill(Qt.transparent)
    #     painter = QPainter(pixmap)
    #     painter.setRenderHint(QPainter.Antialiasing)
    #     painter.setBrush(color)
    #     painter.setPen(Qt.NoPen)
    #     painter.drawEllipse(0, 0, 20, 20)
    #     painter.end()
    #
    #     led_label.setPixmap(pixmap)

    # 连接工业相机
    # def connect_industrial_camera(self):
    #     """连接工业相机"""
    #     try:
    #         # 获取IP和端口
    #         ip = self.ui.IndIP.text().strip()
    #         port_text = self.ui.IndPort.text().strip()
    #
    #         if not ip or not port_text:
    #             QMessageBox.warning(self, "输入错误", "请输入IP地址和端口号")
    #             return
    #
    #         try:
    #             port = int(port_text)
    #         except ValueError:
    #             QMessageBox.warning(self, "输入错误", "端口号必须是数字")
    #             return
    #
    #         # 连接设备
    #         success, message = self.ind_communication.connect_to_device(ip, port)
    #
    #         # 更新UI状态
    #         self.ui.InfoCon1.setText(message)
    #         self.update_led_status(self.ui.led1, success)
    #
    #         if success:
    #             QMessageBox.information(self, "连接成功", "工业相机连接成功！")
    #         else:
    #             QMessageBox.warning(self, "连接失败", f"工业相机连接失败: {message}")
    #
    #     except Exception as e:
    #         error_msg = f"连接过程中发生错误: {str(e)}"
    #         self.ui.InfoCon1.setText("连接错误")
    #         self.update_led_status(self.ui.led1, False)
    #         QMessageBox.critical(self, "错误", error_msg)

    # def connect_plc(self):
    #     """连接PLC"""
    #     try:
    #         # 获取IP和端口
    #         ip = self.ui.PLCIP.text().strip()
    #         port_text = self.ui.PLCPort.text().strip()
    #
    #         if not ip or not port_text:
    #             QMessageBox.warning(self, "输入错误", "请输入IP地址和端口号")
    #             return
    #         try:
    #             port = int(port_text)
    #         except ValueError:
    #             QMessageBox.warning(self, "输入错误", "端口号必须是数字")
    #             return
    #
    #         # 连接设备
    #         success, message = self.plc_communication.connect_to_device(ip, port)
    #
    #         # 更新UI状态
    #         self.ui.PLCCon.setText(message)
    #         self.update_led_status(self.ui.led2, success)
    #
    #         if success:
    #             QMessageBox.information(self, "连接成功", "PLC连接成功！")
    #         else:
    #             QMessageBox.warning(self, "连接失败", f"PLC连接失败: {message}")
    #
    #     except Exception as e:
    #         error_msg = f"连接过程中发生错误: {str(e)}"
    #         self.ui.PLCCon.setText("连接错误")
    #         self.update_led_status(self.ui.led2, False)
    #         QMessageBox.critical(self, "错误", error_msg)

    # def on_feature_button_clicked(self, button, feature_name):
    #     """功能按钮点击处理"""
    #     # 更新按钮颜色
    #     self.update_button_color(button)
    #     # 显示未实现功能提示
    #     self.show_not_implemented(feature_name)
    #
    def switch_to_connect_page(self):
        """切换到通讯页面"""
        # 更新按钮颜色
        self.update_button_color(self.ui.connect)
        # 切换到connectPage页面
        self.ui.stackedWidget.setCurrentIndex(1)
        print("切换到通讯页面")

    def update_button_color(self, clicked_button):
        """更新按钮颜色"""
        left_buttons = [
            self.ui.industrialC,
            self.ui.hyperspectralC,
            self.ui.connect,
            self.ui.F1,
            self.ui.F2,
            self.ui.F3
        ]

        # 重置所有按钮颜色
        for button in left_buttons:
            button.setStyleSheet("background-color: none;")

        # 设置点击按钮的背景色为蓝色
        clicked_button.setStyleSheet("background-color: #007bff; color: white;")
        self.current_active_button = clicked_button

    def reset_all_buttons_style(self):
        """重置所有按钮为默认颜色"""
        left_buttons = [
            self.ui.industrialC,
            self.ui.hyperspectralC,
            self.ui.connect,
            self.ui.F1,
            self.ui.F2,
            self.ui.F3
        ]

        for button in left_buttons:
            button.setStyleSheet("background-color: none;")

    def open_industrial_camera(self):
        """工业相机"""
        try:
            # 更新工业相机按钮颜色
            self.update_button_color(self.ui.industrialC)

            # 导入并创建工业相机窗口
            from modules.industrial_camera import IndustrialCameraWindow

            if self.industrial_window is None:
                self.industrial_window = IndustrialCameraWindow()
                # 连接关闭信号，以便在工业相机窗口关闭时清理引用
                self.industrial_window.close_signal.connect(self.on_industrial_window_closed)

            # 隐藏主窗口，显示工业相机窗口
            self.hide()
            self.industrial_window.show()

            print("打开工业相机窗口")

        except ImportError as e:
            print(f"工业相机模块导入失败: {e}")
            QMessageBox.critical(self, "错误", f"无法加载工业相机模块: {str(e)}")
        except Exception as e:
            print(f"打开工业相机窗口错误: {e}")
            QMessageBox.critical(self, "错误", f"打开工业相机窗口失败: {str(e)}")

    def show_not_implemented(self, feature_name):
        """显示未实现功能的消息"""
        QMessageBox.information(self, "提示", f"{feature_name}正在开发中...")

    def on_industrial_window_closed(self):
        """工业相机窗口关闭时的处理"""
        self.industrial_window = None
        self.show()  # 重新显示主窗口
        print("工业相机窗口已关闭，返回主界面")

    def closeEvent(self, event):
        """关闭事件处理"""
        try:
            # 断开所有通讯连接
            # self.ind_communication.disconnect()
            # self.plc_communication.disconnect()

            # 关闭工业相机窗口
            if self.industrial_window is not None:
                self.industrial_window.close()
        except Exception as e:
            print(f"清理过程中出现错误: {e}")

        event.accept()


def main():
    # 创建应用程序实例
    app = QApplication(sys.argv)

    # 设置应用程序信息
    app.setApplicationName("玉米种子活力检测系统")
    app.setApplicationVersion("1.0.0")

    try:
        # 创建并显示主窗口
        window = MainWindow()
        window.show()

        print("应用程序启动成功")

        # 运行应用程序
        sys.exit(app.exec())

    except Exception as e:
        print(f"应用程序启动失败: {e}")
        QMessageBox.critical(None, "启动错误", f"应用程序启动失败: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    main()