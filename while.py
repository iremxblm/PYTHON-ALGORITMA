#while döngüsü
i=10
durum=True
while i<10:
    print(i)
    i=i+1
while durum:
    cevap=(input("Çıkmak için 1 tuşuna Basınız"))
    if cevap=="1":
        durum=False
        print("Sistemden Çıkıldı....")
    else:
        print("İşlem Devam Ediyor")
