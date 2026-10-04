print("Boy ve Kilo Endeksi")
boy=float(input("Metre Cinsinden Boyunuzu Giriniz:"))
kilo=float(input("Kilonuzu Giriniz:"))
#kilo/boy*boy ortalama indeksi bulmamıza yardımcı oluyor
indeks=(kilo/boy*boy)
if indeks<18.5:
    print("Zayıf")
elif indeks<25:
    print("Normal")
elif indeks<30:
    print("Fazla Kilo")
elif indeks<35:
    print("Obez")
else:
    print("Morbit")

