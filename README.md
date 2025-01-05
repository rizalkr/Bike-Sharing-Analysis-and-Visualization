# Bike Sharing Analysis and Visualization

## Deskripsi
Proyek ini bertujuan untuk menganalisis data penyewaan sepeda menggunakan dataset *Bike Sharing*. Analisis ini mencakup eksplorasi data, klasterisasi menggunakan K-Means, serta pendekatan RFM (*Recency, Frequency, Monetary*) untuk memahami perilaku pengguna. Hasil analisis ditampilkan dalam bentuk dashboard interaktif berbasis Streamlit.

## Fitur Utama

1. **Eksplorasi Data**
   - Menampilkan struktur dan statistik dasar dataset.
   - Memeriksa nilai yang hilang untuk memastikan data bersih.

2. **Klasterisasi K-Means**
   - Standarisasi data untuk analisis klaster.
   - Menentukan jumlah klaster optimal menggunakan metode *Elbow*.

3. **Analisis RFM**
   - Mengklasifikasikan pengguna berdasarkan waktu sejak transaksi terakhir, frekuensi, dan nilai transaksi total.
   - Memberikan skor RFM untuk setiap pengguna.

4. **Visualisasi Data**
   - Distribusi skor R, F, dan M.
   - Grafik Elbow untuk klasterisasi.

5. **Dashboard Interaktif**
   - Dibangun menggunakan Streamlit untuk eksplorasi data secara interaktif.

## Struktur Proyek

- `bike_analysis.ipynb`: Notebook analisis utama.
- `requirements.txt`: File yang berisi pustaka Python yang diperlukan.
- `app.py`: Skrip untuk menjalankan dashboard Streamlit.

## Cara Menggunakan

1. **Clone Repositori**:
   ```bash
   git clone https://github.com/username/bike-sharing-analysis.git
   cd bike-sharing-analysis
   ```

2. **Instalasi Pustaka**:
   Jalankan perintah berikut untuk menginstal pustaka yang diperlukan:
   ```bash
   pip install -r requirements.txt
   ```

3. **Jalankan Notebook**:
   Gunakan Jupyter Notebook atau Google Colab untuk menjalankan file `bike_analysis.ipynb`.

4. **Jalankan Dashboard Streamlit**:
   Untuk menjalankan dashboard, jalankan perintah berikut:
   ```bash
   streamlit run app.py
   ```

## Hasil Analisis

1. **Grafik Elbow**:
   Menunjukkan jumlah klaster optimal berdasarkan inersia.

2. **Distribusi Skor RFM**:
   - **Recency**: Mengukur waktu sejak penyewaan terakhir.
   - **Frequency**: Menghitung jumlah penyewaan.
   - **Monetary**: Total penyewaan dalam dataset.

3. **Tabel RFM Skor**:
   Menampilkan skor pengguna berdasarkan analisis RFM.

## Dependensi

Pustaka yang diperlukan untuk menjalankan proyek ini:

- pandas
- matplotlib
- scikit-learn
- streamlit

## Lisensi
Proyek ini dilisensikan di bawah [MIT License](LICENSE).

## Kontribusi
Silakan buat *issue* atau *pull request* jika Anda ingin berkontribusi pada proyek ini. 😊
