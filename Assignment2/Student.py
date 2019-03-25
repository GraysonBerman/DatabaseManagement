#Grayson Berman
#Student ID: 1760244
#berma117@mail.chapman.edu
#Assignment2

#Description:
#This program is a python program that executes SQLite commands based on user input.
#This is the Student file which creates a Student Class. It is used in the database manipulation function.

#I Used this video for class construction: https://www.youtube.com/watch?v=apACNr7DC_s . It's also why I tried 
#using different naming conventions (like student_id instead of studentID). I think these are the proper
#python naming conventions.

import sqlite3

class Student:
    """This is a student class that contains the student's ID, first name, last name, GPA, Major, and Faculty Advisor"""
    def __init__(self, student_id, first_name, last_name, gpa, major, faculty_advisor):
        self.student_id = student_id
        self.first_name = first_name
        self.last_name = last_name
        self.gpa = gpa
        self.major = major
        self.faculty_advisor = faculty_advisor

    """All get functions below return an attribute or a full record"""
    def getStudentId(self):
        return self.student_id

    def getFirstName(self):
        return self.first_name

    def getLastName(self):
        return self.last_name

    def getGpa(self):
        return self.gpa

    def getMajor(self):
        return self.major

    def getFacultyAdvisor(self):
        return self.faculty_advisor

    def getStudentTuple(self):
        """Returns the touple of one student in following format: student_id, first_name, last_name, gpa, major, faculty_advisor"""
        return self.getStudentId(), self.getFirstName(), self.getLastName(), self.getGpa(), self.getMajor(), self.getFacultyAdvisor()


    """getConn andd getCursor are used for connecting and using the database"""
    def getConn(self):
        conn = sqlite3.connect("StudentDB.db")
        return conn

    def getCursor(self):
        conn = self.getConn()
        cursor = conn.cursor()
        return cursor
