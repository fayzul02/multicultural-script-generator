from dotenv import load_dotenv
import streamlit as st
import utils
import os

load_dotenv()

# Konfigurasi Halaman
st.set_page_config(page_title="GlobalSpeak AI", layout="wide")

# --- SIDEBAR (Konfigurasi) ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/201/201616.png", width=50)
    st.title("Pengaturan")
    
    # Cek apakah ada di .env? Jika ada, pakai itu. Jika tidak, minta input manual.
    env_key = os.getenv("GOOGLE_API_KEY")
    
    if env_key:
        st.success("✅ API Key terdeteksi dari .env")
        api_key = env_key
    else:
        api_key = st.text_input("API MODEL", type="password")
    
    st.markdown("---")
    
    # Pilihan Budaya Target
    target_culture = st.selectbox(
        "Pilih Target Audiens:",
        ("Indonesia 🇮🇩", "Jepang 🇯🇵", "Amerika Serikat 🇺🇸", "Jerman 🇩🇪", "Arab Saudi 🇸🇦")
    )
    
    st.info("Tips: Pastikan file PPT berisi teks yang bisa dibaca, bukan full gambar.")

# --- MAIN CONTENT ---
st.title("🌏 GlobalSpeak: Cultural Presentation Script Generator")
st.markdown(f"""
    Ubah slide presentasi biasa menjadi naskah yang **sensitif budaya** untuk audiens **{target_culture}**.
""")

# 1. Upload File
uploaded_file = st.file_uploader("Upload File PowerPoint (.pptx)", type="pptx")

if uploaded_file is not None:
    st.success("File berhasil diupload! Sedang memproses...")
    
    # Panggil fungsi parsing dari utils.py
    slides_data = utils.extract_text_from_ppt(uploaded_file)
    
    st.subheader(f"Ditemukan {len(slides_data)} Slide")
    
    # Tombol Eksekusi
    if st.button("✨ Generate Script dengan Adaptasi Budaya"):
        if not api_key:
            st.error("Mohon masukkan API Key di sidebar terlebih dahulu.")
        else:
            # Progress Bar
            progress_bar = st.progress(0)
            
            # Container untuk hasil
            results_container = st.container()

            # Loop setiap slide dan generate script
            for i, slide in enumerate(slides_data):
                content = slide['content']
                
                # Update UI progress
                progress_bar.progress((i + 1) / len(slides_data))
                
                with results_container:
                    # Layout 2 kolom: Kiri (Konteks Asli), Kanan (Hasil AI)
                    col1, col2 = st.columns([1, 2])
                    
                    with col1:
                        st.info(f"**Slide {slide['slide_number']} (Original)**")
                        st.caption(content[:300] + "..." if len(content) > 300 else content) # Preview teks asli
                    
                    with col2:
                        st.markdown(f"### 🎙️ Script Adaptasi: {target_culture}")
                        
                        # Panggil AI (Spinner biar user tau sedang loading)
                        with st.spinner(f"Menulis naskah slide {slide['slide_number']}..."):
                            try:
                                # Panggil fungsi dari utils.py
                                script_result = utils.generate_cultural_script(content, target_culture, api_key)
                                st.markdown(script_result)

                                # --- Fitur Download ---
                                st.download_button(
                                    label="📥 Download Naskah (.txt)",
                                    data=script_result,
                                    file_name=f"Script_Presentasi_{target_culture}.txt",
                                    mime="text/plain"
                                )
                            except Exception as e:
                                st.error(f"Terjadi kesalahan: {e}")
                    
                    st.divider() # Garis pemisah antar slide

            st.balloons()
            st.success("Selesai! Semua slide telah diadaptasi.")