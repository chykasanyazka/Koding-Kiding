import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

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

.stSelectbox label {
    color: #4A4A4A !important;
}

</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)
# ===============================

st.title("📊 Visual Data – Penjualan per Produk")
st.markdown("---")

# Inisialisasi session state untuk menyimpan pilihan
if 'selected_x' not in st.session_state:
    st.session_state.selected_x = None
if 'selected_y' not in st.session_state:
    st.session_state.selected_y = None

file_path = "data/genz_money_spends.csv"

try:
    # Baca CSV
    df = pd.read_csv(file_path)
    st.success("✅ File CSV berhasil dibaca!")
    
    # Tampilkan info dataframe
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Jumlah Baris", len(df))
    with col2:
        st.metric("Jumlah Kolom", len(df.columns))
    with col3:
        st.metric("Kolom Tersedia", ", ".join(df.columns[:3]) + "...")
    
    # Tampilkan dataframe
    with st.expander("📋 Lihat Data Lengkap"):
        st.dataframe(df, use_container_width=True)
    
    st.markdown("---")
    st.header("📈 Visualisasi Interaktif")
    
    # -----------------------------
    #       BAR CHART
    # -----------------------------
    st.subheader("📊 Bar Chart")
    
    # Pilih kolom
    col1, col2 = st.columns(2)
    with col1:
        bar_x = st.selectbox(
            "Pilih kolom X untuk Bar Chart:",
            df.columns,
            key="bar_x",
            index=0 if len(df.columns) > 0 else 0
        )
        st.session_state.selected_x = bar_x
    
    with col2:
        bar_y = st.selectbox(
            "Pilih kolom Y untuk Bar Chart:",
            df.columns,
            key="bar_y",
            index=1 if len(df.columns) > 1 else 0
        )
        st.session_state.selected_y = bar_y
    
    # Buat Bar Chart
    if bar_x and bar_y:
        try:
            fig1, ax1 = plt.subplots(figsize=(12, 6))
            
            # Sort data jika kolom X adalah numerik
            if df[bar_x].dtype in ['int64', 'float64']:
                plot_data = df.sort_values(by=bar_x)
            else:
                plot_data = df
            
            # Batasi jumlah bar jika terlalu banyak
            if len(plot_data) > 20:
                plot_data = plot_data.head(20)
                st.info(f"Menampilkan 20 baris pertama dari {len(df)} total baris")
            
            # Buat bar chart
            bars = ax1.bar(
                plot_data[bar_x].astype(str), 
                plot_data[bar_y],
                color=plt.cm.Set3(np.arange(len(plot_data)))
            )
            
            ax1.set_title(f"📊 Bar Chart: {bar_x} vs {bar_y}", fontsize=16, fontweight='bold', pad=20)
            ax1.set_xlabel(bar_x, fontsize=12)
            ax1.set_ylabel(bar_y, fontsize=12)
            
            # Rotasi label x jika perlu
            if len(plot_data[bar_x].astype(str).iloc[0]) > 10 or len(plot_data) > 10:
                plt.xticks(rotation=45, ha='right')
            
            # Tambahkan nilai di atas bar
            for bar in bars:
                height = bar.get_height()
                ax1.text(bar.get_x() + bar.get_width()/2., height + 0.01,
                        f'{height:.1f}', ha='center', va='bottom', fontsize=8)
            
            plt.tight_layout()
            st.pyplot(fig1)
            
            # Statistik data
            with st.expander("📊 Statistik Data"):
                col_stats1, col_stats2, col_stats3 = st.columns(3)
                with col_stats1:
                    st.metric("Rata-rata", f"{df[bar_y].mean():.2f}")
                with col_stats2:
                    st.metric("Maksimum", f"{df[bar_y].max():.2f}")
                with col_stats3:
                    st.metric("Minimum", f"{df[bar_y].min():.2f}")
                    
        except Exception as e:
            st.error(f"❌ Error membuat Bar Chart: {e}")
            st.info("Pastikan kolom yang dipilih memiliki tipe data yang sesuai")
    
    st.markdown("---")
    
    # -----------------------------
    #       LINE CHART
    # -----------------------------
    st.subheader("📈 Line Chart")
    
    # Pilih kolom untuk line chart
    col3, col4 = st.columns(2)
    with col3:
        line_x = st.selectbox(
            "Pilih kolom X untuk Line Chart:",
            df.columns,
            key="line_x",
            index=0 if len(df.columns) > 0 else 0
        )
    
    with col4:
        line_y = st.selectbox(
            "Pilih kolom Y untuk Line Chart:",
            df.columns,
            key="line_y",
            index=1 if len(df.columns) > 1 else 0
        )
    
    # Buat Line Chart
    if line_x and line_y:
        try:
            fig2, ax2 = plt.subplots(figsize=(12, 6))
            
            # Sort data jika kolom X adalah numerik
            if df[line_x].dtype in ['int64', 'float64']:
                line_data = df.sort_values(by=line_x)
            else:
                line_data = df.sort_index()
            
            # Buat line chart
            ax2.plot(
                line_data[line_x].astype(str), 
                line_data[line_y],
                marker='o',
                linestyle='-',
                linewidth=2,
                markersize=6,
                color='#FF6B9D'
            )
            
            ax2.set_title(f"📈 Line Chart: {line_x} vs {line_y}", fontsize=16, fontweight='bold', pad=20)
            ax2.set_xlabel(line_x, fontsize=12)
            ax2.set_ylabel(line_y, fontsize=12)
            ax2.grid(True, alpha=0.3)
            
            # Rotasi label x jika perlu
            if len(line_data) > 10:
                plt.xticks(rotation=45, ha='right')
            
            plt.tight_layout()
            st.pyplot(fig2)
            
        except Exception as e:
            st.error(f"❌ Error membuat Line Chart: {e}")
    
    st.markdown("---")
    
    # -----------------------------
    #       SCATTER PLOT (Bonus)
    # -----------------------------
    st.subheader("🎯 Scatter Plot")
    
    col5, col6 = st.columns(2)
    with col5:
        scatter_x = st.selectbox(
            "Pilih kolom X untuk Scatter Plot:",
            df.columns,
            key="scatter_x",
            index=0 if len(df.columns) > 0 else 0
        )
    
    with col6:
        scatter_y = st.selectbox(
            "Pilih kolom Y untuk Scatter Plot:",
            df.columns,
            key="scatter_y",
            index=1 if len(df.columns) > 1 else 0
        )
    
    if scatter_x and scatter_y:
        try:
            fig3, ax3 = plt.subplots(figsize=(10, 6))
            
            # Buat scatter plot
            scatter = ax3.scatter(
                df[scatter_x],
                df[scatter_y],
                c=range(len(df)),
                cmap='viridis',
                alpha=0.7,
                s=100
            )
            
            ax3.set_title(f"🎯 Scatter Plot: {scatter_x} vs {scatter_y}", fontsize=16, fontweight='bold', pad=20)
            ax3.set_xlabel(scatter_x, fontsize=12)
            ax3.set_ylabel(scatter_y, fontsize=12)
            ax3.grid(True, alpha=0.3)
            
            # Tambahkan colorbar
            plt.colorbar(scatter, ax=ax3, label='Indeks Data')
            
            plt.tight_layout()
            st.pyplot(fig3)
            
        except Exception as e:
            st.error(f"❌ Error membuat Scatter Plot: {e}")
    
    # -----------------------------
    #       DATA SUMMARY
    # -----------------------------
    st.markdown("---")
    st.header("📋 Ringkasan Data")
    
    col_sum1, col_sum2 = st.columns(2)
    
    with col_sum1:
        st.subheader("Statistik Deskriptif")
        st.dataframe(df.describe())
    
    with col_sum2:
        st.subheader("Informasi Kolom")
        info_data = []
        for col in df.columns:
            info_data.append({
                "Kolom": col,
                "Tipe": str(df[col].dtype),
                "Nilai Unik": df[col].nunique(),
                "Kosong": df[col].isnull().sum()
            })
        st.dataframe(pd.DataFrame(info_data))

except FileNotFoundError:
    st.error(f"❌ File tidak ditemukan: {file_path}")
    st.info("""
    **Pastikan:**
    1. File berada di folder `data/`
    2. Nama file tepat: `genz_money_spends.csv`
    3. Struktur folder:
       ```
       your_project/
       ├── app.py
       └── data/
           └── genz_money_spends.csv
       ```
    """)
    
    # Contoh data dummy untuk testing
    if st.button("🔄 Gunakan Data Contoh untuk Testing"):
        st.info("Membuat data contoh...")
        import random
        example_data = {
            'Produk': [f'Produk {i}' for i in range(1, 11)],
            'Penjualan': [random.randint(100, 1000) for _ in range(10)],
            'Bulan': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct'],
            'Kategori': ['A', 'B', 'A', 'C', 'B', 'A', 'C', 'B', 'A', 'C']
        }
        df_example = pd.DataFrame(example_data)
        st.dataframe(df_example)
        
        # Simpan sebagai CSV sementara
        df_example.to_csv("data_example.csv", index=False)
        st.success("✅ Data contoh berhasil dibuat!")
        st.rerun()

except pd.errors.EmptyDataError:
    st.error("❌ File CSV kosong")
    
except Exception as e:
    st.error(f"❌ Terjadi error: {str(e)}")
    st.info("""
    **Tips troubleshooting:**
    1. Pastikan file CSV formatnya benar
    2. Cek apakah ada karakter khusus di data
    3. Pastikan semua library terinstall: `pip install streamlit pandas matplotlib numpy`
    """)

# -----------------------------
#       FOOTER
# -----------------------------
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666;'>
    <p>📊 Dibuat dengan Streamlit | Visualisasi Data Interaktif</p>
</div>
""", unsafe_allow_html=True)
