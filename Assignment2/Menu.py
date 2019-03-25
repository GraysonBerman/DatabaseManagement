#Grayson Berman
#Student ID: 1760244
#berma117@mail.chapman.edu
#Assignment2

#Description:
#This program is a python program that executes SQLite commands based on user input.
#This is the menu file which imports code from the Student file, creates menu options, and creates functions
#which alter the database

import sqlite3
from Student import Student

class Menu:
    """This menu class is used to display the menu, make selections, and alter the database"""
    conn = sqlite3.connect("StudentDB.db")
    cursor = conn.cursor()

    """This displays the menu and the db"""
    def displayMenu(self):
        Menu.cursor.execute("SELECT * FROM Student")
        result = Menu.cursor.fetchall()
        for x in result:
            print (x)
        Menu.conn.commit()


    """This is called so that the user can enter student information and make a student record"""
    def createStudent(self):
        while True:
            try:
                student_id = str(input("Enter the student's ID: "))
                first_name = str(input("Enter the student's first name: "))
                last_name = str(input("Enter the student's last name: "))
                gpa = str(input("Enter the student's GPA"))
                major = str(input("Enter the student's major"))
                faculty_advisor = str(input("Enter the student's faculty advisor"))
                tempStudent = Student(student_id, first_name, last_name, gpa, major, faculty_advisor)
                Menu.cursor.execute("INSERT INTO Student('student_id', 'first_name', 'last_name', 'gpa', 'major', 'faculty_advisor'"
                                           "VALUES (?, ?, ?, ?, ?, ?)", tempStudent.getStudentTuple())
                Menu.conn.commit()
                break

            except ValueError:
                print("One of your inputs was invalid: either it was the wrong type or it exceeded the number of allowed characters. Try again: ")

    """This is called to drop a student from the student DB"""
    def deleteStudent(self):
        while True:
            try:
                student = input("Enter the student's ID that you want to delete from the database as an integer. This won't harm them: ")
                break
            except ValueError:
                print("Invalid input. Either you didn't enter an integer or you entered too many numbers. Enter an integer: ")

        Menu.cursor.execute("DROP FROM Student WHERE student_id = '{0}'".format(student))
        Menu.conn.commit()


    """This alters a student's major, faculty advisor, or both"""
    def updateStudent(self):
        while True:
            try:
                student = int(input("Enter the student's ID that you want to update"))
                selection = int(input("Enter the corresponding numbers to make changes: 1) change advisor, 2) change major, 3) change both: "))
                break
            except ValueError:
                print("One of your inputs was invalid: either it was the wrong type (not a 1, 2, or 3) or it exceeded the number of allowed characters. Try again: ")

        if selection == 1:
            faculty_advisor = input("Enter new faculty advisor: ")
            Menu.cursor.execute("UPDATE Student SET faculty_advisor = ? WHERE StudentID == ?", faculty_advisor, student)

        elif selection == 2:
            major = input("Enter new major: ")
            Menu.cursor.execute("UPDATE Student SET major = ? WHERE StudentID == ?", major, student)

        elif selection == 3:
            faculty_advisor = input("Enter new faculty advisor: ")
            major = input("Enter new major: ")
            Menu.cursor.execute("UPDATE Student SET faculty_advisor = ? WHERE StudentID == ?", faculty_advisor, student)
            Menu.cursor.execute("UPDATE Student SET major = ? WHERE StudentID == ?", major, student)

        else:
            print(selection)
        Menu.conn.commit()


    """This allows the user to search for student records filtered by gpa, major, or faculty_advisor"""
    def findStudent(self):
        while True:
            try:
                gpa = int(input("Do you want to search my gpa? 1 for yes, 2 for no: "))
                major = int(input("Do you want to search by major? 1 for yes, 2 for no: "))
                faculty_advisor = int(input("Do you want to search by advisor? 1 for yes, 2 for no: "))
                break

            except ValueError:
                print("Invalid input for one of the options. Enter 1 for yes or 2 for 0: ")


        while True:
            try:
                if gpa == 1:
                    findGpa = input("Enter GPA: ")
                    Menu.cursor.execute("SELECT * FROM Student WHERE gpa == '{0}'".format(findGpa))
                    gpaResult = Menu.cursor.fetchall()
                    if gpaResult != []:
                        for x in gpaResult:
                            print(x)
                    break
            except ValueError:
                print("Invalid input for gpa. Please re-enter the new gpa")

        if major == 1:
            findMajor = input("Enter the major to search for: ")
            Menu.cursor.execut("SELECT * FROM Student WHERE Major == '{0}'".format(findMajor))
            majorResult = Menu.cursor.fetchall()
            if majorResult != []:
                for x in majorResult:
                    print(x)

        if faculty_advisor == 1:
            findAdvisor = input("Enter the faculty advisor to search for: ")
            Menu.cursor.execute("SELECT * FROM Student WHERE faculty_advisor == '{0}'".format(findAdvisor))
            advisorResult = Menu.cursor.fetchall()
            if advisorResult != []:
                for x in advisorResult:
                    print x


    """This prints out a record"""
    def Print(self):
        for x in self:
            print(x)
