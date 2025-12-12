import streamlit as st
import pandas as pd
import plotly.express as px
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

/* Clear matplotlib cache */
div.stPlotlyChart, div.stPyplot {
    clear: both;
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

    # Filter kolom numerik untuk bar chart
    numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
    categorical_cols = df.select_dtypes(exclude=[np.number]).columns.tolist()

    if not categorical_cols:
        categorical_cols = df.columns.tolist()[:1]
    if not numeric_cols:
        numeric_cols = df.columns.tolist()[-1:]

    bar_x = st.selectbox("Pilih kolom X untuk Bar Chart:", 
                        categorical_cols, 
                        key="bar_x",
                        index=min(0, len(categorical_cols)-1))
    
    bar_y = st.selectbox("Pilih kolom Y untuk Bar Chart:", 
                        numeric_cols, 
                        key="bar_y",
                        index=min(0, len(numeric_cols)-1))

    # Validasi data
    if bar_x in df.columns and bar_y in df.columns:
        # Bersihkan data NaN
        df_clean = df[[bar_x, bar_y]].dropna()
        
        if len(df_clean) > 0:
            fig_bar = px.bar(
                df_clean, 
                x=bar_x, 
                y=bar_y, 
                title=f"Bar Chart: {bar_x} vs {bar_y}",
                barmode="group",
                color_discrete_sequence=['#FF6B9D']
            )
            fig_bar.update_layout(
                plot_bgcolor='rgba(255, 224, 244, 0.3)',
                paper_bgcolor='rgba(255, 255, 255, 0.1)'
            )
            st.plotly_chart(fig_bar, use_container_width=True, config={'displayModeBar': True})
        else:
            st.warning("⚠️ Tidak ada data yang valid untuk ditampilkan.")
    else:
        st.warning("⚠️ Kolom tidak ditemukan.")

    # -----------------------------
    #       LINE CHART INTERAKTIF
    # -----------------------------
    st.subheader("🔹 Line Chart Interaktif")

    line_x = st.selectbox("Pilih kolom X untuk Line Chart:", 
                         df.columns, 
                         key="line_x",
                         index=min(1, len(df.columns)-1))
    
    line_y = st.selectbox("Pilih kolom Y untuk Line Chart:", 
                         numeric_cols, 
                         key="line_y",
                         index=min(0, len(numeric_cols)-1))

    if line_x in df.columns and line_y in df.columns:
        df_line_clean = df[[line_x, line_y]].dropna()
        
        if len(df_line_clean) > 0:
            # Coba konversi ke datetime jika kolom X adalah tanggal
            try:
                if df_line_clean[line_x].dtype == 'object':
                    df_line_clean[line_x] = pd.to_datetime(df_line_clean[line_x], errors='coerce')
                    df_line_clean = df_line_clean.dropna(subset=[line_x])
                    df_line_clean = df_line_clean.sort_values(by=line_x)
            except:
                pass

            fig_line = px.line(
                df_line_clean, 
                x=line_x, 
                y=line_y, 
                markers=True, 
                title=f"Line Chart: {line_x} vs {line_y}",
                line_shape='linear'
            )
            fig_line.update_traces(line_color='#FF6B9D', line_width=2)
            fig_line.update_layout(
                plot_bgcolor='rgba(255, 224, 244, 0.3)',
                paper_bgcolor='rgba(255, 255, 255, 0.1)'
            )
            st.plotly_chart(fig_line, use_container_width=True, config={'displayModeBar': True})
        else:
            st.warning("⚠️ Tidak ada data yang valid untuk line chart.")
    else:
        st.warning("⚠️ Kolom tidak ditemukan.")

    # -----------------------------
    #       LINE CHART MATPLOTLIB (OPTIONAL)
    # -----------------------------
    st.subheader("🔹 Line Chart (Matplotlib)")

    if 'line_x' in locals() and 'line_y' in locals():
        if line_x in df.columns and line_y in df.columns:
            # Gunakan data yang sudah dibersihkan
            plt_data = df[[line_x, line_y]].dropna()
            
            if len(plt_data) > 0:
                fig, ax = plt.subplots(figsize=(10, 4))
                
                # Coba sorting jika data numerik atau datetime
                try:
                    plt_data = plt_data.sort_values(by=line_x)
                except:
                    pass
                
                ax.plot(plt_data[line_x], plt_data[line_y], color='#FF6B9D', linewidth=2, marker='o')
                ax.set_title(f"Line Chart – {line_x} vs {line_y}")
                ax.set_xlabel(line_x)
                ax.set_ylabel(line_y)
                ax.grid(True, alpha=0.3)
                ax.set_facecolor('#FFF0F8')
                fig.patch.set_facecolor('#FFF0F8')
                
                # Rotasi label x jika terlalu panjang
                if plt_data[line_x].dtype == 'object' and len(plt_data[line_x].iloc[0]) > 10:
                    plt.xticks(rotation=45, ha='right')
                
                st.pyplot(fig)
                plt.close(fig)  # Tutup figure untuk menghindari memory leak
            else:
                st.warning("⚠️ Tidak ada data yang valid untuk matplotlib chart.")
        else:
            st.warning("⚠️ Kolom tidak ditemukan untuk matplotlib chart.")

except FileNotFoundError:
    st.error(f"❌ File tidak ditemukan: {file_path}")
    st.info("Pastikan file CSV berada di folder 'data' dengan nama 'genz_money_spends.csv'")

except Exception as e:
    st.error(f"❌ Terjadi error: {str(e)}")
    st.info("Periksa format data dan pastikan kolom yang dipilih sesuai.")