#bankadaki paramız  5000 tl
#bankadan para çekeceğiz
para=5000
cekilen=float(input("Çekmek istediğiniz tutarı yazınız "))

if para >cekilen:
    toplam=para -cekilen
    print(f"Ödenecek tutar {toplam} çekilen tutar {cekilen}")
else:
    print("Bakiye yetersiz")
