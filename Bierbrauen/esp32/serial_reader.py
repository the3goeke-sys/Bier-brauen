import serial
import time


class SerialReader:

    def __init__(self, port="COM9", baudrate=115200):
        self.ser = serial.Serial(port, baudrate)
        time.sleep(2)

    def lese_daten(self):

        line = self.ser.readline().decode("utf-8").strip()

        if not line:
            return None

        data = line.split(",")

        if len(data) != 5:
            return None

        return {
            "gewicht": float(data[0]),
            "mx": float(data[1]),
            "my": float(data[2]),
            "mz": float(data[3]),
            "temperatur": float(data[4])
        }