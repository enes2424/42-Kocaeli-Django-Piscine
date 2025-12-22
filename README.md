# 42 Kocaeli Django Piscine

## Sessions (Oturumlar)

Bu proje, 42 Okulu Django Piscine eğitiminin üçüncü modülüdür. Python'da nesne yönelimli programlama (OOP), sınıf tasarımı, kalıtım, HTML element oluşturma ve template rendering konularını kapsar.

## 📚 Egzersizler

### ex00 - Template Engine

**Dosyalar:** `ex00/render.py`, `ex00/settings.py`, `ex00/myCV.template`

Basit bir template rendering motoru.

- **Fonksiyon:** `render_template(template_file)`
- **Açıklama:** `.template` uzantılı dosyaları okur, içindeki değişkenleri `settings.py`'den alınan değerlerle değiştirir ve `.html` dosyası oluşturur
- **Özellikler:**
  - Regex ile `{variable}` formatındaki placeholder'ları bulur ve değiştirir
  - Dosya uzantısı kontrolü yapar
  - Hata yönetimi içerir
- **Kullanım:**
  ```bash
  python render.py myCV.template
  # myCV.html dosyası oluşturulur
  ```

### ex01 - Intern Class

**Dosya:** `ex01/intern.py`

Stajyer sınıfı ve iç içe sınıf (nested class) kullanımı.

- **Sınıf:** `Intern`
- **Açıklama:** Bir stajyeri temsil eden sınıf, varsayılan isim ile veya parametreli oluşturulabilir
- **Metodlar:**
  - `__init__(Name)`: Constructor, varsayılan isim parametresi
  - `__str__()`: Stajyerin ismini döndürür
  - `work()`: Exception fırlatır (stajyer çalışamaz)
  - `make_coffee()`: Coffee nesnesi döndürür
- **İç Sınıf:** `Coffee` - Kötü bir kahveyi temsil eder
- **Örnek:**
  ```python
  intern = Intern("Mark")
  print(intern)  # Mark
  coffee = intern.make_coffee()
  intern.work()  # Exception: I'm just an intern...
  ```

### ex02 - Hot Beverages

**Dosya:** `ex02/beverages.py`

Sıcak içecek sınıf hiyerarşisi ve kalıtım.

- **Ana Sınıf:** `HotBeverage` (Base class)
- **Alt Sınıflar:** `Coffee`, `Tea`, `Chocolate`, `Cappuccino`
- **Özellikler:**
  - Her içeceğin fiyatı (`price`)
  - Her içeceğin ismi (`name`)
  - Her içeceğin açıklaması (`description()`)
- **Metodlar:**
  - `__str__()`: İçeceğin formatlanmış bilgilerini döndürür
- **Fiyatlar:**
  - Hot Beverage: €0.30
  - Coffee: €0.40
  - Tea: €0.30
  - Chocolate: €0.50
  - Cappuccino: €0.45

### ex03 - Coffee Machine

**Dosya:** `ex03/machine.py`, `ex03/beverages.py`

Kahve makinesi simülasyonu ve exception handling.

- **Sınıf:** `CoffeeMachine`
- **Açıklama:** Sınırlı kullanım hakkı olan kahve makinesi simülasyonu
- **Özellikler:**
  - 10 kullanım hakkı ile başlar
  - Her kullanımda rastgele içecek veya boş bardak verir
  - Kullanım hakkı bittiğinde özel exception fırlatır
- **Metodlar:**
  - `serve(beverage)`: İstenen içeceği veya boş bardak döndürür
  - `repair()`: Makineyi tamir eder, kullanım hakkını 10'a sıfırlar
- **İç Sınıflar:**
  - `EmptyCup`: Boş bardak sınıfı
  - `BrokenMachineException`: Makine arızası exception'ı

### ex04 - HTML Elements (Base)

**Dosya:** `ex04/elem.py`, `ex04/tests.py`

HTML elementlerini temsil eden temel sınıf yapısı.

- **Sınıf:** `Elem`, `Text`
- **Açıklama:** HTML elementlerini Python objeleri olarak oluşturma sistemi
- **Özellikler:**
  - Tag ismi (`tag`)
  - Attribute'lar (`attr`)
  - İçerik (`content`)
  - Tag tipi: "double" veya "simple"
- **Metodlar:**
  - `__str__()`: HTML çıktısı üretir
  - `add_content()`: İçerik ekler, validasyon yapar
  - `check_type()`: İçerik tipini kontrol eder (static method)
- **Text Sınıfı:** HTML özel karakterlerini escape eder (`<`, `>`, `"`)

### ex05 - HTML Elements (Extended)

**Dosya:** `ex05/elem.py`, `ex05/elements.py`

Tüm standart HTML elementlerinin sınıf implementasyonları.

- **Sınıflar:** `Html`, `Head`, `Body`, `Title`, `Meta`, `Img`, `Table`, `Th`, `Tr`, `Td`, `Ul`, `Ol`, `Li`, `H1`, `H2`, `P`, `Div`, `Span`, `Hr`, `Br`
- **Açıklama:** Elem sınıfından türetilmiş özelleştirilmiş HTML element sınıfları
- **Özellikler:**
  - Her sınıf kendi HTML tag'ını temsil eder
  - Simple veya double tag tipinde olabilir
  - Meta ve Img gibi elementler self-closing
- **Kullanım:**
  ```python
  html = Html([
      Head(Title(Text("Page Title"))),
      Body([H1(Text("Hello")), P(Text("Content"))])
  ])
  ```

### ex06 - Page Validator

**Dosya:** `ex06/elem.py`, `ex06/elements.py`, `ex06/Page.py`

HTML sayfa yapısını validate eden sistem.

- **Sınıf:** `Page`
- **Açıklama:** HTML sayfa yapısının doğruluğunu kontrol eder ve dosyaya yazar
- **Validasyon Kuralları:**
  - Html elementi tam olarak 1 Head ve 1 Body içermeli
  - Head elementi tam olarak 1 Title içermeli
  - Body ve Div sadece belirli elementler içerebilir (H1, H2, Div, Table, Ul, Ol, Span, Text)
  - Title, H1, H2, Li, Th, Td elementleri sadece 1 Text içermeli
  - P elementi sadece Text içerebilir
  - Ul ve Ol elementleri sadece Li içerebilir
  - Tr elementi sadece Th veya sadece Td içerebilir
  - Table elementi sadece Tr içerebilir
- **Metodlar:**
  - `is_valid()`: HTML yapısını validate eder
  - `__str__()`: HTML çıktısı üretir (DOCTYPE ile)
  - `write_to_file(filename)`: Sayfayı dosyaya yazar

## 🔧 Kullanım

### Python Kurulumu

```bash
# Ubuntu/Debian
sudo apt-get install python3

# macOS (Homebrew)
brew install python3

# Windows
# Python.org'dan indirin
```

### Dosyaları Çalıştırma

```bash
# Template rendering
python ex00/render.py ex00/myCV.template

# Intern sınıfı test
python ex01/intern.py

# Beverages test
python ex02/beverages.py

# Coffee machine simülasyonu
python ex03/machine.py

# HTML elements test
python ex04/tests.py

# Page validator test
python ex06/Page.py
```

### Import Kullanımı

```python
# Elem sınıfını kullanma
from ex04.elem import Elem, Text

# HTML elementlerini kullanma
from ex05.elements import *

# Page sınıfını kullanma
from ex06.Page import Page
```

## 🎯 Öğrenilen Kavramlar

1. **Nesne Yönelimli Programlama**: Sınıf tasarımı, constructor'lar, metodlar
2. **Kalıtım (Inheritance)**: Base class ve derived class yapıları
3. **İç İçe Sınıflar (Nested Classes)**: Sınıf içinde sınıf tanımlama
4. **Exception Handling**: Özel exception sınıfları ve hata yönetimi
5. **Template Rendering**: String manipülasyonu ve regex kullanımı
6. **HTML Generation**: Programatik HTML oluşturma
7. **Validation Logic**: Karmaşık yapısal doğrulama algoritmaları
8. **Static Methods**: Sınıf seviyesinde utility metodlar

## 📋 Notlar

- Tüm sınıflar Python OOP prensipleri ile yazılmıştır
- Clean code ve SOLID prensipleri uygulanmıştır
- HTML çıktıları W3C standartlarına uygun indent edilmiştir
- Exception handling ile hata yönetimi sağlanmıştır
- Type hints ve docstring'ler ile kod belgelendirmesi yapılmıştır
