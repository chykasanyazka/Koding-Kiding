import streamlit as st
import pandas as pd
import plotly.express as px

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



st.title("📊 Visual Data – Penjualan per Produk")

file_path = "data/genz_money_spends.csv"

try:
    # Baca CSV
    df = pd.read_csv(file_path)
    st.success("File CSV berhasil dibaca!")

    # Tampilkan dataframe
    st.write("### Data:")
    st.dataframe(df)

    st.write("### Baris terakhir:")
    st.write(df.tail())

    st.markdown("---")
    st.header("📈 Visualisasi Interaktif")

    # -----------------------------
    #       BAR CHART INTERAKTIF
    # -----------------------------
    st.subheader("🔹 Bar Chart Interaktif")

    bar_x = st.selectbox("Pilih kolom X untuk Bar Chart:", df.columns, key="bar_x")
    bar_y = st.selectbox("Pilih kolom Y untuk Bar Chart:", df.columns, key="bar_y")

    fig_bar = px.bar(df, x=bar_x, y=bar_y, title="Bar Chart Interaktif", barmode="group")
    st.plotly_chart(fig_bar, use_container_width=True)

    # -----------------------------
    #       LINE CHART INTERAKTIF
    # -----------------------------
    st.subheader("🔹 Line Chart Interaktif")

    line_x = st.selectbox("Pilih kolom X untuk Line Chart:", df.columns, key="line_x")
    line_y = st.selectbox("Pilih kolom Y untuk Line Chart:", df.columns, key="line_y")

    fig_line = px.line(df, x=line_x, y=line_y, markers=True, title="Line Chart Interaktif")
    st.plotly_chart(fig_line, use_container_width=True)

    # -----------------------------
    #       LINE CHART MATPLOTLIB
    # -----------------------------
    st.subheader("🔹 Line Chart")

    plt.figure(figsize=(10, 4))
    plt.plot(df[line_x], df[line_y])
    plt.title(f"Line Chart – {line_x} vs {line_y}")
    plt.xlabel(line_x)
    plt.ylabel(line_y)
    st.pyplot(plt)

except FileNotFoundError:
    st.error(f"❌ File tidak ditemukan: {file_path}")
    st.info("Pastikan file CSV berada di folder 'data' dengan nama 'genz_money_spends.csv'")

except Exception as e:
    st.error(f"❌ Terjadi error: {e}")
