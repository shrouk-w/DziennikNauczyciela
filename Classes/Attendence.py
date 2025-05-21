from datetime import date

from Classes.TypeOfAttendence import TypeOfAttendence


class Attendence:
    def __init__(self, nameOfClass, typeOfAttendence): # hintery i wyjątki jak zły typ
        self.nameOfClass = nameOfClass
        self.typeOfAttendence = TypeOfAttendence(typeOfAttendence)
        self.dateOfAttendence = date.today()