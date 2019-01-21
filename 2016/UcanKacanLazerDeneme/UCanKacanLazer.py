import sys
r = int(sys.stdin.readline())
def oku():

    dizi = []
    altDizi = []
    for i in range(r):
        altDizi = map(int,sys.stdin.readline().split())
        dizi.append(altDizi)
    return dizi

sonuc=oku()

for i in range(r):
    kutu= sonuc[i]
    if((kutu[1]%2=0 and kutu[0]%2==0):
        print "HAYIR"
    else:
        print "EVET"
