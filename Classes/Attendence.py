from datetime import date

from Classes.TypeOfAttendence import TypeOfAttendence
from Classes.Exceptions import (
    InvalidAttendenceClassName,
    InvalidTypeOfAttendence
)


class Attendence:
    def __init__(self, nameOfClass:str, typeOfAttendence, date=date.today()):
        if not isinstance(nameOfClass, str):
            raise InvalidAttendenceClassName("Nazwa klasy musi być w postaci tekstu")

        self.nameOfClass = nameOfClass
        self.typeOfAttendence = TypeOfAttendence(typeOfAttendence)
        self.dateOfAttendence = date

    def __str__(self):
        return f"from: {self.nameOfClass} type: {self.typeOfAttendence} date: {self.dateOfAttendence}"