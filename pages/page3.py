import streamlit as st

page_bg = """
<style>
/* Background Page */
[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #FFE0F4, #FFB5E2);
    background-attachment: fixed;
}

/* Sidebar Background */
[data-testid="stSidebar"] {
    background: linear-gradient(135deg, #FFE0F4, #FFB5E2);
}

/* Default text putih */
p, label, h2, h4, h5, h6 {
    color: #ffffff !important;
}

/* Judul utama (h1) warna hitam */
h1 {
    color: #000000 !important;
}

/* Style khusus untuk tulisan Anggota Kelompok */
.anggota-title {
    color: #000000 !important;
    font-weight: bold;
}

/* Button styling */
div.stButton > button {
    background-color: #FFE0F4;
    color: black;
    border-radius: 8px;
}
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

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


st.image("data/bigdata.jpg", caption="ilustrasi", width=750)

