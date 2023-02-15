import sys
import csv
# stale zmienne
ARG_PLIKU_IN = 1
ARG_PLIKU_OUT = 2
ARG_ZMIANY = 3
#
plik_wejscia = sys.argv[ARG_PLIKU_IN]
plik_wyjscia = sys.argv[ARG_PLIKU_OUT]
zmiana = sys.argv[ARG_ZMIANY:]  # format zmiany to "x,y,wartosc", moze ich byc n ilosc
# trzeba podzielic n zmian, na trojki, wrzucic w strukture:
wartosci_do_zmiany = []
for n in range(ARG_ZMIANY, len(sys.argv)):  # ARG ZMIANY to w zasadzie 3, drugi argument to nr ostatniego arg. w linii komend
    wybrana_komorka = sys.argv[n].split(',')
    kolumna = int(wybrana_komorka[0])
    wiersz = int(wybrana_komorka[1])
    tresc = wybrana_komorka[2]
    wartosci_do_zmiany.append((kolumna, wiersz, tresc))
#












