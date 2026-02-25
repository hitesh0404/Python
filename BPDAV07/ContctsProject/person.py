from contact import Contacts
class Person:
    def __init__(self,fname,lname,contact:dict=dict.fromkeys(["home","office","business","personal"])):
        self.fname = fname
        self.lname = lname
        self.contacts = contact
    def __str__(self):
        numbers = ""
        for key,value in self.contacts.items():
            if value is not None:
                numbers +=f"\n {key} : {value}"
        return f""" 
                {self.fname} {self.lname}
                {numbers}
            """
    @staticmethod
    def add_new_person():
        fname = input("Enter First name : ")
        lname = input("Enter Last name : ")
        title,contact = Contacts.create_new_contact()
        return Person(fname,lname,{title:contact})