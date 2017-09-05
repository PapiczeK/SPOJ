from math import pi

def CircleArea(r, d):
	return (r*r - d*d/4)*pi

numbers = list(map(float,input().split(' ')))
print('{0:.2f}'.format(CircleArea(numbers[0],numbers[1])))
