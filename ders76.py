class Ogrenci:
    def __init__(self,ad,notu):
        self.ad=ad
        self.__notu=notu
    #setter
    def set_notu(self,yeni_notu):
        if yeni_notu<=0 or yeni_notu<=100:
            self.__notu=yeni_notu
        else:
            print("Girilen Notunuz 0 ile 100 arasında olmalıdır...")
    #getter
    def get_notu(self):
        return self.__notu
caner=Ogrenci("Caner",90)
print(caner.get_notu())
caner.set_notu(-50)
print(caner.get_notu())