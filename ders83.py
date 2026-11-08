#hazine bulma oyunu

import random
print("---HAZİNE AVI OYUNU---")
print("Gizli Olan Hazineyi Bulmaya Çalış")
print("Harita Boyutları 5*5 Şeklindedir")
print("1-5 Arasında Bir Satır ve Sutün Seçmelisin..")
hazine_satir=random.randint(1,5)
hazine_sutün=random.randint(1,5)
hak=3
while hak>0:
    print("\n Kalan Hak Miktarı:")
    satir=int(input("Satır Seçiniz (1-5)"))
    sutun=int(input("Sutün Seçiniz (1-5)"))
    if satir<1 or satir>5 or sutun<1 or sutun>5:
        print("Geçersiz Seçim Yapıldı... 1 ile 5 arasında seçim")
        continue
    if satir==hazine_satir and sutun==hazine_sutün:
        print("----------------------------------")
        print("\n Tebrikler Kazandınız..")
        print("----------------------------------")
        break
    else:
        print("Burada Hazine Yok...")
        if satir<hazine_satir:
            print("Hazine daha aşağıda bir satırdadır")
        elif satir>hazine_satir:
            print("Hazine daha yukarıda bir satırdadır")

        if sutun<hazine_sutün:
            print("Hazine daha sağda yer almaktadır")
        elif sutun>hazine_sutün:
            print("Hazine daha soldadır")
        hak-=1
    if hak==0:
        print("Malesef Hakkınız Bitti...")
        print("Hazineyi Bulamadınız....")
        print(f"Hazine Satır {hazine_satir}, Hazine Sutün {hazine_sutün}")
        print("\n Oynadığınız İçin Teşekkür Ederiz....")