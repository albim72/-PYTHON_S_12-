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
