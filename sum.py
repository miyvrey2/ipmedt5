import random

class sum:
	strSum = ""
	intAnswer = 0
	
	def createSum(self):
		som = "";
		val1 = random.randint(1,99)
		val2 = random.randint(1, 99)
		som = str(val1) + "+" + str(val2)
		
		if(val1 <= 9 and val2 <= 9):
			som = " " + som
		
		# Set class variables
		self.strSum = som
		self.intAnswer = (val1 + val2)
		
		return som;

	def checkSum(self, answer):
		if self.intAnswer == answer:
			return "1";
		else:
			return "0";

	def retrieveAnswer(self):
		return self.intAnswer;