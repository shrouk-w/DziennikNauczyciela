from Classes.Attendence import Attendence
from Classes.Exceptions import StudentAlreadyExists

class StudentManager():
    allStudents = []
    unsignedStudents = []
    classMap = {}

    @classmethod
    def add_student(cls, student):
        if student in cls.allStudents:
            raise StudentAlreadyExists("Student jest juz zapisany w systemie")
        cls.allStudents.append(student)
        cls.unsignedStudents.append(student)

    @classmethod
    def add_student_assigned(cls, student, className: str):
        if student in cls.allStudents:
            raise StudentAlreadyExists("Student jest juz zapisany w systemie")
        cls.allStudents.append(student)
        if not className in cls.classMap:
            cls.classMap[className] = []
        cls.classMap[className].append(student)

    @classmethod
    def reassign_class(cls,student,newClass):
        for clas, studs in cls.classMap.items():
            if student in studs:
                cls.classMap[clas].remove(student)
                break
        if not newClass in cls.classMap:
            cls.classMap[newClass] = []
        cls.classMap[newClass].append(student)


    @classmethod
    def show_all_students(cls):
        for className, students in cls.classMap.items():
            print(f"{className}:")
            for student in students:
                print(f"  {student}")
        if len(cls.unsignedStudents) != 0:
            print("unsigned:")
            for student in cls.unsignedStudents:
                print(f"  {student}")

    @classmethod
    def show_all_students_failling(cls):
        for className, students in cls.classMap.items():
            print(f"{className}:")
            for student in students:
                if student.is_failling():
                    print(f"  {student}")
        if len(cls.unsignedStudents) != 0:
            print("unsigned:")
            for student in cls.unsignedStudents:
                if student.is_failling():
                    print(f"  {student}")



    @classmethod
    def show_unsigned_students(cls):
        for stud in cls.unsignedStudents:
            print(stud)

    @classmethod
    def show_class_students(cls, className: str):
        print(f"{className}:")
        for stud in cls.classMap[className]:
            print(stud)

    @classmethod
    def delete_student(cls, student):
        if cls.allStudents.count(student) == 0:
            return
        cls.allStudents.remove(student)
        if student in cls.unsignedStudents:
            cls.unsignedStudents.remove(student)
            return
        for className, students in cls.classMap.items():
            if student in students:
                students.remove(student)
                return

    @classmethod
    def add_class(cls, className):
        cls.classMap[className] = []


    @classmethod
    def delete_class(cls, className):
        if className in cls.classMap:
            for student in cls.classMap[className]:
                cls.unsignedStudents.append(student)
            cls.classMap.pop(className, None)


    @classmethod
    def show_all_classes(cls):
        for className in cls.classMap:
            print(f"{className}")

    @classmethod
    def assign_student(cls, student, className):
        if cls.allStudents.count(student) == 0:
            return
        if cls.unsignedStudents.count(student) == 0:
            return
        cls.unsignedStudents.remove(student)
        if not className in cls.classMap:
            cls.classMap[className] = []
        cls.classMap[className].append(student)

    @classmethod
    def get_student(cls, id):
        for stud in cls.allStudents:
            if stud.id == id:
                return stud
        return None

    @classmethod
    def isClass(cls, className):
        return className in cls.classMap

    @classmethod
    def checkAttendence(cls, className, NameOfClass):
        print("---------legenda--------")
        print("-1. nie ma")
        print("0. spóźniony")
        print("1. obecny")
        print("2. usprawiedliwiony")
        print("------------------------")
        for stud in cls.classMap[className]:
            print(stud.name + " " + stud.lastName)
            dec = input()
            stud.add_attendance(Attendence(NameOfClass, int(dec)))
