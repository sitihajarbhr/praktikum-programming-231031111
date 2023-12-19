
biodata = {'Nama Lengkap'   : 'Siti Hajar Baharuddin', 
           'NIM'            : 231031111,
           'tgl.Lahir'      : '08/08/2004',
           'email'          : 'sitihajarbhr884@gmail.com',
           'alamat'         : 'Agsal',
           'jenis kelamin'  : 'Perempuan',
           'hobi'           : {'Traveling':'sering',
                               'renang'   :'kadang'
                               }
           }

nickname = ['Siti',
            'Hajar',
            'Baharuddin'
            ]
# mengakses data
print(biodata['Nama Lengkap'])
print(nickname[1])
print(biodata.get('NIM'),'\n')

print(biodata,'\n')

# menambah data
biodata['hobi']['badminton']='kadang'  
biodata['hobi']['bersepeda']='kadang'  
biodata['kewarganegaraan']='Indonesia'

print('Hobi:',biodata['hobi'],'\n')

# mengupdate data
biodata['alamat']='Parepare'

# menghapus data
del biodata['jenis kelamin']

print(biodata,'\n\n')

print(biodata.keys())
print(biodata.values(),'\n')

print(biodata['hobi'].keys())
print(biodata['hobi'].values())


