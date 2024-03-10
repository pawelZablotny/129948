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

def rownanie_kwadratowe(a, b, c):
    delta = b ** 2 -4 * a * c
    if delta < 0:
        print('bral pierwiastkow')
