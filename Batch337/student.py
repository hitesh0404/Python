from human import Human
class Student(Human):
    def __init__(self,name,age,gender):
        super().__init__(gender)
        self.name = name
        self.age = age
    def __str__(self):
        return self.name + " "+ str(self.age)+"years old " + self.gender