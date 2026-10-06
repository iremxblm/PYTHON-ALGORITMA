dogru_sifre = 1234
hak = 3

while hak > 0:

    sifre = int(input("Şifrenizi giriniz: "))

    if sifre == dogru_sifre:
        print("Giriş başarılı!")
        break

    else:
        hak = hak - 1
        print("Hatalı şifre!")
        print(f"Kalan deneme hakkınız: {hak}")

if hak == 0:
    print("Kartınız bloke edildi!")