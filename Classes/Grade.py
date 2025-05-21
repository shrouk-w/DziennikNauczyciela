from datetime import date

from Classes.TypeOfGrade import TypeOfGrade


class Grade:
    def __init__(self, grade, desc, nameOfClass, type): # hintery i wyjątki jak złe typy
        self.grade = grade
        self.desc = desc
        self.nameOfClass = nameOfClass
        self.type = TypeOfGrade(type)
        self.date = date.today() # przy dodawaniu oceny trzeba by sprawdzić czy student ma już obecność na tym przedmiocie z tą samą datą