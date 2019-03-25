#Grayson Berman
#Student ID: 1760244
#berma117@mail.chapman.edu
#Assignment2

#Description:
#This program is a python program that executes SQLite commands based on user input.
#This is the main file which implements two other classes, Menu and Student, and calls the functions.

import sqlite3

#Import necessary classes
from Student import Student
from Menu import Menu

def displayMenu():
    print("Entering a number from 1 to 5 lets you select from the menu")
    print("1. Display all student records")
    print("2. Create and insert a student recrod")
    print("3. Update a student record")
    print("4. Delete a student record")
    print("5. Sort and Display students by gpa, major, or faculty advisor")

conn = sqlite3.connect("StudentDB.db")
cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS Student(student_id INTEGER PRIMARY KEY AUTOINCREMENT,first_name varchar(25),"
  "last_name varchar(25), gpa NUMERIC, major varchar(20), faculty_advisor varchar(25));")

conn.commit()

menu = Menu()
loop = True

displayMenu()
while(loop):
    try:
        choice = int(input("Enter an option from 1 to 5"))
        if(choice >= 0 and choice < 6):
            if(choice == 1):
                menu.displayMenu()
            elif(choice == 2):
                menu.createStudent()
            elif(choice == 3):
                menu.updateStudent()
            elif(choice == 4):
                menu.deleteStudent()
            elif(choice == 5):
                menu.findStudent()
        else:
            print("Incorrect input: the input should be an integer from 1 to 5")
            continue
    except ValueError:
        print("Incorrect input:")
        continue

    print()
    cont = input("Enter X to exit the program. Enter C to continue using the program")
    if(cont.lower() == 'x'):
        loop = False
    else:
        print()
        displayMenu()
