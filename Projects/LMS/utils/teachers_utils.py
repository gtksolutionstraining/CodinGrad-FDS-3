from config import LMS
def add_teacher():
    teacher_name = input("Enter Teacher Name")
    teacher_id = input("Enter teacher ID")
    LMS['TEACHERS'][teacher_name] = teacher_id