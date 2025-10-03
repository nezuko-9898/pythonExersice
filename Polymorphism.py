class Morning:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def  display(self):
        print(" pravin")

class star:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def display(self):
        print("Naruto")

class Mr:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def display(self):
        print("Hinata")


m1 = Morning("sher",21)
s1 = star("sher2",21)
m2 = Mr("sher3",23)     


for item in (m1,s1,m2):
    #print(item.name)
    #print(item.age)
    item.display()
