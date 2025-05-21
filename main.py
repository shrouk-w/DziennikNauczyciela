from Classes.Student import Student
from Classes.StudentManager import StudentManager

if __name__ == '__main__':
    student = Student("niga", "balls", "123")
    student1 = Student("niga", "balls", "123", "1A")
    student2 = Student("niga", "ballsack123", "123", "1A")
    student3 = Student("niga", "ballsack123", "123", "1BCD")
    student4 = Student("niga", "ballsack123", "123", "2BCD")
    student5 = Student("niga", "ballsack123", "123", "2A")
    StudentManager.show_all_students()
    StudentManager.delete_student(student1)
    StudentManager.delete_student(student2)
    StudentManager.delete_student(student3)
    StudentManager.delete_class("1A")
    StudentManager.show_all_students()
