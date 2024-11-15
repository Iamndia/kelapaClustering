import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import folium 
from streamlit_folium import st_folium

st.title("Kelapa Sulawesi Barat Tahun 2020")

# Buat menu kustom di sidebar
st.sidebar.title("Kelapa Sulbar")
st.sidebar.page_link("Halamanutama.py", label="Halamana Utama")
st.sidebar.page_link("pages/Majene.py", label="Kelapa Majene 2023")
st.sidebar.page_link("pages/majene22.py", label="Kelapa Majene 2022")
st.sidebar.page_link("pages/majene21.py", label="Kelapa Majene 2021")
st.sidebar.page_link("pages/majene20.py", label="Kelapa Majene 2020")
st.sidebar.page_link("pages/majene19.py", label="Kelapa Majene 2019")
st.sidebar.page_link("pages/majene18.py", label="Kelapa Majene 2018")
st.sidebar.page_link("pages/Sulbar.py", label="Kelapa Sulawesi Barat 2023")
st.sidebar.page_link("pages/Sulbar22.py", label="Kelapa Sulawesi Barat 2022")
st.sidebar.page_link("pages/Sulbar21.py", label="Kelapa Sulawesi Barat 2021")
st.sidebar.page_link("pages/Sulbar20.py", label="Kelapa Sulawesi Barat 2020")
st.sidebar.page_link("pages/Sulbar19.py", label="Kelapa Sulawesi Barat 2019")
st.sidebar.page_link("pages/Sulbar18.py", label="Kelapa Sulawesi Barat 2018")
st.sidebar.page_link("pages/Polman.py", label="Kelapa Polewali Mandar")

# Membaca dataset dari file Excel
df = pd.read_excel("kelapaKabupaten2020.xlsx")
x = df.iloc[:, [4, 5]].values

st.header("Isi Dataset")
st.write(df)

# Elbow method untuk menentukan jumlah cluster yang tepat
clusters = []
for i in range(1, 6):
    kmeans = KMeans(n_clusters=i, init='k-means++', random_state=42)
    kmeans.fit(x)
    clusters.append(kmeans.inertia_)

# Plot Elbow
st.subheader("Elbow Method")
fig1, ax1 = plt.subplots(figsize=(12, 8))
sns.lineplot(x=list(range(1, 6)), y=clusters, ax=ax1)
ax1.set_title("Mencari Elbow")
ax1.set_xlabel("Clusters")
ax1.set_ylabel("Inertia")
st.pyplot(fig1)

# Normalisasi data
scaler = StandardScaler()
x_scaled = scaler.fit_transform(x)

# Proses K-Means Clustering dengan jumlah cluster 3
kmeans = KMeans(n_clusters=2, init='k-means++', random_state=42)
df['Cluster'] = kmeans.fit_predict(x_scaled)

# Mengubah nama kolom untuk lebih rapi
df.columns = df.columns.str.strip()

# Mapping cluster numerik ke kategori
cluster_mapping = {0: 'Rendah', 1: 'Tinggi'}
df['Cluster'] = df['Cluster'].map(cluster_mapping)

# Mapping warna berdasarkan cluster
cluster_colors = {'Rendah': 'green', 'Tinggi': 'red'}

# Membuat plot scatter
st.subheader("Plot Clustering")
fig2, ax2 = plt.subplots(figsize=(15, 6))
sns.scatterplot(x='Kabupaten', y='PROVITAS', hue='Cluster', palette=cluster_colors, s=150, data=df, ax=ax2)
ax2.set_title("Hasil Clustering")
ax2.set_xlabel("Kabupaten")
ax2.set_ylabel("Produktivitas")
st.pyplot(fig2)

st.header("Hasil Cluster")
st.write(df)

# Menampilkan Peta dengan hasil pengelompokan
st.subheader("Peta Hasil Pengelompokan")
def convert_to_float(value):
    try:
        return float(value)
    except (ValueError, TypeError):
        return None

df['latitude'] = df['latitude'].apply(convert_to_float)
df['longtitude'] = df['longtitude'].apply(convert_to_float)

# Buang baris yang memiliki nilai NaN
df = df.dropna(subset=['latitude', 'longtitude'])
map_loc = folium.Map(location=[df['latitude'].mean(), df['longtitude'].mean()], zoom_start=8)
for idx, row in df.iterrows():
    folium.Marker(
        location=[row['latitude'], row['longtitude']], 
        tooltip=f"Kabupaten {row['Kabupaten']} (Cluster: {row['Cluster']})",
        icon=folium.Icon(color='green' if row['Cluster'] == 'Rendah' else 'blue' if row['Cluster'] == 'Sedang' else 'red')
    ).add_to(map_loc)
st_folium(map_loc, width=700)

# Custom CSS untuk mengubah warna latar belakang
st.markdown(
    """
    <style>
    body {
        background-color: #020249FF;
    }
    .stApp {
        background-color: #02023EFF;
    }
    [data-testid="stSidebarContent"] {
    background-color: #020249B9;
    }
     /* Menyembunyikan header */ 
    header.css-1v3fvcr { 
    display: none; 
    } 
    header {visibility: hidden;}
    .css-1y4p8pa.e1fqkh3o0 {visibility: hidden;}
    /* Menyembunyikan footer */ 
    footer.css-1544g2n { 
    display: none; 
    } 
    /* Menyembunyikan tombol hamburger di pojok kanan atas */ 
    .css-6qob1r { 
    display: none; 
    }
    [data-testid="stSidebarNav"] {
        display: none;
    }
    </style>
    """,
    unsafe_allow_html=True
)