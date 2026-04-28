# Telco Customer Churn Analizi (Müşteri Kaybı Analizi)

## 📌 Proje Hakkında
Bu proje, telekomünikasyon sektöründeki müşteri kaybını (churn) önceden tahmin etmeyi ve hangi faktörlerin müşterilerin şirketi terk etmesinde etkili olduğunu analiz etmeyi amaçlamaktadır. Projede popüler **IBM Telco Customer Churn** veri seti kullanılmıştır. 

Müşteri kaybını tahmin etmek, şirketlerin müşteri elde tutma stratejileri geliştirmesi, memnuniyeti artırması ve gelir kayıplarını en aza indirmesi açısından kritik bir öneme sahiptir.

## 📊 Veri Seti Özeti
**IBM Telco Customer Churn** veri seti, kurgusal bir telekomünikasyon şirketinin müşteri verilerini içermektedir. 
İçerdiği temel özellik kategorileri şunlardır:
- **Hizmet Bilgileri:** Telefon hizmeti, internet hizmeti, çevrimiçi güvenlik, cihaz koruması, teknik destek, TV yayını abonelikleri vb.
- **Müşteri Hesap Bilgileri:** Ne kadar süredir müşteri oldukları (tenure), sözleşme türü, ödeme yöntemi, faturasız ödeme (paperless billing), aylık ve toplam fatura tutarı vb.
- **Demografik Bilgiler:** Cinsiyet, yaş, partneri ve bakmakla yükümlü olduğu kişiler olup olmadığı.
- **Hedef Değişken (Churn):** Müşterinin son ay içinde aboneliğini iptal edip etmediği (`Yes` veya `No`).

## 🎯 Projenin Amacı ve Adımları
1. **Keşifçi Veri Analizi (EDA):** Veriyi anlama, eksik veya hatalı değerleri inceleme ve korelasyonları görselleştirme.
2. **Veri Ön İşleme:** Kategorik değişkenlerin sayısal verilere dönüştürülmesi (encoding - One-Hot, Label Encoding), aykırı değer analizi ve özellik ölçeklendirme (scaling).
3. **Makine Öğrenmesi Modellemesi:** Farklı sınıflandırma algoritmaları kullanarak churn tahmini yapan en iyi modellerin geliştirilmesi.
4. **Model Değerlendirme:** Karmaşıklık matrisi (Confusion Matrix), Doğruluk (Accuracy), Kesinlik (Precision), Duyarlılık (Recall) ve F1-Skoru gibi metriklerle modellerin başarılarını kıyaslama ve hiperparametre optimizasyonu.

## 🛠️ Kullanılan Teknolojiler ve Kütüphaneler
- **Programlama Dili:** Python 3.x
- **Veri Manipülasyonu:** Pandas, NumPy
- **Veri Görselleştirme:** Matplotlib, Seaborn vb.
- **Geliştirme Ortamı:** Jupyter Notebook

## 🚀 Kurulum ve Çalıştırma Yönergeleri
Projeyi kendi bilgisayarınızda (lokalinizde) çalıştırmak için aşağıdaki adımları izleyebilirsiniz:

1. Bu projeyi bilgisayarınıza indirin (clone/download).
2. Proje dizininde önceden hazırlanmış olan `churn_env` adlı sanal ortamı aktif edin:
   - Windows (PowerShell) için: `.\churn_env\Scripts\Activate.ps1`
   - Windows (CMD) için: `.\churn_env\Scripts\activate.bat`
   - MacOS/Linux için: `source churn_env/bin/activate`
3. Proje klasöründe Jupyter Notebook'u başlatın:
   \`\`\`bash
   jupyter notebook
   \`\`\`
4. Başlatılan arayüzde **`churn.ipynb`** dosyasını açarak analizleri ve makine öğrenmesi adımlarını çalıştırıp inceleyebilirsiniz.

## 🌐 API ve Canlı Servis Entegrasyonu
Projemiz sadece yerel bir analizden ibaret değildir; geliştirilen model **FastAPI** ve **Render** kullanılarak herkesin erişebileceği canlı bir web servisine (API) dönüştürülmüştür. 

Modelimizi anında test etmek ve veri setindeki özelliklere (tenure, aylık ücret vb.) göre anlık "Churn" (ayrılma) tahmini almak için aşağıdaki bağlantıyı kullanabilirsiniz:

👉 **[Canlı API Test Ekranı (Swagger UI) İçin Tıklayın](https://telco-customer-churn-penc.onrender.com/docs)**

*(Not: Proje ücretsiz Render sunucularında barındırıldığı için, siteye bir süre giriş yapılmadığında sunucu uyku moduna geçer. Linke tıkladığınızda sayfanın açılması ilk seferde 50-60 saniye sürebilir, yüklendikten sonra normal hızında çalışacaktır.)*

## 📌 Sonuçlar ve Değerlendirme
*(Not: Bu bölüm modelleme bittiğinde ve nihai analiz elde edildiğinde elde edilen başarı oranına, en belirleyici değişkenlere (Feature Importance) ve iş çözümlerine göre güncellenebilir.)*
