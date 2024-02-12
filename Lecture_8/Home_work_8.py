# 1. შექმენით გლობალური ცვლადი `int_list = [10,20,30,40]` და დაწერეთ პითონის ფუნქცია,
# რომელიც  მიიღებს რიცხვს პარამეტრად და გლობალურ `int_list` სიაში ჩაამატებს პარამეტრად მიღებულ რიცხვს.

# def list_func():
#     global int_list

#     int_list.append(add_list)


# #=====================================
# int_list = [10,20,30,40]

# add_list = int(input("Type something to add in list: "))
# list_func()
# print(int_list)


# 2. დაწერეთ პითნის ფუნქცია რომელიც პარამეტრად იღებს რიცხვების სიას (ლისტს) და აბრუნებს რიცხვების ჯამს.
# პარამეტრად უნდა მიიღოს შემდეგი სია `[100, 20, 30, 50, 5323, 3321, 22, 56, 700, 90, 10]`.


# def sum_of_arr(arr):
#     total = 0
#     i = 0
#     while i < len(arr):
#         total = total + arr[i]
#         i += 1
#     return total


# #==================================
# arr = [100, 20, 30, 50, 5323, 3321, 22, 56, 700, 90, 10]

# print(f"sum of arr is: {sum_of_arr(arr)}")


# ===============================================================
# ===============================================================

# from functools import reduce

# arr = [100, 20, 30, 50, 5323, 3321, 22, 56, 700, 90, 10]

# sum_of_arr = reduce(lambda x, y: x + y, arr)
# print(sum_of_arr)


# 3. შექმენით გლობალური ცვლადი `gl_str = "Global"` და დაწერეთ პითონის ფუნქცია რომელიც ქმნის ლოკალურ ცვლადს იგივე სახელით რაც გლობალურ ცვლადს აქვს
# `(gl_str)` და აბრუნებს ლოკალური ცვლადის მნიშვნელობას

# def func():
#     gl_str = "Sunny day"

#     print(gl_str)


# #========================
# gl_str = "Rainy day"

# func()


# 4. რეკურსიის გამოყენებით  დაწერეთ პითონის ფუნქცია, რომელიც მიიღებს ერთ პარამეტრს `number` და დააბრუნებს  ციფრების ჯამს
# (მაგალითად თუ ფუნქციამ მიიღო რიცხვი `12345`, უნდა დააბრუნოს `15`. რადგან `1+2+3+4+5`  უდრის `15`-ს).

# def sum_of_digits(number):
#     if number == 0:
#         return 0
#     else:
#         return (number % 10) + sum_of_digits(number // 10)

# #===================================
# number = int(input("Please input your number: "))
# print(f"Sum of digits of your number is: {sum_of_digits(number)}")


# 5. რეკურსიის გამოყენებით დაწერეთ პითონის ფუნქცია, რომელიც მიიღებს პარამეტრად სტრიქონს და დააბრუნებს მის შებრუნებულ (revers) სტრიქონს
# (მაგალითად  `input: Hello   Output: olleH`)


# def reverse(s):
#     if len(s) == 0:
#         return s
#     else:
#         return reverse(s[1:]) + s[0]


# #=========================================
# s = input("Please enter your word: ")

# print("The original word is : ", end="")
# print(s)

# print("The reversed word is : ", end="")
# print(reverse(s))
