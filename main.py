import sys
import os
import socket
import threading
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget,
                               QVBoxLayout, QLabel, QPushButton, QMessageBox)
from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QPixmap, QPainter, QColor

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
        self.yolo_thread = None

        # 初始化界面
        self.init_ui()

        # 连接信号槽
        self.connect_signals()

    ###################################################################################################################
    """通用部分"""
    def init_ui(self):
        """初始化界面设置"""
        # 设置默认显示initialPage页面
        self.ui.stackedWidget.setCurrentIndex(0)

        # 初始化所有按钮为默认颜色
        self.reset_all_buttons_style()

        # 初始化LED状态
        self.update_led_status(self.ui.led1, False)
        self.update_led_status(self.ui.led2, False)

        # 设置默认IP和端口
        self.ui.IndIP.setText("192.168.0.10")
        self.ui.IndPort.setText("502")
        self.ui.PLCIP.setText("192.168.0.10")
        self.ui.PLCPort.setText("502")

    def update_led_status(self, led_label, is_connected):
        """更新LED状态"""

        color = QColor(0, 255, 0) if is_connected else QColor(255, 0, 0)  # 绿色或红色

        # 创建圆形LED
        pixmap = QPixmap(20, 20)
        pixmap.fill(QColor(0, 0, 0, 0))  # 透明背景
        painter = QPainter(pixmap)
        painter.setRenderHint(QPainter.Antialiasing, True)
        painter.setBrush(color)
        painter.setPen(Qt.NoPen)
        painter.drawEllipse(0, 0, 20, 20)
        painter.end()

        led_label.setPixmap(pixmap)

    def reset_all_buttons_style(self):
        """重置所有按钮为默认颜色"""
        left_buttons = [
            self.ui.industrialC,
            self.ui.hyperspectralC,
            self.ui.connect,
            self.ui.yoloDetection,
            self.ui.F2,
            self.ui.F3
        ]

        for button in left_buttons:
            button.setStyleSheet("background-color: none;")

    def connect_signals(self):
        """连接信号和槽"""
        try:
            # 左侧按钮点击事件
            self.ui.industrialC.clicked.connect(self.open_industrial_camera)
            self.ui.hyperspectralC.clicked.connect(
                lambda: self.on_feature_button_clicked(self.ui.hyperspectralC, "高光谱相机"))
            self.ui.connect.clicked.connect(self.switch_to_connect_page)

            self.ui.yoloDetection.clicked.connect(self.switch_to_yolo_page)
            self.ui.pushButton.clicked.connect(self.start_yolo_detection)
            self.ui.F2.clicked.connect(lambda: self.on_feature_button_clicked(self.ui.F2, "F2功能"))
            self.ui.F3.clicked.connect(lambda: self.on_feature_button_clicked(self.ui.F3, "F3功能"))

            # 通讯页面按钮
            self.ui.IndCon.clicked.connect(self.connect_industrial_tcp)  # 添加这行
            self.ui.InfoCon2.clicked.connect(self.connect_plc_tcp)  # 添加这行

            # 底部控制按钮
            self.ui.Start.clicked.connect(lambda: self.show_not_implemented("启动功能"))
            self.ui.Stop.clicked.connect(lambda: self.show_not_implemented("停止功能"))
            self.ui.Pause.clicked.connect(lambda: self.show_not_implemented("暂停功能"))
            self.ui.Reset.clicked.connect(lambda: self.show_not_implemented("重置功能"))

        except Exception as e:
            print(f"信号连接错误: {e}")

    def on_feature_button_clicked(self, button, feature_name):
        """功能按钮点击处理"""
        # 更新按钮颜色
        self.update_button_color(button)
        # 显示未实现功能提示
        self.show_not_implemented(feature_name)

    def update_button_color(self, clicked_button):
        """更新按钮颜色"""
        left_buttons = [
            self.ui.industrialC,
            self.ui.hyperspectralC,
            self.ui.connect,
            self.ui.yoloDetection,
            self.ui.F2,
            self.ui.F3
        ]

        # 重置所有按钮颜色
        for button in left_buttons:
            button.setStyleSheet("background-color: none;")

        # 设置点击按钮的背景色为蓝色
        clicked_button.setStyleSheet("background-color: #007bff; color: white;")
        self.current_active_button = clicked_button

    def show_not_implemented(self, feature_name):
        """显示未实现功能的消息"""
        QMessageBox.information(self, "提示", f"{feature_name}正在开发中...")

    ###################################################################################################################
        """工业相机"""
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

            QTimer.singleShot(10, self._show_industrial_window)

            print("打开工业相机窗口")

        except ImportError as e:
            print(f"工业相机模块导入失败: {e}")
            QMessageBox.critical(self, "错误", f"无法加载工业相机模块: {str(e)}")
        except Exception as e:
            print(f"打开工业相机窗口错误: {e}")
            QMessageBox.critical(self, "错误", f"打开工业相机窗口失败: {str(e)}")

    def _show_industrial_window(self):
        """显示工业相机窗口"""
        if self.industrial_window:
            self.hide()
            self.industrial_window.show()

    def on_industrial_window_closed(self):
        """工业相机窗口关闭时的处理"""
        self.industrial_window = None
        self.show()  # 重新显示主窗口
        print("工业相机窗口已关闭，返回主界面")

    ###################################################################################################################
    """通讯部分"""

    def switch_to_connect_page(self):
        """切换到通讯页面"""
        self.update_button_color(self.ui.connect)
        self.ui.stackedWidget.setCurrentIndex(1)
        self.init_tcp_clients()

    def init_tcp_clients(self):
        """初始化TCP客户端"""
        try:
            from modules.tcp_client import ModbusClientHandler
            # 创建工业相机Modbus客户端
            self.ind_tcp_client = ModbusClientHandler()
            # 创建PLC Modbus客户端
            self.plc_tcp_client = ModbusClientHandler()
        except ImportError as e:
            print(f"TCP客户端模块导入失败: {e}")

    def connect_industrial_tcp(self):
        """连接工业相机TCP"""
        try:
            ip = self.ui.IndIP.text().strip()
            port = int(self.ui.IndPort.text().strip())

            # 工业相机发送10个0
            write_data = [0] * 10
            success, result = self.ind_tcp_client.connect_and_communicate(ip, port, write_data)

            if success:
                self.ui.InfoCon1.setText("连接成功")
                self.update_led_status(self.ui.led1, True)
            else:
                self.ui.InfoCon1.setText("连接断开")
                self.update_led_status(self.ui.led1, False)

        except Exception as e:
            self.ui.InfoCon1.setText("连接错误")
            self.update_led_status(self.ui.led1, False)

    def connect_plc_tcp(self):
        """连接PLC TCP"""
        try:
            ip = self.ui.PLCIP.text().strip()
            port = int(self.ui.PLCPort.text().strip())

            # 获取TCP1-TCP10数据
            write_data = []
            inputs = [
                self.ui.out1, self.ui.out2, self.ui.out3, self.ui.out4, self.ui.out5,
                self.ui.out6, self.ui.out7, self.ui.out8, self.ui.out9, self.ui.out10
            ]

            for input_field in inputs:
                text = input_field.text().strip()
                if text:
                    try:
                        write_data.append(int(text))
                    except:
                        write_data.append(0)
                else:
                    write_data.append(0)

            # 连接并通信
            success, result = self.plc_tcp_client.connect_and_communicate(ip, port, write_data)

            if success:
                self.ui.PLCCon.setText("连接成功")
                self.update_led_status(self.ui.led2, True)

                self._update_in_display(result[10:20])
                self.plc_tcp_client.start_monitoring(self.on_plc_data_received)
                self._setup_out_inputs_listeners()
            else:
                self.ui.PLCCon.setText("连接断开")
                self.update_led_status(self.ui.led2, False)

        except Exception as e:
            self.ui.PLCCon.setText("连接错误")
            self.update_led_status(self.ui.led2, False)

    def _setup_out_inputs_listeners(self):
        """为OUT1-10输入框设置文本改变监听"""
        out_inputs = [
            self.ui.out1, self.ui.out2, self.ui.out3, self.ui.out4, self.ui.out5,
            self.ui.out6, self.ui.out7, self.ui.out8, self.ui.out9, self.ui.out10
        ]

        for input_field in out_inputs:
            try:
                # 使用try-except避免没有连接时的错误
                input_field.textChanged.disconnect()
            except (RuntimeError, TypeError):
                # 如果没有连接或参数不匹配，忽略错误
                pass
            # 连接文本改变信号
            input_field.textChanged.connect(self._on_out_input_changed)

    def _on_out_input_changed(self):
        """当OUT1-10任何输入框内容改变时触发"""
        if hasattr(self, 'plc_tcp_client') and self.plc_tcp_client.is_connected:
            # 延迟执行，避免频繁发送
            QTimer.singleShot(500, self._send_updated_out_data)

    def _send_updated_out_data(self):
        """发送更新后的OUT数据到PLC"""
        try:
            if not hasattr(self, 'plc_tcp_client') or not self.plc_tcp_client.is_connected:
                return

            # 获取当前的OUT1-OUT10数据
            write_data = []
            out_inputs = [
                self.ui.out1, self.ui.out2, self.ui.out3, self.ui.out4, self.ui.out5,
                self.ui.out6, self.ui.out7, self.ui.out8, self.ui.out9, self.ui.out10
            ]

            for input_field in out_inputs:
                text = input_field.text().strip()
                if text:
                    try:
                        write_data.append(int(text))
                    except:
                        write_data.append(0)
                else:
                    write_data.append(0)

            print(f"实时发送数据: {write_data}")

            # === 修改：使用新的 write_data_only 方法，不重新连接 ===
            success, result = self.plc_tcp_client.write_data_only(write_data)
            if success:
                # 更新IN1-IN10显示
                self._update_in_display(result[10:20])
                print("实时发送成功，连接保持")
            else:
                print(f"实时发送失败: {result}")

        except Exception as e:
            print(f"实时发送错误: {e}")

    def on_plc_data_received(self, data):
        """PLC数据接收 """
        try:
            print(f"接收到PLC数据: {data}")
            if len(data) >= 20:
                # 提取后10个数据（索引10-19）
                last_10_data = data[10:20]
                print(f"提取后10位数据: {last_10_data}")
                self._update_plc_display(last_10_data)
            else:
                print(f"数据长度不足20: {len(data)}")
        except Exception as e:
            print(f"数据接收回调错误: {e}")

    def _update_plc_display(self, data):
        """在主线程中更新UI"""
        try:
            self._update_in_display(data)
        except Exception as e:
            print(f"更新显示错误: {e}")

    def _update_in_display(self, in_data):
        """更新IN1-IN10显示"""
        try:
            in_inputs = [
                self.ui.in1, self.ui.in2, self.ui.in3, self.ui.in4, self.ui.in5,
                self.ui.in6, self.ui.in7, self.ui.in8, self.ui.in9, self.ui.in10
            ]

            for i, input_field in enumerate(in_inputs):
                if i < len(in_data):
                    # 设置文本但不允许用户编辑
                    input_field.setText(str(in_data[i]))
                    input_field.setReadOnly(True)  # 设置为只读，用户无法修改
        except Exception as e:
            print(f"更新IN显示错误: {e}")

    def closeEvent(self, event):
        """关闭事件处理"""
        if hasattr(self, 'ind_tcp_client'):
            self.ind_tcp_client.disconnect()
        if hasattr(self, 'plc_tcp_client'):
            self.plc_tcp_client.disconnect()
        event.accept()

    ###################################################################################################################
    """yolo"""
    def switch_to_yolo_page(self):
        """切换到YOLO检测页面"""
        # 更新按钮颜色
        self.update_button_color(self.ui.yoloDetection)
        # 切换到yoloPage页面
        self.ui.stackedWidget.setCurrentIndex(2)
        print("切换到YOLO检测页面")

    def start_yolo_detection(self):
        from modules.yolo_detection import YOLODetection
        """开始YOLO检测"""
        try:
            # 获取文件夹路径
            folder_path = self.ui.yoloEdit.text().strip()
            model_path = "models/best.pt"

            # 验证文件夹路径
            if not folder_path or not os.path.exists(folder_path):
                QMessageBox.warning(self, "路径错误", "请输入有效的文件夹路径")
                return

            # 如果已有检测线程在运行，先停止
            if self.yolo_thread and self.yolo_thread.isRunning():
                self.yolo_thread.stop_detection()
                self.yolo_thread.wait()

            # 创建并启动检测线程
            self.yolo_thread = YOLODetection(folder_path, model_path)

            # 连接信号
            self.yolo_thread.detection_finished.connect(self.on_yolo_finished)
            self.yolo_thread.log_message.connect(self.update_yolo_log)

            # 更新UI状态
            self.ui.pushButton.setEnabled(False)
            self.ui.pushButton.setText("检测中...")

            # 清空之前的日志
            if hasattr(self.ui, 'yoloLog'):
                self.ui.yoloLog.clear()

            self.yolo_thread.start()

            QMessageBox.information(self, "开始检测", "YOLO检测已开始")

        except Exception as e:
            QMessageBox.critical(self, "错误", f"启动检测失败: {str(e)}")

    def update_yolo_log(self, message):
        """更新检测日志到 QPlainTextEdit"""
        try:
            if hasattr(self.ui, 'yoloLog'):
                # 添加日志消息，
                self.ui.yoloLog.appendPlainText(message)

                # 自动滚动到底部
                scrollbar = self.ui.yoloLog.verticalScrollBar()
                scrollbar.setValue(scrollbar.maximum())
            else:
                print(f"YOLO日志: {message}")
        except Exception as e:
            print(f"更新日志错误: {e}")

    def on_yolo_finished(self, status):
        """检测完成处理"""
        try:
            # 恢复按钮状态
            self.ui.pushButton.setEnabled(True)
            self.ui.pushButton.setText("开始检测")

            # 显示完成消息
            if status == "success":
                finish_msg = "所有图片检测完成！"
                QMessageBox.information(self, "完成", finish_msg)
            elif status == "interrupted":
                finish_msg = "检测已被中断"
                QMessageBox.information(self, "中断", finish_msg)
            else:
                finish_msg = "检测过程中出现错误"
                QMessageBox.critical(self, "错误", finish_msg)

            # 清理线程
            self.yolo_thread = None

        except Exception as e:
            print(f"完成处理错误: {e}")

    ###################################################################################################################

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