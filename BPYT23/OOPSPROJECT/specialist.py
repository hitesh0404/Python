class Specalist:
    def __init__(self,speciality_name,speciality_id):
        self.speciality_name = speciality_name
        self.speciality_id = speciality_id
    def display(self):
        print(f" ID = { self.speciality_id},  type : {self.speciality_name} ")
specialitis=[]
def add_speciality():
    name = input("Enter speciality name: ")
    id= input("Enter speciality id: ")
    s=Specalist(name, id)
    specialitis.append(s)
def view_speciality():
    if not specialitis:
        print("no speciality found :")
    else:
        for s in specialitis:
            s.display()
    
    
def find_specility(speciality_id):
    for s in specialitis:
        if s.speciality_id == speciality_id:
            return s.speciality_name
    return None


    