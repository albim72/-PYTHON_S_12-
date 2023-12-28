#przykład 1

def wartosci():
    for i in range(50):
        yield (i+1)**2


print(wartosci())
print(list(wartosci()))

for p in wartosci():
    # print(len(list(wartosci())))
    print(p)


#przykład 2

def dzialania(n,k):
    print(f'działania na wartościach: n = {n}, k = {k}')
    print("dodawanie: ")
    yield n + k
    print("odejmowanie: ")
    yield n - k
    print("mnożenie: ")
    yield n * k
    print("dzielenie: ")
    yield n / k

print(list(dzialania(6,4)))

for d in dzialania(6,4):
    print(d)


#przykład 3

def otwarty():
    x = 0
    while True:
        y = yield x
        if y is None:
            x = x+1
        else:
            x = y

g= otwarty()
print("_"*50)
print(next(g))
print(next(g))
print(next(g))
print(g.send(112))
print(next(g))
print(next(g))
print(g.send(88))
print(next(g))
print(next(g))
print(reversed(g))

