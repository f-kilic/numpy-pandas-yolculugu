
# NumPy ve Pandas Çalışmalarım
Bu repo, veri analizi temelleri ve profesyonel Python standartlarına geçiş notlarımı içermektedir.

Matplotlib ile Object-Oriented veri görselleştirme ve Boolean Masking çalışıldı.

Pandas Serileri, DataFrame yapıları ve NaN (Kayıp Veri) yönetimi incelendi.

Pandas loc, iloc indeksleme ve Series/DataFrame boyut farkları işlendi.

- Pandas ile NaN veri yönetimi, Merge/Concat işlemleri ve GroupBy mantığı eklendi.


# Türkçe Twitter (X) Ürün ve Marka Analizi (NLP Preprocessing)

Bu proje, Türkçe sosyal medya (Twitter) verileri üzerinde Doğal Dil İşleme (NLP) teknikleri kullanılarak marka ve ürün konuşulma frekanslarını (Social Listening) analiz etmeyi amaçlamaktadır.

## 📌 Proje Adımları
1. **Veri Entegrasyonu:** Parçalanmış CSV veri setleri (`pd.concat`) ile tek bir yapı altında birleştirildi.
2. **Veri Temizliği (Data Cleaning):** Gürültü yaratan gereksiz sütunlar (`url`) silindi ve etiketler makine öğrenmesine uygun hale getirilecek şekilde sayısallaştırıldı (Binary Encoding - 0 ve 1).
3. **Metin Ön İşleme (NLP Preprocessing):** - Tüm metinler küçük harfe çevrildi (Lowercasing).
   - Noktalama işaretleri ve özel semboller Regex kullanılarak temizlendi (Punctuation Removal).
4. **Frekans Analizi:** Anlamsız bağlaçlar ve dolgu kelimeleri (Stop Words) filtrelenerek, verideki gerçek marka ve ürün trendleri ortaya çıkarıldı.
5. **Görselleştirme:** Matplotlib kullanılarak en çok konuşulan markalar bir Dashboard grafiğine dönüştürüldü.

## ⚠️ Veri Etiği ve İçerik Uyarısı (Disclaimer)
Bu proje, Kaggle üzerinden alınan gerçek sosyal medya verileri kullanılarak hazırlanmıştır. İnternet ve sosyal medyanın filtresiz doğası gereği, veri seti içerisinde argo, küfür veya rahatsız edici ifadeler bulunabilir. 

Bir veri bilimi projesinde **veriyi sansürlemek, istatistiksel gerçeği bükmek anlamına gelir.** Bu nedenle, ileride yapılacak olası Duygu Analizi (Sentiment Analysis) modellerinin gerçek dünya (real-world) verisiyle doğru eğitilebilmesi ve verinin orijinal yapısının bozulmaması adına metinlere **sansür uygulanmamıştır.** Proje, tamamen teknik analiz ve eğitim amacıyla geliştirilmiştir.

## 🛠️ Kullanılan Teknolojiler
- Python
- Pandas (Data Manipulation)
- Matplotlib (Data Visualization)
- Regex (Text Processing)