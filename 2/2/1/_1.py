a = int(input('a= '))
b = int(input('b= '))
c = int(input('c= '))
def calc(a,b,c):
    p = 12*(a+b+c)
    return p*(p-a)*(p-b)*(p-c)

if (a+b<c):
    print(calc(a,b,c))
elif (a+c<b):
    print(calc(a,b,c))
elif (b+a<c):
    print(calc(a,b,c))
elif (b+c<a):
    print(calc(a,b,c))
elif (c+a<b):
    print(calc(a,b,c))
elif (c+b<a):
    print(calc(a,b,c))
elif (c==b==a):
    print(calc(a,b,c))
else:
    print('Треугольника не существует.')