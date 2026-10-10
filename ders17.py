sayilar=[1,2,3,4,5,6]
print(sayilar)
print(sayilar[4])
print(sayilar[1:4])
print(sayilar[-3])
print(sayilar[2:])
sayilar[5]=10
print(sayilar)
sayilar[1:3]=[15,20]
print(sayilar)
#Belirtilen aralıktaki verileri değiştirir
sayilar.insert(2,41)
print(sayilar)
#append ile sonuna veri ekleriz
sayilar.append(200)
print(sayilar)
sayilar.remove(15) #parantezin içindeki sayı silinir
print(sayilar)
sayilar.sort() #sayıları sıralar
print(sayilar)
sayilar.sort(reverse=True) #sayıları sıralar
print(sayilar)
sayilar.pop(2) #verilen indeksteki değeri siler
print(sayilar)
ogrenci=["İrem","Elif","Alperen"]
for item in ogrenci:
    print(item)
for i in range(5):
    print(i)
for i in range(1,10):
    print(i)
for i in range(1,10,2):
    print(i)
for i in range(1,10,3):
    print(i)
for i in range(100,1,-2):
    print(i)
#range(bitiş)
#range(baslangıc,bitis)
#range(başlangıç,bitiş,adim)