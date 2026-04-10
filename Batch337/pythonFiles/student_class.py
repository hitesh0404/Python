from pythonFiles.human import Human
from pythonFiles.classroom import Classroom
class Student(Human):
    def __init__(self,name,age,gender):
        super().__init__(gender)
        self.__name = name
        self.age = age
    def __str__(self):
        return self.__name + " "+ str(self.age)+"years old " + self.gender