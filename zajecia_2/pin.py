# Napisz program, który prosi użytkownika o wpisanie hasła
# i po trzech nieudahych próbach blokuje dostęp do konta

nadany=input("Proszę o nadanie pinu\n")
podany=""

ilosc_bledow=0
while nadany!=podany:
    podany=input("Proszę o wprowadzenie numeru pin\n")
    if podany==nadany:
        print("Dobry pin")
    else:
        print("Zły pin, złodzieju")
        
    ilosc_bledow+=1

    if ilosc_bledow >= 3:
        print("Zablokowano! Łapy precz!")
        break
    