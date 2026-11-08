import random

class SayiTutmaOyunu:
    def __init__(self):
        self.sayi=random.randint(1,100)
        self.deneme=0
        self.devam_durumu=True
    def tahmin_et(self):
        try:
            tahmin=int(input("1-100 arasında bir sayı giriniz.."))
            if tahmin<1 or tahmin>100:
                print("Girilen Sayı 1 ile 100 arasında olmalıdır...")
                return None
            return tahmin

        except Exception as e:
            print("Hata oluştu",e)
            return None
    def tahmin_kontrol(self,tahmin):
        if tahmin is None:
            return
        self.deneme+=1
        if tahmin>self.sayi:
            print("Daha Küçük Bir Sayı Giriniz:")
        elif tahmin<self.sayi:
            print("Daha Büyük Bir Sayı Giriniz:")
        else:
            print("Tebrikler Kazandınız....")
            print("************************")
            print(f"Deneme Sayısı {self.deneme}")
            print(f"Tutulan Sayı {self.sayi}")
            print("*************************")
            self.devam_durumu=False
    def oyunu_baslat(self):
        print("****SAYI BULMA OYUNUNA HOŞ GELDİNİZ****")
        print("---------------------------------------")
        while self.devam_durumu:
            tahmin=self.tahmin_et()
            self.tahmin_kontrol(tahmin)
irem=SayiTutmaOyunu()
irem.oyunu_baslat()