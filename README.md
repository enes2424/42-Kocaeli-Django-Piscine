# 42 Kocaeli Django Piscine
## Başlangıç - HTML, CSS ve JavaScript

Bu proje, 42 Okulu Django Piscine eğitiminin ilk modülüdür. Web geliştirmenin temel taşları olan HTML, CSS ve JavaScript'in temel kullanımını, form işleme, DOM manipülasyonu ve responsive tasarım becerilerini geliştirmek için tasarlanmıştır.

## 📚 Egzersizler

### ex00 - myawesomescript
**Dosya:** `ex00/myawesomescript.sh`

HTTP yönlendirmelerini takip eden ve son location header'ını döndüren bash scripti.
- **Açıklama:** Verilen URL'nin yönlendirme zincirindeki son konumunu bulur
- **Kullanım:** `./myawesomescript.sh <URL>`
- **Teknik:** curl, grep ve cut komutlarıyla HTTP header parsing
- **Örnek:**
  ```bash
  ./myawesomescript.sh "https://bit.ly/example"
  # Çıktı: https://www.example.com/final-url
  ```

### ex01 - CV (Özgeçmiş)
**Dosya:** `ex01/cv.html`

Semantik HTML5 elementleri kullanılarak oluşturulmuş profesyonel özgeçmiş sayfası.
- **HTML Elementleri:**
  - `<header>`, `<main>`, `<section>`, `<footer>` - Semantik yapı
  - `<table>` - Tablo yapısı ile bilgi gösterimi
  - `<ul>`, `<ol>` - Sıralı ve sırasız listeler
- **Özellikler:**
  - Gömülü CSS ile modern tasarım
  - Responsive layout
  - Tablo border stilleri
  - Section bazlı içerik organizasyonu
- **İçerik:** Kişisel bilgiler, yetenekler, deneyimler, eğitim bilgileri

### ex02 - Form
**Dosyalar:** `ex02/form.html`, `ex02/popup.js`

JavaScript ile form validasyonu ve veri işleme uygulaması.
- **HTML Form Elementleri:**
  - `<input type="text">` - Firstname, Name
  - `<input type="number">` - Age
  - `<input type="tel">` - Phone
  - `<input type="email">` - Email
  - `<input type="checkbox">` - Student status
  - `<input type="radio">` - Gender seçimi
- **JavaScript Fonksiyonları:**
  - `displayFormContents()` - Form verilerini toplama
  - Form validation (required alanlar)
  - Alert ile kullanıcıya geri bildirim
- **Özellikler:**
  - Client-side form validation
  - Event handling (onsubmit)
  - DOM element seçimi ve değer okuma

### ex03 - Copy (Progress Bars)
**Dosyalar:** `ex03/copy.html`, `ex03/style.css`, `ex03/page.png`

Animasyonlu progress bar'lar ile beceri gösterimi sayfası.
- **HTML Yapısı:**
  - `<progress>` elementleri ile skill bars
  - Frontend ve Backend kategorileri
  - Data attributes (`data-value`) kullanımı
- **CSS Özellikleri:**
  - Custom progress bar stillendirme
  - Google Fonts entegrasyonu
  - Cross-browser uyumlu progress bar tasarımı
  - Responsive layout
- **Teknolojiler:**
  - HTML5: 80%
  - CSS3: 60%
  - jQuery: 50%
  - Python: 75%
  - PHP: 65%
  - Node.js: 35%

### ex04 - Snippets (JavaScript Chain)
**Dosyalar:** `ex04/snippets.html`, `ex04/file1.js`, `ex04/file2.js`, `ex04/file3.js`, `ex04/file4.js`

JavaScript fonksiyon zinciri ve script loading sırası uygulaması.
- **Fonksiyon Zinciri:**
  1. `cat()` → `whale()` (file2.js)
  2. `whale()` → `unicorn()` (file3.js)
  3. `unicorn()` → `puffin()` (file1.js)
  4. `puffin()` → Alert mesajı (file4.js)
- **Konsept:**
  - Script loading sırası önemi
  - Fonksiyon scope ve hoisting
  - Call stack kavramı
  - Fonksiyon zinciri (function chaining)
- **Sonuç:** "Exercice réussi!" alert mesajı

### ex05 - Art Gallery Blog
**Dosyalar:** `ex05/index.html`, `ex05/style.css`, `ex05/normalize.css`, `ex05/audio_chain.js`

Responsive blog sayfası ve audio playlist yönetimi.
- **HTML Yapısı:**
  - Semantik HTML5 (header, nav, main, article, footer)
  - Blog post yapısı
  - Navigation menu
  - Multiple audio elements
- **CSS Özellikleri:**
  - Custom font entegrasyonu (BebasNeue, DroidSerif)
  - Normalize.css ile browser consistency
  - Modern blog layout
  - Responsive tasarım
- **JavaScript (jQuery):**
  - Audio playlist yönetimi
  - Sequential audio playback
  - Event binding ("ended" event)
  - DOM manipulation
- **Medya:**
  - Özel font dosyaları (.eot, .svg, .ttf, .woff)
  - Audio dosyaları (.ogg, .aiff)
  - Görseller (.jpg)

## 🔧 Kullanım

### Projeyi Çalıştırma

#### ex00 - Shell Script
```bash
cd ex00
chmod +x myawesomescript.sh
./myawesomescript.sh "https://example.com"
```

#### ex01-ex05 - HTML Sayfaları
```bash
# Basit HTTP sunucusu ile (Python 3)
python3 -m http.server 8000

# Tarayıcıda açın:
# ex01: http://localhost:8000/ex01/cv.html
# ex02: http://localhost:8000/ex02/form.html
# ex03: http://localhost:8000/ex03/copy.html
# ex04: http://localhost:8000/ex04/snippets.html
# ex05: http://localhost:8000/ex05/index.html
```

### Gereksinimler

- Modern web tarayıcı (Chrome, Firefox, Safari, Edge)
- ex05 için jQuery library (CDN veya local)
- Bash shell (ex00 için)
- curl komutu (ex00 için)

## 🎯 Öğrenilen Kavramlar

1. **HTML5 Semantik Elementler**: header, main, section, article, nav, footer
2. **Form İşleme**: Input types, validation, form submission
3. **CSS Styling**: Custom progress bars, font integration, responsive design
4. **JavaScript DOM**: Element selection, event handling, manipulation
5. **jQuery**: Event binding, sequential operations, AJAX hazırlık
6. **Audio API**: HTMLAudioElement, event listeners, playlist management
7. **Bash Scripting**: HTTP requests, text processing, pipeline
8. **Web Fonts**: @font-face, multiple format support
9. **Cross-browser Compatibility**: Normalize.css, vendor prefixes
10. **Project Structure**: File organization, asset management

## 📋 Notlar

- **ex00**: Tamamen orijinal bash script implementasyonu
- **ex01-ex05**: HTML dosyaları orijinal, CSS/JS/asset dosyaları 42 tarafından sağlanmıştır
- Tüm projeler modern web standartları (HTML5, CSS3, ES5+) ile uyumludur
- Responsive tasarım prensipleri göz önünde bulundurulmuştur
- ex05 özellikle medya dosyaları ve web font entegrasyonu için kapsamlı bir örnektir

## 🌐 Teknolojiler

- **Frontend**: HTML5, CSS3, JavaScript (ES5/ES6)
- **Libraries**: jQuery
- **Tools**: Bash, curl, grep, cut
- **Fonts**: Google Fonts, Custom Web Fonts
- **Audio**: HTML5 Audio API, OGG/AIFF formatları
