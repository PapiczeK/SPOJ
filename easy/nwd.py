count = int(input())

for counter in range(count):
	numbers = list(map(int,input().split(' ')))
	while numbers[0] != numbers[1]:
		if numbers[0] > numbers[1]:
			numbers[0] -= numbers[1]
		else:
			numbers[1] -= numbers[0]
	print(numbers[0])
