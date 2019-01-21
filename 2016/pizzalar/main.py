#Euzubillahiminesseydanirracim Bismillahirrahmanirrhim
import sys;

## BUG: BUYUK SAYILARDA TIMEOUT HATASI JAVA DOSYASINA BAKIN

"""
def oku():
    dizi = [];
    r = int(sys.stdin.readline());
    for i in range(r):
        data = sys.stdin.readline();
        data = data.replace("\r\n","");
        dizi.append(int(data));
    return dizi;

dizi = oku();
"""

def diziToplami(dizi):
    a = 0;
    for q in dizi:
        a += q;
    return a;

def coz(dizii, ikinciBinaa):

    dizi = dizii;

    ilkBina = [];
    ilkBinaToplamDilim = 0;
    ikinciBina =ikinciBinaa;
    ikinciBinaToplamDilim = 0;
    enIyiDurum = [-1,-1]; #[kesilen kisim, aradaki fark]


    for i in range(len(dizi)):
        ilkBina.append(dizi[i]);

        del ikinciBina[0]

        ilkBinaToplamDilim += dizi[i];
        ikinciBinaToplamDilim = diziToplami(ikinciBina);

        fark = abs(ilkBinaToplamDilim - ikinciBinaToplamDilim);

        if fark == 0:
            enIyiDurum = [i+1, 0];
            return enIyiDurum;
        elif (fark < enIyiDurum[1]) or (enIyiDurum[1] == -1):
            enIyiDurum = [i+1, fark];

        #print str(ilkBina)+" : "+str(ikinciBina);
        #print str(ilkBinaToplamDilim)+" : "+str(ikinciBinaToplamDilim);



        #print "***************************";

    return enIyiDurum;

a = [2, 3, 5];
enIyiDurum = coz(a,list(a));
print enIyiDurum[0];
