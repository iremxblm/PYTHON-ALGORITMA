#musteri ve istedikleri yemekler var yemeklere göre fiyatlar var
# sipariş tutarı 500tl ve üzeri ise ½10 indirim
#indirim sonrası %5 servis ücreti eklenecek
#müşteri toplam ödeyeceği tutar nedir
def siparis(*fiyatlar):
    toplam=0
    toplam_indirim=0
    for fiyat in fiyatlar:
        toplam += fiyat
        if fiyat>500:
            indirim=(fiyat*10)/100
            servis=indirim*0.5
            toplam_indirim += servis + indirim
        else:
            indirim=0
    genel_toplam=toplam-toplam_indirim
    print(f"Toplam Sipariş Sayısı {len(fiyatlar)}")
    print(f"Sipariş Toplam Fiyatı:{toplam}")
    print(f"İndirim Toplamı: {toplam_indirim}")
    print(f"Genel Toplam:{genel_toplam}")
siparis(600,400,1000)
