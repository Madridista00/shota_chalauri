# 1. დაწერეთ პითონის კოდი, რომელიც იღებს სტრიქონს და აბრუნებს სტრიქონის UTF-8 დაშიფრულ ვერსიას.

# string = input("Please enter a string: ")
# hiden_string = string.encode('utf-8')
# print("Your string hiden version is:", hiden_string)


# 2. დაწერეთ პითონის კოდი, რომელიც იღებს სტრიქონს. ჩამოაშორეთ ზედმეტი ინტერვალები. ყველა სიმბოლო გადაიყვანეთ პატარა ასოებში და დაუმატეთ ქვესტრიქონი 'Python'.
#    თუ შეყვანილ სტრიქონში არსებობს სიტყვა "python", ჩაანაცვლეთ "Python"-ით.

#   მინიშნება: ზედმეტი ინტერვალების ჩამოსაშორებელი მეთოდია `.strip()`.

#   მაგ.:

#   ```python
#   "  Python is funny     ".strip()   ====>  "Python is funny"
#   ```

# string = input("Please enter a string: ")
# string_new = (string.lower().strip() + " 'Python'")

# if "python" in string_new:
#     new_string = string_new.replace("python", "Python")
#     print(new_string)
# else:
#     print(string_new)


# 3. დაწერეთ პითონის კოდი, რომელიც იღებს სტრიქონს და აბრუნებს ახალ სტრიქონს, რომელიც შედგება შეყვანილი სტრიქონის პირველი ნახევრისაგან.

# string = str(input("Please enter a string: "))
# first_part, second_part = string[:len(string)//2], string[:len(string)//2]
# print(f"First half is: {first_part}")

# 4. დაწერეთ პითონის კოდი, რომელიც იღებს სტრიქონს string მოდულის გამოყენებით დაწერეთ შემოწმება.
#    სტრიქონი ვალიდურია მაშინ, როდესაც ის შეიცავს ერთ ციფრს და არ არის დამატებითი სიმბოლოები ('!', '~', '#', '$' და ა.შ.)


# str = input("Enter string: ")

# nums = 0
# letter = 0
# other = 0
# spaces = 0

# for i in str :
#     if i.isalpha():
#           letter += 1
#     elif i.isdigit():
#           nums += 1
#     elif i.isspace():
#           spaces += 1
#     else:
#           other += 1

# if nums == 1 and other == 0 and spaces >= 0:
#     print("The string is valid!")
# else:
#     print("The string is invalid!")


# 5. დაწერეთ პითონის კოდი, რომელიც იღებს სტრიქონს, სტრიქონი გადაყავს ბაიტებში, ბეჭდავს მნიშვნელობას და შემდეგ კი გადაყავს ბაიტებიდან სტრიქონში და ბეჭდავს სტრიქონს.

# string = input("Please enter a string: ")
# code_string = string.encode('utf-16')
# print(f"original string is {string} and it's byte version is {code_string} \n")

# original_string = code_string.decode('utf-16')
# print(f"original string from {code_string} is {original_string}")
