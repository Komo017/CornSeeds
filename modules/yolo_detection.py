# coding:utf-8
import os
from PySide6.QtCore import QThread, Signal
from modules.yolo_processor import YOLOProcessor


class YOLODetection(QThread):
    """YOLO离线检测线程类"""

    progress_updated = Signal(int)  # 进度更新
    detection_finished = Signal(str)  # 检测完成
    log_message = Signal(str)  # 日志消息

    def __init__(self, folder_path, model_path='models/best.pt'):
        super().__init__()
        self.folder_path = folder_path
        self.model_path = model_path
        self.yolo_processor = YOLOProcessor(model_path)
        self.is_running = True
        self._is_finished = False

    def run(self):
        """执行检测任务"""
        try:
            self.log_message.emit("开始加载YOLO模型...")

            # 检查文件夹是否存在
            if not os.path.exists(self.folder_path):
                self.log_message.emit(f"错误：文件夹不存在 {self.folder_path}")
                self.detection_finished.emit("error")
                self._is_finished = True
                return

            # 加载模型
            if not self.yolo_processor.load_model():
                self.log_message.emit(f"错误：模型文件不存在 {self.model_path}")
                self.detection_finished.emit("error")
                self._is_finished = True
                return

            self.log_message.emit("模型加载成功")

            # 获取图片文件
            image_files = []
            for file in os.listdir(self.folder_path):
                if file.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp')):
                    image_files.append(os.path.join(self.folder_path, file))

            if not image_files:
                self.log_message.emit("错误：文件夹中没有图片文件")
                self.detection_finished.emit("error")
                self._is_finished = True
                return

            total_files = len(image_files)
            self.log_message.emit(f"找到 {total_files} 个图片文件")

            # 处理图片
            processed_count = 0
            for index, img_path in enumerate(image_files):
                if not self.is_running:
                    self.log_message.emit("检测被用户中断")
                    break

                # 检查文件是否存在
                if not os.path.exists(img_path):
                    self.log_message.emit(f"警告：图片文件不存在 {img_path}")
                    continue

                # 更新进度
                progress = int((index + 1) / total_files * 100)
                self.progress_updated.emit(progress)
                self.log_message.emit(f"正在处理第 {index + 1}/{total_files} 个文件: {os.path.basename(img_path)}")

                try:
                    # 检测图片
                    result, error = self.yolo_processor.process_image(img_path)

                    if error:
                        self.log_message.emit(f"处理图片失败: {error}")
                        continue

                    file_name = os.path.splitext(os.path.basename(img_path))[0]

                    # 保存检测结果
                    result_img_path, save_error = self.yolo_processor.save_results(
                        result, "TestResult", file_name
                    )

                    if result_img_path:
                        detected_count = len(result.boxes) if result.boxes else 0
                        self.log_message.emit(f"完成: {file_name} - 检测到 {detected_count} 个目标")
                        processed_count += 1
                    else:
                        self.log_message.emit(f"保存结果失败: {save_error}")

                except Exception as e:
                    self.log_message.emit(f"处理图片 {os.path.basename(img_path)} 时出错: {str(e)}")
                    continue

            # 发送完成信号
            if not self.is_running:
                self.log_message.emit(f"检测已中断，已完成 {processed_count}/{total_files} 个文件")
                self.detection_finished.emit("interrupted")
            else:
                self.log_message.emit(f"所有图片检测完成！共处理 {processed_count}/{total_files} 个文件")
                self.detection_finished.emit("success")

            self._is_finished = True

        except Exception as e:
            self.log_message.emit(f"检测过程发生错误: {str(e)}")
            self.detection_finished.emit("error")
            self._is_finished = True
