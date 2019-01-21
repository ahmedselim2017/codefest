#Euzubillahiminesseydanirracim Bismillahirrahmanirrhim
from __future__ import division;
import sys;
import math;

"""
def oku():
    dizi = sys.stdin.readline().split();
    dizi2 = [];
    for o in range(len(dizi)):
        dizi2.append(int(dizi[o]));

    return dizi2;

dizi = oku();
"""


## BUG: Büyük Sayılarda Time Out Veriyor
def coz(dizi):
    if (dizi[0] < dizi[1]) or (dizi[0] == 0) or (dizi[1] == 0) or (not ((dizi[0] / dizi[1]).is_integer())):
        return -1, False;
    saniye = math.log(dizi[0] / dizi[1],2);
    mumkunMu = saniye.is_integer();

    return int(saniye), mumkunMu ;





saniye,mumkunMu = coz([80,10]);
if mumkunMu:
    print "MUMKUN";
    print saniye;
else:
    print "MUMKUN DEGIL";
