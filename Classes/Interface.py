from unittest import case

from Classes.Grade import Grade
from Classes.Student import Student
from Classes.StudentManager import StudentManager
from Classes.TypeOfAttendence import TypeOfAttendence
from Classes.TypeOfGrade import TypeOfGrade


class Interface:

    @classmethod
    def start(cls):
        stud = Student("Jan","Kowalski","12312312312","1A")
        stud.add_grade(Grade(1,"","j. polski",TypeOfGrade.TEST))
        stud = Student("Jan2","Kowalski","12312312312","1A")
        stud = Student("Jan3","Kowalski","12312312312","1A")
        stud = Student("Jan4","Kowalski","12312312312","1A")
        stud = Student("Jan4","Kowalski","12312312312","1A")
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
            print("4. Sprawdź obecność lub wystaw oceny")
            print("5. Wstaw nową klasę")
            print("6. Usuń jedną z klas")
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
                    print("2. edytuj ocenę studenta")
                    print("3. edytuj obecność studenta")
                    print("4. wyświetl średnią")
                    print("5. wyświetl czy jest zagrożony")
                    print("0. usuń studenta")
                    print("-------------------------------------")
                    decision = input()
                    match decision:
                        case "1":
                            pass
                        case "2":
                            pass
                        case "3":
                            pass
                        case "4":
                            print(student.avarage())
                        case "5":
                            print(student.is_failling())
                        case "0":
                            StudentManager.delete_student(student)
                        case _:
                            print("nie ma takiej opcji")

                case _:
                    print()
                    print("nie ma takiej opcji")





    #dodaj ucznia
        #wpisz imie
        #wpisz nazwisko
        #wpisz pesel
        #wpisz klasę lub - jeżęli nie chcesz teraz przypisywać do klasy
    #indywidualny uczeń
        #wybierz klasę
            #wybierz ucznia
                #pokaż listę ocen i obecności
                #wybierz czy chcesz usunać czy edytować
                    #jeżeli usunąć to usuń jeżeli edytować to proś o nowe dane
                #można wybrać pokazanie średniej albo czy jest zagrożony
    #pokaż zagrożenia
        #przejdź po uczniach i pokaż czy są zagrożeni
    #sprawdzenie list obecności albo ocen
        #wybierz klasę
            #wpisz przedmiot
                #wybierz obecność/ocena pewnie nie powinno się dać sprawdzić 1 dnia tego smaego przedmiotu
                    #wyświetl listę uczniów 1 po drugim
                        #przy każdym wpisz czy jest czy nie
                    #pokaż listę wszystkich uczniów
                        #wybierz który
                            #wpisz ocenę
                    #wyjdź tylko jak kliknie się guzik



