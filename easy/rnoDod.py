#Twoim zadaniem jest dodać wszystkie liczby całkowite podane na wejściu.


count = int(input())
answer = []

for counter in range(count):
	sums = 0
	countAdd = int(input())
	numbers = input()
	numbers = numbers.split(' ')
	for index in range(countAdd):
		sums += int(numbers[index])
	answer.append(sums)

for x in answer:
	print(x)
