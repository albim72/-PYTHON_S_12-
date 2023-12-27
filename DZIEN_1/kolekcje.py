#lista

imiona = ["Jan","Monika","Leon","Jan","Halina","Jan","Henryka","Olaf","Leon"]
print(imiona)
print(imiona[0])
print(imiona[1])
print(imiona[2:6])
print(imiona[3:])
print(imiona[:6])
print(imiona[-1])
print(imiona.count("Jan"))
imiona.append("Nadia")
print(imiona)
imiona.insert(2,"Tomasz")
print(imiona)
imiona.remove("Olaf")
print(imiona)

print("_"*60)
print(sorted(imiona))
print(imiona)
imiona.sort()
print(imiona)

imionaparzyste = imiona[::2]
print(imionaparzyste)

ts = [45,8.8,True,"Romek","77"]

s = "lajkonik"
print(s)

print(s[0])
print(s[2])
print(s[1:4])

print(s[::-1])

#kolekcja: krotki (tuple)
miasta = ("Kraków","Lublin","Warszawa","Kielce","Kraków","Toruń","Kraków")
print(miasta)
print(type(miasta))
print(type(imiona))

print(miasta.count("Kraków"))
print(miasta.index("Toruń"))

print("Lublin" in miasta)

#kolekcja: zbiór(set)

kolory = {"zielony","czerwony","biały","niebieski","brązowy","pomarańczowy","biały"}

nb = [5,3,6,2,5,2,6,3,567,32,6,3,6,3]
nb = list(set(nb))
print(nb)

a:int=5
b:float=5
c=5

print(id(a))
print(id(b))
print(id(c))
a = 8
print("_"*60)
print(id(a))
print(id(b))
print(id(c))
print(a is b)

ob = [a,b,c]
ob = list(set(ob))
print(ob)

print(kolory)
print(kolory)
print(kolory)

kolory.add("żółty")
print(kolory)

kolory.update(["burgund","szary","złoty"])
print(kolory)

kolory.remove("szary")
print(kolory)

kolory.discard("srebrny")
print(kolory)

kolory.discard("biały")
print(kolory)
