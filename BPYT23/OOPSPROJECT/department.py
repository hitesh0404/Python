class Department:
    def __init__(self,department_name,department_description,department_id):
        self.department_name = department_name 
        self.department_description = department_description
        self.department_id = department_id
    def display(self):
        print(f" Department Name : {self.department_name}, Description : {self.department_description}, id : {self.department_id} ")
departments= []
def add_department():
    name = input(" Enter department name : ")
    description = input(" Enter department Description : ")
    department_id = input(" Enter department ID : ")

    dp = Department(name, description,department_id)
    departments.append(dp)
def find_department_by_id(department_id):
    for d in departments:
        if d.department_id == department_id:
            return d.department_name
    return None
def view_department():
    if not departments:
        print(" no department found !")
    else:
        for d in departments:
            d.display()
