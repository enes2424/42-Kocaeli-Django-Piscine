# 42 Kocaeli Django Piscine
## Python Fundamentals (Python Temelleri)

Bu proje, 42 Okulu Django Piscine eğitiminin ikinci modülüdür. Python programlama dilinin temel veri türleri, dosya işleme, dictionary manipülasyonu, komut satırı argümanları ve HTML oluşturma becerilerini geliştirmek için tasarlanmıştır.

## 📚 Egzersizler

### ex00 - var
**Dosya:** `ex00/var.py`

Python'da temel veri türlerini tanıtan fonksiyon.
- **Fonksiyon:** `my_var()`
- **Açıklama:** Farklı veri türlerinde değişkenler oluşturur ve her birinin tipini yazdırır
- **Veri Türleri:** int, str, float, bool, list, dict, tuple, set
- **Çıktı:**
  ```
  42 has a type <class 'int'>
  42 has a type <class 'str'>
  quarante-deux has a type <class 'str'>
  42.0 has a type <class 'float'>
  True has a type <class 'bool'>
  [42] has a type <class 'list'>
  {42: 42} has a type <class 'dict'>
  (42,) has a type <class 'tuple'>
  set() has a type <class 'set'>
  ```

### ex01 - numbers
**Dosya:** `ex01/numbers.py` ve `ex01/numbers.txt`

Dosyadan sayıları okuyup işleyen fonksiyon.
- **Fonksiyon:** `print_numbers()`
- **Açıklama:** Text dosyasından virgülle ayrılmış değerleri okur ve sadece geçerli integer değerleri yazdırır
- **Özellik:** ValueError exception handling ile geçersiz değerleri filtreler
- **Örnek:**
  ```python
  # numbers.txt: "1,2,3,hello,4,5"
  # Çıktı: 1, 2, 3, 4, 5 (hello atlanır)
  ```

### ex02 - var_to_dict
**Dosya:** `ex02/var_to_dict.py`

Liste of tuple'ları dictionary'ye dönüştüren fonksiyon.
- **Fonksiyon:** `var_to_dict(var)`
- **Açıklama:** (value, key) formatındaki tuple listesini {key: value} dictionary'sine çevirir
- **Veri:** Ünlü gitaristler ve doğum yılları
- **Örnek:**
  ```python
  d = [("Hendrix", "1942"), ("Clapton", "1945")]
  # Çıktı: {"1942": "Hendrix", "1945": "Clapton"}
  ```

### ex03 - capital_city
**Dosya:** `ex03/capital_city.py`

Eyalet adından başkent bulan program.
- **Fonksiyon:** `printCapitalCity(state)`
- **Açıklama:** Komut satırından verilen eyalet adına göre başkenti yazdırır
- **Veri:** Oregon, Alabama, New Jersey, Colorado eyaletleri
- **Kullanım:**
  ```bash
  python capital_city.py "Oregon"     # Salem
  python capital_city.py "Texas"      # Unknown state
  ```

### ex04 - state
**Dosya:** `ex04/state.py`

Başkent adından eyalet bulan program.
- **Fonksiyon:** `printState(capital_city)`
- **Açıklama:** Komut satırından verilen başkent adına göre eyaleti yazdırır
- **Özellik:** Reverse lookup yaparak başkentten eyalet bulur
- **Kullanım:**
  ```bash
  python state.py "Salem"        # Oregon
  python state.py "Austin"       # Unknown capital city
  ```

### ex05 - all_in
**Dosya:** `ex05/all_in.py`

Çoklu arama ve sınıflandırma programı.
- **Fonksiyon:** `printStatus(elm)`
- **Açıklama:** Virgülle ayrılmış input'u işler, her elemanın eyalet mi başkent mi olduğunu belirler
- **Özellik:** Case-insensitive arama, whitespace handling
- **Kullanım:**
  ```bash
  python all_in.py "Oregon, Salem, Texas"
  # Salem is the capital city of Oregon
  # Salem is the capital city of Oregon  
  # Texas is neither a capital city nor a state
  ```

### ex06 - my_sort
**Dosya:** `ex06/my_sort.py`

Dictionary sıralama algoritması.
- **İşlev:** Müzisyenleri doğum yılına ve isme göre sıralar
- **Açıklama:** Lambda fonksiyonu kullanarak önce yıla, sonra isme göre sıralama
- **Algoritma:** `sorted()` fonksiyonu ile tuple key sorting
- **Çıktı:**
  ```
  Johnson (1911)
  King (1925)
  Berry (1926)
  ...
  White (1975)
  ```

### ex07 - periodic_table
**Dosya:** `ex07/periodic_table.py` ve `ex07/periodic_table.txt`

Periyodik tablo HTML oluşturucu.
- **İşlev:** Text dosyasından element verilerini okur ve HTML tablosu oluşturur
- **Açıklama:** Element pozisyonlarını hesaplayarak doğru HTML table yapısı oluşturur
- **Özellikler:**
  - Element bilgilerini parse etme
  - Electron konfigürasyonundan row hesaplama
  - HTML table generation
  - CSS styling
- **Çıktı:** `periodic_table.html` dosyası

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
# Doğrudan çalıştırma
python3 ex00/var.py

# Komut satırı argümanları ile
python3 ex03/capital_city.py "Oregon"

# Modül olarak çalıştırma
python3 -m ex01.numbers
```

### Gereksinimler
```bash
# Python 3.6+ gereklidir
python3 --version

# Standart library kullanıldığı için ek paket gerekmez
```

## 🎯 Öğrenilen Kavramlar

1. **Veri Türleri**: int, str, float, bool, list, dict, tuple, set
2. **Dosya İşleme**: File I/O, reading, writing, parsing
3. **Exception Handling**: try-except blokları, ValueError yakalama
4. **Dictionary Operations**: Key-value manipulation, reverse lookup
5. **Command Line Arguments**: sys.argv kullanımı
6. **String Processing**: split, strip, case conversion
7. **List Comprehension**: Generator expressions ve filtering
8. **HTML Generation**: Programatik HTML oluşturma
9. **Data Parsing**: Structured text parsing
10. **Sorting Algorithms**: Custom key functions ile sıralama

## 📋 Notlar

- Tüm kodlar Python 3.6+ uyumludur
- PEP 8 code style guidelines takip edilmiştir
- Exception handling best practices uygulanmıştır
- File operations güvenli şekilde (close) yapılmıştır
- Command line interface standartlarına uygun tasarlanmıştır
- HTML output valid ve semantic markup içerir
- Memory efficient algorithms kullanılmıştır
