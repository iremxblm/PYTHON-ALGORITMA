notlar=[50,80,75,89,90]
#sınav not değerlendirmesi
#eğer notu 50den büyük ve eşitse geçti
#değilse >=50
for i in notlar:
    if i>=50:
        print(f"{i} Notu Geçti...")
    else:
        print(f"{i} Notu Kaldı...")
