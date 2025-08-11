import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestRegressor

#load dataset
df = pd.read_excel("DATA RUMAH.xlsx")

#train model
x = data[["LB","LT","KT","KM","GRS"]]
y = data[["HARGA"]]

#streamlit app
st.title("Prediksi Harga Rumah")
st.write('Masukan Rincian Rumah yang diinginkan')

#inputan
luas_bangunan = int(input("Masukkan Luas Tanah: "))
luas_tanah = int(input("Masukkan Luas Bangunan: "))
unit_KM = int(input("Masukkan Banyak Kamar Mandi: "))
unit_KT = int(input("Masukkan Banyak Kamar Tidur: "))
unit_GRS = int(input("Masukkan Banyak Garasi: "))

#tombol prediksi
if st.button('Prediksi'):
    prediksi = model.predict(([[luas_bangunan, luas_tanah, unit_KM, unit_KT, unit_GRS]]))
    st.write("Harga Prediksi Rumah Sebesar Rp" + harga_format)
    harga_format = "{:,.0f}".format(harga).replace(",", ".")


