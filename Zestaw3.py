
"""
Zestaw 3
"""

"""
Zadanie 3.1
x = 2; y = 3;
if (x > y):
    result = x;
else:
    result = y;

for i in "axby": if ord(i) < 100: print (i)

for i in "axby": print (ord(i) if ord(i) < 100 else i)

Kod nie jest poprawny składniowo:
    w jezyku python nie stosujemy średników na końcu linii, średniki służądk oddzielenia wyrażeń
    # w przypadku pętli nie zastosowano wcięć
"""

"""
Zadanie 3.2
Co jest złego w kodzie:

L = [3, 5, 4] ; L = L.sort() # Poprawna forma to po prostu L.sort()

x, y = 1, 2, 3  # Mamy dwie zmienne i trzy wartości

X = 1, 2, 3 ; X[1] = 4 # Nie możemy dodawać bezpośrednio do krotki

X = [1, 2, 3] ; X[3] = 4 # X nie ma indeksu 3 lepiej użyć X.append(4)

X = "abc" ; X.append("d") # str nie ma atrybutu append, można użyć X = X + "d"

L = list(map(pow, range(8))) # Nie przekazano funkcji pow żadnych argumentów
"""

"""
Zadanie 3.3
"""
def zadanie_3_3():
    for i in range (0,31):
        if (i % 3 != 0):
            print(i)

"""
Zadanie 3.4
"""
def zad_3_4():
    while True:
        ipt = input("Podaj liczbe rzeczywista: ")
        if (ipt == 'stop'):
            break
        try:
            print(f'Podana liczba {ipt}, jej trzecia potega {pow(float(ipt), 3)}')
        except ValueError:
            print("Niepoprawny input")

"""
Zadanie 3.5
"""
def zadanie_3_5(dlugosc):
    miarka = ""
    for i in range(dlugosc):
        miarka += "|...."
    miarka += "|"

    liczby = "0"
    for i in range(1, dlugosc + 1):
        liczby += str(i).rjust(5)

    miarka += "\n" + liczby
    print(miarka)

#zadanie_3_5(12)

"""
Zadanie 3.6
"""

def zadanie_3_6(wysokosc, szerokosc):
    if (wysokosc <= 0 or szerokosc <= 0):
        print("Błędne dane")
        return False
    prostokat = ""
    gorna_sciana = "+---" * szerokosc + "+"
    boczna_sciana = "|"
    for _ in range(szerokosc):
        boczna_sciana += "|".rjust(4)

    for i in range(wysokosc * 2):
        if i % 2 == 0:
            prostokat += gorna_sciana + "\n"
        else:
            prostokat += boczna_sciana + "\n"
    prostokat += gorna_sciana + "\n"

    print(prostokat)

#zadanie_3_6(2, 4)
'''
Zadanie 3.8
'''

def zadanie_3_8(sekwencja1, sekwencja2):
    sekwencja1 = sekwencja1.split()
    sekwencja2 = sekwencja2.split()

    wspolne_elementy = list(set(sekwencja1) & set(sekwencja2))
    wszystkie_elementy = list(set(sekwencja1) | set(sekwencja2))

    print(wspolne_elementy)
    print(wszystkie_elementy)

#zadanie_3_8("1 2 6 4", "3 9 2")

'''
Zadanie 3.9
'''

def zadanie_3_9(sekwencje):
    sumy = []
    for sekwencja in sekwencje:
        sumy.append(sum(sekwencja))
    print(sumy)

#zadanie_3_9([[], [4], (1,2), [3,4], (5,6,7)])


'''
Zadanie 3.10
'''

def zadanie_3_10(s):
    roman_to_arabic = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    def roman2int(s):
        total = 0
        prev_value = 0

        for char in reversed(s):
            current_value = roman_to_arabic[char]

            if current_value < prev_value:
                total -= current_value
            else:
                total += current_value

            prev_value = current_value

        return total

    print(roman2int(s))
zadanie_3_10("VI")
