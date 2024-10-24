
# Zad 2.10
# Mozemy uzyc metody split(), ktora dzieli napis wedlug bialych znakow
# A nastepnie zwrocic dlugosc podzielonego napisu

def zad2_10(text):
    words = text.split()
    return len(words)
print(zad2_10("ciag wielu wyrazow"))

# Zad 2.11
# Mozemy uzyc metody join(), ktora wstawia okreslony separator pomiedzy kolejne elementy ciagu znakow
def zad2_11(word):
    return '_'.join(word)
print(zad2_11('slowo'))

# Zad 2.12
def zad2_12_first_letters(line):
    words = line.split()
    return ''.join(word[0] for word in words)

def zad2_12_last_letters(line):
    words = line.split()
    return ''.join(word[-1] for word in words)

print(zad2_12_first_letters('Ala ma kota'))
print(zad2_12_last_letters('Hubert ma psy'))

# Zad 2.13
def zad2_13(line):
    words = line.split()
    return sum(len(word) for word in words)
print(zad2_13('Ala ma kota'))

# Zad 2.14
def zad2_14(line):
    words = line.split()
    longest = max(words, key=len)
    return longest, len(longest)

print(zad2_14('Ala ma kota'))

# Zad 2.15
def zad2_15(L):
    return ''.join(str(number) for number in L)

L = [1, 25, 3, 12]
print(zad2_15(L))

# Zad 2.16
def zad2_16(line):
    return line.replace("GvR", 'Guido van Rossum')

print(zad2_16("Zamieniony ciąg to GvR"))

# Zad 2.17
def zad2_17_alfabetycznie(line):
    words = line.split()
    return sorted(words, key=str.lower)

def zad2_17_dlugosci(line):
    words = line.split()
    return sorted(words, key=len)

line17 = "To zdanie jest zdaniem tekstowym do testu rozwiazania"
print(zad2_17_alfabetycznie(line17))
print(zad2_17_dlugosci(line17))

# Zad 2.18
def zad2_18(number):
    str_number = str(number)
    return str_number.count('0')

print(zad2_18(98324923489849238004328482340))

# Zad 2.19
def zad2_19(L):
    return ''.join(str(number).zfill(3) for number in L)

L = [7, 24, 323, 2, 23, 942]
print(zad2_19(L))