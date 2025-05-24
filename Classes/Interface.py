from datetime import date
from unittest import case

from Classes.Grade import Grade
from Classes.NameOfClass import NameOfClass
from Classes.Student import Student
from Classes.StudentManager import StudentManager
from Classes.TypeOfAttendence import TypeOfAttendence
from Classes.TypeOfGrade import TypeOfGrade
from Classes.Charts import Charts


class Interface:

    @classmethod
    def start(cls):  # trzeba dodac jeszcze kazdemu normalne oceny przykładowe i normalny attendence przykładowy
        NameOfClass.add_class("j. polski")
        NameOfClass.add_class("j. angielski")
        NameOfClass.add_class("matematyka")
        stud = Student("Jan","Kowalski","12312312312","1A")
        stud.add_grade(Grade(1,"","j. polski",TypeOfGrade.TEST, date.fromisocalendar(2025,5,1)))
        stud.add_grade(Grade(5,"","j. polski",TypeOfGrade.QUIZ))
        stud.add_grade(Grade(5,"","j. polski",TypeOfGrade.HOMEWORK))
        stud.add_grade(Grade(5,"","j. polski",TypeOfGrade.HOMEWORK))
        stud.add_grade(Grade(5,"","j. polski",TypeOfGrade.HOMEWORK))
        stud.add_grade(Grade(5,"","j. polski",TypeOfGrade.HOMEWORK))
        stud.add_grade(Grade(5,"","j. polski",TypeOfGrade.HOMEWORK))
        stud = Student("Jan2","Kowalski","12312312312","1A")
        stud = Student("Jan3","Kowalski","12312312312","1A")
        stud = Student("Jan4","Kowalski","12312312312","1A")
        stud = Student("Jan5","Kowalski","12312312312","1A")
        stud = Student("Michal","Kowalski","12312312312","1B")
        stud = Student("Michal2","Kowalski","12312312312","1B")
        stud = Student("Michal3","Kowalski","12312312312","1B")
        stud = Student("Michal4","Kowalski","12312312312","1B")
        stud = Student("Michal5","Kowalski","12312312312","1B")
        while True:
            print("----------Dziennik_Nauczyciela-----------")
            print("1. Dodaj nowego ucznia")
            print("2. Wybierz ucznia")
            print("3. Pokaż zagrożenia")
            print("4. Sprawdź obecność lub wystaw oceny") #to do
            print("5. Wstaw nową klasę")
            print("6. Usuń jedną z klas")
            print("7. Stwórz statystyki")
            print("8. dodaj nowy przedmiot") #to do
            print("9. usuń jeden z przedmiotów") #to do
            print("0. Wyjdź")
            print("-----------------------------------------")
            provided = input()
            match provided:
                case "0":
                    return
                case "1":
                    print()
                    print("Wpisz imię")
                    imie = input()
                    print("Wpisz nazwisko")
                    nazwisko = input()
                    print("Wpisz pesel")
                    pesel = input()
                    if(len(pesel) != 11):
                        return #tu wyjątek
                    print("Wpisz klasę do której chcesz przypisać ucznia lub '-' jeżeli nie chcesz na razie go przypisywać")
                    clas = input() #tu tez mozna sprwadzić czy format klasy to liczba - literka i wyjątek
                    if(clas == '-'):
                        student = Student(imie, nazwisko, pesel)
                    else:
                        student = Student(imie, nazwisko, pesel, clas)
                    print("Dodano studenta: ")
                    print(student)
                case "2":
                    print()
                    print("1. chce wybrać ze wszystkich uczniów")
                    print("2. chce wybrać z listy uczniów z danej klasy")
                    decision = input()
                    if(decision == '1'):
                        StudentManager.show_all_students()
                    elif(decision == '2'):
                        StudentManager.show_all_classes()
                        print("wpisz klasę")
                        clas = input()
                        StudentManager.show_class_students(clas)
                    print("wpisz id studenta ktory cię intereuje")
                    id = input()
                    print("wybrałeś studenta")
                    student = StudentManager.get_student(int(id)) #wyjatek jak zwróci None nie ma studenta
                    print(student)
                    print("grades: ")
                    for grade in student.grades:
                        print(grade.grade)
                    print("attendance: ")
                    for attendance in student.attendance:
                        print(attendance.typeOfAttendence)
                    print("------wybierz co chcesz zrobić-------")
                    print("1. edytuj dane studenta")
                    print("2. edytuj ocenę studenta") #to do
                    print("3. edytuj obecność studenta") #to do
                    print("4. wyświetl średnią")
                    print("5. wyświetl czy jest zagrożony")
                    print("6. przypisz do innej klasy")
                    print("0. usuń studenta")
                    print("-------------------------------------")
                    decision = input()
                    match decision:
                        case "1":
                            print("chce zmienić imię T/N")
                            dec = input()
                            if(dec == 'T'):
                                print("podaj imie: ")
                                name = input()
                                student.name = name
                            print("chce zmienic nazwisko T/N")
                            dec = input()
                            if(dec == 'T'):
                                print("podaj nazwisko: ")
                                nazwisko = input()
                                student.nazwisko = nazwisko
                            print("chce zmienic pesel T/N")
                            dec = input()
                            if(dec == 'T'):
                                print("podaj pesel: ")
                                pesel = input()
                                if(len(pesel) != 11):
                                    return #tu dac wyjątek
                                student.pesel = pesel

                        case "2":
                            pass
                        case "3":
                            pass
                        case "4":
                            print(student.avarage())
                        case "5":
                            if(student.is_failling()):
                                print("zagrożony")
                            else:
                                print("niezagrożony")
                        case "6":
                            print("podaj klase: ")
                            nclas = input()
                            StudentManager.reassign_class(student, nclas)
                        case "0":
                            StudentManager.delete_student(student)
                        case _:
                            print("nie ma takiej opcji")

                case "3":
                    StudentManager.show_all_students_failling()
                case "4":
                    StudentManager.show_all_classes()
                    print("wpisz klasę")
                    clas = input()
                    if not StudentManager.isClass(clas):
                        return # dac wyjatek
                    print("wpisz przedmiot z listy: ")
                    NameOfClass.show_class_names()
                    clasname = input()
                    if not NameOfClass.isNameOfClass(clasname):
                        return # dac wyjatek
                    print("co chcesz zrobić: ")
                    print("1. sprawdzić listę obecności")
                    print("2. wystawić ocenę")
                    dec = input()
                    if(dec == '1'):
                        StudentManager.checkAttendence(clas, clasname)
                    elif(dec == '2'):
                        StudentManager.show_class_students(clas)
                        print("wpisz id ucznia ktoremu chcesz wstawic ocene")
                        id = input()
                        stud = StudentManager.get_student(int(id))
                        if(stud is None):
                            return # wyjątek nie zanleziono taikego ucznia
                        print("wpisz ocene (przdział 1-6)")
                        grade = float(input())
                        print("wpisz opis")
                        desc = input()
                        print("podaj typ: ")
                        print("--legenda--")
                        print("1. praca domowa")
                        print("2. kartkówka")
                        print("3. sprawdzian")
                        print("-----------")
                        type = int(input())
                        stud.add_grade(Grade(grade,desc,clasname, type))
                    else:
                        print("nie ma takiej opcji")
                case "5":
                    print("podaj klase")
                    clas = input()
                    StudentManager.add_class(clas)
                case "6":
                    print("podaj klase")
                    clas = input()
                    StudentManager.delete_class(clas)
                case "7":
                    print("----------------------------------------------------------")
                    print("1. chce wygenerować statystyki dla wszystkich uczniów")
                    print("2. chce wygenerować statystyki dla jednej klasy")
                    print("3. chce wygenerować statystyki dla jednego ucznia")
                    print("----------------------------------------------------------")
                    dec = input()
                    match dec:
                        case "1":
                            Charts.plot_student_averages(StudentManager.allStudents)
                            Charts.plot_attendance_distribution(StudentManager.allStudents)
                        case "2":
                            StudentManager.show_all_classes()
                            print("wybierz klasę")
                            clas = input()
                            Charts.plot_student_averages(StudentManager.classMap[clas])
                            Charts.plot_attendance_distribution(StudentManager.classMap[clas])
                        case "3":
                            StudentManager.show_all_students()
                            print("wybierz id ucznia")
                            id = input()
                            stud = StudentManager.get_student(int(id))
                            Charts.plot_student_grades_over_time(stud)
                        case _:
                            print("nie ma takiej opcji")

                case _:
                    print("nie ma takiej opcji")




