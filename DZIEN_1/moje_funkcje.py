import math
#przykład 1

def g(x):
    return x*math.sqrt(x)
n = 100
def policz(a,b,c,y=1):
    global n
    n = (a+b)*y-c+n+g(b)
    return n

print(policz(46,7,8,2))
print(policz(46,7,8))
print(n)

#przykład 2
def gh(x:int,l:int,k:float=3.333)->float:
    return math.pi * x * math.exp(l-k)

print(gh(5,6,4.5))
print(gh(1.2,False,6))
print(gh(1.2,False))

def zbior(f1,f2):
    return f1+f2

print(zbior(gh(5,7,8),policz(1,2,3)))


#przyklad 3

def ranking(*lang,nrrank,**inne):
    print(f'ranking języków programowania nr {nrrank} -> 1:{lang[0]}, '
          f'2:{lang[1]}, 3: {lang[2]}')

ranking("Python","Java","C#",nrrank=23)
ranking("Python","Java","C++","C#","JavaScript",nrrank=88,wersja="1.0")

#CTRL+D - powielenie linii lub bloku tesktu
#CTRL+/ - komentowanie lub odkomentowanie linii/bloku

