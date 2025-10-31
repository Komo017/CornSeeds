#
#
# # -*- coding: utf-8 -*-
# import os
# import cv2
# import numpy as np
# from datetime import datetime
# from PySide6.QtWidgets import QMainWindow, QMessageBox
# from PySide6.QtCore import Qt, Signal, QTimer
# from PySide6.QtGui import QPixmap, QImage
#
# # 导入工业相机UI文件
# from uipy.industrial_camera_ui import Ui_MainWindow
#
#
# class IndustrialCameraWindow(QMainWindow):
#     # 定义关闭信号
#     close_signal = Signal()
#
#     def __init__(self):
#         super().__init__()
#
#         # 初始化UI
#         self.ui = Ui_MainWindow()
#         self.ui.setupUi(self)
#
#         # 初始化相机
#         self.camera = None
#         self.is_camera_connected = False
#         self.current_image = None
#
#         # 自动拍照相关变量
#         self.auto_capture_timer = QTimer()
#         self.is_auto_capturing = False
#         self.capture_interval = 100  # 0.1秒 = 100毫秒
#         self.auto_photo_count = 0
#
#         # 实时预览定时器 - 新增
#         self.preview_timer = QTimer()
#         self.preview_interval = 30  # 30毫秒，约33fps
#
#         # 连接信号槽
#         self.connect_signals()
#
#         # 初始化相机
#         self.setup_camera()
#
#         # 设置默认页面和按钮样式
#         self.setup_default_state()
#
#         print("工业相机窗口初始化完成")
#
#     def connect_signals(self):
#         """连接信号和槽"""
#         try:
#             # 左侧按钮点击事件
#             self.ui.manualPhoto.clicked.connect(lambda: self.switch_page(0))
#             self.ui.autoPhoto.clicked.connect(lambda: self.switch_page(1))
#             self.ui.ratePhoto.clicked.connect(lambda: self.switch_page(2))
#             self.ui.RGBsettings.clicked.connect(lambda: self.switch_page(3))
#             self.ui.HSVchannel.clicked.connect(lambda: self.switch_page(4))
#             self.ui.Configuration.clicked.connect(lambda: self.switch_page(5))
#             self.ui.Settings.clicked.connect(lambda: self.switch_page(6))
#             self.ui.fromPhoto.clicked.connect(lambda: self.switch_page(7))
#
#             # 手动拍照页面按钮
#             self.ui.onePhoto.clicked.connect(self.capture_single_photo)
#
#             # 自动拍照页面按钮
#             self.ui.startPhoto.clicked.connect(self.start_auto_capture)
#             self.ui.stopPhoto.clicked.connect(self.pause_auto_capture)
#             self.ui.endPhoto.clicked.connect(self.end_auto_capture)
#
#             # 连接自动拍照定时器
#             self.auto_capture_timer.timeout.connect(self.auto_capture_photo)
#
#             # 连接实时预览定时器 - 新增
#             self.preview_timer.timeout.connect(self.update_preview)
#
#         except Exception as e:
#             print(f"工业相机窗口信号连接错误: {e}")
#
#     def setup_default_state(self):
#         """设置默认状态"""
#         # 默认显示手动拍照页面
#         self.switch_page(1)
#
#         # 设置自动拍照按钮初始状态
#         self.update_auto_capture_buttons(False)
#
#         # 开始实时预览 - 新增
#         self.start_preview()
#
#     def switch_page(self, index):
#         """切换页面"""
#         self.ui.stackedWidget.setCurrentIndex(index)
#
#         # 更新按钮高亮样式
#         self.update_button_styles(index)
#
#         # 切换到自动拍照页面时，如果正在自动拍照，更新按钮状态
#         if index == 1 and self.is_auto_capturing:
#             self.update_auto_capture_buttons(True)
#
#         # 根据页面控制实时预览 - 新增
#         if index == 0 or index == 1:  # 手动拍照或自动拍照页面
#             if not self.is_auto_capturing:  # 自动拍照页面只有在未拍照时才显示预览
#                 self.start_preview()
#         else:
#             self.stop_preview()
#
#     def update_button_styles(self, active_index):
#         """更新按钮高亮样式"""
#         # 所有左侧按钮列表
#         left_buttons = [
#             self.ui.manualPhoto,
#             self.ui.autoPhoto,
#             self.ui.ratePhoto,
#             self.ui.RGBsettings,
#             self.ui.HSVchannel,
#             self.ui.Configuration,
#             self.ui.Settings,
#             self.ui.fromPhoto
#         ]
#
#         # 高亮样式
#         active_style = """
#             QPushButton {
#                 background-color: #007bff;
#                 color: white;
#                 font-weight: bold;
#                 border: 2px solid #0056b3;
#             }
#         """
#
#         # 普通样式
#         normal_style = """
#             QPushButton {
#                 background-color: #f8f9fa;
#                 color: black;
#                 border: 1px solid #ccc;
#             }
#             QPushButton:hover {
#                 background-color: #e9ecef;
#             }
#         """
#
#         # 应用样式
#         for i, button in enumerate(left_buttons):
#             if i == active_index:
#                 button.setStyleSheet(active_style)
#             else:
#                 button.setStyleSheet(normal_style)
#
#     def setup_camera(self):
#         """初始化相机"""
#         try:
#             self.camera = cv2.VideoCapture(0)
#
#             if self.camera.isOpened():
#                 self.is_camera_connected = True
#                 print("工业相机连接成功")
#             else:
#                 self.is_camera_connected = False
#                 print("工业相机连接失败")
#
#         except Exception as e:
#             self.is_camera_connected = False
#             print(f"相机初始化错误: {e}")
#
#     def capture_single_photo(self):
#         """单次拍照"""
#         if not self.is_camera_connected:
#             QMessageBox.warning(self, "警告", "相机未连接，无法拍照")
#             return
#
#         try:
#             ret, frame = self.camera.read()
#             if ret:
#                 self.current_image = frame
#                 self.display_image(frame, self.ui.showPhoto)
#                 self.save_image(frame, "manual")
#             else:
#                 QMessageBox.warning(self, "错误", "拍照失败，无法获取图像")
#
#         except Exception as e:
#             QMessageBox.critical(self, "错误", f"拍照过程中出现错误: {str(e)}")
#
#     def start_auto_capture(self):
#         """开始自动拍照"""
#         if not self.is_camera_connected:
#             QMessageBox.warning(self, "警告", "相机未连接，无法开始自动拍照")
#             return
#
#         if self.is_auto_capturing:
#             QMessageBox.information(self, "提示", "自动拍照已经在进行中")
#             return
#
#         self.is_auto_capturing = True
#         self.auto_photo_count = 0
#         self.auto_capture_timer.start(self.capture_interval)
#         self.update_auto_capture_buttons(True)
#
#         # 开始自动拍照时停止预览 - 新增
#         self.stop_preview()
#
#     def pause_auto_capture(self):
#         """暂停自动拍照"""
#         if not self.is_auto_capturing:
#             QMessageBox.information(self, "提示", "自动拍照未开始")
#             return
#
#         self.is_auto_capturing = False
#         self.auto_capture_timer.stop()
#         self.update_auto_capture_buttons(False)
#
#         # 暂停自动拍照时恢复预览 - 新增
#         if self.ui.stackedWidget.currentIndex() == 1:  # 如果在自动拍照页面
#             self.start_preview()
#
#         print("暂停自动拍照")
#         QMessageBox.information(self, "提示", "已暂停自动拍照")
#
#     def end_auto_capture(self):
#         """结束自动拍照"""
#         if not self.is_auto_capturing:
#             QMessageBox.information(self, "提示", "自动拍照未开始")
#             return
#
#         self.is_auto_capturing = False
#         self.auto_capture_timer.stop()
#         self.update_auto_capture_buttons(False)
#
#         # 结束自动拍照时恢复预览 - 新增
#         if self.ui.stackedWidget.currentIndex() == 1:  # 如果在自动拍照页面
#             self.start_preview()
#
#         print(f"结束自动拍照，共拍摄 {self.auto_photo_count} 张照片")
#         QMessageBox.information(self, "提示", f"已结束自动拍照\n共拍摄 {self.auto_photo_count} 张照片")
#
#     def auto_capture_photo(self):
#         """自动拍照定时器回调"""
#         if not self.is_camera_connected or not self.is_auto_capturing:
#             return
#
#         try:
#             ret, frame = self.camera.read()
#             if ret:
#                 self.current_image = frame
#                 self.display_image(frame, self.ui.showPhoto2)
#                 self.save_image(frame, "auto")
#                 self.auto_photo_count += 1
#
#                 # 更新状态显示（可选）
#                 if self.auto_photo_count % 10 == 0:  # 每10张显示一次计数
#                     print(f"自动拍照计数: {self.auto_photo_count}")
#
#             else:
#                 print("自动拍照失败，无法获取图像")
#
#         except Exception as e:
#             print(f"自动拍照过程中出现错误: {e}")
#
#     def update_auto_capture_buttons(self, is_capturing):
#         """更新自动拍照按钮状态"""
#         if is_capturing:
#             # 拍照进行中，禁用开始按钮，启用暂停和结束按钮
#             self.ui.startPhoto.setEnabled(False)
#             self.ui.stopPhoto.setEnabled(True)
#             self.ui.endPhoto.setEnabled(True)
#         else:
#             # 拍照停止，启用开始按钮，禁用暂停和结束按钮
#             self.ui.startPhoto.setEnabled(True)
#             self.ui.stopPhoto.setEnabled(False)
#             self.ui.endPhoto.setEnabled(False)
#
#     def display_image(self, image, display_label):
#         """在指定的QLabel中显示图像"""
#         try:
#             if len(image.shape) == 3:
#                 h, w, ch = image.shape
#                 bytes_per_line = ch * w
#                 rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
#                 q_img = QImage(rgb_image.data, w, h, bytes_per_line, QImage.Format_RGB888)
#             else:
#                 h, w = image.shape
#                 bytes_per_line = w
#                 q_img = QImage(image.data, w, h, bytes_per_line, QImage.Format_Grayscale8)
#
#             pixmap = QPixmap.fromImage(q_img)
#             scaled_pixmap = pixmap.scaled(
#                 display_label.width(),
#                 display_label.height(),
#                 Qt.KeepAspectRatio,
#                 Qt.SmoothTransformation
#             )
#
#             display_label.setPixmap(scaled_pixmap)
#             display_label.setText("")
#
#         except Exception as e:
#             print(f"显示图像错误: {e}")
#
#     def save_image(self, image, mode="manual"):
#         """保存图像到文件"""
#         try:
#             base_dir = "captured_photos"
#             if not os.path.exists(base_dir):
#                 os.makedirs(base_dir)
#
#             today = datetime.now().strftime("%Y-%m-%d")
#             save_dir = os.path.join(base_dir, today)
#             os.makedirs(save_dir, exist_ok=True)
#
#             timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")[:-3]  # 包含毫秒
#
#             if mode == "auto":
#                 filename = f"auto_photo_{timestamp}_{self.auto_photo_count:04d}.jpg"
#             else:
#                 filename = f"manual_photo_{timestamp}.jpg"
#
#             filepath = os.path.join(save_dir, filename)
#
#             success = cv2.imwrite(filepath, image)
#             if success:
#                 print(f"图像已保存: {filepath}")
#             else:
#                 print("图像保存失败")
#
#         except Exception as e:
#             print(f"保存图像错误: {e}")
#
#     # ========== 新增的实时预览功能 ==========
#     def start_preview(self):
#         """开始实时预览"""
#         if self.is_camera_connected and not self.preview_timer.isActive():
#             self.preview_timer.start(self.preview_interval)
#             print("开始实时预览")
#
#     def stop_preview(self):
#         """停止实时预览"""
#         if self.preview_timer.isActive():
#             self.preview_timer.stop()
#             print("停止实时预览")
#
#     def update_preview(self):
#         """更新实时预览画面"""
#         if not self.is_camera_connected:
#             return
#
#         try:
#             ret, frame = self.camera.read()
#             if ret:
#                 self.current_image = frame
#
#                 # 根据当前页面在对应的QLabel中显示实时画面
#                 current_page = self.ui.stackedWidget.currentIndex()
#                 if current_page == 0:  # 手动拍照页面
#                     self.display_image(frame, self.ui.showPhoto)
#                 elif current_page == 1:  # 自动拍照页面
#                     if not self.is_auto_capturing:  # 只有在未拍照时才显示预览
#                         self.display_image(frame, self.ui.showPhoto2)
#
#         except Exception as e:
#             print(f"实时预览错误: {e}")
#
#     def closeEvent(self, event):
#         """关闭窗口时的处理"""
#         try:
#             # 停止自动拍照
#             if self.is_auto_capturing:
#                 self.auto_capture_timer.stop()
#
#             # 停止实时预览 - 新增
#             if self.preview_timer.isActive():
#                 self.preview_timer.stop()
#
#             # 释放相机资源
#             if self.camera is not None:
#                 self.camera.release()
#
#             # 发送关闭信号
#             self.close_signal.emit()
#
#             print("工业相机窗口关闭完成")
#         except Exception as e:
#             print(f"关闭窗口时出现错误: {e}")
#
#         event.accept()


# -*- coding: utf-8 -*-
import os
import cv2
import numpy as np
from datetime import datetime
from PySide6.QtWidgets import QMainWindow, QMessageBox
from PySide6.QtCore import Qt, Signal, QTimer
from PySide6.QtGui import QPixmap, QImage

# 导入工业相机UI文件
from uipy.industrial_camera_ui import Ui_MainWindow


class IndustrialCameraWindow(QMainWindow):
    # 定义关闭信号
    close_signal = Signal()

    def __init__(self):
        super().__init__()

        # 初始化UI
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # 初始化相机
        self.camera = None
        self.is_camera_connected = False
        self.current_image = None

        # 自动拍照相关变量
        self.auto_capture_timer = QTimer()
        self.is_auto_capturing = False
        self.capture_interval = 100  # 0.1秒 = 100毫秒
        self.auto_photo_count = 0

        # 实时预览定时器 - 新增
        self.preview_timer = QTimer()
        self.preview_interval = 30  # 30毫秒，约33fps

        # 手动拍照暂停定时器 - 新增
        self.manual_capture_pause_timer = QTimer()
        self.manual_capture_pause_timer.setSingleShot(True)  # 单次定时器
        self.manual_capture_pause_timer.timeout.connect(self.resume_preview_after_manual_capture)

        # 连接信号槽
        self.connect_signals()

        # 初始化相机
        self.setup_camera()

        # 设置默认页面和按钮样式
        self.setup_default_state()

        print("工业相机窗口初始化完成")

    def connect_signals(self):
        """连接信号和槽"""
        try:
            # 左侧按钮点击事件
            self.ui.manualPhoto.clicked.connect(lambda: self.switch_page(0))
            self.ui.autoPhoto.clicked.connect(lambda: self.switch_page(1))
            self.ui.ratePhoto.clicked.connect(lambda: self.switch_page(2))
            self.ui.RGBsettings.clicked.connect(lambda: self.switch_page(3))
            self.ui.HSVchannel.clicked.connect(lambda: self.switch_page(4))
            self.ui.Configuration.clicked.connect(lambda: self.switch_page(5))
            self.ui.Settings.clicked.connect(lambda: self.switch_page(6))
            self.ui.fromPhoto.clicked.connect(lambda: self.switch_page(7))

            # 手动拍照页面按钮
            self.ui.onePhoto.clicked.connect(self.capture_single_photo)

            # 自动拍照页面按钮
            self.ui.startPhoto.clicked.connect(self.start_auto_capture)
            self.ui.stopPhoto.clicked.connect(self.pause_auto_capture)
            self.ui.endPhoto.clicked.connect(self.end_auto_capture)

            # 连接自动拍照定时器
            self.auto_capture_timer.timeout.connect(self.auto_capture_photo)

            # 连接实时预览定时器 - 新增
            self.preview_timer.timeout.connect(self.update_preview)

        except Exception as e:
            print(f"工业相机窗口信号连接错误: {e}")

    def setup_default_state(self):
        """设置默认状态"""
        # 默认显示手动拍照页面
        self.switch_page(1)

        # 设置自动拍照按钮初始状态
        self.update_auto_capture_buttons(False)

        # 开始实时预览 - 新增
        self.start_preview()

    def switch_page(self, index):
        """切换页面"""
        self.ui.stackedWidget.setCurrentIndex(index)

        # 更新按钮高亮样式
        self.update_button_styles(index)

        # 切换到自动拍照页面时，如果正在自动拍照，更新按钮状态
        if index == 1 and self.is_auto_capturing:
            self.update_auto_capture_buttons(True)

        # 根据页面控制实时预览 - 新增
        if index == 0 or index == 1:  # 手动拍照或自动拍照页面
            if not self.is_auto_capturing:  # 自动拍照页面只有在未拍照时才显示预览
                self.start_preview()
        else:
            self.stop_preview()

    def update_button_styles(self, active_index):
        """更新按钮高亮样式"""
        # 所有左侧按钮列表
        left_buttons = [
            self.ui.manualPhoto,
            self.ui.autoPhoto,
            self.ui.ratePhoto,
            self.ui.RGBsettings,
            self.ui.HSVchannel,
            self.ui.Configuration,
            self.ui.Settings,
            self.ui.fromPhoto
        ]

        # 高亮样式
        active_style = """
            QPushButton {
                background-color: #007bff;
                color: white;
                font-weight: bold;
                border: 2px solid #0056b3;
            }
        """

        # 普通样式
        normal_style = """
            QPushButton {
                background-color: #f8f9fa;
                color: black;
                border: 1px solid #ccc;
            }
            QPushButton:hover {
                background-color: #e9ecef;
            }
        """

        # 应用样式
        for i, button in enumerate(left_buttons):
            if i == active_index:
                button.setStyleSheet(active_style)
            else:
                button.setStyleSheet(normal_style)

    def setup_camera(self):
        """初始化相机"""
        try:
            self.camera = cv2.VideoCapture(0)

            if self.camera.isOpened():
                self.is_camera_connected = True
                print("工业相机连接成功")
            else:
                self.is_camera_connected = False
                print("工业相机连接失败")

        except Exception as e:
            self.is_camera_connected = False
            print(f"相机初始化错误: {e}")

    def capture_single_photo(self):
        """单次拍照"""
        if not self.is_camera_connected:
            QMessageBox.warning(self, "警告", "相机未连接，无法拍照")
            return

        try:
            # 停止实时预览
            self.stop_preview()

            ret, frame = self.camera.read()
            if ret:
                self.current_image = frame
                self.display_image(frame, self.ui.showPhoto)
                self.save_image(frame, "manual")

                # 启动0.5秒的暂停定时器
                self.manual_capture_pause_timer.start(500)  # 500毫秒 = 0.5秒

                print("手动拍照完成，图片将暂停展示0.5秒")
            else:
                QMessageBox.warning(self, "错误", "拍照失败，无法获取图像")
                # 如果拍照失败，立即恢复预览
                self.start_preview()

        except Exception as e:
            QMessageBox.critical(self, "错误", f"拍照过程中出现错误: {str(e)}")
            # 如果出现异常，立即恢复预览
            self.start_preview()

    def resume_preview_after_manual_capture(self):
        """手动拍照暂停结束后恢复预览"""
        if self.ui.stackedWidget.currentIndex() == 0:  # 确保仍在手动拍照页面
            self.start_preview()
            print("手动拍照暂停结束，恢复实时预览")

    def start_auto_capture(self):
        """开始自动拍照"""
        if not self.is_camera_connected:
            QMessageBox.warning(self, "警告", "相机未连接，无法开始自动拍照")
            return

        if self.is_auto_capturing:
            QMessageBox.information(self, "提示", "自动拍照已经在进行中")
            return

        self.is_auto_capturing = True
        self.auto_photo_count = 0
        self.auto_capture_timer.start(self.capture_interval)
        self.update_auto_capture_buttons(True)

        # 开始自动拍照时停止预览 - 新增
        self.stop_preview()

    def pause_auto_capture(self):
        """暂停自动拍照"""
        if not self.is_auto_capturing:
            QMessageBox.information(self, "提示", "自动拍照未开始")
            return

        self.is_auto_capturing = False
        self.auto_capture_timer.stop()
        self.update_auto_capture_buttons(False)

        # 暂停自动拍照时恢复预览 - 新增
        if self.ui.stackedWidget.currentIndex() == 1:  # 如果在自动拍照页面
            self.start_preview()

        print("暂停自动拍照")
        QMessageBox.information(self, "提示", "已暂停自动拍照")

    def end_auto_capture(self):
        """结束自动拍照"""
        if not self.is_auto_capturing:
            QMessageBox.information(self, "提示", "自动拍照未开始")
            return

        self.is_auto_capturing = False
        self.auto_capture_timer.stop()
        self.update_auto_capture_buttons(False)

        # 结束自动拍照时恢复预览 - 新增
        if self.ui.stackedWidget.currentIndex() == 1:  # 如果在自动拍照页面
            self.start_preview()

        print(f"结束自动拍照，共拍摄 {self.auto_photo_count} 张照片")
        QMessageBox.information(self, "提示", f"已结束自动拍照\n共拍摄 {self.auto_photo_count} 张照片")

    def auto_capture_photo(self):
        """自动拍照定时器回调"""
        if not self.is_camera_connected or not self.is_auto_capturing:
            return

        try:
            ret, frame = self.camera.read()
            if ret:
                self.current_image = frame
                self.display_image(frame, self.ui.showPhoto2)
                self.save_image(frame, "auto")
                self.auto_photo_count += 1

                # 更新状态显示（可选）
                if self.auto_photo_count % 10 == 0:  # 每10张显示一次计数
                    print(f"自动拍照计数: {self.auto_photo_count}")

            else:
                print("自动拍照失败，无法获取图像")

        except Exception as e:
            print(f"自动拍照过程中出现错误: {e}")

    def update_auto_capture_buttons(self, is_capturing):
        """更新自动拍照按钮状态"""
        if is_capturing:
            # 拍照进行中，禁用开始按钮，启用暂停和结束按钮
            self.ui.startPhoto.setEnabled(False)
            self.ui.stopPhoto.setEnabled(True)
            self.ui.endPhoto.setEnabled(True)
        else:
            # 拍照停止，启用开始按钮，禁用暂停和结束按钮
            self.ui.startPhoto.setEnabled(True)
            self.ui.stopPhoto.setEnabled(False)
            self.ui.endPhoto.setEnabled(False)

    def display_image(self, image, display_label):
        """在指定的QLabel中显示图像"""
        try:
            if len(image.shape) == 3:
                h, w, ch = image.shape
                bytes_per_line = ch * w
                rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                q_img = QImage(rgb_image.data, w, h, bytes_per_line, QImage.Format_RGB888)
            else:
                h, w = image.shape
                bytes_per_line = w
                q_img = QImage(image.data, w, h, bytes_per_line, QImage.Format_Grayscale8)

            pixmap = QPixmap.fromImage(q_img)
            scaled_pixmap = pixmap.scaled(
                display_label.width(),
                display_label.height(),
                Qt.KeepAspectRatio,
                Qt.SmoothTransformation
            )

            display_label.setPixmap(scaled_pixmap)
            display_label.setText("")

        except Exception as e:
            print(f"显示图像错误: {e}")

    def save_image(self, image, mode="manual"):
        """保存图像到文件"""
        try:
            base_dir = "captured_photos"
            if not os.path.exists(base_dir):
                os.makedirs(base_dir)

            today = datetime.now().strftime("%Y-%m-%d")
            save_dir = os.path.join(base_dir, today)
            os.makedirs(save_dir, exist_ok=True)

            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")[:-3]  # 包含毫秒

            if mode == "auto":
                filename = f"auto_photo_{timestamp}_{self.auto_photo_count:04d}.jpg"
            else:
                filename = f"manual_photo_{timestamp}.jpg"

            filepath = os.path.join(save_dir, filename)

            success = cv2.imwrite(filepath, image)
            if success:
                print(f"图像已保存: {filepath}")
            else:
                print("图像保存失败")

        except Exception as e:
            print(f"保存图像错误: {e}")

    # ========== 新增的实时预览功能 ==========
    def start_preview(self):
        """开始实时预览"""
        if self.is_camera_connected and not self.preview_timer.isActive():
            self.preview_timer.start(self.preview_interval)
            print("开始实时预览")

    def stop_preview(self):
        """停止实时预览"""
        if self.preview_timer.isActive():
            self.preview_timer.stop()
            print("停止实时预览")

    def update_preview(self):
        """更新实时预览画面"""
        if not self.is_camera_connected:
            return

        try:
            ret, frame = self.camera.read()
            if ret:
                self.current_image = frame

                # 根据当前页面在对应的QLabel中显示实时画面
                current_page = self.ui.stackedWidget.currentIndex()
                if current_page == 0:  # 手动拍照页面
                    self.display_image(frame, self.ui.showPhoto)
                elif current_page == 1:  # 自动拍照页面
                    if not self.is_auto_capturing:  # 只有在未拍照时才显示预览
                        self.display_image(frame, self.ui.showPhoto2)

        except Exception as e:
            print(f"实时预览错误: {e}")

    def closeEvent(self, event):
        """关闭窗口时的处理"""
        try:
            # 停止自动拍照
            if self.is_auto_capturing:
                self.auto_capture_timer.stop()

            # 停止实时预览 - 新增
            if self.preview_timer.isActive():
                self.preview_timer.stop()

            # 停止手动拍照暂停定时器
            if self.manual_capture_pause_timer.isActive():
                self.manual_capture_pause_timer.stop()

            # 释放相机资源
            if self.camera is not None:
                self.camera.release()

            # 发送关闭信号
            self.close_signal.emit()

            print("工业相机窗口关闭完成")
        except Exception as e:
            print(f"关闭窗口时出现错误: {e}")

        event.accept()