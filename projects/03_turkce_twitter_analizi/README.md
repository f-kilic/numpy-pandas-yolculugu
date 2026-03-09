# Türkçe Twitter Verisi ile Uçtan Uca NLP ve Metin Sınıflandırma (PoC)

## 📌 Proje Özeti

Bu proje, Twitter üzerinden elde edilen gürültülü metin verilerini Doğal Dil İşleme (NLP) teknikleri ile temizleyerek, tweetlerin **"Ürün Şikayeti/Yorumu (1)"** veya **"Günlük Geyik (0)"** olup olmadığını sınıflandıran bir Makine Öğrenmesi boru hattı oluşturmayı amaçlamaktadır.

Proje bir **Proof of Concept (PoC)** çalışmasıdır ve küçük ölçekli bir veri seti üzerinde temel bir NLP sınıflandırma pipeline’ı kurmayı hedefler.

---

## ⚙️ Kullanılan Teknolojiler

**Veri İşleme**

* Pandas
* NumPy

**Doğal Dil İşleme (NLP)**

* Regular Expressions (Regex)
* Stop Words Filtreleme

**Makine Öğrenmesi**

* Scikit-Learn

  * TF-IDF Vectorizer
  * Logistic Regression
  * Train-Test Split

**Veri Görselleştirme**

* Matplotlib

---

## 🏗️ Proje Mimarisi

Proje, kodun okunabilirliğini ve sürdürülebilirliğini artırmak amacıyla **Separation of Concerns** prensibine uygun şekilde modüler olarak yapılandırılmıştır.

### 1️⃣ Veri Birleştirme

`01_veri_birlestirme.py`

* Parçalı CSV veri setlerinin birleştirilmesi
* Gereksiz sütunların kaldırılması (URL vb.)
* Etiketlerin sayısallaştırılması

---

### 2️⃣ Metin Temizleme ve Analiz

`02_filtreleme_analizi.py`

* Metinlerin küçük harfe dönüştürülmesi
* Noktalama işaretlerinin temizlenmesi
* Türkçe stop words filtreleme
* Makine öğrenmesi için metin verisinin hazırlanması

---

### 3️⃣ Vektörizasyon ve Model Eğitimi

`03_vektorizasyon.py`

* Temizlenmiş metinlerin **TF-IDF** yöntemi ile sayısal özelliklere dönüştürülmesi
* Lojistik Regresyon modeli ile sınıflandırma
* Modelin test verisi üzerinde değerlendirilmesi

TF-IDF çıktısı:

* **594 tweet**
* **9690 benzersiz kelime özelliği**

---

## 📊 Model Performansı

Veri seti **%80 eğitim** ve **%20 test** olacak şekilde ayrılmıştır.

| Metric                     | Değer  |
| -------------------------- | ------ |
| Accuracy                   | %91.67 |
| Precision (Sınıf 1 – Ürün) | 0.98   |
| Recall (Sınıf 0 – Geyik)   | 0.98   |

Bu sonuçlar küçük ölçekli veri üzerinde modelin makul bir ayrım yapabildiğini göstermektedir.

---

## ⚠️ Sınırlamalar

Bu çalışma **küçük ölçekli bir veri seti (~1197 tweet)** üzerinde gerçekleştirilmiştir.
Model, eğitim verisinde bulunmayan bazı spesifik sektör kelimeleri ile karşılaştığında daha temkinli tahminler yapabilmektedir.

Bu nedenle model performansı **veri setinin kapsamı ile sınırlıdır** ve gerçek dünya uygulamaları için daha büyük ve çeşitli veri setleri gereklidir.

---

## 🔮 Gelecek Geliştirmeler

* Veri setinin büyütülmesi
* Cross-validation ile model değerlendirmesi
* Farklı modellerin karşılaştırılması

  * Naive Bayes
  * Linear SVM
* Transformer tabanlı NLP modelleri (BERT vb.) ile performans karşılaştırması

---

## 🎯 Amaç

Bu proje, gürültülü sosyal medya verisi üzerinde:

* temel NLP veri temizleme adımlarını
* TF-IDF tabanlı özellik çıkarımını
* klasik makine öğrenmesi sınıflandırma pipeline’ını

uygulamalı olarak göstermek amacıyla geliştirilmiştir.
