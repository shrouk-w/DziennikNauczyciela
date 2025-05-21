from Classes.StudentManager import StudentManager


class Student(StudentManager):
    def __init__(self, name, lastName, pesel, className = ""):
        self.name = name
        self.lastName = lastName
        self.pesel = pesel
        if className == "":
            StudentManager.add_student(self)
        else:
            StudentManager.add_student_assinged(self, className)

    def __str__(self):
        return str(self.id) + " " +self.name + " " + self.lastName + " " + self.pesel