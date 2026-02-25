from  hospital import Hospital
from doctor import *
from department import *
class Patient:
    def __init__(self,patient_id,patient_name,patient_age,patient_location,patient_contact,patient_bloodgroup,department: Department, department_id,doctor_id,doctor:Doctor):
        self.patient_id = patient_id
        self.patient_name = patient_name
        self.patient_age = patient_age
        self.patient_location = patient_location
        self.patient_contact = patient_contact
        self.patient_bloodgroup =patient_bloodgroup
        self.department = department
        self.department_id = department_id
        self.doctor_id=doctor_id
        self.doctor = doctor

    def display(self):
        print(f" ID : {self.patient_id} , NAME : {self.patient_name} , AGE : {self.patient_age} ,CONTACT : {self.patient_contact} ,LOCATION : {self.patient_location} , BLOODGROUP : {self.patient_bloodgroup} , Doctor Name : {self.doctor} , Department : {self.department}")
patients = []
def add_patient():
    patient_id = int(input("Enter patient id : "))
    patient_name = input("Enter patient name : ")
    patient_age = int(input("Enter patient age : "))
    patient_location = input("Enter patient location : ")
    patient_contact = input("Enter patient contact : ")
    patient_bloodgroup = input("Enter patient bloodgroup : ")
    department_id = input("Enter department id: ")
    department_name = find_department_by_id(department_id)
    doctor_id = int(input("Enter your doctor Id: "))
    doctor_name= find_doctor_by_doctor_id(doctor_id)
    p =  Patient(patient_id,patient_name,patient_age,patient_location,patient_contact,patient_bloodgroup,department_id,department_name,doctor_id,doctor_name)
    patients.append(p)
def view_patient():
    if not patients:
        print("patients not found : ")
    else:
        for p in patients:
            p.display()
def get_patient_by_id(id):
    # for s in patients:
    #     if s.patient_id == id:
    #         return s
    if len(patients)>id and id>-1:
        return patients[id]    
    return None

        