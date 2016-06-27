import time
from rta import rta
from sum import sum
from button import button
from scene import scene

# Get the current objects
sum = sum()
button = button()
rta = rta()
scene = scene()

while True:
	
	# Set variables
	score = 0
	naam = ""
	
	# Define rest, so the pin can react. Then draw a black screen.
	time.sleep(1)
	rta.codeBig("JYM03")
	time.sleep(0.1)
	
	while True:
		scene.startUp(rta)
		if scene.pressStart(rta, button) == True:
			break
	
	
	# Define rest, so the pin can react. Then draw a black screen.
	time.sleep(1)
	for x in range(0, 16):
		
		# Define the variables
		clickIn = 0
		answer = ""
		answerbit = ""
	
		# create new Som
		som = sum.createSum()
		
		# Style some
		if len(som) == 3:
			som = som + "  "
		if len(som) == 4:
			som = som + " "
		
		# Print on screen
		rta.sendBig(sum.scoreCalc(score), "     ", str(som), "     ")
		time.sleep(1)
	
		# Now for input
		maxRange = 96
		for y in range(1, maxRange):
			time.sleep(0.05)
	
			# Answer handling
			answerbit = button.numbuttons()
			answer = answer + str(answerbit)
			returna = answer
	
			if len(answer) > 0 and y == (maxRange - 1):
				if sum.checkSum(float(answer)) == "1":
					score = score + 10
			
			for z in range(1, 6):
				if len(returna) < z:
					returna = returna + " "
	
			rta.sendBig(sum.scoreCalc(score), "     ", str(som), returna)
			time.sleep(0.04)

			# If Green has been clicked, continue
			if button.greenButton(19) == True and answer != "":
				if sum.checkSum(float(answer)) == "1":
					score = score + 10
				break
	
			# If Red has been clicked, continue
			if button.redButton(11) == True:
				if len(answer) > 0:
					answer = answer[:-1]
					returna = answer + "     "
					rta.sendBig(sum.scoreCalc(score), "     ", str(som), returna)
					time.sleep(0.04)
				else:
					score = score + 0
					break
	scene.score(rta, str(score))
	while True:
		output = rta.get2()
		rta.sendBig("Naam:", naam + str(output) + "     ", "     ", "     ")
		
		# If green has been clicked, continue
		if button.greenButton(19) == True:
			if len(naam) < 4:
				naam = naam + output
			else:
				naam = naam + output
				break

		# if red button, remove char
		if button.redButton(11) == True:
			naam = naam[:-1]
	scene.smallScore(rta,naam, str(score))