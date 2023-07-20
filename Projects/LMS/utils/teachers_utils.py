def add_teacher(LMS):
    teacher_name = input("Enter Teacher Name")
    teacher_id = input("Enter teacher ID")
    LMS['TEACHERS'][teacher_name] = teacher_id