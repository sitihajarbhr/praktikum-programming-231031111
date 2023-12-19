
print('\n')
biodata = { 'nama'  : 'Siti Hajar Baharuddin',
'nim'   : '231031111',
'kelas' : 'S123D',
'tempat,tanggal lahir' : 'Parepare, 08 Agustus 2004',
'jenis kelamin' : 'perempuan',
'agama' : 'islam',
'alamat': 'jl. H. Agussalim no.62',
'email' : 'sitihajarbhr884@gmail.com'
}

print(biodata.keys())
print(biodata.values())

print()
selected_biodata = dict(list(biodata.items())[:3])
print(selected_biodata)