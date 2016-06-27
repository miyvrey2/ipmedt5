import time
from rta import rta
from sum import sum
from button import button


sum = sum()
button = button()
rta = rta()

for x in range(0, 15):
	
	# Clear the board
	rta.code("JYM01")
	
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
	#rta.send("som" + current, som)
	rta.send(som, "")
	time.sleep(0.03)

	for y in range(1, 20):
		time.sleep(0.1)
		answerbit = button.numbuttons()
		answer = answer + str(answerbit)
		returna = answer
		
		for z in range(1, 6):
			if len(returna) <= 5:
				returna = returna + " "

		rta.send(som, returna)
		time.sleep(0.03)
		
		if button.buttonClickIn(11) == True:
			clickIn = 1
		if button.buttonClickOut(11) == True and (clickIn == 1):
			break
	button.numbuttonsReset()
	