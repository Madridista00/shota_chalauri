import os, csv

path = "files"

try:
    os.mkdir(path)
except FileExistsError:
    print(f"Folder '{path}' exists")
    print("Continue working...\n")

# head = ["id", "Name", "Age", "Grade", "Subject_Name", "Marks"]
# data = [
#     [1, 'John', 20, 'A', 'Math', 95],
#     [1, 'John', 20, 'B', 'History', 87],
#     [2, 'Ann', 22, 'A', 'Math', 97],
#     [3, 'Tim', 25, 'A', 'Math', 92],
#     [3, 'Tim', 25, 'C', 'Biology', 77],
# ]


# with open(f"{path}/Home_Work_data.csv", mode='w', encoding='utf-8', newline='')as file:
#     writer = csv.writer(file)

"""
 1. დაწერეთ პითონის ფუნქცია , სადაც მომხარებელი შეიყვანს ინფომრაციას 
    `(id,name,age,grade,subject_name,marks)` 
    და თქვენ სტუდენტს დაამატებთ csv ფაილში.
"""
# =================================================================
# ======================= with while loop =========================
# =================================================================

# students = []
# print(f"To add student info please type - '+';\nTo exit from input please type - '-';")

# while True:
#     command = input("Please enter command: ")

#     if command == "-":
#         print("You exited from input!")
#         break
#     elif command == '+':
#         new_id = int(input("Please enter student id: "))
#         new_name = input("Please input student Name: ")
#         new_age = int(input("Please input student Age: "))
#         new_grade = input("Please input student Grade: ")
#         new_subject_name = input("Please input new Subject_Name: ")
#         new_marks = int(input("Please enter new Marks: "))

#         # Create a list for the current student
#         new_student = [new_id, new_name, new_age, new_grade, new_subject_name, new_marks]

#         # Append the new student list to the students list
#         students.append(new_student)
#     elif command not in ['+', '-']:
#         print("Please enter only '+', '-'")
#         continue

# print("You entered students:")
# for student in students:
#     print(student)

# with open(f"{path}/Home_Work_data.csv", mode='a', encoding='utf-8', newline='')as file:
#     writer = csv.writer(file)

#     writer.writerows(students)


# ======================================================================
# ======================= with Function ================================
# ======================================================================

# def add_student():
#     new_id = int(input("Please enter student id: "))
#     new_name = input("Please input student Name: ")
#     new_age = int(input("Please input student Age: "))
#     new_grade = input("Please input student Grade: ")
#     new_subject_name = input("Please input new Subject_Name: ")
#     new_marks = int(input("Please enter new Marks: "))

#     return [new_id, new_name, new_age, new_grade, new_subject_name, new_marks]

# def add_in_database():
#     students = []

#     while True:
#         command = input("Please enter command: ")

#         if command == "-":
#             print("You exited from input!")
#             break
#         elif command == '+':
#             new_student = add_student()
#             students.append(new_student)
#         elif command not in ['+', '-']:
#             print("Please enter only '+', '-'")
#             continue

#     print("You entered students:")
#     for student in students:
#         print(student)


# #============================
# add_in_database()


# with open(f"{path}/Home_Work_data.csv", mode='a', encoding='utf-8', newline='')as file:
#     writer = csv.writer(file)

#     writer.writerows(students)


"""
2. დაწერეთ პითონის ფუნქცია, რომლის საშულებით მომხარებელს შეეძლება, 
როგორც ყველა, ასევე კონკრეტული  სტუდენტის ინფომრაციის წაკითხვა ფაილიდან.
"""


# with open(f"{path}/Home_Work_data.csv", mode="r", encoding="utf-8") as file:
#     reader = list(csv.reader(file))

#     choose_student = input("To see ALL student info type 'all' or choose student: ")
#     print("\n")

#     w1 = 10
#     w2 = 15
#     underline = 64
#     count = 0

#     for row in reader:
#         if choose_student == "all":
#             print(
#                 f"  {row[0]:<{w1}}{row[1]:<{w1}}{row[2]:<{w1}}{row[3]:<{w1}}{row[4]:<{w2}}{row[5]:<{w1}}")
#             if count == 0:
#                 print("=" * underline)
#                 count += 1
#             else:
#                 print("-" * underline)
#         elif choose_student in row[1]:
#             print(f"  {head[0]:<{w1}}{head[1]:<{w1}}{head[2]:<{w1}}{head[3]:<{w1}}{head[4]:<{w2}}{head[5]:<{w1}}")
#             print(f"  {row[0]:<{w1}}{row[1]:<{w1}}{row[2]:<{w1}}{row[3]:<{w1}}{row[4]:<{w2}}{row[5]:<{w1}}")

#             if count == 0:
#                 print("-" * underline)
#                 count += 1

'''
3. დაწერეთ პითონის ფუნქცია, რომლის საშუალებით შესაძლებელი იქნება სტუდენტის ქულის განახლება/ცვლილება.
   მომხარებელი შეიყვანს სტუდენტის აიდს, საგანს და განახლებულ ქულას.
'''
# choose_id = int(input("Choose student id: "))
# choose_subject = input("Choose student subject: ")

# w1 = 10
# w2 = 15
# underline = 64
# count = 0

# with open(f"{path}/Home_Work_data.csv", mode="r", encoding="utf-8") as file:
#     reader = list(csv.reader(file))

#     for row in reader:
#             print(f"  {row[0]:<{w1}}{row[1]:<{w1}}{row[2]:<{w1}}{row[3]:<{w1}}{row[4]:<{w2}}{row[5]:<{w1}}")
#             if count == 0:
#                 print("=" * underline)
#                 count += 1 

#     for row in reader:
#         if choose_id and choose_subject in row:
#             row = row.remove

# def add_student():
#     new_id = int(input("Please enter student id: "))
#     new_name = input("Please input student Name: ")
#     new_age = int(input("Please input student Age: "))
#     new_grade = input("Please input student Grade: ")
#     new_subject_name = input("Please input new Subject_Name: ")
#     new_marks = int(input("Please enter new Marks: "))

#     return [new_id, new_name, new_age, new_grade, new_subject_name, new_marks]
            
# def add_in_database():
#     students = []

#     while True:
#         command = input("Please enter command: ")

#         if command == "-":
#             print("You exited from input!")
#             break
#         elif command == '+':
#             new_student = add_student()
#             students.append(new_student)
#         elif command not in ['+', '-']:
#             print("Please enter only '+', '-'")
#             continue
# #============================
# add_in_database()
