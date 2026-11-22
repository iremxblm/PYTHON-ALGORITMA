import pandas as pd
import numpy as np

veriler={
    "Adi":["Ahmet","Mehmet","Hasan","Hüseyin","Murat"],
    "Soyad":["Yılmaz","Kasım","Fedai","Muallim","Selam"],
    "Yas":[16,26,40,48,None],
    "Not":[70,80,90,100,None]
}

df=pd.DataFrame(veriler)
print(df)
print(df.isnull()) #boş olan değerleri gösterir
print(df.isnull().sum())
df["Not"]=df["Not"].fillna(0)
print(df)
df["Yas"]=df["Yas"].fillna(0)
print(df)
df=df.dropna(how="all") #boş olan alanları siler
print(df)
