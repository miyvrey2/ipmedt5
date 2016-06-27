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
	for x in range(0, 8):
		
		# Define the variables
		clickIn = 0
		answer = ""
		answerbit = ""
		
		print(x)
	
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
		for y in range(1, 16):
			time.sleep(0.1)
	
			# Answer handling
			answerbit = button.numbuttons()
			answer = answer + str(answerbit)
			returna = answer
	
			if len(answer) > 0 and y == 15:
				score = score + 10
			
			for z in range(1, 6):
				if len(returna) < z:
					returna = returna + " "
	
			rta.sendBig(sum.scoreCalc(score), "     ", str(som), returna)
			time.sleep(0.04)
	
			# If Red has been clicked, continue
			if button.redButton(11) == True:
				score = score + 0
				break
	scene.score(rta, str(score))