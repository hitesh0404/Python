from department import *
class Staff:
    def __init__(self,staff_name,staff_role,department_name:Department,department_id):
        self.staff_name = staff_name
        self.staff_role = staff_role
        self.department_name= department_name
        self.department_id= department_id
    def display(self):
        print(f"Name : {self.staff_name} , Role : {self.staff_role} , Department Name : {self.department_name}")

staffs = []        
def create_staff():
    name = input("Enter Staff name: ")
    role = input("Enter Staff role: ")
    department_id= input("Enter Department ID: ")
    department_name = find_department_by_id(department_id)
    s= Staff(name,role,department_id,department_name)
    staffs.append(s)

def view_staff():
    if not staffs:
        print("staff not found")
    else:
        for s in staffs:
            s.display()

