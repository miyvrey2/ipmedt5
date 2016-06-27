import RPi.GPIO as GPIO
import time

class button:

	# Pre-check for when clicked
	array = {}
	array[0] = 0
	array[1] = 0
	array[2] = 0
	array[3] = 0
	array[4] = 0
	array[5] = 0
	array[6] = 0
	array[7] = 0
	array[8] = 0
	array[9] = 0



	GPIO.setmode(GPIO.BOARD)

	def buttonClickIn(self, GPIOPIN):

		GPIO.setup(GPIOPIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	
		while True:
			input = GPIO.input(GPIOPIN)

			if input == False:
				return True	
			else:
				return False

	def buttonClickOut(self, GPIOPIN):

		GPIO.setup(GPIOPIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	
		while True:
			input = GPIO.input(GPIOPIN)

			if input == False:
				return False	
			else:
				return True

	def numbuttons(self):
		
		GPIO.setup(3, GPIO.IN, pull_up_down=GPIO.PUD_UP)
		GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_UP)
		GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_UP)
		GPIO.setup(8, GPIO.IN, pull_up_down=GPIO.PUD_UP)
		GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_UP)
		GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_UP)
		GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_UP)
		GPIO.setup(15, GPIO.IN, pull_up_down=GPIO.PUD_UP)
		GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP)
		GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)

		# Initiate variables of the buttons
		btn = {}
		btn[0] = GPIO.input(7)
		btn[1] = GPIO.input(13)
		btn[2] = GPIO.input(5)
		btn[3] = GPIO.input(3)		
		btn[4] = GPIO.input(16)
		btn[5] = GPIO.input(12)
		btn[6] = GPIO.input(8)
		btn[7] = GPIO.input(15)
		btn[8] = GPIO.input(10)
		btn[9] = GPIO.input(18)

		# Check each if they are pressed
		for x in range(0, 10):
			if btn[x] == False:
				self.array[x] = 1

			# Check wether released already or not
			if self.array[x] == 1 and btn[x] == True:
				self.array[x] = 7

			# Now presscontinuation, return in 5th of second back
			if self.array[x] > 2:
				self.array[x] -= 1
			if self.array[x] == 6:
				# print(x)
				return x
		return ""
	
	def numbuttonsReset(self):

		# Reset each button
		for x in range(-1, 10):
			self.array[x] = 0