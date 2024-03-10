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

#Zadanie 4

def trojkat_prostakat(a, b, c):
    if a**2 + b**2 == c**2:
        print("Jest prostokatny")
    elif b**2 + c**2 == a**2:
        print("Jest prostokatny")
    elif a**2 + c**2 == b**2:
        print("Jest prostokatny")
