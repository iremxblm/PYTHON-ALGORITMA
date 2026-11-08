#taş kağıt makas oyunu
import random
secenekler=["taş","kağıt","makas"]
bilgisayar_secim=random.randint(1,3)
oyuncu_puan=0
bilgisayar_puan=0
print("---TAŞ KAĞIT MAKAS OYUNU---")
print("İlk 3 puana erişen kazanır....")
#while kural uyduğu sürece devam eder...
while oyuncu_puan<3 and bilgisayar_puan<3:
    oyuncu_secim=input("\n Taş,Kağıt,Makas Seçiniz:").lower()
    if oyuncu_secim not in secenekler: #dizi içerisinde arama yapıyoruz
        print("Girilen Seçim Doğru Değil...")
        continue
    bilgisayar=random.choice(secenekler)
    print("Senin Seçimin:",oyuncu_secim)
    print("Bilgisayar Seçim:",bilgisayar)
    if (oyuncu_secim==bilgisayar_secim):
        print("Berabere..")
    elif (oyuncu_secim=="taş" and bilgisayar=="makas"):
        print("Sen Kazandın..")
        oyuncu_puan+=1
    elif (oyuncu_secim=="kağıt" and bilgisayar=="taş"):
        print("Sen Kazandın..")
        oyuncu_puan += 1
    elif (oyuncu_secim=="makas" and bilgisayar=="kağıt"):
        print("Sen Kazandın..")
        oyuncu_puan += 1
    else:
        print("Kaybettiniz..")
        bilgisayar_puan+=1
    print(f"Bilgisayar puanı {bilgisayar_puan} --- Oyuncu Puanı {oyuncu_puan}")
    if(oyuncu_puan==3):
        print("Siz Kazandınız Tebrikler Oyun Bitti..")
    else:
        print("Bilgisayar Kazandı Oyun Bitti..")