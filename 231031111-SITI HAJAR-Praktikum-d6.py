while True:
    try:
        num = int(input("Masukkan bilangan ganjil: "))
        if num % 2 == 0:
            print("Harap masukkan bilangan ganjil.")
        else:
            print("Bilangan ini ganjil.")
            break
    except ValueError:
        print("Masukan tidak valid, harap masukkan bilangan.")
