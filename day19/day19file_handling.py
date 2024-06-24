def tulis_file():
    with open('contoh.txt', 'w') as file:
        file.write("Halo, ini adalah baris pertama di file.\n")
        file.write("Ini adalah baris kedua di file.\n")
    print("Penulisan ke file selesai.")

def baca_file():
    with open('contoh.txt', 'r') as file:
        content = file.read()
    print("Isi file:")
    print(content)

def tambah_ke_file():
    with open('contoh.txt', 'a') as file:
        file.write("Ini adalah baris tambahan di file.\n")
    print("Penambahan ke file selesai.")

def baca_per_baris():
    with open('contoh.txt', 'r') as file:
        for line in file:
            print(line, end='')

# Menulis ke file
tulis_file()

# Membaca isi file
baca_file()

# Menambahkan teks ke file
tambah_ke_file()

# Membaca file baris demi baris
baca_per_baris()