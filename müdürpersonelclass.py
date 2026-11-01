class Personel:
    def __init__(self,ad,soyad,maas):
        self.ad=ad
        self.soyad=soyad
        self.maas=maas
    def bilgi_goster(self):
        print(f"Personel adı {self.ad} Personel Soyad {self.soyad} Maaş {self.maas}")
#alt klass

class Ogretmen(Personel):
    def ders_ver(self):
        print(f"Öğretmen Personel  {self.ad} {self.soyad} Ders Verildi")

class Mudur(Personel):
    def toplanti_yap(self):
        print(f"Müdür {self.ad} {self.soyad} Toplantı Yapıyor...")

murat=Personel("Murat","Çıplak","5000")
murat.bilgi_goster()
mudur=Mudur("Esranur","Çakmak","15000")
mudur.bilgi_goster()
mudur.toplanti_yap()

irem=Ogretmen("İrem","Bulum","20000")
irem.bilgi_goster()
irem.ders_ver()
