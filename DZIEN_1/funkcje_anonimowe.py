print((lambda e:e+4)(12))

b = lambda u,w:2*u/w

print(b(2,5))

h = lambda a,b,c=5.5:(a+b)/c

print(h(2,1,2))
print(h(2,1))

def multi(n,l1,l2):
    print((lambda b:b*88)(l1))
    return lambda a:a*n*(lambda c:c-3)(l2)

print(multi(4,1,1)(9))


liczba = [3,2,45,67,-8,0,-34,24,111,-99,0,2,67,3,35,133,-83,55]

parzyste = list(filter(lambda x:x%2==0,liczba))
print(parzyste)

cube = list(map(lambda x:x**3,liczba))
print(cube)

def fiveplus(x):
    return x+5

five = list(map(fiveplus,liczba))
print(five)

#list comprehension
wynik_suma = sum([i**7 for i in range(10000)])
print(wynik_suma)
