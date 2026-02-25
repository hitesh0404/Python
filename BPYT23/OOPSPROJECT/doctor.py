from specialist import *
from department import *
class Doctor:
    def __init__(self, name:str, contact:str,Dr_id:str,department_id,department:Department,speciality:Specalist,speciality_name):
        self.name = name
        self.contact = contact
        self.Dr_id = Dr_id
        self.department_id = department_id
        self.deaprtment = department
        self.speciality  =  speciality
        self.speciality_name = speciality_name
    def display(self):
        print(f" Doctor Name : {self.name} , Contact : {self.contact} ,  Dr_id :{self.Dr_id} , Department Name : {self.deaprtment} ,  Speciality_name : {self.speciality_name}")


doctors = []
def Add_Doctor():
    name = input("Enter Doctor name : ")
    contact = input("enter doctor contact : ")
    Dr_id = input("Enter  doctor id : ")
    Department_id = input("Enter department id : ")
    department = find_department_by_id(Department_id)
    speciality_id= input("Enter Doctor speciality ID: ") 
    speciality_name = find_specility(speciality_id)
    dr = Doctor(name , contact, Dr_id,Department_id,department,speciality_id,speciality_name)
    doctors.append(dr)
def View_Doctor():
    if not doctors:
        print("no doctors found :")
    else:
        for d in doctors:
            d.display()
def find_doctor_by_doctor_id(doctor_id):
    for d in doctors:
        if d.Dr_id == doctor_id:
            return d.name
    return None


