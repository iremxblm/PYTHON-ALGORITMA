bakiye=10000
print("ABC Bankasına Hoşgeldiniz..")
print("Yapacağınız işlemi seçiniz..")
islem=int(input("1- Bakiye GÖrüntüle 2- Para Yatır 3- Para Çek"))

if islem==1:
    print(f"Bakiyeniz {bakiye} TLdir.")
elif islem==2:
    yatır=int(input("Yatırmak istediğiniz tutarı giriniz"))
    toplam=yatır+bakiye
    print(f"Güncel Bakiyeniz {toplam} Tldir.")
else:
    cek=int(input("Çekmek istediğiniz tutarı giriniz"))
    if cek<= bakiye:
        toplam=bakiye-cek
        print(f"Tebrikler {cek} para çektiniz. Güncel bakiyeniz {toplam}")
    else:
        print("Bakiyeniz yetersiz...")
        
    
