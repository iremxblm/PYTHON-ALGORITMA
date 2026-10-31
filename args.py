def topla(*args):
    toplam=0
    for i in args:
        toplam+=i
    print(toplam)

topla(10,20,50,70)
def sinif_durum(*args):
    for i in args:
        if (i>=50):
            print(f"Girilen NOTU {i} geçti")
        else:
            print(f"Girilen NOTU {i} kaldı")

sinif_durum(10,20,30,40)
