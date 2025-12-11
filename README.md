# 🌏 Multicultural Presentation Script Generator

Aplikasi berbasis AI yang membantu profesional bisnis membuat naskah presentasi yang sensitif secara budaya. Aplikasi ini mengubah slide PowerPoint standar menjadi naskah lisan yang disesuaikan dengan etiket dan gaya komunikasi negara target (misal: Jepang, Indonesia, Jerman).

## ✨ Fitur Utama
- **PPT Parsing**: Otomatis mengekstrak teks dari file PowerPoint (.pptx).
- **Cultural Adaptation**: Menggunakan AI untuk menyisipkan idiom, sapaan, dan gaya bahasa yang sesuai dengan budaya negara tujuan.
- **AI Engine**: Ditenagai oleh **Google Gemini (gemini-2.5-flash)** untuk kecepatan dan akurasi konteks.
- **Streamlit UI**: Antarmuka web yang sederhana dan interaktif.

## 🛠️ Tech Stack
- **Bahasa**: Python
- **Framework UI**: Streamlit
- **LLM Orchestration**: LangChain (LCEL)
- **Model AI**: Google Gemini Pro / Flash
- **Tools**: python-pptx (untuk membaca file slide)

## 🚀 Cara Menjalankan di Lokal (Installation)

Ikuti langkah ini untuk menjalankan proyek di komputer Anda:

### 1. Clone Repository
```bash
git clone [https://github.com/USERNAME_ANDA/nama-repo-anda.git](https://github.com/USERNAME_ANDA/nama-repo-anda.git)
cd nama-repo-anda
2. Buat Virtual Environment (Opsional tapi Disarankan)
Bash

python -m venv venv
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate
3. Install Dependencies
Bash

pip install -r requirements.txt
4. Konfigurasi API Key
Buat file baru bernama .env di dalam folder root proyek. Copy & Paste API Key Google Gemini Anda di sana:

Cuplikan kode

GOOGLE_API_KEY=masukkan_api_key_anda_disini
(Dapatkan API Key gratis di Google AI Studio)

5. Jalankan Aplikasi
Bash

streamlit run app.py
Aplikasi akan otomatis terbuka di browser Anda pada alamat http://localhost:8501.

📂 Struktur Project
├── app.py           # File utama (UI Streamlit)
├── utils.py         # Logika AI & PPT Parsing
├── requirements.txt # Daftar library yang dibutuhkan
├── .env             # File konfigurasi API Key (Tidak di-upload ke GitHub)
└── README.md        # Dokumentasi