import streamlit as st
import requests
import folium
from streamlit_folium import st_folium

st.title("Visualisasi Mobil Terpilih")

# Memanggil data dari API Flask yang sedang jalan
try:
    response = requests.get("http://127.0.0.1:5000")
    data = response.json()

    # Membuat Peta
    m = folium.Map(location=[-6.2, 106.8], zoom_start=15)
    folium.GeoJson(data).add_to(m)
    
    # Tampilkan Peta
    st_folium(m, width=700)
    st.success("Data berhasil dimuat!")
except:
    st.error("Gagal mengambil data. Pastikan Flask API masih menyala!")