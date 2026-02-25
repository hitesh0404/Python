from contact import Contacts
from person import Person
import os

raj = Person("Raj","Rathod")
c1 = Contacts(8764321112)
raj.contacts["home"] = c1

def clear_terminal():
    # Check the operating system
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For Linux/macOS (and other Unix-like systems)
        os.system('clear')
print(raj)

c1.number = 534534525
raj.contacts["office"] = Contacts(63732486432)

persons = []
persons.append(raj)
def show_all_persons():
    for i,val in enumerate(persons):
        print(f"{i}. {val.fname}  {val.lname}")

def view_person():
    show_all_persons()
    index = int(input("enter the id "))
    print(persons[index])
    return index
def add_or_new_contact_for_a_person():
    index = view_person()
    title,contact = Contacts.create_new_contact()
    persons[index].contacts[title] = contact


def delete_person():
    index = view_person()
    persons.remove(persons[index])
    print("Deleted!")


options = """ 

1 : To view the List 
2 : To view the Contacts of a person
3 : To add new Person
4 : To add new contact for a person
5 : To delete person 
"""
choice = -1

while (choice != 0):
    print(options)
    choice = int(input("enter the choice "))
    match choice:
        case 1:
            clear_terminal()
            show_all_persons()
        case 2:
            clear_terminal()
            view_person()
        case 3: 
            clear_terminal()
            persons.append(Person.add_new_person())
        case 4 :
            clear_terminal()
            add_or_new_contact_for_a_person()
        case 5:
            clear_terminal()
            delete_person()
        case _: 
            clear_terminal()
            print("onvalid input")
