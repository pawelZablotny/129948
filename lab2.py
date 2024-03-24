# Zad 1
#
# favorite_sports = ["football", "f1", "tennis"]
# favorite_sports.reverse()
# favorite_sports.extend(["box", "basketball"])
#
#
# Zad 2
#
# abbreviations = {
#     "itd.": "i tak dalej",
#     "itp.": "i tym podobne",
#     "np.": "na przyklad"
# }
#
# 
# Zad 3
#
# favorite_games = {
#     "League of Legends": "Moba",
#     "Starcraft 2": "RTS",
#     "Counter Strike": "FPS"
# }
# games_count = len(favorite_games)
#
#
# Zad 4
#
# sentence = input("Enter a sentence: ")
# a_count = sentence.lower().count('a')
# print(a_count)
#
#
# Zad 5
#
# import sys
#
# sys.stdout.write("Podaj liczbę a: ")
# a = int(sys.stdin.readline())
#
# sys.stdout.write("Podaj liczbę b: ")
# b = int(sys.stdin.readline())
#
# sys.stdout.write("Podaj liczbę c: ")
# c = int(sys.stdin.readline())
#
# wynik = a * b + c
#
# sys.stdout.write(f"Wynik ab + c: {wynik}\n")
#
#
# Zad 6
#
# a = int(input("Enter the first number (a): "))
# b = int(input("Enter the second number (b): "))
# c = int(input("Enter the third number (c): "))
#
# if a > b:
#     if a > c:
#         print("a is the largest number.")
#     else:
#         print("c is the largest number.")
# else:
#     if b > c:
#         print("b is the largest number.")
#     else:
#         print("c is the largest number.")
#
#
# Zad 7
#
# numbers = [1, 2.3, 4, 5.6, 7]
#
# squared_numbers = [number ** 2 for number in numbers]
#
# print("Original numbers:", numbers)
# print("Squared numbers:", squared_numbers)
#
#
# Zad 8
#
# even_numbers = []
#
# count = 0
#
# while count < 10:
#     number = int(input(f"Enter number {count + 1}: "))
#     if number % 2 == 0:
#         even_numbers.append(number)
#     count += 1
#
# print("Even numbers:", even_numbers)
#
#
# Zad 9
#
# import math
#
# number = float(input("Enter a number: "))
#
# if number < 0:
#     print("Error: the number cannot be negative.")
# else:
#     square_root = math.sqrt(number)
#     print(f"The square root of {number} is {square_root}.")
