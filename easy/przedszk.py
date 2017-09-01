counterTires = int(input())
answers = []

def CandyCounter(numChildren):
	grupChildrenOne = numChildren[0]
	grupChildrenTwo = numChildren[1]
	if numChildren[0] == numChildren[1]:
		return numChildren[0]
	else:
		while numChildren[0] != numChildren[1]:
			if numChildren[0] > numChildren[1]:
				numChildren[1] += grupChildrenTwo
			elif numChildren[0] < numChildren[1]:
				numChildren[0] += grupChildrenOne
	return numChildren[0] 

for x in range(counterTires):
	numberOfChildren = input()
	numberOfChildren = numberOfChildren.split(' ')
	numberOfChildren = map(int,numberOfChildren)
	answers.append(CandyCounter(numberOfChildren))

for x in answers:
	print(x)
