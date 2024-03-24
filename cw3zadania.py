import math
import random

# Zadanie 1

A = [x for x in range(1, 11)]
print(A)

B = [4**x for x in range(7)]
print(B)

C = [x for x in B if x%2 == 0]
print(C)

# Zadanie 2



list = [random.randint(1, 100) for x in range(10)]
even_list = [x for x in list if x % 2 == 0]
print(list)
print(even_list)

# Zadanie 3

shopping = {"jablko": "szt", "banan": "kg", "wisnie": "kg", "melon": "szt"}
products_szt = [x for x, szt in shopping.items() if szt == "szt"]
print(shopping)
print(products_szt)

def czy_prostokatny(a, b, c):
    boki = sorted([a, b, c])
    return boki[0]**2 + boki[1]**2 == boki[2]**2

# Zadanie 5
def pole_trapezu(a=10, b=5, h=3):
    return (a + b) * h / 2

# Zadanie 6
def iloczyn_ciagu(a1=1, b=4, ile=10):
    iloczyn = 1
    for i in range(ile):
        iloczyn *= a1
        a1 *= b
    return iloczyn

# Zadanie 7
def pierwiastek_liczby():
    liczba = float(input("Podaj liczbę: "))
    if liczba < 0:
        return "Liczba nie może być ujemna!"
    else:
        return liczba**0.5
