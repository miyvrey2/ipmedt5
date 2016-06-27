## Raspberry to Arduino
import serial
import time

class rta:

	ser = serial.Serial('/dev/ttyACM0', 9600)

	def send(self, value1, value2):	
		self.ser.write(value1)
		self.ser.write(value2)

	def code(self, code):
		self.ser.write("JYM01")

	def autoSend(self):
		ser = serial.Serial('/dev/ttyACM0', 9600)
		time.sleep(2)
		ser.write("10101")
		time.sleep(2)
