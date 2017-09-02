count = int(input())
answers = []

def TurnAway(word):
	return word[::-1]

def IsPalindrome(word):
	lenghtWord = len(word)
	for index in range(int(lenghtWord/2)):
		if word[index] != word[lenghtWord-index-1]:
			return False
		

def CheckThisShit(word):
	counter = 0
	while IsPalindrome(word) == False:
		word = str(int(word) + int(TurnAway(word)))
		counter += 1
	return word + ' ' + str(counter)

for counter in range(count):
	palindrome = input()
	if int(palindrome)>10 and int(palindrome)<100:
		answers.append(CheckThisShit(palindrome))
	else:
		answers.append(palindrome + ' 0')

for x in answers:
	print(x)
