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
#         self._stop_event = threading.Event()
#
#     def connect_and_communicate(self, ip, port, write_data):
#         """连接并通信"""
#         try:
#             self.disconnect()
#             self.client = ModbusClient(host=ip, port=port)
#
#             print(f"尝试连接到 {ip}:{port}")
#             if not self.client.connect():
#                 return False, "连接失败"
#             print("Modbus连接成功")
#
#             # 确保有10个数据
#             if len(write_data) < 10:
#                 write_data = write_data + [0] * (10 - len(write_data))
#
#             print(f"准备写入数据: {write_data}")
#             write_result = self.client.write_registers(
#                 address=0,
#                 values=write_data[:10],
#                 slave=1
#             )
#             if write_result.isError():
#                 print(f"写入失败: {write_result}")
#                 return False, "写入失败"
#             print("数据写入成功")
#
#             print("开始读取20个寄存器...")
#             read_result = self.client.read_holding_registers(
#                 address=0,
#                 count=20,
#                 slave=1
#             )
#             if read_result.isError():
#                 print(f"读取失败: {read_result}")
#                 return False, "读取失败"
#
#             print(f"成功读取数据: {read_result.registers}")
#             self.is_connected = True
#             return True, read_result.registers
#
#         except Exception as e:
#             print(f"通信异常: {e}")
#             return False, f"通信错误: {str(e)}"
#
#     def start_monitoring(self, callback):
#         """启动监控"""
#         self._stop_event.clear()
#
#         def monitor():
#             while not self._stop_event.is_set() and self.is_connected:
#                 try:
#                     if not self.client or not self.is_connected:
#                         break
#
#                     result = self.client.read_holding_registers(
#                         address=0,
#                         count=20,
#                         slave=1
#                     )
#                     if not result.isError():
#                         # 使用线程安全的回调
#                         try:
#                             callback(result.registers)
#                         except Exception as e:
#                             print(f"回调执行错误: {e}")
#                     time.sleep(1)
#                 except Exception as e:
#                     print(f"监控异常: {e}")
#                     time.sleep(2)
#
#         self.monitoring = True
#         threading.Thread(target=monitor, daemon=True).start()
#
#     def disconnect(self):
#         """安全断开连接"""
#         self.monitoring = False
#         self.is_connected = False
#         self._stop_event.set()
#
#         if self.client:
#             try:
#                 self.client.close()
#             except:
#                 pass
#             self.client = None


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
        self._monitor_thread = None  # === 修改1：保存线程引用 ===

    def write_data_only(self, write_data):
        """只写入数据，不重新连接（用于实时更新）"""
        try:
            if not self.is_connected or not self.client:
                return False, "未连接"

            # 确保有10个数据
            if len(write_data) < 10:
                write_data = write_data + [0] * (10 - len(write_data))

            print(f"实时写入数据: {write_data}")
            # 写入10个寄存器
            write_result = self.client.write_registers(
                address=0,
                values=write_data[:10],
                slave=1
            )
            if write_result.isError():
                print(f"实时写入失败: {write_result}")
                return False, "写入失败"

            # 读取20个寄存器
            read_result = self.client.read_holding_registers(
                address=0,
                count=20,
                slave=1
            )
            if read_result.isError():
                print(f"实时读取失败: {read_result}")
                return False, "读取失败"

            print(f"实时读取数据: {read_result.registers}")
            return True, read_result.registers

        except Exception as e:
            print(f"实时通信异常: {e}")
            return False, f"通信错误: {str(e)}"

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
        # === 修改2：如果已经在监控，先停止 ===
        if self.monitoring:
            self.stop_monitoring()

        self._stop_event.clear()
        self.monitoring = True

        def monitor():
            print("监控线程启动...")  # === 修改3：添加启动日志 ===
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
                        print(f"监控收到数据: {result.registers}")  # === 修改4：添加数据接收日志 ===
                        # 使用线程安全的回调
                        try:
                            callback(result.registers)
                        except Exception as e:
                            print(f"回调执行错误: {e}")
                    else:
                        print(f"监控读取失败: {result}")  # === 修改5：添加读取失败日志 ===

                    # === 修改6：缩短监控间隔，提高实时性 ===
                    time.sleep(0.5)  # 0.5秒读取一次

                except Exception as e:
                    print(f"监控异常: {e}")
                    time.sleep(1)  # 异常时等待1秒再重试

            print("监控线程结束")  # === 修改7：添加结束日志 ===

        # === 修改8：创建并保存监控线程 ===
        self._monitor_thread = threading.Thread(target=monitor, daemon=True)
        self._monitor_thread.start()
        print("监控线程已启动")

    def stop_monitoring(self):
        """停止监控"""
        self.monitoring = False
        self._stop_event.set()
        if self._monitor_thread and self._monitor_thread.is_alive():
            self._monitor_thread.join(timeout=2)  # 等待线程结束

    def disconnect(self):
        """安全断开连接"""
        self.stop_monitoring()  # === 修改9：先停止监控 ===
        self.is_connected = False

        if self.client:
            try:
                self.client.close()
            except:
                pass
            self.client = None
        print("Modbus连接已断开")  # === 修改10：添加断开日志 ===