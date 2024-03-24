# Zad 1

# sentence = input("Enter a sentence: ")
# words = sentence.split()
# print("Number of words:", len(words))

# Zad 2

# import sys

# sys.stdout.write("Enter a (base): ")
# a = int(sys.stdin.readline())
# sys.stdout.write("Enter b (exponent): ")
# b = int(sys.stdin.readline())
# sys.stdout.write("Enter c: ")
# c = int(sys.stdin.readline())

# result = a ** b + c

# sys.stdout.write(f"Result of a^b + c: {result}\n")

# Zad 4

# number = int(input("Enter a number: "))
# if number > 1:
#     for i in range(2, int(number**0.5) + 1):
#         if number % i == 0:
#             print("The number is not prime.")
#             break
#     else:
#         print("The number is prime.")
# else:
#     print("The number is not prime.")

# Zad 5

# def is_perfect(n):
#     return sum(i for i in range(1, n) if n % i == 0) == n

# perfect_numbers = [n for n in range(1, 1001) if is_perfect(n)]
# print("Number of perfect numbers up to 1000:", len(perfect_numbers))

# Zad 6

# numbers = [1, 2.5, 3, 4.5, 5]
# squared_numbers = [number ** 2 for number in numbers]
# print(squared_numbers)

# Zad 7

# even_numbers = []
# count = 0
# while count < 10:
#     number = int(input(f"Enter number {count + 1}: "))
#     if number % 2 == 0:
#         even_numbers.append(number)
#     count += 1
# print(even_numbers)
