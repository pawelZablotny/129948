# plik = open('tekst.txt', 'r', encoding='utf-8')
# znaki = plik.read(10)
#
# linia = plik.readline()
# linie = plik.readlines()
# plik.close()
# print(znaki)
# print(linia)
# print(linie)
#
# for l in linie:
#     print(l)

# plik = open('tekst1.txt', 'w')
# plik.write('ITS OVER 9000')
# plik.close()

# plik = open('tekst.txt', 'a+')
# plik.write('ITS OVER 9000')
# plik.seek(105)
# znaki = plik.read(10)
# plik.close()
# print(znaki)

with open('tekst.txt', 'r') as f:
    lines = f.readlines()
print(lines)