renk=input("Trafik Işığı Seçiniz Kırmızı Yeşil Sarı").lower()
#lower kucuk harfe çevir upper buyuk harfe çevir
if renk=="yesil":
    print("Geçebilirsiniz")
elif renk=="kırmızı":
    print("Dur")
elif renk=="sarı":
    print("Hazırlan")
else:
    print("Bekle")