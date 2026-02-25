class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def __str__(self):
        return f"my is {self.name} and i am {self.age} years old"