import streamlit as st
import pandas as pd

# Judul
st.title('Bike Sharing Dashboard Analyze')

# Bagian 1: Visualisasi Metode Elbow
st.header('Metode Elbow untuk Cluster Optimal')
st.image('elbow_plot.png', caption='Grafik Elbow untuk Menentukan Cluster Optimal')

# Bagian 2: Distribusi Skor RFM
st.header('Distribusi Skor RFM')
st.image('rfm_distribution.png', caption='Distribusi Skor Recency, Frequency, Monetary')

# Bagian 3: Tabel RFM
st.header('Tabel Analisis RFM')
rfm = pd.read_csv('rfm_analysis.csv')
st.dataframe(rfm)

# Bagian 4: Upload Data Baru
st.header('Unggah Dataset Baru')
uploaded_file = st.file_uploader("Upload dataset (CSV)", type=["csv"])
if uploaded_file:
    data = pd.read_csv(uploaded_file)
    st.write("Pratinjau Data:")
    st.dataframe(data)
