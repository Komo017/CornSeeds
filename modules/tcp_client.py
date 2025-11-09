# # modules/tcp_client.py
# from pymodbus.client import ModbusTcpClient as ModbusClient
# import threading
# import time
#
#
# class ModbusClientHandler:
#     def __init__(self):
#         self.client = None
#         self.is_connected = False
#         self.monitoring = False
#
#     def connect_and_communicate(self, ip, port, write_data):
#         """连接并通信"""
#         try:
#             self.disconnect()
#             self.client = ModbusClient(host=ip, port=port)
#
#             if not self.client.connect():
#                 return False, "连接失败"
#
#             # 写入10个寄存器
#             write_result = self.client.write_registers(0, write_data[:10], slave=1)
#             if write_result.isError():
#                 return False, "写入失败"
#
#             # 读取20个寄存器
#             read_result = self.client.read_holding_registers(0, 20, slave=1)
#             if read_result.isError():
#                 return False, "读取失败"
#
#             self.is_connected = True
#             return True, read_result.registers
#
#         except Exception as e:
#             return False, str(e)
#
#     def start_monitoring(self, callback):
#         """启动监控"""
#
#         def monitor():
#             while self.monitoring and self.is_connected:
#                 try:
#                     result = self.client.read_holding_registers(0, 20, slave=1)
#                     if not result.isError():
#                         callback(result.registers)
#                     time.sleep(1)
#                 except:
#                     time.sleep(2)
#
#         self.monitoring = True
#         threading.Thread(target=monitor, daemon=True).start()
#
#     def disconnect(self):
#         self.monitoring = False
#         self.is_connected = False
#         if self.client:
#             self.client.close()

# modules/tcp_client.py
from pymodbus.client import ModbusTcpClient as ModbusClient
import threading
import time


class ModbusClientHandler:
    def __init__(self):
        self.client = None
        self.is_connected = False
        self.monitoring = False
        self._stop_event = threading.Event()

    def connect_and_communicate(self, ip, port, write_data):
        """连接并通信"""
        try:
            self.disconnect()
            self.client = ModbusClient(host=ip, port=port)

            print(f"尝试连接到 {ip}:{port}")
            if not self.client.connect():
                return False, "连接失败"
            print("Modbus连接成功")

            # 确保有10个数据
            if len(write_data) < 10:
                write_data = write_data + [0] * (10 - len(write_data))

            print(f"准备写入数据: {write_data}")
            write_result = self.client.write_registers(
                address=0,
                values=write_data[:10],
                slave=1
            )
            if write_result.isError():
                print(f"写入失败: {write_result}")
                return False, "写入失败"
            print("数据写入成功")

            print("开始读取20个寄存器...")
            read_result = self.client.read_holding_registers(
                address=0,
                count=20,
                slave=1
            )
            if read_result.isError():
                print(f"读取失败: {read_result}")
                return False, "读取失败"

            print(f"成功读取数据: {read_result.registers}")
            self.is_connected = True
            return True, read_result.registers

        except Exception as e:
            print(f"通信异常: {e}")
            return False, f"通信错误: {str(e)}"

    def start_monitoring(self, callback):
        """启动监控"""
        self._stop_event.clear()

        def monitor():
            while not self._stop_event.is_set() and self.is_connected:
                try:
                    if not self.client or not self.is_connected:
                        break

                    result = self.client.read_holding_registers(
                        address=0,
                        count=20,
                        slave=1
                    )
                    if not result.isError():
                        # 使用线程安全的回调
                        try:
                            callback(result.registers)
                        except Exception as e:
                            print(f"回调执行错误: {e}")
                    time.sleep(1)
                except Exception as e:
                    print(f"监控异常: {e}")
                    time.sleep(2)

        self.monitoring = True
        threading.Thread(target=monitor, daemon=True).start()

    def disconnect(self):
        """安全断开连接"""
        self.monitoring = False
        self.is_connected = False
        self._stop_event.set()

        if self.client:
            try:
                self.client.close()
            except:
                pass
            self.client = None