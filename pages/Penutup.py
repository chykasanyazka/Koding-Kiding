import streamlit as st

# ===============================
# CSS Styling - DIPERBAIKI
# ===============================
st.markdown("""
<style>
/* Reset padding dan margin untuk semua elemen */
.main .block-container {
    padding-top: 1rem;
    padding-bottom: 1rem;
    padding-left: 0.5rem !important;
    padding-right: 1rem;
    max-width: 95% !important;
}

/* Kontainer utama lebih ke kiri */
section.main {
    padding-left: 0 !important;
    margin-left: 0 !important;
}

/* Paragraf mulai dari paling kiri */
.kesimpulan-text {
    font-size: 16px;
    line-height: 1.6;
    text-align: left;
    margin-left: 0 !important;
    padding-left: 0 !important;
    text-indent: 0;
    width: 100%;
}

     b  
/* Force semua konten ke kiri */
div.stMarkdown {
    padding-left: 0 !important;
    margin-left: 0 !important;
}

/* Judul mulai dari kiri */
h1, h2, h3 {
    text-align: left !important;
    padding-left: 0 !important;
    margin-left: 0 !important;
}

/* Override default Streamlit styling */
[data-testid="stVerticalBlock"] {
    padding-left: 0 !important;
}
</style>
""", unsafe_allow_html=True)

# ===============================
# Content
# ===============================
# Judul dengan HTML untuk kontrol penuh
st.markdown("""
<h1 style='text-align: left; padding-left: 0; margin-left: 0;'>Kesimpulan</h1>
""", unsafe_allow_html=True)

# Paragraf pertama dengan container khusus
col1, col2 = st.columns([0.02, 0.98])  # Kolom pertama sangat kecil untuk padding
with col2:
    st.markdown("""
    <div class="kesimpulan-text">
    Analisis menunjukkan bahwa pengeluaran Gen Z paling banyak terserap di kategori makanan, 
    transportasi, hiburan, dan belanja online, dengan porsi lifestyle yang hampir menyamai 
    kebutuhan esensial. Temuan ini sejalan dengan fenomena nyata seperti self-reward, nongkrong 
    di coffee shop, skincare, hingga penggunaan paylater yang membuat transaksi impulsif makin 
    mudah. Secara keseluruhan, Gen Z mostly bukan sekadar hedon, tetapi lebih experience-oriented 
    mengutamakan kenyamanan, kebahagiaan kecil, dan efisiensi dalam keseharian. Namun, kemudahan 
    pembayaran digital membuat sebagian dari mereka rentan pada pengeluaran spontan dan kurangnya 
    kontrol finansial. Dengan demikian, pola belanja Gen Z mencerminkan gaya hidup digital modern, 
    bukan sekadar perilaku konsumtif tanpa alasan.
    </div>
    """, unsafe_allow_html=True)

# Spacer
st.markdown("<br>", unsafe_allow_html=True)

# Paragraf kedua
col3, col4 = st.columns([0.02, 0.98])
with col4:
    st.markdown("""
    <div class="kesimpulan-text">
    Analisis ini menunjukkan bahwa pola pengeluaran Gen Z bukan sekadar soal hedon, tetapi 
    dipengaruhi oleh gaya hidup digital, kemudahan pembayaran modern, dan tren sosial yang 
    membentuk preferensi belanja mereka. Dashboard ini memberikan gambaran objektif tentang 
    bagaimana Gen Z mengelola pendapatannya dan membantu memahami perilaku ekonomi generasi ini 
    secara lebih utuh. Jadi, kesimpulannya: uang boleh keluar, tapi insight harus masuk — stay 
    financially sane, guys, jangan sampai bulan panjang, saldo pendek!
    </div>
    """, unsafe_allow_html=True) 

    st.image("data/bigdata.jpg , width=750)