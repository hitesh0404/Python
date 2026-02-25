from hospital import Hospital
from patient import Patient
from doctor import Doctor
from time import time
class Appointment:
    def __init__(self,doctor:Doctor,hospital:Hospital,patient:Patient,time_stamp=time()):
        self.time_stamp = time_stamp
        self.hospital = hospital
        self.doctor = doctor
        self.patient = patient
    
