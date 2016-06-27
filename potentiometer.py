from rta import rta
from button import button
import time
naam = ""
button = button()
rta = rta()

time.sleep(1)

while True:
	output = rta.get2()
	rta.sendBig("Naam:", naam + str(output) + "     ", "     ", "     ")
	
	# If green has been clicked, continue
	if button.redButton(19) == True:
		if len(naam) < 5:
			naam = naam + output
		else:
		break