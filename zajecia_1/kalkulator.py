# Przygotuj skrypt - kalkulator. Powinien on pobierać dwie liczby od użytkownika, a następnie wyświetlać podsumowanie:
# Zostały podane liczby ... oraz .... (od nowej linii) 
# Wynik ich dodawania to..., a mnożenia ..... (od nowej linii) Jeśli od pierwszej liczby odejmiemy drugą, otrzymamy... (od nowej linii) 
# Jeśli natomiast drugą liczbę podzielimy przez pierwszą ......
# *uwaga - wyjściowo input() pobiera zawartość zmiennej w formacie łańcuchowym (string)

pierwsza_liczba = int(input("Dawaj pierwszą liczbę: "))
druga_liczba = int(input("Dawaj drugą liczbę: "))
print("Zostały podane liczby " + str(pierwsza_liczba) + " oraz " + str(druga_liczba) + ".")

suma = pierwsza_liczba + druga_liczba
mnozenie = pierwsza_liczba * druga_liczba
print("Wynik ich dodawania to " + str(suma) +", a mnożenia " + str(mnozenie) + ".")

odejmowanie = pierwsza_liczba - druga_liczba
dzielenie = druga_liczba / pierwsza_liczba
print("Jeśli od pierwszej liczby odejmiemy drugą, otrzymamy " + str(odejmowanie) + ".")
print("Jeśli natomiast drugą liczbę podzielimy przez pierwszą - " + str(dzielenie) + ".")
