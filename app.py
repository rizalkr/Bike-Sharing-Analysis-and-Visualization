with open('requirements.txt', 'w') as f:
    f.write("pandas\nmatplotlib\nscikit-learn\nstreamlit\n")

print("\nUntuk menjalankan dashboard Streamlit, gunakan skrip berikut:")
print("""
import streamlit as st

st.title('Analisis Penyewaan Sepeda')

st.header('Analisis Cluster')
st.image('elbow_plot.png', caption='Metode Elbow untuk Cluster Optimal')

st.header('Analisis RFM')
st.dataframe(rfm)

# Unggah file ini sebagai app.py ke Streamlit Cloud untuk menjalankan dashboard.
""")
