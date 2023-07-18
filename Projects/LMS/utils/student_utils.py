from config import LMS

def add_student():
    name = input("Enter Student name")
    roll_number = input("Enter Roll Number")
    LMS['STUDENTS'][name] = roll_number