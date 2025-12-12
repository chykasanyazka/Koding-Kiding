# app.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

# ===============================
# 🌸 PINK GRADIENT SOFT BACKGROUND
# ===============================
st.set_page_config(page_title="Visual Data Dashboard", layout="wide")

page_bg = """
<style>
[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #FFE0F4, #FFFFFF);
    background-attachment: fixed;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

[data-testid="stSidebar"] {
    background: rgba(255, 224, 244, 0.9);
    backdrop-filter: blur(10px);
}

h1, h2, h3, h4, h5, h6 {
    color: #4A4A4A !important;
    font-weight: 600 !important;
}

p, label, div {
    color: #4A4A4A !important;
}

.stSelectbox label, .stSlider label {
    font-weight: 500 !important;
    color: #4A4A4A !important;
}

div.stButton > button {
    background: linear-gradient(45deg, #FFB5E2, #FFE0F4);
    color: #4A4A4A;
    border-radius: 12px;
    border: 2px solid #FF9AD6;
    padding: 10px 24px;
    font-weight: 600;
    transition: all 0.3s ease;
}

div.stButton > button:hover {
    background: linear-gradient(45deg, #FF9AD6, #FFB5E2);
    transform: translateY(-2px);
    box-shadow: 0 5px 15px rgba(255, 154, 214, 0.3);
}

.metric-card {
    background: white;
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.05);
    border: 1px solid #FFE0F4;
}

</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

# ===============================
# 🏆 HEADER
# ===============================
col_header1, col_header2, col_header3 = st.columns([1, 2, 1])
with col_header2:
    st.markdown("<h1 style='text-align: center;'>📊 DASHBOARD VISUALISASI DATA</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #666;'>Analisis Data Interaktif dengan Visualisasi yang Menarik</p>", unsafe_allow_html=True)

st.markdown("---")

# ===============================
# 📁 UPLOAD FILE
# ===============================
st.sidebar.header("📂 Upload Data")
uploaded_file = st.sidebar.file_uploader("Upload file CSV Anda", type=['csv'])

# File path default
default_file = "data/genz_money_spends.csv"

# Pilih sumber data
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.sidebar.success(f"✅ File {uploaded_file.name} berhasil diupload!")
    data_source = "Upload"
else:
    # Coba baca dari file default
    try:
        if os.path.exists(default_file):
            df = pd.read_csv(default_file)
            data_source = "File Default"
            st.sidebar.info(f"📁 Menggunakan file default: {default_file}")
        else:
            # Buat data contoh
            st.sidebar.warning("⚠️ File default tidak ditemukan, menggunakan data contoh")
            data_source = "Contoh"
            
            # Buat data contoh yang lebih menarik
            np.random.seed(42)
            categories = ['Makanan', 'Fashion', 'Elektronik', 'Hiburan', 'Transportasi', 'Pendidikan']
            months = ['Jan', 'Feb', 'Mar', 'Apr', 'Mei', 'Jun', 'Jul', 'Agt', 'Sep', 'Okt', 'Nov', 'Des']
            
            data = {
                'Bulan': np.tile(months, 2),
                'Kategori': np.repeat(categories[:4], 6),
                'Penjualan': np.random.randint(1000, 10000, 24),
                'Profit': np.random.randint(200, 2000, 24),
                'Customer': np.random.randint(50, 500, 24),
                'Rating': np.round(np.random.uniform(3.0, 5.0, 24), 1)
            }
            df = pd.DataFrame(data)
    except Exception as e:
        st.error(f"Error membaca data: {e}")
        st.stop()

# ===============================
# 📊 INFO DATA
# ===============================
st.header("📋 Informasi Data")
col_info1, col_info2, col_info3, col_info4 = st.columns(4)

with col_info1:
    st.markdown('<div class="metric-card">', unsafe_allow_html=True)
    st.metric("Jumlah Data", f"{len(df):,}")
    st.markdown('</div>', unsafe_allow_html=True)

with col_info2:
    st.markdown('<div class="metric-card">', unsafe_allow_html=True)
    st.metric("Jumlah Kolom", len(df.columns))
    st.markdown('</div>', unsafe_allow_html=True)

with col_info3:
    st.markdown('<div class="metric-card">', unsafe_allow_html=True)
    missing_values = df.isnull().sum().sum()
    st.metric("Data Kosong", missing_values)
    st.markdown('</div>', unsafe_allow_html=True)

with col_info4:
    st.markdown('<div class="metric-card">', unsafe_allow_html=True)
    st.metric("Sumber Data", data_source)
    st.markdown('</div>', unsafe_allow_html=True)

# Tampilkan data
with st.expander("👁️ Lihat Data Lengkap", expanded=False):
    st.dataframe(df, use_container_width=True)
    
    col_dl1, col_dl2, col_dl3 = st.columns(3)
    with col_dl1:
        st.write("**5 Data Teratas:**")
        st.dataframe(df.head(), use_container_width=True)
    with col_dl2:
        st.write("**5 Data Terbawah:**")
        st.dataframe(df.tail(), use_container_width=True)
    with col_dl3:
        st.write("**Statistik Deskriptif:**")
        st.dataframe(df.describe(), use_container_width=True)

st.markdown("---")

# ===============================
# 📈 VISUALISASI DATA
# ===============================
st.header("📈 Visualisasi Interaktif")

# Sidebar untuk pengaturan
st.sidebar.header("⚙️ Pengaturan Visualisasi")
chart_type = st.sidebar.selectbox(
    "Pilih Jenis Chart:",
    ["Bar Chart", "Line Chart", "Scatter Plot", "Pie Chart", "Area Chart"],
    index=0
)

# Pilih kolom
col1, col2 = st.columns(2)
with col1:
    x_col = st.selectbox(
        "Pilih Kolom X (Horizontal):",
        df.columns,
        key="x_col",
        index=0 if len(df.columns) > 0 else 0
    )

with col2:
    y_options = [col for col in df.columns if col != x_col]
    y_col = st.selectbox(
        "Pilih Kolom Y (Vertical):",
        df.columns,
        key="y_col",
        index=1 if len(df.columns) > 1 else 0
    )

# Tambahan pengaturan
st.sidebar.subheader("🎨 Customisasi")
color_palette = st.sidebar.selectbox(
    "Pilih Warna:",
    ["Pastel", "Vibrant", "Cool", "Warm", "Rainbow"],
    index=0
)

show_grid = st.sidebar.checkbox("Tampilkan Grid", value=True)
show_values = st.sidebar.checkbox("Tampilkan Nilai", value=True)

# Pilih warna berdasarkan palette
if color_palette == "Pastel":
    colors = ['#FFB5E2', '#A0E7E5', '#B5DEFF', '#FBE7C6', '#D9E7FF']
elif color_palette == "Vibrant":
    colors = ['#FF6B6B', '#4ECDC4', '#FFD166', '#06D6A0', '#118AB2']
elif color_palette == "Cool":
    colors = ['#3A86FF', '#8338EC', '#FB5607', '#FF006E', '#00BBF9']
elif color_palette == "Warm":
    colors = ['#FF9A76', '#FFC896', '#FFEBA1', '#C5E3BF', '#8AC6D1']
else:  # Rainbow
    colors = ['#FF595E', '#FFCA3A', '#8AC926', '#1982C4', '#6A4C93']

# ===============================
# BUAT VISUALISASI
# ===============================
fig, ax = plt.subplots(figsize=(14, 7))

try:
    # Sort data untuk line/area chart
    if chart_type in ["Line Chart", "Area Chart"] and df[x_col].dtype in [np.int64, np.float64]:
        plot_df = df.sort_values(by=x_col)
    else:
        plot_df = df
    
    # Batasi data untuk performa
    if len(plot_df) > 50:
        plot_df = plot_df.head(50)
        st.info(f"⚠️ Menampilkan 50 data pertama dari {len(df)} total data untuk performa")
    
    x_values = plot_df[x_col].astype(str) if plot_df[x_col].dtype == 'object' else plot_df[x_col]
    y_values = plot_df[y_col]
    
    # Buat chart berdasarkan pilihan
    if chart_type == "Bar Chart":
        bars = ax.bar(x_values, y_values, color=colors, edgecolor='white', linewidth=2)
        ax.set_title(f'📊 Bar Chart: {x_col} vs {y_col}', fontsize=18, fontweight='bold', pad=20)
        
        # Tambahkan nilai di atas bar
        if show_values:
            for bar in bars:
                height = bar.get_height()
                ax.text(bar.get_x() + bar.get_width()/2., height + 0.01,
                       f'{height:,.0f}', ha='center', va='bottom', fontsize=9, fontweight='bold')
    
    elif chart_type == "Line Chart":
        ax.plot(x_values, y_values, marker='o', linewidth=3, markersize=8, 
                color=colors[0], markeredgecolor='white', markeredgewidth=2)
        ax.set_title(f'📈 Line Chart: {x_col} vs {y_col}', fontsize=18, fontweight='bold', pad=20)
        
        # Tambahkan titik data
        if show_values:
            for i, (x, y) in enumerate(zip(x_values, y_values)):
                ax.text(x, y + (max(y_values)*0.02), f'{y:,.0f}', 
                       ha='center', va='bottom', fontsize=9, fontweight='bold')
    
    elif chart_type == "Scatter Plot":
        scatter = ax.scatter(x_values, y_values, s=150, c=range(len(x_values)), 
                            cmap='viridis', alpha=0.7, edgecolors='white', linewidth=2)
        ax.set_title(f'🎯 Scatter Plot: {x_col} vs {y_col}', fontsize=18, fontweight='bold', pad=20)
        
        # Tambahkan colorbar
        plt.colorbar(scatter, ax=ax, label='Indeks Data')
    
    elif chart_type == "Pie Chart":
        # Untuk pie chart, ambil top 10 saja
        if len(plot_df) > 10:
            top_data = plot_df.sort_values(by=y_col, ascending=False).head(10)
            x_values = top_data[x_col].astype(str)
            y_values = top_data[y_col]
            st.info("Menampilkan 10 data teratas untuk Pie Chart")
        
        wedges, texts, autotexts = ax.pie(y_values, labels=x_values, autopct='%1.1f%%',
                                         colors=colors, startangle=90, 
                                         wedgeprops={'edgecolor': 'white', 'linewidth': 2})
        ax.set_title(f'🥧 Pie Chart: Distribusi {y_col} berdasarkan {x_col}', 
                    fontsize=18, fontweight='bold', pad=20)
        
        # Style teks
        for text in texts:
            text.set_fontsize(11)
            text.set_fontweight('bold')
        for autotext in autotexts:
            autotext.set_color('white')
            autotext.set_fontweight('bold')
    
    elif chart_type == "Area Chart":
        ax.fill_between(x_values, y_values, alpha=0.4, color=colors[0])
        ax.plot(x_values, y_values, linewidth=3, color=colors[0])
        ax.set_title(f'🌊 Area Chart: {x_col} vs {y_col}', fontsize=18, fontweight='bold', pad=20)
    
    # Styling umum
    ax.set_xlabel(x_col, fontsize=14, fontweight='bold')
    ax.set_ylabel(y_col, fontsize=14, fontweight='bold')
    
    if show_grid:
        ax.grid(True, alpha=0.3, linestyle='--')
    
    # Rotasi label x jika panjang
    if len(x_values) > 5 or any(len(str(x)) > 10 for x in x_values):
        plt.xticks(rotation=45, ha='right', fontsize=10)
    else:
        plt.xticks(fontsize=11)
    
    plt.yticks(fontsize=11)
    plt.tight_layout()
    
    # Tampilkan chart
    st.pyplot(fig)
    
    # Statistik tambahan
    st.subheader("📊 Statistik Data Terpilih")
    col_stat1, col_stat2, col_stat3, col_stat4 = st.columns(4)
    
    with col_stat1:
        st.metric("Rata-rata", f"{df[y_col].mean():,.2f}")
    with col_stat2:
        st.metric("Total", f"{df[y_col].sum():,.2f}")
    with col_stat3:
        st.metric("Maksimum", f"{df[y_col].max():,.2f}")
    with col_stat4:
        st.metric("Minimum", f"{df[y_col].min():,.2f}")

except Exception as e:
    st.error(f"❌ Error membuat visualisasi: {str(e)}")
    st.info("⚠️ Pastikan kolom yang dipilih memiliki tipe data yang sesuai untuk chart ini")

# ===============================
# 🎯 MULTI-CHART VIEW
# ===============================
st.markdown("---")
st.header("🔍 Multi-Chart Comparison")

# Pilih hingga 3 chart untuk dibandingkan
selected_charts = st.multiselect(
    "Pilih chart untuk ditampilkan bersama:",
    ["Bar Chart", "Line Chart", "Scatter Plot"],
    default=["Bar Chart", "Line Chart"],
    max_selections=3
)

if selected_charts:
    cols = st.columns(len(selected_charts))
    
    for idx, chart in enumerate(selected_charts):
        with cols[idx]:
            st.subheader(chart)
            fig_small, ax_small = plt.subplots(figsize=(6, 4))
            
            try:
                if chart == "Bar Chart":
                    ax_small.bar(plot_df[x_col].astype(str)[:15], plot_df[y_col][:15], 
                                color=colors[idx % len(colors)])
                elif chart == "Line Chart":
                    ax_small.plot(plot_df[x_col].astype(str)[:15], plot_df[y_col][:15], 
                                 marker='o', color=colors[idx % len(colors)])
                elif chart == "Scatter Plot":
                    ax_small.scatter(plot_df[x_col].astype(str)[:15], plot_df[y_col][:15],
                                    color=colors[idx % len(colors)], s=50)
                
                ax_small.set_title(chart, fontsize=12)
                ax_small.tick_params(axis='x', rotation=45)
                ax_small.grid(True, alpha=0.3)
                plt.tight_layout()
                st.pyplot(fig_small)
                
            except:
                st.warning(f"Tidak bisa menampilkan {chart}")

# ===============================
# 📥 DOWNLOAD DATA
# ===============================
st.markdown("---")
st.header("📥 Export Data")

col_exp1, col_exp2, col_exp3 = st.columns(3)

with col_exp1:
    if st.button("💾 Download Data as CSV", use_container_width=True):
        csv = df.to_csv(index=False)
        st.download_button(
            label="Klik untuk Download CSV",
            data=csv,
            file_name="data_export.csv",
            mime="text/csv",
            use_container_width=True
        )

with col_exp2:
    if st.button("🖼️ Download Chart", use_container_width=True):
        # Save chart
        fig.savefig("chart_export.png", dpi=300, bbox_inches='tight')
        with open("chart_export.png", "rb") as file:
            btn = st.download_button(
                label="Klik untuk Download PNG",
                data=file,
                file_name="chart_export.png",
                mime="image/png",
                use_container_width=True
            )

with col_exp3:
    if st.button("🔄 Reset Pilihan", use_container_width=True):
        st.rerun()

# ===============================
# 📱 FOOTER
# ===============================
st.markdown("---")
st.markdown("""
<div style='text-align: center; padding: 20px; color: #666;'>
    <p style='font-size: 14px;'>📊 <strong>Dashboard Visualisasi Data Interaktif</strong> | Dibuat dengan Streamlit</p>
    <p style='font-size: 12px; margin-top: 5px;'>✨ Tips: Upload file CSV Anda sendiri untuk analisis data yang lebih personal!</p>
</div>
""", unsafe_allow_html=True)
