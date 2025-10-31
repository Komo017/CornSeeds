# modules/__init__.py
from abc import ABC, abstractmethod


class BaseModule(ABC):
    """所有功能模块的基类"""

    @abstractmethod
    def get_ui(self):
        """返回模块的UI组件"""
        pass

    @abstractmethod
    def start(self):
        """启动模块"""
        pass

    @abstractmethod
    def stop(self):
        """停止模块"""
        pass

    @abstractmethod
    def pause(self):
        """暂停模块"""
        pass

    @abstractmethod
    def reset(self):
        """重置模块"""
        pass