#sinema salonu
#sinema salonu tanımla
#boş koltuk sayısını gir
#bilet fiyatları 1.Normal 250 2. Öğrenci 125
#her alınan bilet sayısı ile koltuk sayını 1 azaltacağoz
#en son döküm al sekmesi tıklayınca satılan bilet tutarı
#boş koltuk sayısı dolu koltuk sayısı ekrana gelecek
import os
os.system("cls")
print("------SİNEMA OTOMASYON PROGRAMI------")
salon_adi=input("Salon Adını Girin......")
koltuk_sayisi=int(input("Koltuk Sayısını Girin...."))
normal_fiyat=250
ogrenci_fiyat=125
bakiye=0
os.system("cls")
while True:
    print("Bilet Satmak İçin 1 Tuşuna Basın:")
    print("Bilet İade Etmek İçin 2 Tuşuna Basın:")
    print("Salon Bilgisini Göstermek İçin 3 Tuşuna Basın:...")
    print("Salon Koltuk Bilgisini Göstermek İçin 4 Tuşuna Basın...")
    print("Çıkış İçin 5 Tuşuna Basın..")
    print("********************************************************")
    secim=input("Lütfen bir Seçim Yapınız..")
    #Bilet Satışı Kısmı
    if secim =="1":
        bilet_tipi=input("Normal İçin 1,Öğrenci 2 Seçiniz")
        if bilet_tipi=="1":
            bakiye=bakiye+normal_fiyat
            koltuk_sayisi = koltuk_sayisi - 1
            os.system("cls")
        elif bilet_tipi=="2":
            bakiye = bakiye+ogrenci_fiyat
            koltuk_sayisi = koltuk_sayisi - 1
        else:
            print("Geçersiz Bir Tuşa Bastınız")
    #Bilet satış kısmı buraya kadar
    elif secim =="2":
       bilet_tipi=input("Normal İçin 1, Öğrenci İçin 2 Seçiniz")
       if bilet_tipi=="1":
           bakiye=bakiye+normal_fiyat
           koltuk_sayisi = koltuk_sayisi + 1
       elif bilet_tipi=="2":
            bakiye = bakiye-ogrenci_fiyat
            koltuk_sayisi = koltuk_sayisi + 1
       else:
           print("Geçersiz Bir Tuşa Bastınız")
    elif secim =="3":
        print(f"Toplanan Para Tutarı {bakiye} TL...")
    elif secim =="4":
        print(f"Boş Koltuk Sayısı {koltuk_sayisi}dır...")
    elif secim == "5":
        print("Sistemden Çıkış Yaptınız...")
        break