
# Pandas, veri biliminin ve analizinin "inşaat alanıdır".
# NumPy kusursuz ve homojen sayılarla matematiksel işlemler yaparken; Pandas gerçek dünyanın kirli,
# eksik (NaN), metin ve sayıların birbirine girdiği dağınık verilerini alıp, SQL veya Excel tablolarına 
# benzeyen düzenli veri çerçevelerine (DataFrame) dönüştürerek analiz etmeyi, filtrelemeyi ve temizlemeyi sağlar.
# Pandas'ta 3 temel veri objesi vardır: Series, DataFrame ve Index

import numpy as np
import pandas as pd

# 1. SERIES (SERİLER) MANTIĞI
data = pd.Series([0.25, 0.5, 0.75, 1.0])
# Default olarak indeksler sıfırdan başlar
print("--- Basit Seri ---")
print(type(data))
print("2. indeksdeki eleman:", data[2])
print(data)
print("İndeks yapısı:", data.index)

# Pandas serilerinin diğer sıralı bilgi saklayan objelerden (list/array) farklı
# olduğu noktalardan bir tanesi indekslere isteğe bağlı etiketler (label) atayabilmemizdir.
data2 = pd.Series([0.25, 0.5, 0.75, 1.0], index=['a', 'b', 'c', 'd'])
print("\n--- Etiketli Seri ---")
print(data2)
print("Yeni indeks yapısı:", data2.index)

# 2. VERİ YAPILARI ARASINDAKİ FARKLAR (List vs NumPy vs Pandas)
# NumPy tekrar edenleri teke İNDİRGEMEZ (o set'in işidir). 
# NumPy, farklı tipleri tek bir tipe (genelde string'e) zorla dönüştürür (Upcasting).
# Pandas ise farklı data tiplerini bir DataFrame içinde kendi orijinal halleriyle tutabilir.

new_data_list = [2, 3.25, 6, 0.75, None]
new_data_array = np.array([2, 3.25, 6, 0.75, np.nan])
new_data_series = pd.Series(new_data_list) # None değerini otomatik NaN'a çevirir

print("\n--- Kayıp Veri (NaN) ile Başa Çıkma ---")
# print(sum(new_data_list)) # HATA VERİR! Liste None ile matematiksel işlem yapamaz.
print("NumPy Sum:", new_data_array.sum()) # nan çıktısı verir, nan'ı görürse işlemi bozar.
print("Pandas Sum:", new_data_series.sum()) # Pandas NaN'ı göz ardı eder ve geriye kalanı toplar.

# 3. SÖZLÜKLERDEN (DICTIONARY) SERİ OLUŞTURMA
population_dict = {
    'California': 38332521,
    'Texas': 26448193,
    'New York': 19651127,
    'Florida': 19552860,
    'Illinois': 12882135
}
population = pd.Series(population_dict)

print("\n--- Dilimleme (Slicing) Farkı ---")
# String (etiket) indekslemede bitiş noktası DAHİLDİR.
print(population['California':'Florida'])

# 4. DATAFRAME (VERİ ÇERÇEVESİ) OLUŞTURMA
# İki veya daha fazla 1 boyutlu Serinin yan yana gelmesiyle oluşan 2 boyutlu tablolardır.


area_dict = {
    'California': 423967, 'Texas': 695662, 'New York': 141297,
    'Florida': 170312, 'Illinois': 149995
}
area = pd.Series(area_dict)

# İki ayrı Seriyi (population ve area) birleştirip DataFrame yapıyoruz
states = pd.DataFrame({
    'population': population,
    'area': area
})

print("\n--- İlk DataFrame ---")
print(states)
print("Satır İndeksleri:", states.index)
print("Sütun İsimleri:", states.columns)

# 5. FARKLI DATAFRAME OLUŞTURMA YÖNTEMLERİ
print("\n--- Eksik Veri İçeren Sözlükten DataFrame ---")
a8 = pd.DataFrame([{'a': 1, 'b': 2}, {'b': 3, 'c': 4}])
# İlk sözlükte 'c', ikinci sözlükte 'a' yok. Pandas bunlara otomatik NaN basar.
print(a8)

print("\n--- NumPy Matrisinden DataFrame ---")
a9 = pd.DataFrame(
    np.random.rand(3, 2), 
    columns=['foo', 'bar'], 
    index=['a', 'b', 'c']
)
print(a9)