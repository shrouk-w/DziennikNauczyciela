from Classes.Student import Student


class Interface:

    @classmethod
    def start(cls):
        stud = Student("Jan","Kowalski","12312312312","1A")
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
            print("0. Wyjdź")
            print("-----------------------------------------")
            provided = input()
            match provided:
                case "0":
                    return
                case "1":
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

                case _:
                    print("zły argument")





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



