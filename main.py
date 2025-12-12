import streamlit as st
import pandas as pd

# ================================
# 🎀 PINK GRADIENT BACKGROUND CSS
# ================================
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
# ================================


# ================================
# 📌 Sidebar Menu Navigation
# ================================
menu = st.sidebar.selectbox(
    "Menu",
    ["Home", "Visual Data", "Settings"]
)


# ================================
# 📌 HOME PAGE
# ================================
if menu == "Home":
    st.title("Analisis Pola Pengeluaran Gen Z: Memahami Money Behaviour Usia 18–27 Tahun")

    # Judul anggota kelompok (HTML agar bisa dikasih CSS custom)
    st.markdown("<h3 class='anggota-title'>Anggota Kelompok:</h3>", unsafe_allow_html=True)

    anggota = [
        "Danille Villareal (021002301006)",
        "Arnindya Zetira Diarra (021002301011)",
        "Chyka Sanyazka Nugraha (021002301008)",
        "Vina Nurlita Natiana (021002301008)"
    ]

    for nama in anggota:
        st.markdown(f"- {nama}")

    # Foto ilustrasi
    st.image("data/genz.jpg", caption="ilustrasi", width=1000)



# ================================
# 📌 VISUAL DATA PAGE
# ================================
elif menu == "Visual Data":
    st.title("📊 Visual Data")
    st.write("Silakan tambahkan visualisasi kamu di sini.")
    st.write("Belum ada grafik, tinggal kamu isi ✨")



# ================================
# 📌 SETTINGS PAGE
# ================================
elif menu == "Settings":
    st.title("⚙️ Settings")
    st.write("Pengaturan aplikasi masih kosong.")



# ================================
# 📌 FALLBACK
# ================================
else:
    st.title("Page Not Found")
    st.write("Select a valid option from the menu.")
