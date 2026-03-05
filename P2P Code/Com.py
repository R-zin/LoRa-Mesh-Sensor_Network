import sx126x
class Net:
    con : sx126x.sx126x
    def __init__(self,frequency,address,power,rssi,air_speed,relay):
        self.con = sx126x.sx126x(serial_num="/dev/ttyS0",freq=frequency,addr=address,power=power,rssi=rssi,air_speed=air_speed,relay=relay)
        self.con.set(frequency,address,power,rssi,air_speed,relay=relay)






