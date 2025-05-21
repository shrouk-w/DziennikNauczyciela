from enum import Enum


class TypeOfAttendence(Enum):
    LATE = "late"
    NOTPRESENT = "notpresent"
    PRESENT = "present"
    JUSTIFIED = "justified"