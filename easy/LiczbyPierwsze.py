#Sprawdź, które spośród danych liczb są liczbami pierwszymi

counterTests = input()
answers = []

for test in range(int(counterTests)):
	number = input()
	checkingNumber = sqrt(int(number))
        divider = 2
        while checkingNumber >= divider:
                if checkingNumber % divider == 0 or checkingNumber == 1:
                        return 'NIE'
                divider += 1
        
	answers.append(CheckPrimeNumber(number))

for x in answers:
	print(x)
