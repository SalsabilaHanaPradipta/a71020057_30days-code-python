from datetime import datetime, timedelta

# Mendapatkan tanggal dan waktu saat ini
current_time = datetime.now()
print("Waktu saat ini:", current_time)

# Memformat tanggal dan waktu
formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
print("Waktu yang diformat:", formatted_time)

# Mengkonversi string ke datetime
date_string = "2023-06-21 15:30:00"
converted_time = datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
print("Waktu yang dikonversi dari string:", converted_time)

# Menambahkan atau mengurangi waktu menggunakan timedelta
future_time = current_time + timedelta(days=5)
print("Waktu 5 hari dari sekarang:", future_time)

past_time = current_time - timedelta(days=5)
print("Waktu 5 hari yang lalu:", past_time)

# Mendapatkan perbedaan antara dua tanggal
time_difference = future_time - current_time
print("Perbedaan waktu dalam hari:", time_difference.days)