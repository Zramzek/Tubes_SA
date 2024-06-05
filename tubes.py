import streamlit as st
import time

data = [
    {'Nama':'es cekek', 'Harga': 3000, 'Jenis':'Minuman', 'Tetangga1': 'roti bakar', 'Tetangga2': 'cireng'},
    {'Nama':'cireng', 'Harga': 5000, 'Jenis':'Makanan', 'Tetangga1': 'es cekek', 'Tetangga2': 'kentang'},
    {'Nama':'es teh', 'Harga': 5000, 'Jenis':'Minuman', 'Tetangga1': 'dimsum', 'Tetangga2': 'batagor'},
    {'Nama':'roti bakar', 'Harga': 6000, 'Jenis':'Makanan', 'Tetangga1': 'dimsum', 'Tetangga2': 'es cekek'},
    {'Nama':'kentang', 'Harga': 8000, 'Jenis':'Makanan', 'Tetangga1': 'es cekek', 'Tetangga2': 'cireng'},
    {'Nama':'batagor', 'Harga': 10000, 'Jenis':'Makanan', 'Tetangga1': 'es teh', 'Tetangga2': 'es cekek'},
    {'Nama':'dimsum', 'Harga': 12000, 'Jenis':'Makanan', 'Tetangga1': 'es teh', 'Tetangga2': 'roti bakar'},
]

def find_item(data, cari):
    for j in data:
        if cari == j['Nama']:
            return j
    return None

def knapsack_greedy(data, w, n):
    total_harga = 0
    minuman = 0
    x = []

    found = find_item(data, n)
    if not found:
        return x, total_harga

    x.append(found)
    total_harga += found['Harga']

    while total_harga <= w:  
        item = found
        data.remove(found)
        t1 = find_item(data, item['Tetangga1'])
        t2 = find_item(data, item['Tetangga2'])
        if t1 and t2:
            if t1['Harga'] < t2['Harga']:
                found = t1
            else:
                found = t2
        elif t1:
            found = t1
        elif t2:
            found = t2
        else:
            break

        if found['Jenis'] == 'Minuman':
            minuman+=1
        
        if minuman >= 1 and found['Jenis'] == 'Minuman':
            continue

        if total_harga + found['Harga'] > w:
            continue

        x.append(found)
        total_harga += found['Harga']
        
    return x, total_harga


st.title("Mencari Takjil Greedy vs Brute Force")
edited_df = st.data_editor(data, num_rows="dynamic")

w = st.number_input("Tentukan Batas Harga!", placeholder="nilai awal ialah 25000", value=25000)
nama_options = [item['Nama'] for item in edited_df]
n = st.selectbox("Tentukan 1 Item Yang Wajib Dibeli!", nama_options)

col1, col2 = st.columns(2)

greedy = col1.button("Greedy")
dp = col2.button("Dynamic Programming")


if greedy:
    with st.spinner('Menghitung Data'):
        time.sleep(3)
    hasil, total = knapsack_greedy(edited_df, w, n)
    col1.write('Hasil Algoritma Greedy')
    col1.dataframe(hasil)
    col1.write('total harga :')
    col1.write(total)

if dp:
    with st.spinner('Menghitung Data'):
        time.sleep(3)
    col2.write('Hasil Algoritma Dynamic Programming')
