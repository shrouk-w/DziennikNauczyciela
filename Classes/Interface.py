﻿from datetime import date
from unittest import case

from Classes.Attendence import Attendence
from Classes.Exceptions import InvalidStudentData, ClassDoesNotExist, InvalidClassNameType, InvalidGradeType, \
    InvalidPesel
from Classes.Grade import Grade
from Classes.NameOfClass import NameOfClass
from Classes.Student import Student
from Classes.StudentManager import StudentManager
from Classes.TypeOfAttendence import TypeOfAttendence
from Classes.TypeOfGrade import TypeOfGrade
from Classes.Charts import Charts


class Interface:

    @classmethod
    def start(cls) -> None:
        NameOfClass.add_class("j. polski")
        NameOfClass.add_class("j. angielski")
        NameOfClass.add_class("matematyka")

        stud = Student("Jan", "Kowalski", "12312312312", "1A")
        stud.add_grade(Grade(1, "", "j. polski", TypeOfGrade.TEST, date(2025, 5, 1)))
        stud.add_grade(Grade(5, "", "j. polski", TypeOfGrade.QUIZ, date(2025, 5, 2)))
        stud.add_grade(Grade(6, "", "j. angielski", TypeOfGrade.HOMEWORK, date(2025, 5, 3)))
        stud.add_grade(Grade(4, "", "matematyka", TypeOfGrade.HOMEWORK, date(2025, 5, 4)))
        stud.add_grade(Grade(3, "", "j. polski", TypeOfGrade.HOMEWORK, date(2025, 5, 5)))
        stud.add_attendance(Attendence("j. polski", TypeOfAttendence.LATE, date(2025, 5, 1)))
        stud.add_attendance(Attendence("matematyka", TypeOfAttendence.NOTPRESENT, date(2025, 5, 2)))
        stud.add_attendance(Attendence("j. angielski", TypeOfAttendence.JUSTIFIED, date(2025, 5, 3)))
        stud.add_attendance(Attendence("j. polski", TypeOfAttendence.PRESENT, date(2025, 5, 4)))
        stud.add_attendance(Attendence("matematyka", TypeOfAttendence.PRESENT, date(2025, 5, 5)))


        stud = Student("Anna", "Nowak", "11111111111", "1A")
        stud.add_grade(Grade(3, "", "j. angielski", TypeOfGrade.TEST, date(2025, 5, 2)))
        stud.add_grade(Grade(4, "", "j. angielski", TypeOfGrade.QUIZ, date(2025, 5, 3)))
        stud.add_grade(Grade(5, "", "matematyka", TypeOfGrade.HOMEWORK, date(2025, 5, 4)))
        stud.add_grade(Grade(2, "", "j. polski", TypeOfGrade.HOMEWORK, date(2025, 5, 5)))
        stud.add_grade(Grade(6, "", "j. angielski", TypeOfGrade.HOMEWORK, date(2025, 5, 6)))
        stud.add_attendance(Attendence("j. angielski", TypeOfAttendence.LATE, date(2025, 5, 2)))
        stud.add_attendance(Attendence("matematyka", TypeOfAttendence.PRESENT, date(2025, 5, 3)))
        stud.add_attendance(Attendence("j. polski", TypeOfAttendence.NOTPRESENT, date(2025, 5, 4)))
        stud.add_attendance(Attendence("j. angielski", TypeOfAttendence.JUSTIFIED, date(2025, 5, 5)))
        stud.add_attendance(Attendence("matematyka", TypeOfAttendence.PRESENT, date(2025, 5, 6)))


        stud = Student("Krzysztof", "Wiśniewski", "22222222222", "1A")
        stud.add_grade(Grade(4, "", "matematyka", TypeOfGrade.TEST, date(2025, 5, 3)))
        stud.add_grade(Grade(2, "", "j. polski", TypeOfGrade.QUIZ, date(2025, 5, 4)))
        stud.add_grade(Grade(5, "", "j. angielski", TypeOfGrade.HOMEWORK, date(2025, 5, 5)))
        stud.add_grade(Grade(3, "", "j. angielski", TypeOfGrade.HOMEWORK, date(2025, 5, 6)))
        stud.add_grade(Grade(4, "", "matematyka", TypeOfGrade.HOMEWORK, date(2025, 5, 7)))
        stud.add_attendance(Attendence("matematyka", TypeOfAttendence.PRESENT, date(2025, 5, 3)))
        stud.add_attendance(Attendence("j. polski", TypeOfAttendence.LATE, date(2025, 5, 4)))
        stud.add_attendance(Attendence("j. angielski", TypeOfAttendence.JUSTIFIED, date(2025, 5, 5)))
        stud.add_attendance(Attendence("matematyka", TypeOfAttendence.PRESENT, date(2025, 5, 6)))
        stud.add_attendance(Attendence("j. polski", TypeOfAttendence.NOTPRESENT, date(2025, 5, 7)))


        stud = Student("Maria", "Dąbrowska", "33333333333", "1A")
        stud.add_grade(Grade(6, "", "j. polski", TypeOfGrade.TEST, date(2025, 5, 4)))
        stud.add_grade(Grade(5, "", "j. angielski", TypeOfGrade.QUIZ, date(2025, 5, 5)))
        stud.add_grade(Grade(4, "", "matematyka", TypeOfGrade.HOMEWORK, date(2025, 5, 6)))
        stud.add_grade(Grade(3, "", "j. polski", TypeOfGrade.HOMEWORK, date(2025, 5, 7)))
        stud.add_grade(Grade(2, "", "j. angielski", TypeOfGrade.HOMEWORK, date(2025, 5, 8)))
        stud.add_attendance(Attendence("j. polski", TypeOfAttendence.PRESENT, date(2025, 5, 4)))
        stud.add_attendance(Attendence("j. angielski", TypeOfAttendence.LATE, date(2025, 5, 5)))
        stud.add_attendance(Attendence("matematyka", TypeOfAttendence.PRESENT, date(2025, 5, 6)))
        stud.add_attendance(Attendence("j. polski", TypeOfAttendence.JUSTIFIED, date(2025, 5, 7)))
        stud.add_attendance(Attendence("j. angielski", TypeOfAttendence.NOTPRESENT, date(2025, 5, 8)))


        stud = Student("Tomasz", "Zieliński", "44444444444", "1A")
        stud.add_grade(Grade(5, "", "j. angielski", TypeOfGrade.TEST, date(2025, 5, 5)))
        stud.add_grade(Grade(4, "", "matematyka", TypeOfGrade.QUIZ, date(2025, 5, 6)))
        stud.add_grade(Grade(6, "", "j. polski", TypeOfGrade.HOMEWORK, date(2025, 5, 7)))
        stud.add_grade(Grade(3, "", "j. angielski", TypeOfGrade.HOMEWORK, date(2025, 5, 8)))
        stud.add_grade(Grade(2, "", "matematyka", TypeOfGrade.HOMEWORK, date(2025, 5, 9)))
        stud.add_attendance(Attendence("j. angielski", TypeOfAttendence.PRESENT, date(2025, 5, 5)))
        stud.add_attendance(Attendence("matematyka", TypeOfAttendence.JUSTIFIED, date(2025, 5, 6)))
        stud.add_attendance(Attendence("j. polski", TypeOfAttendence.NOTPRESENT, date(2025, 5, 7)))
        stud.add_attendance(Attendence("j. angielski", TypeOfAttendence.LATE, date(2025, 5, 8)))
        stud.add_attendance(Attendence("matematyka", TypeOfAttendence.PRESENT, date(2025, 5, 9)))


        stud = Student("Michał", "Wójcik", "55555555555", "1B")
        stud.add_grade(Grade(2, "", "j. polski", TypeOfGrade.TEST, date(2025, 5, 6)))
        stud.add_grade(Grade(3, "", "matematyka", TypeOfGrade.QUIZ, date(2025, 5, 7)))
        stud.add_grade(Grade(4, "", "j. angielski", TypeOfGrade.HOMEWORK, date(2025, 5, 8)))
        stud.add_grade(Grade(5, "", "j. polski", TypeOfGrade.HOMEWORK, date(2025, 5, 9)))
        stud.add_grade(Grade(6, "", "matematyka", TypeOfGrade.HOMEWORK, date(2025, 5, 10)))
        stud.add_attendance(Attendence("j. polski", TypeOfAttendence.PRESENT, date(2025, 5, 6)))
        stud.add_attendance(Attendence("matematyka", TypeOfAttendence.LATE, date(2025, 5, 7)))
        stud.add_attendance(Attendence("j. angielski", TypeOfAttendence.NOTPRESENT, date(2025, 5, 8)))
        stud.add_attendance(Attendence("j. polski", TypeOfAttendence.JUSTIFIED, date(2025, 5, 9)))
        stud.add_attendance(Attendence("matematyka", TypeOfAttendence.PRESENT, date(2025, 5, 10)))


        stud = Student("Kacper", "Kamiński", "66666666666", "1B")
        stud.add_grade(Grade(3, "", "j. angielski", TypeOfGrade.TEST, date(2025, 5, 7)))
        stud.add_grade(Grade(2, "", "j. polski", TypeOfGrade.QUIZ, date(2025, 5, 8)))
        stud.add_grade(Grade(4, "", "matematyka", TypeOfGrade.HOMEWORK, date(2025, 5, 9)))
        stud.add_grade(Grade(5, "", "j. angielski", TypeOfGrade.HOMEWORK, date(2025, 5, 10)))
        stud.add_grade(Grade(6, "", "matematyka", TypeOfGrade.HOMEWORK, date(2025, 5, 11)))
        stud.add_attendance(Attendence("j. angielski", TypeOfAttendence.LATE, date(2025, 5, 7)))
        stud.add_attendance(Attendence("j. polski", TypeOfAttendence.PRESENT, date(2025, 5, 8)))
        stud.add_attendance(Attendence("matematyka", TypeOfAttendence.JUSTIFIED, date(2025, 5, 9)))
        stud.add_attendance(Attendence("j. angielski", TypeOfAttendence.NOTPRESENT, date(2025, 5, 10)))
        stud.add_attendance(Attendence("matematyka", TypeOfAttendence.PRESENT, date(2025, 5, 11)))


        stud = Student("Tomasz", "Lewandowski", "77777777777", "1B")
        stud.add_grade(Grade(5, "", "matematyka", TypeOfGrade.TEST, date(2025, 5, 8)))
        stud.add_grade(Grade(4, "", "j. polski", TypeOfGrade.QUIZ, date(2025, 5, 9)))
        stud.add_grade(Grade(3, "", "j. angielski", TypeOfGrade.HOMEWORK, date(2025, 5, 10)))
        stud.add_grade(Grade(2, "", "j. angielski", TypeOfGrade.HOMEWORK, date(2025, 5, 11)))
        stud.add_grade(Grade(6, "", "j. polski", TypeOfGrade.HOMEWORK, date(2025, 5, 12)))
        stud.add_attendance(Attendence("matematyka", TypeOfAttendence.PRESENT, date(2025, 5, 8)))
        stud.add_attendance(Attendence("j. polski", TypeOfAttendence.LATE, date(2025, 5, 9)))
        stud.add_attendance(Attendence("j. angielski", TypeOfAttendence.PRESENT, date(2025, 5, 10)))
        stud.add_attendance(Attendence("j. angielski", TypeOfAttendence.NOTPRESENT, date(2025, 5, 11)))
        stud.add_attendance(Attendence("j. polski", TypeOfAttendence.JUSTIFIED, date(2025, 5, 12)))


        stud = Student("Marek", "Zając", "88888888888", "1B")
        stud.add_grade(Grade(6, "", "j. polski", TypeOfGrade.TEST, date(2025, 5, 9)))
        stud.add_grade(Grade(5, "", "j. angielski", TypeOfGrade.QUIZ, date(2025, 5, 10)))
        stud.add_grade(Grade(4, "", "matematyka", TypeOfGrade.HOMEWORK, date(2025, 5, 11)))
        stud.add_grade(Grade(3, "", "j. polski", TypeOfGrade.HOMEWORK, date(2025, 5, 12)))
        stud.add_grade(Grade(2, "", "j. angielski", TypeOfGrade.HOMEWORK, date(2025, 5, 13)))
        stud.add_attendance(Attendence("j. polski", TypeOfAttendence.PRESENT, date(2025, 5, 9)))
        stud.add_attendance(Attendence("j. angielski", TypeOfAttendence.JUSTIFIED, date(2025, 5, 10)))
        stud.add_attendance(Attendence("matematyka", TypeOfAttendence.LATE, date(2025, 5, 11)))
        stud.add_attendance(Attendence("j. polski", TypeOfAttendence.PRESENT, date(2025, 5, 12)))
        stud.add_attendance(Attendence("j. angielski", TypeOfAttendence.NOTPRESENT, date(2025, 5, 13)))


        stud = Student("Filip", "Szymański", "99999999999", "1B")
        stud.add_grade(Grade(2, "", "j. angielski", TypeOfGrade.TEST, date(2025, 5, 10)))
        stud.add_grade(Grade(3, "", "matematyka", TypeOfGrade.QUIZ, date(2025, 5, 11)))
        stud.add_grade(Grade(4, "", "j. polski", TypeOfGrade.HOMEWORK, date(2025, 5, 12)))
        stud.add_grade(Grade(5, "", "j. polski", TypeOfGrade.HOMEWORK, date(2025, 5, 13)))
        stud.add_grade(Grade(6, "", "matematyka", TypeOfGrade.HOMEWORK, date(2025, 5, 14)))
        stud.add_attendance(Attendence("j. angielski", TypeOfAttendence.PRESENT, date(2025, 5, 10)))
        stud.add_attendance(Attendence("matematyka", TypeOfAttendence.JUSTIFIED, date(2025, 5, 11)))
        stud.add_attendance(Attendence("j. polski", TypeOfAttendence.LATE, date(2025, 5, 12)))
        stud.add_attendance(Attendence("j. polski", TypeOfAttendence.PRESENT, date(2025, 5, 13)))
        stud.add_attendance(Attendence("matematyka", TypeOfAttendence.NOTPRESENT, date(2025, 5, 14)))

        while True:
            print("----------Dziennik_Nauczyciela-----------")
            print("1. Dodaj nowego ucznia")
            print("2. Wybierz ucznia")
            print("3. Pokaż zagrożenia")
            print("4. Sprawdź obecność lub wystaw oceny")
            print("5. Wstaw nową klasę")
            print("6. Usuń jedną z klas")
            print("7. Stwórz statystyki")
            print("8. dodaj nowy przedmiot")
            print("9. usuń jeden z przedmiotów")
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
                        raise InvalidPesel("PESEL musi mieć dokładnie 11 cyfr.")
                    print("Wpisz klasę do której chcesz przypisać ucznia lub '-' jeżeli nie chcesz na razie go przypisywać")
                    clas = input()
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
                    student = StudentManager.get_student(int(id))
                    if student is None:
                        raise InvalidStudentData("Nie znaleziono ucznia o podanym ID.")
                    print(student)
                    print("grades: ")
                    for grade in student.grades:
                        print(grade.grade)
                    print("attendance: ")
                    for attendance in student.attendance:
                        print(attendance.typeOfAttendence)
                    print("------wybierz co chcesz zrobić-------")
                    print("1. edytuj dane studenta")
                    print("2. edytuj ocenę studenta")
                    print("3. edytuj obecność studenta")
                    print("4. wyświetl średnią")
                    print("5. wyświetl czy jest zagrożony")
                    print("6. przypisz do innej klasy")
                    print("7. wyświetl oceny z detalami")
                    print("8. wyświetl obecności z detalami")
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
                                    raise InvalidPesel("PESEL musi mieć dokładnie 11 cyfr.")
                                student.pesel = pesel

                        case "2":
                            for i in range(len(student.grades)):
                                print(f"{i+1}: {student.grades[i]}")
                            print("wybierz id oceny którą chcesz edytować")
                            id = int(input())-1
                            if student.grades[id].date != date.today():
                                raise InvalidGradeType("Można edytować tylko ocenę wystawioną dzisiaj.")
                            print("chce zmienić ocenę numeryczną T/N")
                            dec = input()
                            if(dec == 'T'):
                                print("podaj nową ocene")
                                grad = float(input())
                                student.grades[id].grade = grad
                            print("chce zmienić opis T/N")
                            dec = input()
                            if(dec == 'T'):
                                print("podaj nowy opis")
                                desc = input()
                                student.grades[id].desc = desc
                            print("chce zmienić przedmiot T/N")
                            dec = input()
                            if(dec == 'T'):
                                NameOfClass.show_class_names()
                                print("wybierz przedmiot")
                                clasname = input()
                                if not NameOfClass.isNameOfClass(clasname):
                                    raise InvalidClassNameType(f"Nie znaleziono przedmiotu: {clasname}")
                                student.grades[id].nameOfClass = clasname
                            print("chce edytować typ oceny T/N")
                            dec = input()
                            if(dec == 'T'):
                                print("podaj typ: ")
                                print("--legenda--")
                                print("1. praca domowa")
                                print("2. kartkówka")
                                print("3. sprawdzian")
                                print("-----------")
                                type = int(input())
                                student.grades[id].type = TypeOfGrade(type)

                        case "3":
                            for i in range(len(student.attendance)):
                                print(f"{i + 1}: {student.attendance[i]}")
                            print("wybierz id obecności którą chcesz edytować")
                            id = int(input()) - 1
                            if student.grades[id].date != date.today():
                                raise InvalidGradeType("Można edytować tylko ocenę wystawioną dzisiaj.")
                            print("chce zmienić przedmiot T/N")
                            dec = input()
                            if (dec == 'T'):
                                NameOfClass.show_class_names()
                                print("wybierz przedmiot")
                                clasname = input()
                                if not NameOfClass.isNameOfClass(clasname):
                                    raise InvalidClassNameType(f"Nie znaleziono przedmiotu: {clasname}")
                                student.attendance[id].nameOfClass = clasname
                            print("chce edytować typ obecności T/N")
                            dec = input()
                            if(dec == 'T'):
                                print("---------legenda--------")
                                print("-1. nie ma")
                                print("0. spóźniony")
                                print("1. obecny")
                                print("2. usprawiedliwiony")
                                print("------------------------")
                                print("podaj typ")
                                type = int(input())
                                student.attendance[id].typeOfAttendence = TypeOfAttendence(type)

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
                        case "7":
                            for g in student.grades:
                                print(g)
                        case "8":
                            for a in student.attendance:
                                print(a)
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
                        raise ClassDoesNotExist(f"Nie ma takiej klasy: {clas}")
                    print("wpisz przedmiot z listy: ")
                    NameOfClass.show_class_names()
                    clasname = input()
                    if not NameOfClass.isNameOfClass(clasname):
                        raise InvalidClassNameType(f"Nie znaleziono przedmiotu: {clasname}")
                    while True:
                        print("co chcesz zrobić: ")
                        print("1. sprawdzić listę obecności")
                        print("2. wystawić ocenę")
                        print("0. skończyłem")
                        dec = input()
                        if(dec == '1'):
                            StudentManager.checkAttendence(clas, clasname)
                        elif(dec == '2'):
                            StudentManager.show_class_students(clas)
                            print("wpisz id ucznia ktoremu chcesz wstawic ocene")
                            id = input()
                            stud = StudentManager.get_student(int(id))
                            if stud is None:
                                raise InvalidStudentData("Nie znaleziono ucznia o podanym ID.")
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
                            break
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
                            Charts.export_all(StudentManager.allStudents)

                        case "2":
                            StudentManager.show_all_classes()
                            print("wybierz klasę")
                            clas = input()
                            if not NameOfClass.isNameOfClass(clas):
                                raise ClassDoesNotExist(f"Nie ma takiej klasy: {clas}")
                            Charts.export_all(StudentManager.classMap[clas])

                        case "3":
                            StudentManager.show_all_students()
                            print("wybierz id ucznia")
                            id = input()
                            stud = StudentManager.get_student(int(id))
                            if stud is None :
                                raise InvalidStudentData("Nie znaleziono ucznia o podanym ID.")
                            Charts.export_one(stud)
                        case _:
                            print("nie ma takiej opcji")
                case "8":
                    NameOfClass.show_class_names()
                    NameOfClass.add_class(input())
                    NameOfClass.show_class_names()
                case "9":
                    NameOfClass.show_class_names()
                    NameOfClass.del_class(input())
                    NameOfClass.show_class_names()

                case _:
                    print("nie ma takiej opcji")




