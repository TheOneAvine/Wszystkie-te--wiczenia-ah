
produkty = {'jabłko' :  2,
            'jabłka' : 2,
            'jajko' : 1,
            'jajka' : 1,
            'chleb' : 3,
            'chleby' : 3}

licznik_produktów = 0
kupujemy = True

while kupujemy == True:
    produkt = input('Co chcesz kupić? ')
    ile = input("Ile potrzebujesz tego produktu? ")

    if produkt in produkty:
        licznik_produktów += produkty[produkt] * int(ile)

        dalej = input("Płacisz? Tak/Nie ")
        dalej.lower()
        if dalej == "tak":
            break
        else:
            pass 
    
    else:
        print("Nieznany produkt.")

print("Do zapłacenia masz:", licznik_produktów, "PLN.")

