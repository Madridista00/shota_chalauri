"""შექმენით ორი კლასი:
I. Student, ატრიბუტებით: name, mark, address, სტატიკური ატრიბუტი row_id
II. Address, ატრიბუტებით: city, street


Student კლასის address ატრიბუტს მნიშვნელობად უნდა მიანჭოთ Address კლასის ეგზემპლარი.

შექმენთ ორივე კლასის რამდენინე ეგზემპლარი.

json მოდულის დახმარებით ფაილში შეინახეთ სტუდენტები.

მოახდინეთ წაკითხვა. შეცვალეთ ატრიბუტ(ებ)ის მნიშვნელობა (მაგ.mark, str), დაამატეთ ახალი ატრიბუტი grade მნიშვნელობით A, B, C, D (A -> [91-100], B -> [81-90], C -> [71-80], D -> <=70).

შეცვლილი მონაცემები შეინახეთ ფაილში."""



import json

class Students:
    row_id = 1

    def __init__(self, row_id, name, mark, address):
        self.row_id = row_id
        self.name = name
        self.mark = mark
        self.address = address

        Students.row_id += 1

    @classmethod
    def student_row_id(cls):
        return cls.row_id

    @staticmethod
    def assign_grade(mark):
        if mark >= 91:
            return 'A'
        elif mark >= 81:
            return 'B'
        elif mark >= 71:
            return 'C'
        else:
            return 'D'

class Address:
    def __init__(self, city, street):
        self.city = city
        self.street = street

class StudentEncode(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, Address):
            return o.__dict__
        return super().default(o)

# studentisa da address clasis instansebi
adr1 = Address("Tbilisi", "Saburtalo")
st1 = Students(Students.student_row_id(), "Paata", 87, adr1)

adr2 = Address("Tbilisi", "Gldani-7-11-4-93")
st2 = Students(Students.student_row_id(), "Demetre", 100, adr2)

st3 = Students(Students.student_row_id(), "Alexander", 100, adr2)

st4 = Students(Students.student_row_id(), "Teona", 92, adr2)

adr3 = Address("Tbilisi", "Leselidzs str. 25")
st5 = Students(Students.student_row_id(), "Nino", 99, adr3)

adr4 = Address("Tbilisi", "Varketili IV 407-5-123")
st6 = Students(Students.student_row_id(), "Andria", 87, adr4)

# sheicvalos mark_is mnishvneloba titoeul studentze
# st1.mark = 90
# st2.mark = 85
# st3.mark = 75
# st4.mark = 65
# st5.mark = 95
# st6.mark = 80

# daematos gradis logika
data = [
    {**st1.__dict__, 'grade': Students.assign_grade(st1.mark)},
    {**st2.__dict__, 'grade': Students.assign_grade(st2.mark)},
    {**st3.__dict__, 'grade': Students.assign_grade(st3.mark)},
    {**st4.__dict__, 'grade': Students.assign_grade(st4.mark)},
    {**st5.__dict__, 'grade': Students.assign_grade(st5.mark)},
    {**st6.__dict__, 'grade': Students.assign_grade(st6.mark)}
]

# chaiweros axali paili
with open("students.json", mode='w', encoding='utf-8') as file:
    json.dump(data, file, indent=2, cls=StudentEncode)
