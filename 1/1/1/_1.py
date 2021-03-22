import math 
x=int(input())
print('Результат:')
print(pow(int(math.tan((pow(int(x),2)/2)-1)),2) + (2*math.cos((x-math.pi/6))) / (1/2)+math.pow(math.sin(x),2))
