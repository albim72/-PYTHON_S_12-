from pojazd import Pojazd

p1 = Pojazd()
odl = 567
lt = 51
cena_l = 6.49

print(f'spalanie [l/100km]: {p1.spalanie(odl,lt):.2f}')
print(f'koszt spalania na odcinku: {odl} km wynosi: {p1.kosztyprzejazdu(odl,lt,cena_l):.2f} zł')
