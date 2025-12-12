import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

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

# Cek apakah plotly tersedia
try:
    import plotly.express as px
    import plotly.graph_objects as go
    PLOTLY_AVAILABLE = True
except ImportError:
    PLOTLY_AVAILABLE = False
    st.warning("⚠️ Plotly tidak terinstall. Beberapa visualisasi tidak akan tersedia.")
    st.info("Install dengan: `pip install plotly`")

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
    #       BAR CHART INTERAKTIF (PLOTLY)
    # -----------------------------
    if PLOTLY_AVAILABLE:
        st.subheader("🔹 Bar Chart Interaktif")
        
        bar_x = st.selectbox("Pilih kolom X untuk Bar Chart:", df.columns, key="bar_x")
        bar_y = st.selectbox("Pilih kolom Y untuk Bar Chart:", df.columns, key="bar_y")
        
        fig_bar = px.bar(df, x=bar_x, y=bar_y, title="Bar Chart Interaktif", barmode="group")
        st.plotly_chart(fig_bar, use_container_width=True)
        
        # -----------------------------
        #       LINE CHART INTERAKTIF (PLOTLY)
        # -----------------------------
        st.subheader("🔹 Line Chart Interaktif")
        
        line_x = st.selectbox("Pilih kolom X untuk Line Chart:", df.columns, key="line_x")
        line_y = st.selectbox("Pilih kolom Y untuk Line Chart:", df.columns, key="line_y")
        
        fig_line = px.line(df, x=line_x, y=line_y, markers=True, title="Line Chart Interaktif")
        st.plotly_chart(fig_line, use_container_width=True)
        
        line_x_ml, line_y_ml = line_x, line_y  # Simpan untuk matplotlib
    else:
        # Tampilkan pilihan untuk matplotlib jika plotly tidak tersedia
        st.subheader("🔹 Visualisasi dengan Matplotlib")
        
        bar_x = st.selectbox("Pilih kolom X untuk Bar Chart:", df.columns, key="bar_x")
        bar_y = st.selectbox("Pilih kolom Y untuk Bar Chart:", df.columns, key="bar_y")
        
        # Bar Chart dengan Matplotlib
        fig_bar_ml, ax_bar = plt.subplots(figsize=(10, 4))
        df_sorted = df.sort_values(by=bar_x)
        ax_bar.bar(df_sorted[bar_x], df_sorted[bar_y])
        ax_bar.set_title(f"Bar Chart – {bar_x} vs {bar_y}")
        ax_bar.set_xlabel(bar_x)
        ax_bar.set_ylabel(bar_y)
        plt.xticks(rotation=45)
        st.pyplot(fig_bar_ml)
        
        line_x_ml = st.selectbox("Pilih kolom X untuk Line Chart:", df.columns, key="line_x")
        line_y_ml = st.selectbox("Pilih kolom Y untuk Line Chart:", df.columns, key="line_y")

    # -----------------------------
    #       LINE CHART MATPLOTLIB (SELALU TERSEDIA)
    # -----------------------------
    st.subheader("🔹 Line Chart (Matplotlib)")
    
    fig_line_ml, ax_line = plt.subplots(figsize=(10, 4))
    df_sorted_line = df.sort_values(by=line_x_ml)
    ax_line.plot(df_sorted_line[line_x_ml], df_sorted_line[line_y_ml], marker='o')
    ax_line.set_title(f"Line Chart – {line_x_ml} vs {line_y_ml}")
    ax_line.set_xlabel(line_x_ml)
    ax_line.set_ylabel(line_y_ml)
    plt.xticks(rotation=45)
    st.pyplot(fig_line_ml)

except FileNotFoundError:
    st.error(f"❌ File tidak ditemukan: {file_path}")
    st.info("Pastikan file CSV berada di folder 'data' dengan nama 'genz_money_spends.csv'")

except Exception as e:
    st.error(f"❌ Terjadi error: {e}")
