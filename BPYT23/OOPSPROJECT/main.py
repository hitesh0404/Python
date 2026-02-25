from department import *
from doctor import *
from patient import *
from hospital import *
from appointment import *
from specialist import *
from staff import *

while True:
    print("""
        1.Create new staff
        2.View staff
        3.Add patient
        4.View patients
        5.Add Doctor
        6.View Doctor
        7.Add department
        8.View Departments
        9.Add Specility
        10.View Specialitis
        11.Add Appointment
        12.View Appointment
        13.Exit
        """)
    choice = int(float(input("enter choice: ")))
    match choice:
        case 1:
            create_staff()
        case 2:
            view_staff()
        case 3:
            add_patient()
        case 4:
            view_patient()
        case 5:
            Add_Doctor()
        case 6:
            View_Doctor()
        case 7:
            add_department()
        case 8:
            view_department()
        case 9:
            add_speciality()
        case 10:
            view_speciality()
        case 11:
            make_appointment()
        case 12:
            view_appointment()
        case 13:
            break