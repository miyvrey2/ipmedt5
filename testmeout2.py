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

		# If Red has been clicked, continue
		if button.buttonClickIn(11) == True:
			clickIn = 1
		if button.buttonClickOut(11) == True and (clickIn == 1):
			score = score + 0
			print("Clicked Red Button")
			break
scene.score(rta, str(score))