from patient import *
from doctor import *
from time import time
from datetime import date

class Appointment:
    def __init__(self,doctor:Doctor, patient:Patient,date:date, time = time()):
        self.time = time
        self.date = date
        self.doctor = doctor
        self.patient = patient
        # self.appointment_id = appointment_id
        
    def display_info(self):
        print(f"Patient Name: {self.patient.patient_name}")
        print(f"Doctor: {self.doctor.name}")
        print(f"Date: {self.date}")
        print(f"Time: {self.time}")
        
appointments = []
def make_appointment():
    if not patients or not doctors:
        print("Add both patients and doctors before making an appointment.")
        return
    print("\nAvailable Patients:")
    for i, p in enumerate(patients):
        print(f"{i+1}. {p.patient_name}")
    p_choice = int(input("Select patient number: "))-1
    p_obj=get_patient_by_id(p_choice)
    if not p_obj:
        raise Exception("No patient found")
    print("\nAvailable Doctors:")
    for i, d in enumerate(doctors):
        print(f"{i+1}. {d.name} ")
    d_choice = int(input("Select doctor number: ")) -1
    d_obj = doctors[d_choice] if len(doctors)>d_choice and d_choice>-1 else exec(" raise Exception('invalid choice for dr')")

    date = input("Enter appointment date (e.g., 10-Nov-2025): ")
    time = input("Enter appointment time (e.g., 11:00 AM): ")

    appt = Appointment(d_obj, p_obj, date, time)
    appointments.append(appt)
    print(appt.__dict__)
    print("Appointment booked successfully!")

def view_appointment():
    if not appointments:
        print("No appointments found.")
        return
    for appt in appointments:
        appt.display_info()
