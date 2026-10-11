sepet = []
while True:

    urunler={"1":"Çikolata","2":"Kek","3":"Soda","4":"Kola"}
    print("Otomat Programı")
    print("Çikolata için 1 Basın..")
    print("Kek için 2 Basın..")
    print("Soda için 3 Basın..")
    print("Kola için 4 Basın..")
    secim=input("Seçim Yapınız...")
    if secim=="1":
        print(urunler[secim])
        sepet.append(urunler[secim])
    elif secim=="2":
        print(urunler[secim])
        sepet.append(urunler[secim])
    elif secim=="3":
        print(urunler[secim])
        sepet.append(urunler[secim])
    elif secim=="4":
        print(urunler[secim])
        sepet.append(urunler[secim])
    else:
        print("Seçilen ürün bulunmamaktadır...")
    soru=input("Sistemden Çıkmak İstiyor Musunuz Evet(E) Hayır(H)")
    if soru.lower()=="e":
        t=1
        for i in sepet:
            print(f"{t}.Seçilen Ürünler {i}")
            print("=================")
            print(len(sepet),"Ürün Seçildi..")
            t=t+1
        False
    elif soru.lower()=="h":
        print("Sistem Çalışmaya Devam ediyor")
    else:
        print("Geçerli bir harfe basın")
