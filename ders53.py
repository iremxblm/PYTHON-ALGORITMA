def kullanici_bilgisi(**kwargs):
    for anahtar, deger in kwargs.items():
        print(anahtar,":",deger)

kullanici_bilgisi(
    isim="İrem",
    yas=26,
    meslek="Mühendis"
)