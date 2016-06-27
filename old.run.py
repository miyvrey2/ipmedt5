import time
from rta import rta
from sum import sum
from button import button
from scene import scene


sum = sum()
button = button()
rta = rta()
scene = scene()

score = 0

while True:
	if scene.pressStart(rta, button) == True:
		break

for x in range(0, 3):
	
	# Clear the board
	rta.codeBig("JYM01")
	time.sleep(1)
	
	clickIn = 0
	answer = ""
	answerbit = ""	

	current = x
	som = sum.createSum()

	if len(som) == 3:
		som = som + "  "
	if len(som) == 4:
		som = som + " "
	
	# Make sure we have a white space if current under 10
	wsinye = ""
	if x < 10:
		wsinye = " "
	current = wsinye + str(x)

	# Now print
	#rta.sendBig("som" + current, som)
	rta.codeBig("JYM01")
	time.sleep(1)

	rta.sendBig(str(score),som, "     ", "     ")
	time.sleep(0.03)

	for y in range(1, 16):
		time.sleep(0.1)
		answerbit = button.numbuttons()
		answer = answer + str(answerbit)
		returna = answer

		if len(answer) > 0 and y == 15:
			score = score + 10
		
		for z in range(1, 6):
			if len(returna) <= 5:
				returna = returna + " "
		# Less time
		#rta.codeBig("JYM02")
		time.sleep(0.1)

		rta.sendBig(som, returna, "     ","     ")
		time.sleep(0.04)
		
		if button.buttonClickIn(11) == True:
			clickIn = 1
		if button.buttonClickOut(11) == True and (clickIn == 1):
			score = score + 0
			break
	button.numbuttonsReset()
print(score)
scene.score(rta, str(score))