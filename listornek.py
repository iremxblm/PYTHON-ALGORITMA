#list [] {key:value}
#meyveler[0] sebzeler ["Domates"]
#liste tekrarlı var anahtar tekrar etmez değer tekrar edebilir
#list anahtar dictionary var
#veri append dizi["anahtar"]=yeni
#pop remove list dictionary pop ve del
#sıralı ve numaralı liste sıralama anahatr ya da içindeki değere sıralama yapılabilir
ogrenci={"numara":1,"Adi":"Deniz","sinif":"10A","yas":17}
print(ogrenci["yas"])
print(ogrenci["numara"])
print(ogrenci["sinif"])
ogrenci["Adi"]=("İrem")

for k,v in ogrenci.items():
    print(k,v)
