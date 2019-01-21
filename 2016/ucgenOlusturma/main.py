#Euzubillahiminesseydanirracim Bismillahirrahmanirrhim
from itertools import combinations;


"""
import sys;

def oku():
    sys.stdin.readline();
    dizi = sys.stdin.readline().split();
    dizi2 = [];
    for i in dizi:
        dizi2.append(int(i));

    return dizi2;
"""



def ucgenMi(a, b, c):#3,4,7
    if a > 0 and b > 0 and c > 0:
        if ( (a + b) > c > abs(a - b) ) and ( (a + c) > b > abs(a - c) ) and ( (c + b) > a > abs(b - c) ):
            return True
        else:
            return False;
    else:
        return False;



def coz(dizi):
    comb = combinations(dizi, 3);
    sayac = 0;
    for p in list(comb):
        if ucgenMi(p[0],p[1],p[2]):
            sayac += 1;

    print sayac;







coz([7, 3, 5, 4]);
