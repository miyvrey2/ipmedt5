## Scenes are parts of whole function, like showing score or loop trough questions

import time

class scene:

	clickIn = 0	

	def pressStart(self, rta, button):

		rta.send("Start", "groen")
		time.sleep(0.03)
		if button.buttonClickIn(11) == True:
			self.clickIn = 1
		if button.buttonClickOut(11) == True and (self.clickIn == 1):
			self.clickIn = 0
			return True

	def score(self, rta, scoreAmount):
		# Clear the board
		rta.code("JYM03")
		time.sleep(0.1)
		for x in range (0, 5):
			rta.send("SCORE", scoreAmount)
			time.sleep(0.5)
			rta.send("SCORE", "")
			time.sleep(0.5)
		rta.code("JYM03")
		time.sleep(0.03)