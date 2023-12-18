a = [2, 3, 1, 0, 3, 1, 1, 1, 1]
    #0, 1, 2, 3, 4, 5, 6, 7, 8
    #-9,-8,-7,-6,-5,-4,-3,-2,-1
#akses 
print(a)
print('\nAkses Item')
print(f'item indeks:0 {a[0]}')
print(f'item indeks:3 {a[3]}')
print(f'item indeks:terakhir {a[len(a)-1]}')

#akses item indeks negatif
print('\nAkses Item Indeks Negatif')
print(f'item indeks:terakhir(-1) {a[-1]}')
print(f'item indeks:pertama (-9) {a[-len(a)]}')
print(f'item indeks:1 -8 {a[-8]}')
print(f'item indeks:5 -4 {a[-4]}')

#indeks batas
print('\nIndeks Batas')
print(f'item indeks:1,2,3 {a[1:4]}')
print(f'item indeks:1,2... {a[1:]}')
print(f'item indeks:3,4... {a[3:]}')
print(f'item indeks:0,1,2,3,4 {a[:5]}')
print(f'item indeks:semua {a[:]}')

#pengirisan indeks
print('\nPengirisan Indeks')
print(f'item indeks:1,2,3 {a[1:4]}')
print(f'item indeks:2,3,4 {a[2:5]}')
print(f'item indeks:[1:8]{a[1:-1]}')

#nested list
print('\nNested List')
kelas = [('agama',3),
         ('kaldas1',2),
        ('pemrograman',2)]
print(f'data kelas {kelas}')
kelas.append(('bahasa',3))
print(f'data kelas {kelas}')
kelas.append(('pancasila',3))
print(f'data kelas  {kelas}')

#nama mata kuliah 1: Agama dengan jumlah sks: 3
#nama mata kuliah 2: Kaldas dengan jumlah sks: 2
#nama mata kuliah 3: pemrograman dengan jumlah sks: 2
#nama mata kuliah 4: Bahasa dengan jumlah sks: 3
#nama mata kuliah 4: Pancasila dengan jumlah sks: 3

print('\n\n--------------TUGAS PRAKTIKUM-D4--------------')

data = [('Siti Hajar Baharuddin',2023,'Aktif'),
        (90,98,93,97,100),
        (20,22),
        ('S1-Reguler','Sistem Informasi D','Ganjil')]
# Nama Mahasiswa: Siti Hajar Baharuddin
print(f'Nama Mahasiswa: {data[0][0]}')

# NIM Mahasiswa: 231031111
print(f'NIM Mahasiswa: {a[0]}{a[1]}{a[2]}{a[3]}{a[4]}{a[5]}{a[6]}{a[7]}{a[8]}')

# Program pendidikan : Sistem Informasi D S1-Reguler
print(f'Program Pendidikan: {data[3][1]} {data[3][0]}')

# Angkatan: 2023-Ganjil
print(f'Angkatan: {data[0][1]}-{data[-1][-1]}')

# Jumlah nilai Siti Hajar Baharuddin adalah
print(f'Jumlah Nilai Hajar adalah: {len(data[1])}')

# Data terbesar Hajar adalah
print(f'Data Terbesar Hajar Adalah: {max(data[1])}')

# Data Terkecil adalah
print(f'Data Terkecil Hajar Adalah: {min(data[1])}')

# Rata-Rata nilai adalah
rata= sum(data[1])/len(data[1])
print(f'Rata-rata Nilai Hajar adalah: {rata}')













































