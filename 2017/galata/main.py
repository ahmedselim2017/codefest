#Euzubillahiminesseydanirracim Bismillahirrahmanirrhim
"""
import sys;

def oku():
    return int(sys.stdin.readline());

basamakSayisi = oku();
"""
basamakSayisi = 1000;


def kontrol(a):
    while(a>=0):
        a = a-9;
        if a % 11 == 0:
            return True;
    return False;


def coz(basamakSayisi):
    a  = 0;
    for i in range(basamakSayisi):
        a = i+1;
        if a != 0 and (a % 9 == 0 or a % 11 == 0 or kontrol(a)):
            print "Kos Mahmut";
        else:
            print "Yuksel Mahmut";



coz(basamakSayisi);
