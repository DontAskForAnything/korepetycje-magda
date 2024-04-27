# Napisz program (bez użycia funkcji pop()) symulujący działanie Dużego Lotka. 
# Użytkownik typuje 6 niepowtarzających się liczb, następnie następuje losowanie 6
# (również niepowtarzających się) liczb z 49.
# W zależności od wyniku, wydrukuj gratulacje lub pocieszenie. 
# Pamiętaj, nagradzane jest 3, 4, 5 i 6 trafień.

import random

numery_gracza = []

ilosc_cyfr = 6

while len(numery_gracza) < ilosc_cyfr:
    podana_liczba = int(input("Podaj twoje liczby: "))
    if podana_liczba not in numery_gracza and podana_liczba > 0 and podana_liczba < 50:
        numery_gracza.append(podana_liczba)
    else:
        print("Taka liczba już jest dodana lub jest nie w zakresie!")

wygrywajace_liczby = []
while len(wygrywajace_liczby) < ilosc_cyfr:
    wylosowana_liczba = random.randint(1,49)
    if wylosowana_liczba not in wygrywajace_liczby:
        wygrywajace_liczby.append(wylosowana_liczba)

wynik = 0
for liczba_gracza in numery_gracza:
    # sposob 1, sprawdzasz czy kolejno liczba gracza jest w wygrywajacych liczbach
    if liczba_gracza in wygrywajace_liczby:
        wynik += 1

    # sposob 2, sprawdzasz czy liczba gracza rowna sie po kolei ktorejs z liczb w wygrywajace_liczbach 
    # for wygrywajaca_liczba in wygrywajace_liczby:
    #     if liczba_gracza == wygrywajaca_liczba:
    #         wynik += 1
    #         break

# print(wynik)
# print(numery_gracza)
# print(wygrywajace_liczby)

if wynik >= 3:
    print("WOW wygrałeś coś, udało ci sie trafić: " , wynik, "razy!")
else:
    print("Nie ma nagrody.... trafiłeś tylko " , wynik, "liczby")
    
    