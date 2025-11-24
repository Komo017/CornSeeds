# coding:utf-8
import os
import cv2
from ultralytics import YOLO
import datetime


class YOLOProcessor:
    """YOLO处理工具类"""

    def __init__(self, model_path='models/best.pt'):
        self.model_path = model_path
        self.model = None

    def load_model(self):
        """加载模型"""
        if self.model is None and os.path.exists(self.model_path):
            self.model = YOLO(self.model_path, task='detect')
        return self.model is not None

    def process_image(self, image_path):
        """处理单张图片"""
        try:
            if not self.load_model():
                return None, "模型加载失败"

            if not os.path.exists(image_path):
                return None, f"图片文件不存在: {image_path}"

            # 执行检测
            results = self.model(image_path)
            return results[0], None

        except Exception as e:
            return None, f"处理图片时出错: {str(e)}"

    def save_results(self, result, base_dir, image_name):
        """保存检测结果"""
        try:
            # 创建输出目录
            photo_dir = os.path.join(base_dir, "result_photo")
            txt_dir = os.path.join(base_dir, "result_txt")
            os.makedirs(photo_dir, exist_ok=True)
            os.makedirs(txt_dir, exist_ok=True)

            # 保存检测图片
            result_img = result.plot()
            result_img_path = os.path.join(photo_dir, f"{image_name}_detected.jpg")
            cv2.imwrite(result_img_path, result_img)

            # 保存文本结果
            txt_path = os.path.join(txt_dir, f"{image_name}_results.txt")
            self._save_text_results(result, txt_path, image_name)

            return result_img_path, txt_path

        except Exception as e:
            return None, f"保存结果失败: {str(e)}"

    def _save_text_results(self, result, txt_path, image_name):
        """保存文本结果"""
        with open(txt_path, 'w', encoding='utf-8') as f:
            f.write(f"图片: {image_name}\n")
            f.write(f"时间: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write("=" * 40 + "\n")

            if result.boxes and len(result.boxes) > 0:
                f.write(f"检测到 {len(result.boxes)} 个目标:\n\n")
                for i, box in enumerate(result.boxes):
                    xyxy = box.xyxy[0].cpu().numpy()
                    conf = box.conf[0].cpu().numpy()
                    cls = int(box.cls[0].cpu().numpy())

                    f.write(f"目标 {i + 1}:\n")
                    f.write(f"  类别: {cls}\n")
                    f.write(f"  置信度: {conf:.3f}\n")
                    f.write(f"  位置: {xyxy}\n")
                    f.write("-" * 20 + "\n")
            else:
                f.write("未检测到目标\n")

    def get_latest_images(self, photo_dir, count=4):
        """获取最新的图片文件"""
        if not os.path.exists(photo_dir):
            return []

        image_files = []
        for file in os.listdir(photo_dir):
            if file.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp')):
                file_path = os.path.join(photo_dir, file)
                image_files.append((file_path, os.path.getmtime(file_path)))

        # 按修改时间排序，最新的在前
        image_files.sort(key=lambda x: x[1], reverse=True)
        return [img[0] for img in image_files[:count]]