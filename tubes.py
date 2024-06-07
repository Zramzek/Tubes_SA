import streamlit as st
import time
import random

data = [
    {'Nama': 'es cekek', 'Harga': 3000, 'Jenis': 'Minuman', 'Tetangga1': 'roti bakar', 'Tetangga2': 'cireng'},
    {'Nama': 'cireng', 'Harga': 5000, 'Jenis': 'Makanan', 'Tetangga1': 'es cekek', 'Tetangga2': 'kentang'},
    {'Nama': 'es teh', 'Harga': 5000, 'Jenis': 'Minuman', 'Tetangga1': 'dimsum', 'Tetangga2': 'batagor'},
    {'Nama': 'roti bakar', 'Harga': 6000, 'Jenis': 'Makanan', 'Tetangga1': 'dimsum', 'Tetangga2': 'es cekek'},
    {'Nama': 'kentang', 'Harga': 8000, 'Jenis': 'Makanan', 'Tetangga1': 'es cekek', 'Tetangga2': 'cireng'},
    {'Nama': 'batagor', 'Harga': 10000, 'Jenis': 'Makanan', 'Tetangga1': 'es teh', 'Tetangga2': 'es cekek'},
    {'Nama': 'dimsum', 'Harga': 12000, 'Jenis': 'Makanan', 'Tetangga1': 'es teh', 'Tetangga2': 'roti bakar'},
    {'Nama': 'bakso', 'Harga': 9000, 'Jenis': 'Makanan', 'Tetangga1': 'sate', 'Tetangga2': 'nasi goreng'},
    {'Nama': 'sate', 'Harga': 11000, 'Jenis': 'Makanan', 'Tetangga1': 'bakso', 'Tetangga2': 'mie ayam'},
    {'Nama': 'nasi goreng', 'Harga': 8000, 'Jenis': 'Makanan', 'Tetangga1': 'martabak', 'Tetangga2': 'sate'},
    {'Nama': 'mie ayam', 'Harga': 12000, 'Jenis': 'Makanan', 'Tetangga1': 'es krim', 'Tetangga2': 'nasi goreng'},
    {'Nama': 'martabak', 'Harga': 15000, 'Jenis': 'Makanan', 'Tetangga1': 'es krim', 'Tetangga2': 'bakso'},
    {'Nama': 'es krim', 'Harga': 5000, 'Jenis': 'Minuman', 'Tetangga1': 'martabak', 'Tetangga2': 'nasi goreng'},
    {'Nama': 'gulai', 'Harga': 13000, 'Jenis': 'Makanan', 'Tetangga1': 'tahu isi', 'Tetangga2': 'pempek'},
    {'Nama': 'tahu isi', 'Harga': 6000, 'Jenis': 'Makanan', 'Tetangga1': 'gulai', 'Tetangga2': 'kerak telor'},
    {'Nama': 'pempek', 'Harga': 9000, 'Jenis': 'Makanan', 'Tetangga1': 'gulai', 'Tetangga2': 'ketoprak'},
    {'Nama': 'kerak telor', 'Harga': 7000, 'Jenis': 'Makanan', 'Tetangga1': 'ketoprak', 'Tetangga2': 'tahu isi'},
    {'Nama': 'ketoprak', 'Harga': 10000, 'Jenis': 'Makanan', 'Tetangga1': 'pempek', 'Tetangga2': 'kerak telor'},
    {'Nama': 'siomay', 'Harga': 12000, 'Jenis': 'Makanan', 'Tetangga1': 'gorengan', 'Tetangga2': 'es campur'},
    {'Nama': 'gorengan', 'Harga': 3000, 'Jenis': 'Makanan', 'Tetangga1': 'siomay', 'Tetangga2': 'rujak'},
    {'Nama': 'es campur', 'Harga': 8000, 'Jenis': 'Minuman', 'Tetangga1': 'rujak', 'Tetangga2': 'siomay'},
    {'Nama': 'rujak', 'Harga': 6000, 'Jenis': 'Makanan', 'Tetangga1': 'es campur', 'Tetangga2': 'gorengan'},
    {'Nama': 'lumpia', 'Harga': 10000, 'Jenis': 'Makanan', 'Tetangga1': 'bakwan', 'Tetangga2': 'pisang goreng'},
    {'Nama': 'bakwan', 'Harga': 4000, 'Jenis': 'Makanan', 'Tetangga1': 'lumpia', 'Tetangga2': 'cendol'},
    {'Nama': 'pisang goreng', 'Harga': 6000, 'Jenis': 'Makanan', 'Tetangga1': 'cendol', 'Tetangga2': 'lumpia'},
    {'Nama': 'cendol', 'Harga': 5000, 'Jenis': 'Minuman', 'Tetangga1': 'pisang goreng', 'Tetangga2': 'bakwan'},
    {'Nama': 'kolak', 'Harga': 8000, 'Jenis': 'Makanan', 'Tetangga1': 'jajanan pasar', 'Tetangga2': 'nasi uduk'},
    {'Nama': 'jajanan pasar', 'Harga': 7000, 'Jenis': 'Makanan', 'Tetangga1': 'kolak', 'Tetangga2': 'bubur ayam'},
    {'Nama': 'nasi uduk', 'Harga': 9000, 'Jenis': 'Makanan', 'Tetangga1': 'ayam penyet', 'Tetangga2': 'kolak'},
    {'Nama': 'bubur ayam', 'Harga': 8000, 'Jenis': 'Makanan', 'Tetangga1': 'jajanan pasar', 'Tetangga2': 'es kelapa'},
    {'Nama': 'es kelapa', 'Harga': 5000, 'Jenis': 'Minuman', 'Tetangga1': 'bubur ayam', 'Tetangga2': 'tahu gejrot'},
    {'Nama': 'tahu gejrot', 'Harga': 4000, 'Jenis': 'Makanan', 'Tetangga1': 'es kelapa', 'Tetangga2': 'mie kocok'},
    {'Nama': 'mie kocok', 'Harga': 7000, 'Jenis': 'Makanan', 'Tetangga1': 'serabi', 'Tetangga2': 'tahu gejrot'},
    {'Nama': 'es teler', 'Harga': 12000, 'Jenis': 'Minuman', 'Tetangga1': 'mie kocok', 'Tetangga2': 'somay'},
    {'Nama': 'somay', 'Harga': 9000, 'Jenis': 'Makanan', 'Tetangga1': 'es teler', 'Tetangga2': 'ayam penyet'},
    {'Nama': 'ayam penyet', 'Harga': 13000, 'Jenis': 'Makanan', 'Tetangga1': 'somay', 'Tetangga2': 'nasi uduk'},
    {'Nama': 'ayam geprek', 'Harga': 11000, 'Jenis': 'Makanan', 'Tetangga1': 'ayam goreng', 'Tetangga2': 'ikan bakar'},
    {'Nama': 'ayam goreng', 'Harga': 10000, 'Jenis': 'Makanan', 'Tetangga1': 'ayam geprek', 'Tetangga2': 'udang bakar'},
    {'Nama': 'ikan bakar', 'Harga': 15000, 'Jenis': 'Makanan', 'Tetangga1': 'ayam geprek', 'Tetangga2': 'cumi bakar'},
    {'Nama': 'udang bakar', 'Harga': 17000, 'Jenis': 'Makanan', 'Tetangga1': 'ayam goreng', 'Tetangga2': 'sop buntut'},
    {'Nama': 'cumi bakar', 'Harga': 16000, 'Jenis': 'Makanan', 'Tetangga1': 'ikan bakar', 'Tetangga2': 'sop iga'},
    {'Nama': 'sop buntut', 'Harga': 20000, 'Jenis': 'Makanan', 'Tetangga1': 'udang bakar', 'Tetangga2': 'sop iga'},
    {'Nama': 'sop iga', 'Harga': 18000, 'Jenis': 'Makanan', 'Tetangga1': 'sop buntut', 'Tetangga2': 'cumi bakar'},
    {'Nama': 'soto ayam', 'Harga': 7000, 'Jenis': 'Makanan', 'Tetangga1': 'soto betawi', 'Tetangga2': 'sate padang'},
    {'Nama': 'soto betawi', 'Harga': 9000, 'Jenis': 'Makanan', 'Tetangga1': 'soto ayam', 'Tetangga2': 'soto'}
]

def find_item(data, cari):
    for j in data:
        if cari == j['Nama']:
            return j
    return None

def knapsack_greedy(data, w, n):
    start = time.time()
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
        end = time.time()
        
    return x, total_harga, end-start


st.title("Mencari Takjil Greedy vs Brute Force")
st.dataframe(data)

w = st.number_input("Tentukan Batas Harga!", placeholder="nilai awal ialah 25000", value=25000)
nama_options = [item['Nama'] for item in data]
n = st.selectbox("Tentukan 1 Item Yang Wajib Dibeli!", nama_options)

col2, col3 = st.columns(2)

greedy = col2.button("Greedy")


if greedy:
    # with st.spinner('Menghitung Data'):
        # time.sleep(1)
    hasil, total, waktu = knapsack_greedy(data, w, n)
    col2.header('Hasil Algoritma Greedy')
    col2.dataframe(hasil)
    col2.header('total harga :')
    col2.subheader(total)
    col2.subheader(waktu)