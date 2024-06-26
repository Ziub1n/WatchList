from datetime import datetime
from colorama import init, Fore


init()

class FilmExistenceError(Exception):
    """dodawanie filmu ktory istnieje"""

    def __init__(self, tytul):
        self.tytul = tytul

    def __str__(self):
        return f"Film o tytule '{self.tytul}' już istnieje w kolekcji."

def menu():
    print(Fore.BLUE+"\nWatch List\n")
    print("1. Dodaj film")
    print("2. Usuń film")
    print("3. Edytuj film")
    print("4. Wyszukaj film")
    print("5. Wyswietl kolekcje")
    print("6. Eksportuj do txt")
    print("7. Oglądaj filmy")
    print("8. Wyswietl historie")
    print("9. Wyswietl statystyki\n")

class Film:
    def __init__(self, tytul, rezyser, rok, gatunek, status, ocena, opis=""):
        self.tytul = tytul
        self.rezyser = rezyser
        self.rok = rok
        self.gatunek = gatunek
        self.status = status
        self.ocena = ocena
        self.opis = opis

class CollectionManager:
    def __init__(self):
        self.kolekcja = []
        self.historia =[]

    def czy_film_istnieje(self, nowy_film):
        for film in self.kolekcja:
            if film.__dict__ == nowy_film.__dict__:
                return True
        return False
    def dodaj_film(self, tytul, rezyser, rok, gatunek, status, ocena, opis=""):
        nowy_film = Film(tytul, rezyser, rok, gatunek, status, ocena, opis)
        if self.czy_film_istnieje(nowy_film):
            raise FilmExistenceError(tytul)
        else:
            self.kolekcja.append(nowy_film)
            print(Fore.GREEN+"Film został poprawnie dodany do kolekcji")

    def usun_film(self):
        self.wyswietl_tytul()
        rm = int(input("Który film chcesz usunąć? : "))
        del self.kolekcja[rm - 1]
        print(Fore.GREEN+"Film został usunięty z kolekcji.")

    def edytuj_film(self):
        self.wyswietl_tytul()

        while True:
            try:
                edit = int(input(Fore.BLUE+"Który film chcesz edytować? : "))
                if edit <= 0 or edit > len(self.kolekcja):
                    print(Fore.RED + "Nie znaleziono filmu, podaj prawidłową liczbę")
                else:
                    break
            except ValueError:
                print(Fore.RED + "Podaj prawidłową liczbę")


        dane = ["tytul: ", "rezyser: ", "rok: ", "gatunek: ", "status: ", "ocena: ", "opis: "]
        informacje = []

        informacje.append(input(dane[0]))
        informacje.append(input(dane[1]))

        while True:
            try:
                rok = int(input(Fore.BLUE + dane[2]))
                informacje.append(str(rok))
                break
            except ValueError:
                print(Fore.RED + "\nProszę podać liczbę!!!")

        informacje.append(input(dane[3]))
        informacje.append(input(dane[4]))

        while True:
            try:
                ocena = float(input(dane[5]))
                if 0.0 <= ocena <= 5.0:
                    informacje.append(str(ocena))
                    break
                else:
                    print(Fore.RED + "Ocena musi być w przedziale od 0 do 5.")
            except ValueError:
                print(Fore.RED + "Ocena musi być liczbą.")

        informacje.append(Fore.BLUE + input(dane[6]))

        self.kolekcja[edit - 1].tytul = informacje[0]
        self.kolekcja[edit - 1].rezyser = informacje[1]
        self.kolekcja[edit - 1].rok = informacje[2]
        self.kolekcja[edit - 1].gatunek = informacje[3]
        self.kolekcja[edit - 1].status = informacje[4]
        self.kolekcja[edit - 1].ocena = informacje[5]
        self.kolekcja[edit - 1].opis = informacje[6]

        print(Fore.GREEN + "\nZaktualizowano informacje o filmie.")

    def wyszukaj_film(self):
        print("\nWyszukaj film\n")
        print("Jakiego kryterium chcesz użyć do wyszukiwania filmu ?\n1.tytul\n2.rezyser\n3.rok\n4.gatunek")

        while True:
            try:
                x = int(input(Fore.BLUE+ "Podaj numer kryterium: "))
                if x < 1 or x > 4:
                    print(Fore.RED + "Podaj poprawny numer (1-4).")
                else:
                    break
            except ValueError:
                print(Fore.RED + "Podaj poprawny numer (1-4).")

        if x == 1:
            a = input("Podaj tytuł: ")
            counter = 1
            znaleziono = False
            for i in self.kolekcja:
                if i.tytul == a:
                    print(counter, ". ", i.tytul, ", ", i.rezyser, ", ", i.rok, ", ", i.gatunek, ", ", i.status)
                    counter += 1
                    znaleziono = True
            if not znaleziono:
                print(Fore.RED + "Nie znaleziono filmu z podanego kryterium ")

        if x == 2:
            a = input("Podaj rezysera: ")
            counter = 1
            znaleziono = False
            for i in self.kolekcja:
                if i.rezyser == a:
                    print(counter, ". ", i.tytul, ", ", i.rezyser, ", ", i.rok, ", ", i.gatunek, ", ", i.status)
                    counter += 1
                    znaleziono = True
            if not znaleziono:
                print(Fore.RED + "Nie znaleziono filmu z podanego kryterium ")

        if x == 3:
            while True:
                try:
                    a = int(input(Fore.BLUE + "Podaj rok: "))
                    counter = 1
                    znaleziono = False
                    for i in self.kolekcja:
                        if i.rok == str(a):
                            print(counter, ". ", i.tytul, ", ", i.rezyser, ", ", i.rok, ", ", i.gatunek, ", ", i.status)
                            counter += 1
                            znaleziono = True
                    if not znaleziono:
                        print(Fore.RED + "Nie znaleziono filmu z podanego kryterium ")
                    break
                except ValueError:
                    print(Fore.RED + "Podany rok nie jest liczbą. Spróbuj ponownie.")

        if x == 4:
            a = input("Podaj gatunek: ")
            counter = 1
            znaleziono = False
            for i in self.kolekcja:
                if i.gatunek == a:
                    print(counter, ". ", i.tytul, ", ", i.rezyser, ", ", i.rok, ", ", i.gatunek, ", ", i.status)
                    counter += 1
                    znaleziono = True
            if not znaleziono:
                print(Fore.RED + "Nie znaleziono filmu z podanego kryterium ")
    def wyswietl_tytul(self):
        i=1
        for c in film.kolekcja:
            print(i,". ",c.tytul)
            i+=1

    def wyswietl_kolekcje(self):
        i=1
        for film in self.kolekcja:
            print(i," tytuł: ",film.tytul,", reżyser: ", film.rezyser,", rok: ", film.rok,", gatunek: ", film.gatunek,", status: ", film.status,", ocena: ", film.ocena,", opis: ", film.opis)
            i+=1

    def eksportuj_do_txt(self):
        try:
            with open("/Users/ziub1n/Desktop/PY/Jakub_Ziubinski_s28486_Watchlist/pythonProject/kolekcja.txt", 'w') as plik:
                for film in self.kolekcja:
                    plik.write(f"Tytuł: {film.tytul}\n")
                    plik.write(f"Reżyser: {film.rezyser}\n")
                    plik.write(f"Rok: {film.rok}\n")
                    plik.write(f"Gatunek: {film.gatunek}\n")
                    plik.write(f"Status: {film.status}\n")
                    plik.write(f"Ocena: {film.ocena}\n")
                    plik.write(f"Opis: {film.opis}\n")
                    plik.write("\n")
            print(Fore.GREEN+"Kolekcja została pomyślnie wyeksportowana do pliku")
        except Exception as e:
            print(Fore.RED+"Wystąpił błąd podczas eksportowania kolekcji:", str(e))

    from datetime import datetime

    def ogladanie_filmow(self):
        print("\nKtóry film chcesz obejrzeć? : ")
        i = 1
        for film in self.kolekcja:
            print(i, ". ", film.tytul + " (" + film.rok + ")")
            i += 1

        while True:
            try:
                x = int(input())
                if 0 < x <= len(self.kolekcja):
                    break
                else:
                    print("Nie znaleziono filmu, podaj prawidłową liczbę")
            except ValueError:
                print("Podaj prawidłową liczbę")

        wybrany_film = self.kolekcja[x - 1]
        print("Obejrzano film - " + wybrany_film.tytul + " (" + wybrany_film.rok + ")")

        while True:
            try:
                ocena = float(input("Podaj ocenę (0.0 - 5.0): "))
                if 0.0 <= ocena <= 5.0:
                    break
                else:
                    print(Fore.RED + "Ocena musi być w przedziale od 0 do 5.")
            except ValueError:
                print(Fore.RED + "Ocena musi być liczbą.")

        komentarz = input("Dodaj komentarz: ")


        now = datetime.now()
        data_i_godzina = now.strftime("%Y-%m-%d %H:%M:%S")

        wpis = {
            'tytul': wybrany_film.tytul,
            'ocena': ocena,
            'komentarz': komentarz,
            'data': data_i_godzina
        }
        self.historia.append(wpis)

        print(Fore.GREEN + "Ocena, komentarz oraz data i godzina obejrzenia zostały dodane do historii.")

    def wyswietl_historie(self):
        print("\n")
        if not self.historia:
            print(Fore.RED + "Historia jest pusta.")
            return

        for wpis in self.historia:
            tytul = wpis['tytul']
            ocena = wpis['ocena']
            komentarz = wpis['komentarz']
            data = wpis['data']
            print(f"Tytuł: {tytul}, Ocena: {ocena}, Komentarz: {komentarz}, Data: {data}")

    def generuj_statystyki(self):
        gatunki = {}
        for film in self.kolekcja:
            if film.gatunek in gatunki:
                gatunki[film.gatunek] += 1
            else:
                gatunki[film.gatunek] = 1

        print("Liczba filmów w poszczególnych gatunkach:")
        for gatunek, liczba in gatunki.items():
            print(f"{gatunek}: {liczba}")


        suma_ocen = 0
        for film in self.kolekcja:
            suma_ocen += float(film.ocena)
        srednia_ocena = suma_ocen / len(self.kolekcja)
        print(f"Średnia ocena filmów: {srednia_ocena:.2f}")


        najlepiej_oceniane = sorted(self.kolekcja, key=lambda x: float(x.ocena), reverse=True)[:3]
        print("3 najlepiej oceniane filmy:")
        for idx, film in enumerate(najlepiej_oceniane, start=1):
            print(f"{idx}. {film.tytul} ({film.ocena})")


film = CollectionManager()


film.dodaj_film("Gwiezdne Wojny: Nowa Nadzieja", "Lucas", "1977", "sci-fi", "klasyk", "4.9", "Epicka przygoda w kosmosie, która zdefiniowała gatunek science fiction i rozpoczęła jedną z najbardziej ikonicznych serii w historii kina.")
film.dodaj_film("Incepcja", "Nolan", "2010", "thriller", "w dystrybucji", "4.8", "Złożony thriller psychologiczny o złodziejach, którzy infiltrują sny, aby kraść i manipulować wspomnieniami.")
film.dodaj_film("Król Lew", "Allers", "1994", "animacja", "klasyk", "4.7", "Wzruszająca animacja o dorastaniu i odpowiedzialności, opowiadająca historię lwiątka Simby, przyszłego króla sawanny.")
film.dodaj_film("Forrest Gump", "Zemeckis", "1994", "dramat", "klasyk", "4.8", "Opowieść o niezwykłym życiu prostodusznego mężczyzny, którego niewinność i determinacja prowadzą go przez kluczowe momenty amerykańskiej historii XX wieku.")
film.dodaj_film("Titanic", "Cameron", "1997", "romans", "klasyk", "4.5", "Romantyczna tragedia osadzona na tle historycznego zatonięcia Titanica, opowiadająca o zakazanej miłości między pasażerami z różnych klas społecznych.")
film.dodaj_film("Joker", "Phillips", "2019", "dramat", "w dystrybucji", "4.6", "Mroczne studium postaci odczuwającego odrzucenie komika, który transformuje się w ikonicznego przestępcę z Gotham City.")

print("\n\n\n")
menu()
while(True):
    while True:
        try:
            x = int(input("Wybierz opcje: "))
            if 0 < x <= 9:
                break
            else:
                print("Proszę podać liczbę z przedziału (1-9)")
        except ValueError:
            print(Fore.RED+ "\nProszę podać liczbę!!!")
            menu()

    try:
        if x == 1:
            print("\nDodawanie filmów\n")
            a = input("Podaj tytuł: ")
            b = input("Podaj reżysera: ")
            while True:
                try:
                    c = int(input(Fore.BLUE + "Podaj rok: "))
                    break
                except ValueError:
                    print(Fore.RED + "\nProszę podać liczbę!!!")

            d = input("Podaj gatunek: ")
            e = input("Podaj status: ")
            while True:
                try:
                    f = float(input("Podaj ocenę: "))
                    if 0.0 <= f <= 5.0:
                        break
                    else:
                        print(Fore.RED + "Ocena musi być w przedziale od 0 do 5.")
                except ValueError:
                    print(Fore.RED + "Ocena musi być liczbą.")

            g = input(Fore.BLUE + "Podaj opis: ")
            film.dodaj_film(a, b, str(c), d, e, f, g)
        menu()

    except FilmExistenceError as e:
        print(Fore.RED + str(e))
        menu()

    if x == 2:
        film.usun_film()
        menu()
    if x == 3:
        film.edytuj_film()
        menu()
    if x == 4:
        film.wyszukaj_film()
        menu()
    if x == 5:
        film.wyswietl_kolekcje()
        menu()
    if x == 6:
        film.eksportuj_do_txt()
        menu()
    if x == 7:
        film.ogladanie_filmow()
        menu()
    if x == 8:
        film.wyswietl_historie()
        menu()
    if x == 9:
        film.generuj_statystyki()
        menu()
