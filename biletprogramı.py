para=float(input("Paranızı Girin:"))
tipi=int(input("Bilet Tipini Seçiniz: 1.NORMAL (50TL) 2.ÖĞRENCİ (25TL"))
adet=float(input("Bilet Adetini Giriniz:"))

if tipi==1:
    print("Normal")
    toplam=50*adet
elif tipi==2:
    print("Öğrenci")
    toplam=25*adet
else:
    print("Hatalı Seçim Yaptınız")

if para>toplam:
    bakiye=para-toplam
    print(f"İade edilecek tutar {bakiye} alınan bilet sayısı {adet} bilet tutarı {toplam}")

else:
    print("Bakiyeniz Yetersiz")























