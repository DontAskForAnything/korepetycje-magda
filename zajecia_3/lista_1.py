# Utwórz listę wypełnioną 10 liczbami (5 ujemnych, 5 dodatnich). 
# Liczby tym razem mają być podane przez użytkownika. 
# Zadaniem programu jest wyświetlenie tylko ujemnych liczb parzystych występujących w liście w kolejności od najmniejszej do największej. 
# Program pilnuje podania odpowiedniej liczby liczb dodatnich i ujemnych poprzez użycie funkcji len().

lista = []

while len(lista) < 5:
    podana_liczba = int(input("Podaj liczby ujemne: "))
    if podana_liczba < 0:
        lista.append(podana_liczba)
    else:
        print("To nie liczba ujemna!")

while len(lista) >= 5 and len(lista) < 10:
    podana_liczba = int(input("Podaj liczby dodatnie: "))
    if podana_liczba > 0:
        lista.append(podana_liczba)
    else:
        print("To nie liczba dodatnia!")
    
ujemne_parzyste = []

for liczba in lista:
    if liczba < 0 and liczba % 2 == 0:
        ujemne_parzyste.append(liczba)

ujemne_parzyste.sort()

print(ujemne_parzyste)
