# Okrutny budzik stwórz program pytający przed snem czy budzik
# dzwoniący rano ma się wyłączyć po podaniu 5 (prawidłowych!) wyników
# dodawania (opcja „light") czy mnożenia (opcja „pro") losowych dwóch 
# liczb dwycyfrowych. Budzik będzie dzwonił tak długo, aż budzona osoba poda wynik. 
# Najgorsze, że na podanie każdego prawidłowego wyniku 
# jest 10s... Wykorzystaj pętlę while.

import random
import time

operacja = input("Wybierz operację ('light' lub 'pro'): ")

if operacja == "light" or operacja == "pro":

    ilosc_wynikow=0

    while ilosc_wynikow <5:
        print("Zrobiles: " + str(ilosc_wynikow) + "/5")

        liczba1 = random.randint(0,2) # zmienić na jakiś lepszy przedział np 0-99
        liczba2 = random.randint(0,2) # zmienić na jakiś lepszy przedział np 0-99

        prawidlowy_wynik = 0

        if operacja == "light":
            prawidlowy_wynik= liczba1 + liczba2
        else:
            prawidlowy_wynik= liczba1 * liczba2
         
        print("Oblicz:",liczba1, "+" if operacja == "light" else "*", liczba2)

        start_timer = time.time()

        podany=input("Podaj wynik: ")

        if time.time() - start_timer > 10:
            print("Czas minął! Odpowiedź nie zostanie zaliczona.\n")
            continue

        if podany == str(prawidlowy_wynik):
            print("Wow! Wynik sie zgadza!\n")
            ilosc_wynikow += 1
        else:
            print("Ale sraka! Zle!\n")


    print("Gratulacje! Wszystkie odpowiedzi są poprawne. Możesz iść spać spokojnie.")

else:
    print("WTF???")
    