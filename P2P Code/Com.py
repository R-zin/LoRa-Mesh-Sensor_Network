import sx126x
import Test
import time
class Net:
    con : sx126x.sx126x
    BROADCAST_ADDR = 0xFFFF
    def __init__(self,frequency,address,power,rssi,air_speed,relay):
        self.con = sx126x.sx126x(serial_num="/dev/ttyS0",freq=frequency,addr=address,power=power,rssi=rssi,air_speed=air_speed,relay=relay)
        self.con.set(frequency,address,power,rssi,air_speed,relay=relay)
    def send(self,data:bytes):
        self.con.send(data)

    def receive(self, r_buff: bytes) -> dict:
        sender_addr = (r_buff[0] << 8) + r_buff[1]
        freq = r_buff[2] + self.con.start_freq
        if self.con.rssi:
            message = r_buff[3:-1].decode()
            rssi_val = -(256 - r_buff[-1])
        else:
            message = r_buff[3:].decode()
            rssi_val = None
        parsed = {
            "addr": sender_addr,
            "freq": freq,
            "message": message,
            "rssi": rssi_val
        }
        print(parsed)
        return parsed

    def send_to_node(self,addr:int,freq:int,payload:str):
        high_addr = addr >> 8 & 0xFF  # Splits the 16-bit destination address into 2 bytes
        low_addr = addr & 0xFF
        freq_byte = freq - self.con.start_freq
        data = bytes([high_addr,low_addr,freq_byte]) + payload.encode()
        self.con.send(data)
        print(f"Data sent Successfully Data: {data}")
    def broadcast(self,freq:int,payload:str):  #Used for Broadcasting
        high_addr = self.BROADCAST_ADDR >> 8 & 0xFF
        low_addr = self.BROADCAST_ADDR & 0xFF
        freq_byte = freq - self.con.start_freq
        data = bytes([high_addr, low_addr, freq_byte]) + payload.encode()
        self.con.send(data)
    def Test(self):
        Test.Extended_response_test()

Mod = Net(868,1,10,True,2400,False)
Mod.Test()






