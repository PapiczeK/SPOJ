#Flamaster
#Kasia niedawno poznała wszystkie literki w szkole. Z wielką pasją potrafiła całe dnie spędzać na pisaniu długich słów swoim ulubionym flamastrem. Pisała i pisała "tasiemce" tak długo, aż flamaster wypisał się. Kasia posmutniała. Z trudem, ale udało jej się uprosić swoją mamę, aby kupiła jej nowy pisak. Musiała jednak obiecać, że tym razem będzie bardziej oszczędna przy jego używaniu żeby wystarczył na dłużej. Kasia zaczęła zastanawiać się w jaki sposób będzie mogła zrealizować obietnicę daną mamie.

#Postanowiła, że aby zaoszczędzić wkład flamastra będzie wypisywała skróconą wersję wymyślanych wyrazów. Jeśli miała zamiar napisać więcej niż dwie takie same literki obok siebie w wyrazie, to teraz napisze literkę a następnie liczbę, określającą ilość wystąpień tej literki.
#Zadanie
#Twoim zadaniem jest dla zadanego wyrazu, który wymyśliła Kasia, podanie skróconej wersji tego wyrazu.
#Wejście
#W pierwszej linijce wejścia znajduje się liczba naturalna C, 1 ≤ C ≤ 50, oznaczająca ilość zestawów danych. W kolejnych C wierszach wejścia znajdują się zestawy danych. Każdy zestaw składa się z niepustego wyrazu złożonego z samych dużych liter alfabetu amerykańskiego. Długość wyrazu nie przekracza 200 znaków.
#Wyjście
#Dla każdego zestawu danych, dla zadanego wyrazu, na wyjściu powinna znaleźć się jego skrócona wersja. 

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
