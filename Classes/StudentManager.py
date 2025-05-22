

class StudentManager():
    allStudents = [] # for checking if student already is in our base
    unsignedStudents = []
    classMap = {}

    @classmethod
    def add_student(cls, student): # dodac hintery i wyjatki jak zle typy danych
        cls.allStudents.append(student)  # wyjatek jak student juz tu jest
        cls.unsignedStudents.append(student)

    @classmethod
    def add_student_assinged(cls, student, className: str): # dodac hintery i wyjatki jak zle typy danych
        cls.allStudents.append(student)  # wyjatek jak student juz tu jest
        if not className in cls.classMap:
            cls.classMap[className] = []
        cls.classMap[className].append(student)


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
    def show_unsigned_students(cls):
        for stud in cls.unsignedStudents:
            print(stud)

    @classmethod
    def show_class_students(cls, className: str): # tu mozna dać wyjątek jak nie ma takiej klasy
        print(f"{className}:")
        for stud in cls.classMap[className]:
            print(stud)

    @classmethod
    def delete_student(cls, student):  #hintery i wyjątki jak złe typy
        if cls.allStudents.count(student) == 0:
            return # dodać wyjątek jeżeli studenta nie ma w all students
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
        #mozna dac wyjatek jak juz jest

    @classmethod
    def delete_class(cls, className):
        if className in cls.classMap:
            cls.classMap.pop(className, None)
        # mozna dac wyjatek jak nie ma

    @classmethod
    def show_all_classes(cls):
        for className in cls.classMap:
            print(f"{className}")

    @classmethod
    def assign_student(cls, student, className):
        if cls.allStudents.count(student) == 0:
            return # wyjatek można dać
        if cls.unsignedStudents.count(student) == 0:
            return # wyjątek można dać
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
