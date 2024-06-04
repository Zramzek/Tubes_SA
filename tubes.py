import streamlit as st
import time

data = [
    {'Nama':'Es Cekek', 'Harga': 3000, 'Jenis':'Minuman', 'Tetangga1': 'Roti Bakar', 'Tetangga2': 'Cireng'},
    {'Nama':'Cireng', 'Harga': 5000, 'Jenis':'Makanan', 'Tetangga1': 'Es Cekek', 'Tetangga2': 'Kentang'},
    {'Nama':'Es Teh', 'Harga': 5000, 'Jenis':'Minuman', 'Tetangga1': 'Dimsum', 'Tetangga2': 'Batagor'},
    {'Nama':'Roti Bakar', 'Harga': 6000, 'Jenis':'Makanan', 'Tetangga1': 'Dimsum', 'Tetangga2': 'Es Cekek'},
    {'Nama':'Kentang', 'Harga': 8000, 'Jenis':'Makanan', 'Tetangga1': 'Es Cekek', 'Tetangga2': 'Cireng'},
    {'Nama':'Batagor', 'Harga': 10000, 'Jenis':'Makanan', 'Tetangga1': 'Es Teh', 'Tetangga2': 'Es Cekek'},
    {'Nama':'Dimsum', 'Harga': 12000, 'Jenis':'Makanan', 'Tetangga1': 'Es Teh', 'Tetangga2': 'Roti Bakar'},
]

data2 = data

def knapsack_greedy(data, w, n):
    start_time = time.process_time()
    total_harga = 0
    item = find_item(data, n)

    x = []
    x.append(item)
    total_harga += item['Harga']          
    while total_harga <= w: 
        data.remove(item)
        t1 = find_item(data, item['Tetangga1'])
        t2 = find_item(data, item['Tetangga2'])
        if t1 != None and t2 != None:
            if t1['Harga'] < t2['Harga']:
                item = t1
            else:
                item = t2
        elif t1 != None:
            item = t1
        else:
            item = t2

        x.append(item)
        total_harga += item['Harga']          
    
    end_time = time.process_time()
    return x, total_harga, end_time-start_time

def find_item(data, cari):
    for j in data:
        if cari == j['Nama']:
            return j
        return None

st.title("Mencari Takjil Greedy vs Brute Force")

st.dataframe(data)
w = st.number_input("Tentukan Batas Harga!", placeholder="nilai awal ialah 25000", value=25000)
nama_options = [item['Nama'] for item in data]
n = st.selectbox("Tentukan 1 Item Yang Wajib Dibeli!", nama_options)

hasil, total, waktu = knapsack_greedy(data2, w, n)
st.dataframe(hasil)
st.write(total)
st.write(waktu)


# def knapsack_greedy(data, w, first):
#     start_time = time.process_time()
#     x = []
#     minuman = 0
#     total_harga = 0
#     item = find_item(data, first)

#     x.append(item)
#     total_harga += item['Harga']
#     while total_harga <= w:
#         t1 = find_item(data, item['Tetangga1'])
#         t2 = find_item(data, item['Tetangga2'])
#         x1 = find_item(x, item['Nama'])
#         x2 = find_item(x, item['Nama'])
#         if x1 == None and x2 == None:
#             if t1['Harga'] < t2['Harga']:
#                 item = t1
#             else:
#                 item = t2
#         elif x1 == None and x2 != None:
#             item = t1
#         elif x2 == None and x1 != None:
#             item = t1
#         else:
#             break
#         x.append(item)
#         total_harga += item['Harga']          
#     return x