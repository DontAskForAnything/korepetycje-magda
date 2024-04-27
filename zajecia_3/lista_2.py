# Napisz program, który będzie: wyświetlał największy lub najmniejszy element listy liczbowej
# stworzonej przez użytkownika, użytkownik decyduje który. 
# Nie korzystaj z funkcji max() i min().
# Wyświetl listę posortowaną od najmniejszego do największego elementu lub na odwót 
# - również tu użytkownik podejmuje decyzję. 
# Przypilnuj, żeby do listy zostały dołączone tylko niepowtarzające się elementy.


lista = []

wielkosc_tablicy = int(input("Podaj wielkosc tablicy: "))

while len(lista) < wielkosc_tablicy:
    podana_liczba = int(input("Podaj liczby: "))
    if podana_liczba not in lista:
        lista.append(podana_liczba)
    else:
        print("Taka liczba już jest dodana!")

lista.sort()

wybor_min_max = input("max czy min: ")

if wybor_min_max == "max":
    print(lista[len(lista) - 1])
else:
    # najmniejsza_liczba = lista[0]
    # for liczba in lista:
    #     if najmniejsza_liczba > liczba:
    #         najmniejsza_liczba = liczba
    print(lista[0])

wybor_kolejnosc = input("rosnaco czy malejaco: ")
if wybor_kolejnosc == "rosnaco":
    print(lista)
else:
    lista.reverse()
    print(lista)
