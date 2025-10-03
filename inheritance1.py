class Morning:
    def __init__(self,name,Age,Grade):
        self.name = name
        self.age = Age
        self.grade=Grade

    def putdata(self):
        print(self.name,self.age,self.grade) 

class star(Morning):
    def __init__(self, name, Age, Grade, stream):
        super().__init__(name, Age, Grade)

        self.stream = stream

    def display(self):
        print(f"My name is {self.name}. I am {self.age} old. My class {self.grade} grade. my {self.stream} stream.")   


s1 = star("Naruto",21,"A","Commerce")
s1.display()         