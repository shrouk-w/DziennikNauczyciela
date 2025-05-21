from Classes.StudentManager import StudentManager


class Student(StudentManager):
    id = 1
    def __init__(self, name, lastName, pesel, className = ""): # hintery, sprawdzić czy pesel ma 11 cyfr
        self.id = Student.id
        Student.id += 1
        self.name = name
        self.lastName = lastName
        self.pesel = pesel
        self.grades = []
        self.attendance = []
        if className == "":
            StudentManager.add_student(self)
        else:
            StudentManager.add_student_assinged(self, className)

    def __str__(self):
        return str(self.id) + " " +self.name + " " + self.lastName + " " + self.pesel