# each python file is a module
from pythonFiles.student_class import Student
class Classroom:
    def __init__(self,students,subject,mode,std):
        self.students = students 
        self.subject = subject
        self.mode = mode
        self.std = std

raj = Student("Raj",12,"Male")
raju = Student("Raju",13,"Male")
rajesh = Student("Rajesh",11,"Male")
rakesh = Student("Rakesh",12,"Male")

class5 = Classroom(
    [raj,raju,rajesh,rakesh],
    "History","offline","5th")

for s in class5.students:
    print(s)

print(class5.students[0])