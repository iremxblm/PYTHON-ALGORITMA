dosya=open("ogrenci.txt","r",encoding="utf-8")
for satir in dosya:
    print(satir.strip())
dosya.close()
#satır içerisindeki dosyaları ayrı satırlarda ekrana yazdırır
