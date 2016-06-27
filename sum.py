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
	
	def scoreCalc(self, score):
		score = str(score)
		if len(score) < 2:
			score = "0000" + score
		
		elif len(score) < 3 and len(score) >= 2:
			score = "000" + score

		elif len(score) < 4 and len(score) >= 3:
			score = "00" + score

		elif len(score) < 5 and len(score) >= 4:
			score = "0" + score
		else:
			score = score
		
		return score