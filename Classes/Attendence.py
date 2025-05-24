from datetime import date

from Classes.TypeOfAttendence import TypeOfAttendence
from Classes.Exceptions import (
    InvalidAttendenceClassName,
    InvalidTypeOfAttendence
)


class Attendence:
    def __init__(self, nameOfClass, typeOfAttendence):
        if not isinstance(nameOfClass, str):
            raise InvalidAttendenceClassName("Nazwa klasy musi być w postaci tekstu")
        if not isinstance(typeOfAttendence, str):
            raise InvalidTypeOfAttendence("Typ obecności musi być w postaci tekstu")

        self.nameOfClass = nameOfClass
        self.typeOfAttendence = TypeOfAttendence(typeOfAttendence)
        self.dateOfAttendence = date.today()