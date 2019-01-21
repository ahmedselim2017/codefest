#Euzubillahiminesseydanirracim Bismillahirrahmanirrhim

"""
import sys;

def oku():
    kisiSayisi = int(sys.stdin.readline());
    dizi = [];
    for i in range(5):
        dizi.append(sys.stdin.readline().replace("\r\n",""));
    return dizi;

dizi = oku();

"""

dizi = ['CABBBAAC', 'BACCCAAB', 'ABCCCBBA', 'BCAAACCB', 'CBAAABBC'];


def coz(dizi):
    g = dizi[0].replace("A","1").replace("B","2").replace("C","3")
    g1 = g.replace("1","A").replace("2","B").replace("3","C");
    g2 = g.replace("1","A").replace("2","C").replace("3","B");
    g3 = g.replace("1","B").replace("2","A").replace("3","C");
    g4 = g.replace("1","B").replace("2","C").replace("3","A");
    g5 = g.replace("1","C").replace("2","A").replace("3","B");
    g6 = g.replace("1","C").replace("2","B").replace("3","A");

    asilDizi = [g1,g2,g3,g4,g5,g6];

    for gorev in asilDizi:
        if (gorev not in dizi):
            return gorev;

print coz(dizi);
