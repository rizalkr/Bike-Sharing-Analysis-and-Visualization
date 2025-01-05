import streamlit as st
import pandas as pd

# Judul aplikasi
st.title('Dashboard Analisis Penyewaan Sepeda')

# Bagian Analisis Cluster
st.header('Analisis Cluster')
st.text("Metode Elbow untuk menentukan jumlah cluster optimal.")
st.image('elbow_plot.png', caption='Grafik Elbow')

# Bagian Analisis RFM
st.header('Analisis RFM')
st.text("Hasil analisis RFM pada data penyewaan sepeda.")
uploaded_file = st.file_uploader("Upload file hasil RFM dalam format CSV", type=["csv"])
if uploaded_file:
    rfm_data = pd.read_csv(uploaded_file)
    st.dataframe(rfm_data)
