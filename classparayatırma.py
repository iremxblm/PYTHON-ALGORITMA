#ad public değişken yani her taraftan ulaşılabilir değiştirilebilir
#_ad protected yani kısıtlı korumalı değişken
#__ad private yani ulaşıma kapalıdır gizli

class Banka:
    def __init__(self,ad,bakiye):
        self.ad=ad
        #self.bakiye=bakiye public
        self.__bakiye=bakiye  #protected değişken oluşturuldu
    def para_yatir(self,miktar):
        if miktar>=0:
            self.__bakiye+=miktar
            print("Para Yatırıldı.....")
        else:
            print("Hatalı Rakam Girişi.....")
    def bakiye_goster(self):
        print(f"Hesaptaki Bakiye {self.__bakiye}")
deniz=Banka("deniz",5000)
deniz.para_yatir(3000)
deniz.bakiye_goster()
