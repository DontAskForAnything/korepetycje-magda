# Stwórz quiz składający się z 4 pytań.
# Pytania powinny znajdować się na jednej liście.
# Druga lista to lista odpowiadających im odpowiedzi 
# (jeden element może zawierać wszystkie możliwe odpowiedzi na dane pytanie, np. a, b, c id). 
# Przygotuj program testujący użytkownika. Pytania powinny być prezentowane w losowej kolejności,
# bez powtórzeń. Na koniec wydrukuj procent prawidłowych odpowiedzi

import random

pytania = [
    "Pytanie: Które to stolica Polski?",
    "Pytanie: Jaki jest symbol chemiczny tlenu?",
    "Pytanie: Kto napisał dramat Hamlet?",
    "Pytanie: Która planeta jest największa w Układzie Słonecznym?"
]

odpowiedzi =[
    "a) Warszawa b) Kraków c) Berlin d) Paryż",
    "a) O b) H c) T d) O2",
    "a) William Shakespeare b) Jane Austen c) Fiodor Dostojewski d) Homer",
    "a) Mars b) Jowisz c) Ziemia d) Saturn"
]

poprawne = ["a", "d", "a", "b"]


punkty = 0

kopia_pytania = pytania.copy()

random.shuffle(kopia_pytania)

for pytanie in kopia_pytania:
    indeks_pytania = pytania.index(pytanie)
    odpowiedz_do_wyboru = odpowiedzi[indeks_pytania]

    print(pytanie)
    print(odpowiedz_do_wyboru)

    odpowiedz_uzytkownika = input("Twoja odpowiedz: ")

    if odpowiedz_uzytkownika == poprawne[indeks_pytania]:
        print("Udalo ci sie!")
        punkty += 1
    else:
        print("Zle :<")
    
    print()

procenty_poprawne = ( punkty / len(pytania)) * 100
print("Twoj wynik to:" , procenty_poprawne, "%")
