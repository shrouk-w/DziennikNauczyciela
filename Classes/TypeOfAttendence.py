from enum import Enum


class TypeOfAttendence(Enum):
    LATE = 0
    NOTPRESENT = -1
    PRESENT = 1
    JUSTIFIED = 2