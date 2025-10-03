class morning:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def  display_info(self):

        print(f'Name: {self.name} \n  Age: {self.age} ')


class star(morning):
    def __init__(self, name, age,grade):
        super().__init__(name, age)             
        self.grade = grade

    def display(self):
        super().display_info()
        print(f' Grade: {self.grade}')        


name = input("Enter your name : ")
age  = int(input("Enter your age : "))
grade = input("Enter your grade : ")



s1 = star(name,age,grade)
s1.display()