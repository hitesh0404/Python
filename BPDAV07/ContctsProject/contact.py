import time
class Contacts:
    def __init__(self, number:int):
        object.__setattr__(self, "number", number)
        object.__setattr__(self, "added_on", time.time())
        object.__setattr__(self, "updated_on", time.time())

    def __str__(self):
        return f"{self.number} added on {self.added_on} and updated on {self.updated_on}"

    def __setattr__(self, name, value):
        if name == "number":
            object.__setattr__(self, "updated_on", time.time())
        object.__setattr__(self, name, value)
    @staticmethod
    def create_new_contact():
        print(f"""
        Contact Number Title Types
        home :
        office : 
        personal : 
        business :
        """)
        title = input("enter the tite of Contact ")
        return title,Contacts(int(input("Enter the Number : ")))