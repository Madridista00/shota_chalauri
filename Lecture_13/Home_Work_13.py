# # დაწერეთ ფუნქცია რომელიც ტერმინალში მომხმარებელს გამოუტანს სტუდენტების აიდის (id) სიას,
# # მომხარებელი აირჩევს სტუდენტის აიდის, მიიღებული აიდისთვის დაბეჭდავს სტუდენტის მონაცემებს
# # მონაცემებში უნდა დაიბეჭდოს (სახელი, გვარი, ასაკი და ქულა თითოეული საგნის მიხედვით)

my_dict = {
  "students": [
    {"id": 20, "name": "giorgi", "age": 25},
    {"id": 25, "name": "giorgi", "age": 23},
    {"id": 100, "name": "nika", "age": 22},
    {"id": 56, "name": "nika", "age": 25},
    {"id": 1232, "name": "dato", "age": 22},
    {"id": 846723, "name": "archili", "age": 32}
  ],
  "subjects": [
    {"id": 1, "name": "Math", "grades": {"20": "B", "25": "A", "100": "A", "56": "B", "1232": "C", "846723": "A"}},
    {"id": 2, "name": "Physics", "grades": {"20": "A", "25": "B", "100": "A", "56": "B", "1232": "C", "846723": "B"}},
    {"id": 3, "name": "English", "grades": {"20": "A", "25": "A", "100": "A", "56": "A", "1232": "B", "846723": "A"}},
    {"id": 4, "name": "Chemistry", "grades": {"20": "B", "25": "B", "100": "A", "56": "B", "1232": "A", "846723": "A"}},
    {"id": 5, "name": "History", "grades": {"20": "C", "25": "B", "100": "A", "56": "B", "1232": "A", "846723": "A"}},
  ]
}

# #===============================#
# #===============================#

# student_id = ''
# st_id = ''
# st_name = ''
# st_age = ''
# st_grade = 'Not_Found'
# st_subject = ''
# new_grade = '' 


# print("Studentebis ID: ", end = "")

# for student in my_dict["students"]:
#     student_id = student.get('id')
    
#     print(student_id, end = " ")

# sub_id = int(input("\nAirchiet studentis ID: - "))
# key = str(sub_id)
# print("Student information:")

# for stu in my_dict['students']:
#     st_id = stu.get("id")
#     st_name = stu.get("name")
#     st_age = stu.get('age')

#     if sub_id == st_id:
#         print(f"ID: {st_id}, Name: {st_name.title()}, age: {st_age}")


# for grade in my_dict["subjects"]:
#     st_grade = grade.get('grades')
#     if key in st_grade:
#         new_grade = st_grade.get(key)

#     for subject in my_dict['subjects']:
#         st_subject = subject.get('name')

#     print(f"subject: {st_subject}, grade: {new_grade}")
    
