print("Hesaplama Programına Hoş Geldiniz")
print("******************************************************")
a=int(input("1.SAYI:"))
b=int(input("2.SAYI:"))
islem=int(input("1.Toplam 2.Çıkarma 3.Çarpma 4.Bölme için seçiniz"))
if islem==1:
    sonuc=a+b
elif islem==2:
    sonuc=a-b
elif islem==3:
    sonuc=a*b
elif islem==4:
    sonuc=a/b
else:
    print("Hatalı Tuşlama Yaptınız")
print(f"İşlem sonucu: {sonuc}")
print("******************************************************")
