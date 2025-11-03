# modules/tcp_client.py
import socket
import threading


class TCPClient:
    """TCP客户端通讯模块"""

    def __init__(self):
        self.tcp_client_socket = None
        self.is_connected = False
        self.receive_thread = None
        self.should_receive = False
        self.receive_callback = None

    def connect_to_server(self, ip, port, timeout=5):
        """连接到TCP服务器"""
        try:
            self.tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.tcp_client_socket.settimeout(timeout)
            self.tcp_client_socket.connect((ip, port))
            self.is_connected = True

            # 启动接收线程
            self.should_receive = True
            self.receive_thread = threading.Thread(target=self._receive_data)
            self.receive_thread.daemon = True
            self.receive_thread.start()

            return True, "连接成功"

        except socket.timeout:
            return False, "连接超时"
        except ConnectionRefusedError:
            return False, "连接被拒绝"
        except Exception as e:
            return False, f"连接错误: {str(e)}"

    def _receive_data(self):
        """接收数据的线程函数"""
        while self.should_receive and self.is_connected:
            try:
                recv_data = self.tcp_client_socket.recv(1024)
                if recv_data:
                    # 将字节数据转换为列表显示
                    res_data = list(recv_data)
                    if self.receive_callback:
                        self.receive_callback(res_data)
                else:
                    self.is_connected = False
                    break
            except Exception:
                if self.should_receive:
                    self.is_connected = False
                break

    def send_data(self, data):
        """发送数据"""
        if self.is_connected and self.tcp_client_socket:
            try:
                self.tcp_client_socket.send(data)
                return True
            except Exception:
                self.is_connected = False
                return False
        return False

    def disconnect(self):
        """断开连接"""
        self.should_receive = False
        self.is_connected = False
        if self.tcp_client_socket:
            try:
                self.tcp_client_socket.close()
            except:
                pass
            self.tcp_client_socket = None

    def set_receive_callback(self, callback):
        """设置数据接收回调函数"""
        self.receive_callback = callback