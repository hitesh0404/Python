# step 1:
# pip install mysql-connector-python

# Step 2:
# Open Mysql 
# CREATE DATABASE peoplebase;

# step3:
# Open Pycharm or visual studio and create a file named as Employee.py
import mysql.connector
import pymysql

def link():
    # return pymysql.connect()
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Admin@123",
        database="batch23"
    )

def make_table():
    db = link()
    cur = db.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS person(
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100),
        age INT,
        city VARCHAR(100)
    )
    """)
    db.commit()
    db.close()

def add_person():
    name = input("Name: ")
    age = input("Age: ")
    city = input("City: ")
    db = link()
    cur = db.cursor()
    cur.execute("INSERT INTO person(name, age, city) VALUES (%s, %s, %s)", (name, age, city))
    db.commit()
    db.close()
    print("Saved")

def show_people():
    db = link()
    cur = db.cursor()
    cur.execute("SELECT * FROM person")
    rows = cur.fetchall()
    db.close()
    if rows:
        for r in rows:
            print(r[0], r[1], r[2], r[3])
    else:
        print("No records")

def edit_person():
    pid = input("Enter ID to update: ")
    name = input("New Name: ")
    age = input("New Age: ")
    city = input("New City: ")
    db = link()
    cur = db.cursor()
    cur.execute("UPDATE person SET name=%s, age=%s, city=%s WHERE id=%s",(name, age, city, pid))
    db.commit()
    db.close()
    print("Updated")

def remove_person():
    pid = input("Enter ID to delete: ")
    db = link()
    cur = db.cursor()
    cur.execute("DELETE FROM person WHERE id=%s",(pid,))
    db.commit()
    db.close()
    print("Deleted")

def menu():
    print("1 Add")
    print("2 View")
    print("3 Update")
    print("4 Delete")
    print("5 Exit")
    return input("Choose: ")

def main():
    make_table()
    while True:
        ch = menu()
        if ch == "1":
            add_person()
        elif ch == "2":
            show_people()
        elif ch == "3":
            edit_person()
        elif ch == "4":
            remove_person()
        elif ch == "5":
            break
        else:
            print("Try again")


import mysql.connector
if __name__ == "__main__":
    connection  = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Admin@123",
        database="batch23"
    )
    mycursor = connection.cursor()
    sql = """ 
    create table if not Exists petient (
                            id int primary key,
                            name varchar(20) not null,
                            age int check(age>0)
                            )
    """
    mycursor.execute(sql)

    values = [
        (4,"Rajesh",12),
        (5,"Raj",15)
    ]

    sql = "insert into petient(id,name,age) VALUES(%s, %s, %s)"

    # mycursor.executemany(sql,values)
    name = input("enter your name")
    mycursor.execute(f"insert into petient(id,name,age) VALUES(6,{name},13)")
    mycursor.execute("select * from petient ")
    for row in mycursor.fetchall():
        print(row)
    connection.commit()
    connection.close()

# step 4: run this file