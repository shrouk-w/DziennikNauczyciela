from Classes.Grade import Grade
from Classes.StudentManager import StudentManager
from Classes.Attendence import TypeOfAttendence, Attendence
from Classes.Exceptions import InvalidStudentData, InvalidPesel


class Student(StudentManager):
    id = 1
    def __init__(self, name: str, lastName: str, pesel: str, className: str = "") -> None:
        if not all(isinstance(val, str) for val in [name, lastName]):
            raise InvalidStudentData("Imię i nazwisko muszą być w postaci tekstu")
        if len(pesel) != 11:
            raise InvalidPesel("Pesel musi miec 11 cyfr")

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
            StudentManager.add_student_assigned(self, className)

    def __str__(self) -> str:
        return str(self.id) + " " +self.name + " " + self.lastName + " " + self.pesel


    def add_grade(self, grade: Grade) -> None:
        self.grades.append(grade)

    def add_attendance(self, attendance: Attendence) -> None:
        self.attendance.append(attendance)

    def avarage(self) -> float:
        if len(self.grades) <= 0 :
            return 0 # rzucić wyjątek
        suma = 0
        for grade in self.grades:
            suma += grade.grade
        return suma / len(self.grades)

    def is_failling(self) -> bool:
        if self.avarage() < 3:
            return True

        attendance_by_class = {}

        for a in self.attendance:
            if a.nameOfClass not in attendance_by_class:
                attendance_by_class[a.nameOfClass] = []
            attendance_by_class[a.nameOfClass].append(a.typeOfAttendence)

        for subject, attendances in attendance_by_class.items():
            total = len(attendances)
            lates = attendances.count(TypeOfAttendence.LATE)
            not_present = attendances.count(TypeOfAttendence.NOTPRESENT)

            if total > 0 and lates / total > 0.5:
                return True

            if not_present >= 2:
                return True

        return False

