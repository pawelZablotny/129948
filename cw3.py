# try:
#
#     a = int(input())
#     b = int(input())
#     result = a/b
#    print(result)
#
# except ZeroDivisionError:
#     print("Error")
#
# except ValueError:
#     print("wrong value")
# else:
#     print(result)

# except Exception:
#     print("Error")
# else:
#     print(result)

# list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# l2 = []
# for i in list1:
#     l2.append(pow(i, 2))
# print(l2)
# l2 = [x**2 for x in list1]
# print(l2)
# l3 = [3**y for y in range(0, 6)]
# print(l3)
# l4 = [x for x in l2 if x%2 == 1]
# print(l4)
# l5 = [(x, y) for x  in l3 for y in l4]
# print(l5)
# l6 = []
# for x in l3:
#     for y in l4:
#         l6.append((x, y))
# print(l6)

# s1 = {1: 2, 2: 3, 3: 4, 4: 5}
# s2 = {}
# for key, value in s1.items():
#     s2[value] = key
# print(s1)
# print(s2)
# s3 = {v: k for k, v in s1.items()}
# print(s3)
# import math
# def rownanie_kwadratowe(a, b, c):
#     delta = b ** 2 - 4 * a * c
#     if delta < 0:
#         print('brak pierwiastkow')
#         return 0
#     elif delta == 0:
#         print('jeden pierwiastek')
#         x = (-b) / (2 * a)
#         return x
#     elif delta > 0:
#         print('dwa pierwiastki')
#         x1 = (-b + math.sqrt(delta)) / (2 * a)
#         x1 = (-b - math.sqrt(delta)) / (2 * a)
#         return x1, x2
# print(rownanie_kwadratowe(a=6, b=1, c=3))
# print(rownanie_kwadratowe(a=6, b=1, c=3))
# print(rownanie_kwadratowe(a=6, b=1, c=3))

import math

def dlugosc_odcinka(x1=1, x2=2, y1=3, y2=4):
    return sqrt((x1-x2)**2 + (y1-y2)**2)
print(dlugosc_odcinka())
print(dlugosc_odcinka(x1:4, x2:2, y1:6, y2:3))

print(dlugosc_odcinka(y2=5, y1=5, x2=4, x1=8))
