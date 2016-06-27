## Raspberry to Arduino
from __future__ import division
import serial
import time

class rta:

	ser2 = serial.Serial('/dev/ttyACM0', 9600)
	ser1 = serial.Serial('/dev/ttyACM1', 9600)

	def sendSmall(self, value1, value2):	
		self.ser1.write(value1)
		self.ser1.write(value2)

	def sendBig(self, value1, value2, value3, value4):	
		self.ser2.write(value1)
		self.ser2.write(value2)
		self.ser2.write(value3)
		self.ser2.write(value4)

	def codeSmall(self, code):
		self.ser1.write(code)

	def codeBig(self, code):
		self.ser2.write(code)

	def autoSend(self):
		ser = serial.Serial('/dev/ttyACM0', 9600)
		time.sleep(2)
		ser.write("10101")
		time.sleep(2)
	
	def get2(self):
		charArray = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"," "]
		charArray = charArray[::-1]

		outcome = self.ser2.readline();
		print(outcome)
		if outcome != "0":
			outcome = float(outcome)
		else:
			outcome = 1
		outcome = int(outcome)
		inputCharKey = outcome / 37.8889
		inputCharKey = outcome / 39.34615
		inputCharKey = round(inputCharKey)
		inputCharKey = int(inputCharKey)
			
		if(inputCharKey <= 28):
			inputCharKey = charArray[inputCharKey]
		else:
			inputCharKey = "_"
		return inputCharKey
