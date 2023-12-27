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
