﻿from datetime import date

from Classes.Exceptions import (
    InvalidGradeType,
    InvalidDescriptionType,
    InvalidClassNameType)
from Classes.TypeOfGrade import TypeOfGrade


class Grade:
    def __init__(self, grade: int | float, desc: str, nameOfClass: str, type: int | TypeOfGrade, date: date = date.today()) -> None:
        if not isinstance(grade, (int, float)):
            raise InvalidGradeType("Ocena musi być liczbą")
        if grade < 1 or grade > 6:
            raise InvalidGradeType("oceny mieszczą się w przedziale 1-6")
        if not isinstance(desc, str):
            raise InvalidDescriptionType("Opis musi być w postaci tekstu")
        if not isinstance(nameOfClass, str):
            raise InvalidClassNameType("Nazwa klasy musi być w postaci tekstu")

        self.grade = grade
        self.desc = desc
        self.nameOfClass = nameOfClass
        self.type = TypeOfGrade(type)
        self.date = date

    def __str__(self) -> str:
        return f"grade: {self.grade} desc: {self.desc} from: {self.nameOfClass} type: {self.type} date: {self.date}"

