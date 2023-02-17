import sys
import csv
# stale zmienne
ARG_PLIKU_IN = 1
ARG_PLIKU_OUT = 2
ARG_ZMIANY = 3
# oczekiwane argumenty podane w Cl
plik_wejscia = sys.argv[ARG_PLIKU_IN]
plik_wyjscia = sys.argv[ARG_PLIKU_OUT]
zmiana = sys.argv[ARG_ZMIANY:]  # format zmiany to "x,y,wartosc", moze ich byc n ilosc
# wyciagniecie wartosci do zmiany:
wartosci_do_zmiany = []
for n in range(ARG_ZMIANY, len(sys.argv)):  # arg zmiany to co do zasady bedzie 3, a koniec to n, stad dwukropek
    komorka_i_tresc = sys.argv[n].split(',')  # 'x,y,tresc' czyli 'kolumna,wiersz,tresc'
    wybrana_kolumna = int(komorka_i_tresc[0])  # to tylko zamysl usera, jeszcze nie idx z csv, x
    wybrany_wiersz = int(komorka_i_tresc[1])  # same here, to jeszcze nie idx z csv, y
    tresc = komorka_i_tresc[2]  # "cokolwiek"
# przerobienie wybranych wartosci na indexy listy:
    zmieniany_index_kolumna = int(wybrana_kolumna - 1)  # same but different, z userowego na kompowy, x
    zmieniany_index_wiersz = int(wybrany_wiersz - 1)  # same but different, z userowego na kompowy, y
    wartosci_do_zmiany.append([zmieniany_index_kolumna, zmieniany_index_wiersz, tresc])  # wdz = [[1,2,tresc], [x,y,cokolwiek]]
#
# zmiana zawartosci pliku wejsciowego na liste list:
with open(plik_wejscia, "r") as pwe:
    reader = csv.reader(pwe)
    zawartosc_pliku = list(reader)  # zp = [[a,a,a][b,b,b],[c,c,c]]
#
for element in wartosci_do_zmiany:
# dla elementow mojej listy list, np:
# wartosci_do_zmiany =
# [[x,y,cokolwiek], [1,2,zmiana]]
# "zmieniany_index_kolumna" bedzie miec wartosc pierwszego el. listy "wartosci do zmiany" and so on
    zmieniany_index_kolumna, zmieniany_index_wiersz, tresc = element
    zawartosc_pliku[zmieniany_index_wiersz][zmieniany_index_kolumna] = tresc  # idx wiersza na liscie 'zaw.pliku' wybiera konkretna liste, idx kolumny wybiera nr elementu wybranej listy
# zawartosc_pliku[][] np:
# [[a,b,c], <- a to zp[1][1]
# [d,e,f,], <- f to zp[2][3]
# [g,h,i]]
# zapis do nowego pliku
with open(plik_wyjscia, "w") as pwy:
    writer = csv.writer(pwy)
    writer.writerows(zawartosc_pliku)














