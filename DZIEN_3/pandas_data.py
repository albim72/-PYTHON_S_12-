import pandas as pd
import numpy as np

s1 = pd.Series([6,23,4,-6,8,24,6,0,-6],index=['a','b','c','d','e','h','v','x','t'])
print(s1)

print("_"*50)

sdata = {'Warszawa':45600,'Lublin':43200,'Wrocław':43560}
s2 = pd.Series(sdata)
print(s2)

#obiekt DataFrame = ramka danych

mdane = {
    'miasto':['Warszawa','Radom','Lublin','Kraków','Gdańsk'],
    'populacja':[2.1,0.2,0.5,0.9,0.6],
    'stolica_woj':[True,False,True,True,True]
}

print("_"*50)
df = pd.DataFrame(mdane)
print(df)

print("_"*50)
# nowa ramka oparat na indeksach wierszy w postaci dat

daty = pd.date_range("20231229",periods=6)
print(daty)

fr = pd.DataFrame(np.random.randn(6,4),index=daty,columns=list('ABCD'))
print(fr)

print("_"*50)

df = pd.read_csv('dane/ex1.csv')
print(df)

print("_"*50)

par = pd.read_csv('dane/csv_mindex.csv',index_col=['key1','key2'])
print(par)

print("_"*50)

fd = pd.read_csv('dane/ex4.csv',skiprows=[0,2,3])
print(fd)

print("_"*50)

dane = pd.read_csv('dane/ex5.csv')
print(dane)

dane.to_csv('dane/outdn.csv')

