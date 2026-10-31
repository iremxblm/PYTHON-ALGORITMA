

while True:
    print("\n---Öğrenci Kayıt Programı---")
    print("1-Öğrenci Ekle:")
    print("2-Öğrenci Listeleme")
    print("3-Öğrenci Arama..")
    print("4-Çıkış..")
    secim=input("Bir Seçim Yapınız......:")
    if secim == "1":
       ad=input("Öğrencinin Adını Girin........")
       notu=input("Notunu Girin")
       with open("ogrenci.txt","a",encoding="utf_8") as dosya:
           dosya.write(ad+";" +notu+"\n")
           print("Öğrenci Kaydı Yapıldı")
    elif secim == "2":
        try:
            with open("ogrenci.txt","r",encoding="utf_8") as dosya:
                for satir in dosya:
                    bilgiler=satir.strip().split(";")
                    print(f"Öğrenci Adı {bilgiler[0]} Öğrenci Notu {bilgiler[1]}")
                print("---------------")
        except FileNotFoundError:
            print("Dosya Bulunamadı!")
    elif secim == "3":
        aranan=input("Aranacak Öğrenci Adını Girin")
        bulundu=False
        with open("ogrenci.txt","r",encoding="utf_8") as dosya:
            for satir in dosya:
                bilgiler=satir.strip().split(";")
                if bilgiler[0].lower()==aranan.lower():
                    bulundu=True
                    print(f"Öğrenci Adı {bilgiler[0]} Notu {bilgiler[1]}")
            if bulundu==True:
                print("Kayıt Bulundu")
            else:
                print("Kayıt Bulunamadı")
    elif secim == "4":
        print("Sistemden Çıkış Yapıldı...")
        break
    else:
        print("Hatalı Seçim Yaptınız..")