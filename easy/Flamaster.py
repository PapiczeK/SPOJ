counterLoop = 0
goodWords = []
counterWords = input()
words = []
for x in range(int(counterWords)):
	checkingWord = input()
	words.append(checkingWord)

for checkingWord in words:
	while len(checkingWord) > (counterLoop + 1):		
		if checkingWord[counterLoop] != checkingWord[counterLoop+1]:
			counterLoop += 1 
		elif checkingWord[counterLoop] == checkingWord[counterLoop + 1]:
		#	checkingWord = checkingWord[0:counterLoop] + checkingWord[counterLoop + 1:]
			counterLetter = 0
			while len(checkingWord)>(counterLoop + counterLetter + 1) and checkingWord[counterLoop + counterLetter] == checkingWord[counterLoop + counterLetter + 1] :
				counterLetter += 1 
	#			print(checkingWord[counterLoop + counterLetter + 1] + " , " + str(counterLetter))
			if counterLetter > 1:		
				checkingWord = checkingWord[0:counterLoop+1] + str(counterLetter+1) + checkingWord[counterLoop + counterLetter + 1:]
			else:
				counterLoop += 1
	goodWords.append(checkingWord)
#	print(checkingWord)
	counterLoop = 0

for checkingWord in goodWords:
	print(checkingWord)
