Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
sp = 45
total = 0
kode = [0, 'A', 'B', 'C', 'D', 'E']
jenis = [0, 'Cuci kering Express', 'Setrika', 'Seprei', 'Karpet', 'Bedcover']
harga = [0, 7000, 6000, 10000, 25000, 15000]

def display_separator():
    print('='.center(sp, '='))

def display_welcome_message():
    display_separator()
    print('SELAMAT DATANG DI LAUNDRY BOY'.center(sp))
    display_separator()
    print()

def display_service_list():
    print('Daftar layanan'.center(sp))
    display_separator()
    print('|', 'Kode'.center(6), '|', 'Jenis Layanan'.center(20), '|', 'Harga (kg)'.center(10), '|')
    display_separator()
    for i in range(1, len(kode)):
        print('|', kode[i].center(6), '|', jenis[i].ljust(20), '|', str(harga[i]).rjust(10), '     |')
    display_separator()

def fungsilayanan():
    global jenislayanan
    global jumlah
    global bayar
    global total
    global kodelayanan

    while True:
        berapa = int(input('\nBerapa jenis Layanan yang ingin digunakan: '))
        if berapa <= 5:
            for i in range(berapa):
                while True:
                    kodelayanan = input('Masukkan kode: ')
                    kodelayananbesar = kodelayanan.upper()
                    if kodelayananbesar in kode[1:]:
                        jenislayanan = print(jenis[kode.index(kodelayananbesar)])
                        jumlah = int(input('jumlah(kg)   : '))
                        bayar = harga[kode.index(kodelayananbesar)] * jumlah
                        print("Sub.total    : Rp.", bayar, '\n')
                        total += bayar
                        break 
                    else:
                        print('\n!!!Kode layanan tidak ditemukan\n   Silahkan memilih ulang!!!\n')
... 
...         else:
...             print('\n**Permintaan anda melebihi jenis layanan (max.5)\n**')
...             continue
... 
...         print('-'.center(sp, '-'))
...         print('Total        : ', total)
... 
...         bayarbayar()
... 
...         lanjut = input('Ada tambahan? (ya/tidak): ')
...         if lanjut.lower() != 'ya':
...             break
...         elif lanjut.lower() == 'ya':
...             total = 0
...             
...     print("\n\n~~TERIMA KASIH TELAH MENGGUNAKAN JASA LAYANAN KAMI~~")
... 
... def bayarbayar():
...     pembayaran = int(input("Masukkan Jumlah Uang Anda : "))
...     if pembayaran >= total:
...         kembalian = pembayaran - total
...         print("Kembalian anda            : Rp.", kembalian)
...     else:
...         print("\nDuh... pembayarannya kurang nih. Bayar dengan cukup yah :D\n")
...         return bayarbayar()
... 
... display_welcome_message()
... display_service_list()
... while True:
... #    display_welcome_message()
... #    display_service_list()
...     fungsilayanan()
... 
...     ulangi = input('\nNEXT CUSTUMER?? (ya/tidak): ')
...     if ulangi.lower() != 'ya':
...       break
... 
... 
