import re

# Pola regex untuk mencocokkan kata 'Halo'
pattern = r'Halo'

# Teks yang akan dicari
text = 'Halo, dunia!'

# Mencari pola dalam teks
match = re.search(pattern, text)

if match:
    print("Pola ditemukan!")
else:
    print("Pola tidak ditemukan.")