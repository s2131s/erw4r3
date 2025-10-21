# Google Search Automation (Python)

Python ile Google'da otomatik arama yapan basit bir script.

## Özellikler

- Selenium WebDriver kullanarak Google'da otomatik arama
- Kolay kullanım
- Özelleştirilebilir arama terimleri

## Kurulum

### 1. Python Paketlerini Yükle

```bash
pip install -r requirements.txt
```

### 2. Chrome WebDriver

Bu script Chrome tarayıcısı kullanır. Sisteminizde Chrome yüklü olmalıdır.

#### Linux'ta Chrome Kurulumu:

```bash
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo apt install ./google-chrome-stable_current_amd64.deb
```

#### ChromeDriver Kurulumu (Otomatik):

Script, Selenium 4.15+ sürümü ile birlikte gelen otomatik driver yönetimini kullanır.

## Kullanım

### Varsayılan Arama ("selam"):

```bash
python google_search.py
```

### Script İçinden Farklı Kelime Arama:

`google_search.py` dosyasını düzenleyip farklı bir arama terimi belirtin:

```python
if __name__ == "__main__":
    google_search("Python programlama")
```

## Script Çalışması

Script şu adımları gerçekleştirir:

1. Chrome tarayıcısını açar
2. Google.com'a gider
3. Arama kutusunu bulur
4. Belirtilen kelimeyi yazar
5. Enter tuşuna basar
6. Sonuçları gösterir
7. 5 saniye bekler
8. Tarayıcıyı kapatır

## Notlar

- Tarayıcıyı görünmez (headless) modda çalıştırmak için `google_search.py` dosyasındaki ilgili satırı aktif edin
- İnternet bağlantısı gereklidir
- Google'ın güvenlik kontrollerini (CAPTCHA vb.) tetikleyebilir