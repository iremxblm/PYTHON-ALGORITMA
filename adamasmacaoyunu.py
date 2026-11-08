#ADAM ASMACA OYUNU
import random
kelimeler=["bilgisayar","kalem","deniz","kitap","araba"]
kelime=random.choice(kelimeler)
print(kelime)
tahminler=[]
can=6
print("-----ADAM ASMACA OYUNU---")
print("Kelimeyi Bulmak İçin Harf Tahmin Edilecek..")
print("6 adet hakkınız bulunmaktadır")
while can>0:
    gorunen=""
    for harf in kelime:
        if harf in tahminler:
            gorunen+=harf+""
        else:
            gorunen+="_"
    print("\n Kelime:",gorunen)
    print("Kalan Can:",can)
    if all(harf in tahminler for harf in kelime):
        print("Tebrikler Kazandınız")
        break
    tahmin=input("Bir Harf Girin:").lower()
    if len(tahmin)!=1 or not tahmin.isalpha():
        print("Lütfen Bir Harf Girin")
        continue
    if tahmin in tahminler:
        print("Bu harfı zaten tahmin ettiniz....")
    tahminler.append(tahmin)
    if tahmin in kelime:
        print("Doğru Harf Girdiniz..")
    else:
        print("Yanlış Harf Girdiniz..")
        can-=1
    if can==0:
        print("\n Oyun Bitti")
        print("Doğru Kelime",kelime)
