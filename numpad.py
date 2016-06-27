## PIN 9 EN PIN 12 

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
	input_btn1 = GPIO.input(7)
	input_btn2 = GPIO.input(11)
	input_btn3 = GPIO.input(12)
	
	if input_btn1 == False:
	  print("button 1 pressed")
	if input_btn2 == False:
	  print("button 2 pressed")
	if input_btn3 == False:
	  print("button 3 pressed")
	time.sleep(0.2)