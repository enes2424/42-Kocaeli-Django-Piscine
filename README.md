# 42 Kocaeli Django Piscine

## Librairies

Bu proje, 42 Okulu Django Piscine eğitiminin dördüncü modülüdür. Python temelleri, dosya yönetimi, HTTP istekleri, web verisi çekme, sanal ortam kurulumu ve temel Django uygulama yapısı konularını kapsar.

Bu modül, Django öğrenmeye başlamak için gerekli ilk adımları içerir. Basit scriptlerden başlayarak temel web kavramlarına giriş yapılır ve daha sonra Django projeleri oluşturulmaya başlar.

## 📚 Egzersizler

### ex00 - Geohashing

**Dosya:** `ex00/geohashing.py`

Koordinat bilgisi ve tarih kullanarak geohash benzeri işlemler yapan temel Python scripti.

- **Fonksiyon:** `main()`
- **Açıklama:** Komut satırı argümanlarını alır, latitude ve longitude değerlerini işler ve `antigravity` kütüphanesiyle işlemi gerçekleştirir
- **Özellikler:**
  - Argüman kontrolü yapar
  - Geçersiz girişlerde hata mesajı verir
  - Çalışma zamanı hatalarını yönetir
- **Kullanım:**
  ```bash
  python3 ex00/geohashing.py 41.0082 28.9784 2024-01-01
  ```

### ex01 - Directory & File Creation

**Dosya:** `ex01/my_program.py`

Klasör ve dosya oluşturma işlemi yapan basit bir örnek.

- **Kütüphane:** `path`
- **Açıklama:** Yeni bir dizin oluşturur, içine bir dosya yazıp içeriği ekrana basar
- **Özellikler:**
  - Klasör oluşturma
  - Dosya oluşturma
  - Metin yazma ve okuma
- **Örnek:**
  ```python
  dir = Path("enes")
  dir.mkdir_p()
  file = dir / "ates.txt"
  file.write_text("Hello, World!\n")
  ```

### ex02 - Wikipedia API Request

**Dosyalar:** `ex02/request_wikipedia.py`, `ex02/requirements.txt`

Harici bir API'den veri çekme ve içeriği dosyaya dönüştürme örneği.

- **Fonksiyonlar:**
  - `fetch_page_by_title(title)`
  - `extract_content_from_query(data)`
  - `write_to_file(search_term, content)`
- **Açıklama:** Wikipedia API'ye istek atar, sayfa içeriğini çıkarır ve temizlenmiş metni `.wiki` dosyası olarak kaydeder
- **Özellikler:**
  - `requests` ile HTTP isteği gönderir
  - JSON veriyi işler
  - Wiki markup formatını temizler
- **Kullanım:**
  ```bash
  python3 ex02/request_wikipedia.py "Python"
  ```

### ex03 - Roads to Philosophy

**Dosya:** `ex03/roads_to_philosophy.py`

Wikipedia sayfaları arasında geçiş yaparak “Philosophy” sayfasına ulaşma mantığını simüle eden uygulama.

- **Açıklama:** Başlangıç sayfasından ilk geçerli bağlantı üzerinden devam eder ve hedefe ulaşmaya çalışır
- **Özellikler:**
  - Web sayfası çekme
  - HTML ayrıştırma
  - Link takibi
  - Sonsuz döngü ve dead end kontrolü
- **Temel Mantık:**
  - Sayfa başlığı kontrol edilir
  - Redirect ve geçerli bağlantı bulunur
  - “Philosophy” hedefi bulunana kadar devam eder

### ex04 - Python Environment Setup

**Dosyalar:** `ex04/my_script.sh`, `ex04/requirements.txt`

Python sanal ortamı kurulumu ve bağımlılık yükleme işlemini otomatikleştiren betik.

- **Açıklama:** Python 3 kurulumunu hazırlar, sanal ortam oluşturur ve gerekli paketleri yükler
- **Özellikler:**
  - `venv` kullanır
  - Paket güncellemesini yapar
  - `requirements.txt` dosyasını okur
- **Kullanım:**
  ```bash
  bash ex04/my_script.sh
  ```

### ex05 - Django Hello World

**Dosyalar:** `ex05/manage.py`, `ex05/helloworld/settings.py`, `ex05/helloworld/urls.py`, `ex05/helloworld/views.py`

En temel Django uygulamasını oluşturma örneği.

- **Açıklama:** Django projesi başlatılır, URL tanımlanır ve temel bir view oluşturulur
- **Özellikler:**
  - `manage.py` ile proje çalıştırılır
  - `urls.py` ile endpoint tanımlanır
  - `views.py` içinde `HttpResponse` döndürülür
- **Kullanım:**
  ```bash
  cd ex05
  python3 manage.py runserver
  ```

Ardından tarayıcıda şu adrese gidilir:

```text
http://localhost:8000/helloworld/
```

## 🔧 Kullanım

### Python Kurulumu

```bash
# Ubuntu / Debian
sudo apt-get install python3

# macOS
brew install python3
```

### Sanal Ortam Oluşturma

```bash
python3 -m venv venv
source venv/bin/activate
```

### Gereksinimlerin Yüklenmesi

```bash
pip install -r ex02/requirements.txt
pip install -r ex03/requirements.txt
pip install -r ex04/requirements.txt
```

### Django Projesini Çalıştırma

```bash
cd ex05
python3 manage.py runserver
```

## 🎯 Öğrenilen Kavramlar

1. **Python Script Yapısı**: Komut satırı argümanları ve hata yönetimi
2. **Dosya ve Klasör Yönetimi**: `pathlib` ve dosya işlemleri
3. **HTTP İstekleri**: `requests` kullanımı ve API çağrıları
4. **HTML ve Veri Çıkarma**: Web içeriğinin ayrıştırılması
5. **Sanal Ortam Kurulumu**: `venv` ile proje bağımlılık yönetimi
6. **Django Proje Yapısı**: `settings`, `urls`, `views` kavramları
7. **Request / Response Mantığı**: Web isteklerinin işlenmesi
8. **Temel Web Geliştirme**: İlk Django uygulaması oluşturma

## 📋 Notlar

- Bu modül, Django öğrenmeye başlamak için hazırlanmış temel bir başlangıç setidir
- Her egzersiz, sonraki adımlarda daha karmaşık web geliştirme mantığını öğrenmek için bir ön hazırlıktır
- Proje boyunca Python, HTTP, veri işleme ve Django'nun temel çalışma yapısı anlaşılır
- Çalışmalar, temeli sağlamlaştırmak amacıyla küçük ve net örnekler üzerinden ilerler
