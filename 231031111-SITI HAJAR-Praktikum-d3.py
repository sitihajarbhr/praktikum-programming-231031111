




nama    = 'Siti Hajar Baharuddin'
nim     = '231031111'
prodi   = 'Sistem Informasi D'
meet    = 'Praktikum d3'
email   = 'sitihajarbhr884@gmail.com'

sp = 40

print('_'.center(sp,'-'))
#print(len(nama))
print(nama.center(31))
print(nim.center(31))
print('\n'*2)
print(meet.rjust(31))
print(prodi.rjust(31))
print(email.rjust(31))

#print(len(nama))
print('-'.center(sp,'-'))
print(nama.center(sp))
print(nim.center(sp))
print('\n'*2)
print(meet.rjust(sp))
print(prodi.rjust(sp))
print(email.rjust(sp))

print('-'.center(sp,'-'))

#print(f'''Halo, selamat datang perkenalkan nama
#saya {nama} dengan NIM {nim} dari prodi {prodi}. 
#Ini adalah file {meet}.''')

paragraf = '''\tHalo, selamat datang perkenalkan nama
saya {} dengan NIM {} dari prodi {}. 
Ini adalah file {}.'''

p = paragraf.format(nama,nim,prodi,meet)
print(p)


#-----------------5+++++++++++9----------
x = int(input('masukkan nilai --5++9--= '))
cek1 = x>=5
cek2 = x<=9
status = cek1 and cek2
print('hasilnya adalah',status)

x = int(input('masukkan nilai ++5--9++= '))
cek1 = x>=5
cek2 = x<=9
status = cek1 or cek2
print('hasilnya adalah',status)

x = int(input('masukkan nilai ++5--9++13--= '))
cek1 = x<5
cek2 = x>9
cek3 = x<13
status = cek1 and cek2 or cek3
print('hasilnya adalah',status)

print('\n\ntugas praktikum d3')
#Tugas 1
x = int(input('\nmasukkan nilai ---5+++9---13++16---= '))
cek1 = x<5
cek2 = x>9
cek3 = x<13
cek4 = x>16
status = cek1 and cek2 or cek3 and cek4
print('hasilnya adalah',status)

#Tugas 2
x = int(input('\nmasukkan nilai +++5---9+++13---16+++= '))
cek1 = x<5
cek2 = x>9
cek3 = x>13
cek4 = x<16
status = cek1 or cek2 and cek3 or cek4
print('hasilnya adalah',status)

#Tugas 3
x = int(input('\nmasukkan nilai ---5+++9---13+++16---20+++24---= '))
cek1 = x<5
cek2 = x>9
cek3 = x<13
cek4 = x>16
cek5 = x<20
cek6 = x>24
status = cek1 and cek2 or cek3 and cek4 or cek5 and cek6
print('hasilnya adalah',status)

#Tugas 4
x = int(input('\nmasukkan nilai +++5---9+++13---16+++20---24+++= '))
cek1 = x>5
cek2 = x<9
cek3 = x>13
cek4 = x<16
cek5 = x>20
cek6 = x<24
status = cek1 and cek2 or cek3 or cek4 and cek5 or cek6
print('hasilnya adalah',status)
