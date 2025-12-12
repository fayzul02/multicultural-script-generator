
# 🌏 Multicultural Presentation Script Generator

Aplikasi berbasis AI yang membantu profesional bisnis membuat **naskah presentasi yang sensitif secara budaya**.
Aplikasi ini mengubah slide PowerPoint standar menjadi naskah lisan yang disesuaikan dengan **etiket, gaya komunikasi, dan kebiasaan bahasa negara target** (misal: Jepang, Indonesia, Jerman).

---

## ✨ Fitur Utama

* **PPT Parsing**
  Mengekstrak teks secara otomatis dari file **.pptx** menggunakan `python-pptx`.
* **Cultural Adaptation**
  AI menyisipkan idiom, sapaan, formalitas, serta gaya komunikasi sesuai budaya negara tujuan.
* **AI Engine (LLM)**
  Ditenagai oleh **Google Gemini (gemini-2.5-flash)** untuk hasil cepat dan kontekstual.
* **Streamlit UI**
  Antarmuka web sederhana, interaktif, dan mudah digunakan.
* **LangChain Integration**
  Menggunakan LCEL untuk mengorkestrasi prompt dan pemanggilan model.

---

## 🛠️ Tech Stack

* **Bahasa**: Python
* **Framework UI**: Streamlit
* **LLM Orchestration**: LangChain (LCEL)
* **Model AI**: Google Gemini Pro / Flash
* **Tools**: python-pptx (PPT parsing)

---

## 🚀 Cara Menjalankan di Lokal

Ikuti langkah-langkah berikut untuk menjalankan proyek ini di lingkungan lokal Anda.

### 1. Clone Repository

```bash
git clone https://github.com/fayzul02/multicultural-script-generator.git
cd multicultural-script-generator
```

### 2. Buat Virtual Environment (Opsional, tetapi disarankan)

```bash
python -m venv venv
```

**Aktifkan venv:**

Windows:

```bash
venv\Scripts\activate
```

Mac/Linux:

```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Konfigurasi API Key

Buat file baru bernama **.env** di folder root proyek.

Isi dengan:

```
GOOGLE_API_KEY=masukkan_api_key_anda
```

Dapatkan API Key di **Google AI Studio**.

### 5. Jalankan Aplikasi

```bash
streamlit run app.py
```

Aplikasi akan terbuka otomatis di browser:
[http://localhost:8501](http://localhost:8501)

---

## 📂 Struktur Project

```
├── app.py           # Main Streamlit UI
├── utils.py         # AI logic & PPT parsing
├── requirements.txt # Dependencies
├── .env             # API Key config (excluded from GitHub)
└── README.md        # Dokumentasi
```