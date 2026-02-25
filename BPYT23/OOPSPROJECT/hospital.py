from department import Department
class Hospital:
    def __init__(self,hospital_name,hospital_location,department:Department):
        self.hospital_name = hospital_name
        self.location = hospital_location
        self.department = department