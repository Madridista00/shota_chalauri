# 1. დაწერეთ პითონის პროგრამა, რომელიც მიიღებს მომხმარებლისგან რიცხვს "n" და ბეჭდავს 1-დან "n"-მდე რიცხვების ჯამს.

# A)
# number = int(input("Please, entere your number: "))
# i = 0
# sum = 0
# for i in range(1, number+1):
#     sum += i
# print(f"The sum of every number untill {number} is {sum}.")

# B)
# number = int(input("Please, entere your number: "))
# i = 0
# sum = 0
# while i <= number:
#     sum += i
#     i += 1
# print(f"The sum of every number untill {number} is {sum}.")


# 2. დაწერეთ პითონის პროგრამა, რომელიც მიიღებს მომხმარებლისგან რიცხვს და შემდეგ იყენებს "while" ციკლს რომ რევესრულად დაბეჭდოს რიცხვები 0-მდე.
#    მაგალითად თუ შეიყვანს 4, დაიბეჭდოს 4, 3, 2, 1.

# i = int(input("Please, entere your number: "))

# print("Every number untill your number is:", end=' ')
# while i != 0:
#     print(i, end=' ')
#     i -= 1
# print("\nEnd of program!")


# 3. დაწერეთ პითონის პროგრამა თამაშისთვის, რომელიც მუდმივად სთხოვს მომხმარებელს გამოიცნოს წინასწარ განსაზღვრული რიცხვი.
# როდესაც მომხმარებელი გამოიცნობს სწორ რიცხვს, დაასრულებს პროგრამა მუშაობას.

# from random import randint
# nummber = randint(1, 100)
# i = 0

# print("I guessed a number between 1 and 100. Please guess it\n")

# while True:
#     i += 1
#     guess = int(input(f"Try {i}, my number is: "))

#     if guess == nummber:
#         print(f"You guess the nummber. It was {nummber}.")
#         break
#     elif guess > nummber:
#         print("Your nummber is greater than mine.")
#     else:
#         print("Your nummber is less than mine.")
#     print()
# print("\nGame over!")


# 4. დაწერეთ პითონის პროგრამა, რომელიც მიიღებს მუდმივად რიცხვებს. შექმენით საწყისი ცვლადი total_sum = 0, შეამოწმეთ რიცხვი თუ დადებითია, მხოლოდ მაშინ დაუმატეთ total_sum ცვლადს.
# ეს პროცესი გაგრძელდეს იქამდე სანამ მომხმარებელი არ შეიყვანს 'sum' ტექსტს, რის შემდეგაც დაიბეჭდება შეყვანილი დადებითი რიცხვების ჯამი.

# total_sum = 0

# print('To finish enter "sum".')
# while True:
#     data = input("Pelase enter number: ")
#     if data == "sum": # input is sum
#         break
#     num = int(data)
#     if num < 0: # number is positive
#         print("number must be pozitive!")
#         continue
#     total_sum += num # sum of all numbers

# print("The sum of your numbers is: ", total_sum , sep='', end='!')

