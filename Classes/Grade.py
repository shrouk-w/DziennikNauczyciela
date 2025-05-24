from datetime import date

from Classes.Exceptions import (
    InvalidGradeType,
    InvalidDescriptionType,
    InvalidClassNameType)
from Classes.TypeOfGrade import TypeOfGrade


class Grade:
    def __init__(self, grade, desc, nameOfClass, type, date=date.today()):
        if not isinstance(grade, (int, float)):
            raise InvalidGradeType("Ocena musi być liczbą")
        if not isinstance(desc, str):
            raise InvalidDescriptionType("Opis musi być w postaci tekstu")
        if not isinstance(nameOfClass, str):
            raise InvalidClassNameType("Nazwa klasy musi być w postaci tekstu")

        self.grade = grade
        self.desc = desc
        self.nameOfClass = nameOfClass
        self.type = TypeOfGrade(type)
        self.date = date