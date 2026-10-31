try:
    dosya = open("ogrenci.txt","r", encoding="utf-8")
    icerik=dosya.read()
    print(icerik)
    dosya.close()


except  FileNotFoundError:
    print("Dosya Bulunamadı...")
except PermissionError:
    print("Dosya Erişim Hatası")
