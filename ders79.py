#polimorfizm örneği

class Ogretmen:
    def calis(self):
        print("Öğretmen Ders Anlatıyor")

class Mudur:
    def calis(self):
        print("Müdür Toplantı Yapıyor")
class Ogrenci:
    def calis(self):
        print("Öğrenci Ders Çalışıyor")
deniz=Ogrenci()
irem=Mudur()
caner=Ogretmen()
deniz.calis()
irem.calis()
caner.calis()
