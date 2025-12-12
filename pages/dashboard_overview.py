import streamlit as st

# ===============================
# 🌸 PINK GRADIENT SOFT BACKGROUND
# ===============================
page_bg = """
<style>
[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #FFE0F4, #FFFFFF);
    background-attachment: fixed;
}

[data-testid="stSidebar"] {
    background: #FFE0F4;
}

h1, h2, h3, h4, h5, h6, p, label {
    color: #4A4A4A !important;
}

div.stButton > button {
    background-color: #FFE0F4;
    color: black;
    border-radius: 8px;
    border: 1px solid #FFB5E2;
}

</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)
# ===============================



st.title("Analisis Pola Pengeluaran Gen Z: Memahami Money Behaviour Usia 18–27 Tahun")
st.divider()

# Deskripsi dengan container yang lebih baik
with st.container():
    st.header("Deskripsi Singkat Penelitian")
    st.markdown("""
    Penelitian ini bertujuan untuk memahami bagaimana Gen Z (usia 18–27 tahun) *membagi pengeluaran bulanannya* 
    untuk kebutuhan sehari-hari dan gaya hidup di era digital. 
    
    Dengan memvisualisasikan data secara interaktif, dashboard ini membantu menjelaskan apakah perilaku belanja 
    Gen Z benar-benar *"hedon"*, atau justru mengikuti pola konsumsi modern yang wajar di tengah maraknya 
    layanan digital, cashless, dan tren self-reward.
    """)

st.divider()

# Kartu Statistik
st.header("Kartu Statistik Utama")

col1, col2, col3 = st.columns(3)

with col1:
    with st.container(border=True, height=200):
        st.subheader("Rata-rata Total Pengeluaran Gen Z")
        st.markdown("""
        *Menampilkan rata-rata nominal yang dikeluarkan per individu per bulan.*
        
        Contoh: Rp 2.500.000/bulan
        """)

with col2:
    with st.container(border=True, height=200):
        st.subheader("Kategori Pengeluaran Terbesar")
        st.markdown("""
        *Menggambarkan pos belanja mana yang paling menyerap budget.*
        
        Contoh: Makanan, Transportasi, Hiburan
        """)

with col3:
    with st.container(border=True, height=200):
        st.subheader("Proporsi Essential vs Lifestyle")
        st.markdown("""
        *Menunjukkan apakah Gen Z lebih banyak membelanjakan uangnya untuk kebutuhan atau gaya hidup.*
        
        Contoh: 65% Essential, 35% Lifestyle
        """)

st.divider()

with st.container():
    st.markdown("### 💡 Catatan Ringan")
    st.info("""
    **"Dashboard ini membantu kita melihat apakah Gen Z benar-benar hedon, 
    atau sekadar hidup di era yang serba digital. Don't judge—just analyze! 😊"**
    """)

# Spasi footer
for _ in range(2):
    st.write("")

