plik = open('tekst.txt', 'r', encoding='utf-8')
znaki = plik.read(10)

linia = plik.readline()
linie = plik.readlines()
plik.close()
print(znaki)
print(linia)
print(linie)

