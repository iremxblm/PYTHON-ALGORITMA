#tuples
listem=[1,2,3,4,5,6,7,8,9]
meyveler=("Elma","Armut","Kivi")
for i in listem:
    print(i)
for i in meyveler:
    print(i)
#list[] tuples()
#liste ekleme güncelleme değiştirme yapılıyor
#listede veriler değişebilir tuples da veriler değişmez
#set {} süslü parantez kullanılır list []
#tuple ve liste eleman tekrarı olur sette olmaz
#liste içindeki eleman sırası korunur set korunmaz
#list append eleman eklerken add
#list remove pop set remove discard silme yapılıyor
#list ve set değiştirilir içindeki değeri değiştirebiliriz
#kullanım amacı list sıralı ve tekrarlı set benzersiz bir liste oluşturur
sebzeler={"Maydonoz","Dere Otu","Nane","Roka"}
for i in sebzeler:
    print(i)
sebzeler.add("pırasa")
print(sebzeler)
sebzeler.remove("Roka")
