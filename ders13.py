#ilk açılış 235 tl
#kilometre başına 43.56
#5,34 kilometre
mesafe=float(input("Mesafeyi Giriniz........."))
if mesafe<=5.34:
    print(f"Ödenecek Ücret 235 TL")
else:
    toplam=mesafe*43.56
    print(f"Ödenecek Tutar {toplam}")