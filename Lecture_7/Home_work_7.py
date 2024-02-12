# 1. დაწერეთ პითონის ფუნქცია, რომელიც მიიღებს პარამეტრად n, და გამოიტანს ფიბონაჩის n რაოდენობის მიმდევრობას.


# def Fibonacci(n):
#     # თუ n ნაკლებია ნოლზე
#     if n < 0:
#         print("Invalid value.")
#     # თუ n უდრის 0-ს
#     elif n == 0:
#         return 0
#     # თუ n ერთის ან ორის ტოლია
#     elif n == 1 or n == 2:
#         return 1
#     # თუ n მეტია ორზე
#     else:
#         return Fibonacci(n - 1) + Fibonacci(n - 2)


# # ================================
# n = int(input("Please enter n: "))
# fib = Fibonacci(n)
# for n in range(n + 1):
#     print(Fibonacci(n), end=" ")


# 2. დაწერეთ პითონის ფუნქცია, რომელიც მიიღებს პარამეტრად ორ სტრიქონს და შეამოწმებს არის თუ არა სტრიქონები ანაგრამები.
# (ანაგრამი არის სიტყვა ან შესიტყვება, რომელიც წარმოიქმნება სხვა სიტყვის ან შესიტყვების ასოების გადაადგილებით). მაგ.: `race` და `care` ანაგრამებია.


# def anagram(str1, str2):

#     if(sorted(str1) == sorted(str2)):
#         print("These words are anagrams!")
#     else:
#         print("These words are not anagrams!")


# #=================================
# str1 = input("Please enter first word: ")
# str2 = input("Please enter second word: ")
# anagram(str1, str2)

# 3. დაწერეთ პითონის ფუნქცია რომელიც მიიღებს n რიცხვს და დააბრუნებს მის ფაქტორიალს.


# def factorial(n):

#     if n < 0:
#         return 0
#     elif n == 0 or n == 1:
#         return 1
#     else:
#         fact = 1
#         while(n > 1):
#             fact *= n
#             n -= 1
#         return fact


# #==================================
# n = int(input("Please enter number:"))
# fact = factorial(n)
# print(f"Factorial of {n} is {fact}")

# 4. დაწერეთ პითნის ფუნქცია რომელიც მიიღებს  ორ პარამეტრს, პირველს სტრიქონს და მეორეს სიმბოლოს.
# ფუნქციამ უნდა მოძებნოს სტრიქონში რამდენჯერ მეორდება პარამეტრად მიღებული სიმბოლო და დააბრუნოს  მისი რაოდენობა.


# def count(string, symbol):
#     found = 0
#     for i in string:
#         if i == symbol:
#             found += 1
#     return found


# #=========================================
# string = input("Please enter string: ")
# symbol = input("Please enter symbol: ")
# Count = count(string, symbol)
# print(f"Count of '{symbol}' in '{string}' is: ", Count)
