bakiye=5000
try:
    cekilecek=int(input("Çekilecek Tutarı Giriniz"))
    if cekilecek<=0:
        raise ValueError("Çekilecek Rakam Sıfırdan Küçük Olamaz")
    if cekilecek>bakiye:
        raise Exception("Bakiye Yetersiz")


    bakiye=bakiye-cekilecek
    print(f"Para Çekme İşlemi Başarılı {bakiye} Çekilen Tutar {cekilecek}")

except Exception as e: #hata yakalama
    print(f"Hata {e}")

finally: #hata olsa da olmasa da finally içerisine yazılan kodlar çalışır
    print("İşlem Bitti")
