#Sprawdź, które spośród danych liczb są liczbami pierwszymi

import math

counterTests = input()
answers = []

def CheckPrimeNumber(number):
	divider = 2
	sqrtNumber = math.sqrt(number)
	while sqrtNumber >= divider:
		if number % divider  == 0:
#			print(number%divider)
			return False
		else:
			divider+=1
#			print(number%divider)
	return True

for test in range(int(counterTests)):
	number = int(input())
	number = int(number)
	if number > 1:
		if CheckPrimeNumber(number):
			answers.append('TAK')
		else:
	        	answers.append('NIE')
	else:
		answers.append('NIE')

for x in answers:
	print(x)
