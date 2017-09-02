for count in range(int(input())):
	array = input().split(' ')
	array = array[::-1]
	del array[-1]
	print(' '.join(array))	
