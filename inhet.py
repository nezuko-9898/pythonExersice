class Naruto:
    def __init__(self,name,Age):
        self.name=name
        self.Age=Age

    def morning(self):
        print(f"Name is {self.name} years old {self.Age}.")

class Hinata(Naruto):
    pass 


h1=Hinata("Name" ,21)
h1.morning()