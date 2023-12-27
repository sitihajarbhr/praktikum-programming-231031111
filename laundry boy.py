sp = 45

print('='.center(sp,'='))
print('SELAMAT DATANG DI LAUNDRY BOY'.center(sp))
print('='.center(sp,'='),'\n')

total = 0
kode  = [0,'A','B','C','D','E']
jenis = [0,'Cuci kering Express','Setrika','Seprei','Karpet','Bedcover']
harga = [0,7000,6000,10000,25000,15000]

print('Daftar layanan'.center(sp))
print('-'.center(sp,'-'))
print('|','Kode'.center(6),'|','Jenis Layanan'.center(20),'|','Harga (kg)'.center(10),'|')
print('-'.center(sp,'-'))
print('|',kode[1].center(6),'|',jenis[1].ljust(20),'|',harga[1],'     |')
print('|',kode[2].center(6),'|',jenis[2].ljust(20),'|',harga[2],'     |')
print('|',kode[3].center(6),'|',jenis[3].ljust(20),'|',harga[3],'    |')
print('|',kode[4].center(6),'|',jenis[4].ljust(20),'|',harga[4],'    |')
print('|',kode[5].center(6),'|',jenis[5].ljust(20),'|',harga[5],'    |')

def fungsilayanan():
    global jenislayanan
    global jumlah
    global bayar
    global total
    global kodelayanan
    berapa = int(input('\nBerapa jenis Layanan yang ingin digunakan: '))
    if berapa <= 5 :
      for i in range(berapa):
        kodelayanan = input('Masukkan kode: ')
        kodelayananbesar = kodelayanan.upper()
        if kodelayananbesar == 'A':
            jenislayanan = print(jenis[1])
            jumlah       = int(input('jumlah(kg)   : '))
            bayar        = harga[1]*jumlah
            print("Sub.total    : Rp.", bayar,'\n')
            total += bayar
        elif kodelayananbesar == 'B':
            jenislayanan = print(jenis[2])
            jumlah       = int(input('jumlah(kg)   : '))
            bayar        = harga[2]*jumlah
            print("Sub.total    : Rp.", bayar,'\n')
            total += bayar
        elif kodelayananbesar == 'C':
            jenislayanan = print(jenis[3])
            jumlah       = int(input('jumlah(kg)   : '))
            bayar        = harga[3]*jumlah
            print("Sub.total    : Rp.", bayar,'\n')
            total += bayar
        elif kodelayananbesar == 'D':
            jenislayanan = print(jenis[4])
            jumlah       = int(input('jumlah(kg)   : '))
            bayar        = harga[4]*jumlah
            print("Sub.total    : Rp.", bayar,'\n')
            total += bayar
        elif kodelayananbesar == 'E':
            jenislayanan = print(jenis[5])
            jumlah       = int(input('jumlah(kg)   : '))
            bayar        = harga[5]*jumlah
            print("Sub.total    : Rp.", bayar,'\n')
            total += bayar
        else :
            print('\n!!!Kode layanan tidak ditemukan\n   Silahkan memilih ulang!!!')
            return fungsilayanan()
    else :
        print('permintaan anda melebihi jenis layanan\n')
        return fungsilayanan()
    #print('Sub.Total = Rp.',bayar)
    #total += bayar
    print('-'.center(sp,'-'))
    print('Total        : ',total) 

def bayarbayar():
    pembayaran = int(input("Masukkan Jumlah Uang Anda : "))
    if pembayaran >= total :
        kembalian = pembayaran - total
        print("Kembalian anda            : Rp.", kembalian)
    else:
        print("\nUang anda tidak mencukupi. Silahkan bayar dengan cukup!!!\n")
        return bayarbayar()
    
fungsilayanan()
bayarbayar()

print('\n\n~~TERIMA KASIH TELAH MENGGUNAKAN JASA LAYANAN KAMI~~')








