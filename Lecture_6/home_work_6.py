# 1. დაწერეთ პითონის პროგრამა, რომელიც დასაწყისში შექმნის ცარიელ სიას ([]), თუ მომხარებელი შეიყვანს სიმბოლო 'a'-ს,
# ნიშნავს რომ უნდა დაამატოთ სიაში რიცხვი; თუ აკრიფა 'r', სიიდან უნა წაიშალოს რიცხვი; 'e'-ს შეტანისას პროგრამამ უნდა დაასრულოს მუშაობა.
# მიღებული შედეგი დაბეჭდეთ კონსოლში.
# მომხარებელმა უნდა შეიყვანოს შემდეგი სტრუქტურით ბრძანება "{command} {number}" commands:
# a – append
# r – remove
# e – exit
# მხოლოდ გამოიყენეთ ეს ბრძანებები და მოახდინეთ სიაზე ზემოქმედება.


# list = []
# print(f"Now my list is empty: {list} \n     to add number in list please type - 'a';\n     to delete number from list please type - 'r';\n     to exit from please type - 'e';")

# while True:
#     command = input("Please enter command: ")
#     if command == "e":
#             print("You exit from list!")
#             break
#     elif command == 'a':
#         add = int(input("please enter number: "))
#         list.append(add)
#         print(f"You add {add} in list, now list contains:\n\b{list}")
#     elif command == 'r':
#         delete = int(input("please remove number: "))
#         if delete in list:
#             list.remove(delete)
#             print(f"You removed {delete} in list, now list contains:\n\b{list}")
#         else:
#             print("number not found!")
#     elif command != 'a' or 'b' or  'e':
#         print("Please enter only 'a', 'r' or 'e'.")
#         continue
# print(f"Now your list is:\n\b{list}")


# 2. დაწერეთ პითონის პროგრამა, რომელიც შექმნის სიას `my_list = [43, '22', 12, 66, 210, ["hi"]`, და შეასრულებს შემდეგ ნაბიჯებს:
# a. დაბეჭდავს `210`-ის ინდექსს;
# b. დაამატებს ბოლო ელემენტში ტექსტს `"hello"`;
# c. წაშლის მეორე ინდექსზე მდგომ ელემენტს და დაბეჭდავს სიას;
# d. შექმენით ახალი სია `my_llist_2`, რომელსაც ექნება `my_llist`-ის მნიშვნელობა, გაასუფთავეთ `my_llist_2`-ის მნიშნველობა და დაბეჭდეთ ორივე სია.

# my_list = [43, '22', 12, 66, 210, ["hi"]]

# "a."
# print(my_list.index(210))

# "b."
# my_list.append('"hello"')
# print(my_list)

# "c."
# my_list.pop(1)
# print(my_list)

# "d."
# import copy
# my_list_2 = copy.deepcopy(my_list)
# my_list_2.clear()
# print(f"{my_list}\n{my_list_2}")


# 3. დაწერეთ პითნის პროგრამა, რომელიც მიიღებს ტელეფონის ნომერს და regex-ით შეამოწმებს შეყვანილი ნომერი
#    იცავს თუ არა  "(123) 456-789" ფორმატს, თუ იცავს დააბრუნეთ შეყნვაილი ტელეფონის ნომერი,
#    წინააღმდეგ შემთხვევაში გამოიტანეთ "Invalid format" ტექსტი.

# import re

# phone = input("Please enter your phone number: ")
# pattern = r"\(\d{3}\)\s\d{3}[-]\d{3}$"
# valid = re.search(pattern, phone)

# if valid:
#     print(f"Your number '{phone}' is valid")
# else:
#     print("Invalid format")
