
# Class And Object

class Morning:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def display(self):
        print(f"My Name is {self.name}. {self.age} years old")

m1 = Morning("Naruto",21)
m2 = Morning('itachi',33)



m1.display()
m2.display()




# Inheritance 



class Lucifer:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def put(self):
       pass

class show(Lucifer):
    def __init__(self, name, age,grade):
        super().__init__(name, age)            
        self.grade=grade

    def result(self):

         Name=input("Enter your name===>")
         Age = int(input("Enter your Age===>"))    
         Grade=input("Enter Your grade ===>")

s1 = show("Name","Age","Grade") 
s1.result   