sayilar=[10,37,45,68,3,42,15,1]
#1.soru bunları tek tek ekrana yazdırın
#2.soru bunları küçükten büyüğe doğru sıralayın
#3.soru bunları büyükten küçüğe doğru sıralayın
#4.soru çift rakamları ekrana yazdırın
#5.soru tek rakamları ekrana yazdırın

#1.SORU
print(sayilar)

#2.soru
sayilar.sort()
print(sayilar)

#3.soru
sayilar.sort(reverse=True)
print(sayilar)

#4.soru
for i in sayilar:
    if i % 2 == 0:
        print(f"Çift sayılar {i}")

#5.soru
for i in sayilar:
    if i % 2 !=0:
        print(f"Tek sayılar {i}")
print(sum(sayilar))
#dizi içindeki sayıların toplamını alır
print(max(sayilar))
#dizi içindeki enbüyük sayıyı bulur
print(min(sayilar))
ortalama=sum(sayilar)/len(sayilar)
#sayıların ortalaması toplam/adet
print(ortalama)