import json

jsource = '{"imię":"Jan","nazwisko":"Nowak","wiek":40,"miasto":"Zamość"}'

print(jsource)
print(type(jsource))

osoba = json.loads(jsource)
print(osoba)
print(type(osoba))

print(osoba["miasto"])

samochod = {
    "marka":"Jeep",
    "model":"Cherokee",
    "rocznik":2020,
    "poj":4.8
}

print(samochod)
jsonauto = json.dumps(samochod,indent=4)
print(jsonauto)
with open("samochod.json","w",encoding="utf-8") as f:
    f.write(jsonauto)

with open("samochod.json","r",encoding="utf-8") as f:
    auto_dict = json.load(f)

print(auto_dict)
print(type(auto_dict))

print("_______________________________________________________")

info = '{"organizacja":"Fundacja BIOTECH","miasto":"Zamość","kraj":"Polska"}'
projekt = {"id":7546,"temat":"Innowacyjne technologie AI","kwota":89762338}

# połącz oba żródła i ostatecznia 'zrzuć' pełne żródło do formatu json, zapisz je w pliku projekt.json
