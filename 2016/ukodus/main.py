import sys

"""
dizi = [];

def oku():
    for i in range(9):
        data = sys.stdin.readline();
        data2 = data.split();
        dizi.append(data2);

    return dizi;

dizi = oku();
"""

dizi =[['1', '7', '4', '2', '6', '5', '3', '9', '8'],
        ['5', '3', '9', '8', '1', '7', '6', '2', '4'],
        ['8', '6', '2', '9', '4', '3', '5', '7', '1'],
        ['3', '8', '1', '7', '5', '2', '9', '4', '6'],
        ['9', '4', '7', '6', '3', '8', '1', '5', '2'],
        ['6', '2', '5', '1', '9', '4', '7', '8', '3'],
        ['2', '5', '3', '4', '7', '6', '8', '1', '9'],
        ['7', '9', '8', '3', '2', '1', '4', '6', '5'],
        ['4', '1', '6', '5', '8', '9', '2', '3', '7']]

def kontrol(sayaclar, s):
    if (s == "1"):
        sayaclar[0] += 1;
    elif (s == "2"):
        sayaclar[1] += 1;
    elif (s == "3"):
        sayaclar[2] += 1;
    elif (s == "4"):
        sayaclar[3] += 1;
    elif (s == "5"):
        sayaclar[4] += 1;
    elif (s == "6"):
        sayaclar[5] += 1;
    elif (s == "7"):
        sayaclar[6] += 1;
    elif (s == "8"):
        sayaclar[7] += 1;
    elif (s == "9"):
        sayaclar[8] += 1;


    return sayaclar;

def coz(dizi):
    sayaclar = [0,0,0,0,0,0,0,0,0];

    for d in dizi:
        for s in d:
            sayaclar = kontrol(sayaclar, s);
        for sayac in sayaclar:
            if sayac > 1 :
                print sayaclar;
                return False;
        sayaclar = [0,0,0,0,0,0,0,0,0];


    for i in range(9):
        for j in range(9):
            s = dizi[j][i];
            sayaclar = kontrol(sayaclar ,s);
            for sayac in sayaclar:
                if sayac > 1 :
                    print sayaclar;
                    return False;

            sayaclar = [0,0,0,0,0,0,0,0,0];

    return True;


if(coz(dizi)):
    print "DOGRU";
elif(coz(dizi)):
    print "YANLIS";
