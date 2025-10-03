class morning:
    def __init__(self,name,age,grade):
        self.name=name
        self.age=age
        self.grade=grade


    def putdata(self):
        pass
       # print( self.name, self.age, self.grade)



class star(morning):

    def __init__(self, name, age, grade,stream):
        super().__init__(name, age, grade)

        self.stream=stream

    def display(self):    

        print(f"My name is {self.name} im years {self.age} old.studey in Grade {self.grade} stream in {self.stream}")


s1 = star("Naruto",21,"A","Commerce")

s1.display()









