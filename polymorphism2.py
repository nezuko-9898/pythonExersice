class Principal:
    def salary():
        print("Salary is 10000")

class teacher:
    def salary():
        print("salary is 5000")

class student:
    def salary():
        print('salary is 2000')

s1 = Principal
s2 = teacher
s3 = student

for item in (s1,s2,s3):
    item.salary()
