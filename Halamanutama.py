import streamlit as st

st.set_page_config(
    page_title="Kelapa Sulbar",
    # initial_sidebar_state="auto"
)
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

st.title("Selamat Datang di Aplikasi Potensi Kelapa Sulawesi Barat")
# Custom CSS untuk mengubah warna latar belakang
st.markdown(
    """
    <style>
    body {
        background-color: #020249FF;
    }
    [data-testid="stSidebarNav"] {
        display: none;
    }
    .stApp {
        background-color: #02023EFF;
    }
    [data-testid="stSidebarContent"] {
    background-color: #020249B9;
    }
    header {visibility: hidden;}
    .css-1y4p8pa.e1fqkh3o0 {visibility: hidden;}
    </style>
    """,
    unsafe_allow_html=True
)