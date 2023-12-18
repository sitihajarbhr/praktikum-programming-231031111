print('Praktikum-2')
print('\n===============Ini and===============')
a = True
b = False
hasil = a and a
print('Nilai',a,'and',a,'adalah',hasil)
hasil = a and b
print('Nilai',a,'and',b,'adalah',hasil)
hasil = b and a
print('Nilai',b,'and',a,'adalah',hasil)
hasil = b and b
print('Nilai',b,'and',b,'adalah',hasil)

print('\n===============Ini or===============')
hasil = a or a
print('Nilai',a,'or',a,'adalah',hasil)
hasil = a or b
print('Nilai',a,'or',b,'adalah',hasil)
hasil = b or a
print('Nilai',b,'or',a,'adalah',hasil)
hasil = b or b
print('Nilai',b,'or',b,'adalah',hasil)

print('\n===============Ini not===============')
hasil = not a
print('Hasil not',a,'adalah',hasil)
hasil = not b
print('Hasil not',b,'adalah',hasil)
 
print('\n===============Ini xor===============')
hasil = a ^ a
print('hasil',a,'xor',a,'adalah',hasil)
hasil = a ^ b
print('hasil',a,'xor',b,'adalah',hasil)
hasil = b ^ a
print('hasil',b,'xor',a,'adalah',hasil)
hasil = b ^ b
print('hasil',b,'xor',b,'adalah',hasil)

print('\n===============Ini nand===============')
hasil = not (a and a)
print('Nilai',a,'nand',a,'adalah',hasil)
hasil = not (a and b)
print('Nilai',a,'nand',b,'adalah',hasil)
hasil = not (b and a)
print('Nilai',b,'nand',a,'adalah',hasil)
hasil = not (b and b)
print('Nilai',b,'nand',b,'adalah',hasil)

print('\n===============Ini nor===============')
hasil = not (a or a)
print('Nilai',a,'nor',a,'adalah',hasil)
hasil = not (a or b)
print('Nilai',a,'nor',b,'adalah',hasil)
hasil = not (b or a)
print('Nilai',b,'nor',a,'adalah',hasil)
hasil = not (b or b)
print('Nilai',b,'nor',b,'adalah',hasil)

print('\n===============Ini nxor===============')
hasil = a ^ a
print('hasil',a,'nxor',a,'adalah',not hasil)
hasil = a ^ b
print('hasil',a,'nxor',b,'adalah',not hasil)
hasil = b ^ a
print('hasil',b,'nxor',a,'adalah',not hasil)
hasil = b ^ b
print('hasil',b,'nxor',b,'adalah',not hasil)

print('\n================ini is================')
a = 5
b = 6
print('nilai',a,'memiliki identitas=',hex(id(a)))
print('nilai',b,'memiliki identitas=',hex(id(b)))
hasil = a is b
print('a is b =',hasil)

a = 6
b = 6
print('nilai',a,'memiliki identitas=',hex(id(a)))
print('nilai',b,'memiliki identitas=',hex(id(b)))
hasil = a is b 
print('a is b =',hasil)

print('\n================ini is not================')
a = 5
b = 6
print('nilai',a,'memiliki identitas=',hex(id(a)))
print('nilai',b,'memiliki identitas=',hex(id(b)))
hasil = a is not b
print('a is not b =',hasil)

a = 6
b = 6
print('nilai',a,'memiliki identitas=',hex(id(a)))
print('nilai',b,'memiliki identitas=',hex(id(b)))
hasil = a is not b 
print('a is not b =',hasil)

print('\n================ini in================')
nama = 'Bacharuddin Jusuf Habibie'

test = 'rud'
cek = test in nama
print(test,'terdapat di',nama,'adalah '+str(cek))

test = 'bach'
cek = test in nama
print(test,'terdapat di',nama,'adalah '+str(cek))

test = 'ib'
cek = test in nama
print(test,'terdapat di',nama,'adalah '+str(cek))

test = 'a'
cek = test in nama
print(test,'terdapat di',nama,'adalah '+str(cek))

test = 'i'
cek = test in nama
print(test,'terdapat di',nama,'adalah '+str(cek))

test = 'u'
cek = test in nama
print(test,'terdapat di',nama,'adalah '+str(cek))

test = 'e'
cek = test in nama
print(test,'terdapat di',nama,'adalah '+str(cek))

test = 'o'
cek = test in nama
print(test,'terdapat di',nama,'adalah '+str(cek))

print('\n================in================')
data = ['Institut',
        'Teknologi',
        'Bacharuddin',
        'Jusuf',
        'Habibie']
print('Data adalah',data)
test1 = 'Habibie'
test2 = 'Parepare'
test3 = 'Kampus'
test4 = 'Institut'

cek = test1 in data
print(test1,'Terdapat di data adalah '+str(cek))
cek = test2 in data
print(test2,'Terdapat di data adalah '+str(cek))
cek = test3 in data
print(test3,'Terdapat di data adalah '+str(cek))
cek = test4 in data
print(test4,'Terdapat di data adalah '+str(cek))

# INI OPERATOR BITWISE
a = 8    # isi dengan tanggal lahir
b = 8    # isi dengan bulan lahir
b += 4
print('\n================operasi and================')
print('nilai',a,'dalam biner     = ',format(a,'08b'))
print('nilai',b,'dalam biner    = ',format(b,'08b'))
print('-----------------------------------------and')
c = a & b
print('nilai',a,'&',b,'dalam biner adalah ', format(c,'08b'))

print('\n================operasi or================')
print('nilai',a,'dalam biner     = ',format(a,'08b'))
print('nilai',b,'dalam biner    = ',format(b,'08b'))
print('-----------------------------------------or')
c = a | b
print('nilai',a,'|',b,'dalam biner adalah ', format(c,'08b'))

# Tugas Buat Nama menjadi nama lengkap masing2
# TUGAS dengan cara yang sama buat operator untuk not in
# Tugas untuk operator XOR c = a ^ b
# Tugas untuk operator not c = ~a
# Tugas untuk operator not c = ~b
# Tugas untuk operator geser kanan, c = a >> 2
# Tugas untuk operator geser kiri, c = a << 2
# Tugas untuk operator not and, c = ~ (a & b)
# Tugas untuk operator not or, c = ~ (a | b)
# Tugas untuk operator not xor, c = ~ (a ^ b)
# Tugas untuk operator not geser kanan, c = ~ (a >> 2)
# Tugas untuk operator not geser kiri, c = ~ (a << 2)


print('\n\n\nTUGAS BUAT NAMA MENJADI NAMA LENGKAP MASING MASING')
# Tugas Buat Nama menjadi nama lengkap 
print('\n================in================')
nama = 'Siti Hajar Baharuddin'

test = 'jar'
cek = test in nama
print(test, 'terdapat di',nama,'adalah '+str(cek))
test = 'siti'
cek = test in nama
print(test,'terdapat di',nama,'adalah '+str(cek))
test = 'haru'
cek = test in nama
print(test,'terdapat di',nama,'adalah '+str(cek))
test = 'a'
cek = test in nama
print(test,'terdapat di',nama,'adalah '+str(cek))
test = 'i'
cek = test in nama
print(test,'terdapat di',nama,'adalah '+str(cek))
test = 'u'
cek = test in nama
print(test,'terdapat di',nama,'adalah '+str(cek))
test = 'e'
cek = test in nama
print(test,'terdapat di',nama,'adalah '+str(cek))
test = 'o'
cek = test in nama
print(test,'terdapat di',nama,'adalah '+str(cek))
print('---------------------------------------------------in')

# TUGAS buat operator untuk not in
print('\n================not in================')
data = ['RS.',
        'Regional',
        'Dr. Hasri',
        'Ainun',
        'Habibie']
print('Data adalah',data)
test1 = 'Regional'
test2 = 'Parepare'
test3 = 'Tipe B'
test4 = 'Ainun'

cek = test1 not in data
print(test1,'tidak terdapat di data adalah '+str(cek))
cek = test2 not in data
print(test2,'tidak terdapat di data adalah '+str(cek))
cek = test3 not in data
print(test3,'tidak terdapat di data adalah '+str(cek))
cek = test4 not in data
print(test4,'tidak terdapat di data adalah '+str(cek))

# Tugas untuk operator xor c = a ^ b
print('\n================xor================')
print('nilai',a,'dalam biner \t = ',format(a,'08b'))
print('nilai',b,'dalam biner \t = ',format(b,'08b'))
print('-----------------------------------------xor')
c = a ^ b
print('nilai',a,'^',b,'dalam biner adalah',format(c,'08b'))

# Tugas untuk operator not, c = ~a
print('\n================not================')
print('nilai',a,'dalam biner \t = ',format(a,'08b'))
print('nilai',b,'dalam biner \t = ',format(b,'08b'))
print('-----------------------------------------not')
c = ~a
print('nilai','~',a,'dalam biner adalah',format(c,'08b'))

# Tugas untuk operator not, c = ~b
print('\n================not================')
print('nilai',a,'dalam biner \t = ',format(a,'08b'))
print('nilai',b,'dalam biner \t = ',format(b,'08b'))
print('-----------------------------------------not')
c = ~b
print('nilai','~',b,'dalam biner adalah',format(c,'08b'))

# Tugas untuk operator geser kanan, c = a >> 2
print('\n================geser kanan >>================')
print('nilai',a,'dalam biner \t = ',format(a,'08b'))
print('nilai',b,'dalam biner \t = ',format(b,'08b'))
print('----------------------------------------->>')
c = a>>2
print('nilai',a,'>> 2','dalam biner adalah',format(c,'08b'))

# Tugas untuk operator geser kiri, c = a << 2
print('\n================geser kiri <<================')
print('nilai',a,'dalam biner \t = ',format(a,'08b'))
print('nilai',b,'dalam biner \t = ',format(b,'08b'))
print('-----------------------------------------<<')
c = a<<2
print('nilai',a,'<< 2','dalam biner adalah',format(c,'08b'))

# Tugas untuk operator not and, c = ~ (a & b)
print('\n================not and================')
print('nilai',a,'dalam biner \t = ',format(a,'08b'))
print('nilai',b,'dalam biner \t = ',format(b,'08b'))
print('----------------------------------------- ~&')
c = ~ (a & b)
print('nilai','~',a,'&',b,'dalam biner adalah',format(c,'08b'))

# Tugas untuk operator not or, c = ~ (a | b)
print('\n================not or================')
print('nilai',a,'dalam biner \t = ',format(a,'08b'))
print('nilai',b,'dalam biner \t = ',format(b,'08b'))
print('----------------------------------------- ~|')
c = ~ a | b
print('nilai','~',a,'|',b,'dalam biner adalah ', format(c,'08b'))

# Tugas untuk operator not xor, c = ~ (a ^ b)
print('\n================not xor================')
print('nilai',a,'dalam biner \t = ',format(a,'08b'))
print('nilai',b,'dalam biner \t = ',format(b,'08b'))
print('----------------------------------------- ~^')
c = ~ a ^ b
print('nilai','~',a,'^',b,'dalam biner adalah ', format(c,'08b'))

# Tugas untuk operator not geser kanan, c = ~ (a >> 2)
print('\n================not geser kanan================')
print('nilai',a,'dalam biner \t = ',format(a,'08b'))
print('nilai',b,'dalam biner \t = ',format(b,'08b'))
print('----------------------------------------- ~ >>')
c = ~ a >> 2
print('nilai','~',a,'>> 2','dalam biner adalah ',format(c,'08b'))

# Tugas untuk operator not geser kiri, c = ~ (a << 2)
print('\n================not geser kiri================')
print('nilai',a,'dalam biner \t = ',format(a,'08b'))
print('nilai',b,'dalam biner \t = ',format(b,'08b'))
print('----------------------------------------- ~ <<')
c = ~ a << 2
print('nilai','~',a,'<< 2','dalam biner adalah ',format(c,'08b'))









print('\n\n\n\n')
