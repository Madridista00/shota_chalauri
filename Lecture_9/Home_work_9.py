# 1. დაწერეთ პითნის ფუნქცია, რომელიც იღებს პარამეტრად ერთი დაიგივე ზომის სიას (list) და zip ფუნქციის გამოყენებით დააჯგუფეთ სიების ელემენტები.

# ```python
# params: [1, 2, 3], ['a', 'b', 'c']
# outputs: ["(1, 'a')", "(2, 'b')", "(3, 'c')"]
#  ```
# number_list = [1, 2, 3]
# letter_list = ['a', 'b', 'c']

# print(list(zip(number_list, letter_list)))

# 2. დაწერეთ პითონის ფუნქცია, რომელიც პარამეტრად იღებს რიცხვების სიას და აბრუნებს ელემენტების ნამრავლს. ფუნქციაში გაითვალისწინეთ გამონაკლისები (Exceptions), თუ მიიღეთ არასწორი ტიპის პარამეტრს (TypeError).

#   ფუქნციის დასაწერად გამოიყენეთ lambda და  functools-ის reduce მეთოდი.

# ```python
# params:[1, 2, 3, 4, 5]
# output: 120
#  ```

# from functools import reduce

# try:
#     params = [1, 2, 3, 4, 5]
#     product_of_params = reduce(lambda x, y: x * y, params)
#     print(f"Product of params is: {product_of_params}")
# except TypeError as e:
#     print("Incorrect type")


# 3. დაწერეთ lambda ფუნქცია რომელიც იღებს მთელი რიცხვების სიას (list) და აბრუნებს მხოლოდ სიის კენტ ელემენტებს.

# ```python
# params: [1, 2, 3, 4, 5, 6, 7]
# outputs: [1, 3, 5, 7]
#  ```

# params = [1, 2, 3, 4, 5, 6, 7]
# odds = filter(lambda x: x % 2 == 1, params)
# print(list(odds))


# 4. დაწერეთ პითნის ფუნქცია, რომელიც იღებს ორ პარამეტრს, სტრიქონების სიასა და სტრიქონს (ending).
# დააბრუნეთ მხოლოდ სიის ის ელემენტები რომელიც მთავრდება, მეორე პარამეტრად მიწოდებული სტრიქონით. გამოიყენეთ lambda და filter ფუნქცია.
# გაითვალისწინეთ გამონაკლისები (TypeError), თუ სხვა გამონაკლისიც აღმოჩნდა ისიც გაითვალისწინეთ.

#   __მინიშნება:__ გადაავლეთ თვალი string მეთოდებს, მონახეთ ისეთი მეთოდი, რომელიც აბრუნებს სიტყვას, რომელიც მთავრდება რაღაც სიმბოლოებით...

# ```python
# params: ['hello', 'world', 'coding', 'nod'], 'ing'
# outputs: ['coding']
#  ```


# def matching(arr1, str):
#     match = list(filter(lambda i: i.endswith(str), arr1))
#     return match
 

        
# # ==================================
# arr1 = ["hello", "world", "coding", "nod"]
# str = "ing"

# try:
#     print(list(matching(arr1, str)))
# except TypeError as e:
#         print("Incorrect type")
# except NameError as e:
#         print("Not correct input")
