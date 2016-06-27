## Scenes are parts of whole function, like showing score or loop trough questions

import time

class scene:

	clickIn = 0

	def startUp(self, rta):
		rta.sendBig("Druk ","op de","knop ","groen")
		time.sleep(0.03)

	def pressStart(self, rta, button):
		if button.buttonClickIn(11) == True:
			self.clickIn = 1
		if button.buttonClickOut(11) == True and (self.clickIn == 1):
			self.clickIn = 0
			return True

	def score(self, rta, scoreAmount):
		# Clear the board
		rta.codeBig("JYM03")
		time.sleep(0.1)
		for x in range (0, 5):
			rta.sendBig("SCORE", scoreAmount + "    ", "     ", "     ")
			time.sleep(0.5)
			rta.sendBig("SCORE", "     ", "     ", "     ")
			time.sleep(0.5)
		rta.codeBig("JYM03")
		time.sleep(0.3)

		rta.codeSmall("JYM01")
		time.sleep(0.3)
		rta.sendSmall("Gamer", scoreAmount)