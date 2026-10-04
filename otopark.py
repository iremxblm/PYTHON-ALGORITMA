#otopark otomasyonu
#ilk 1 saat 50 her saat için 20t l fark alacağız

print("Otoparka Hoşgeldiniz.........")
saat=int(input("Kalacağınız saati giriniz.........."))

if saat==0:
    print("Geçersiz Saat Girdiniz...")
elif saat==1:
    print("Ücretiniz 50TLdir.")
else:
    tutar=50+(saat-1)*20
    print(f"Ödeyeceğiniz tutar {tutar}")
