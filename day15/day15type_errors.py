def add_numbers(a, b):
    try:
        result = a + b
        print(f"Hasil penjumlahan {a} dan {b} adalah {result}")
    except TypeError as e:
        print(f"TypeError: {e}. Pastikan kedua input adalah angka.")

def multiply_numbers(a, b):
    try:
        result = a * b
        print(f"Hasil perkalian {a} dan {b} adalah {result}")
    except TypeError as e:
        print(f"TypeError: {e}. Pastikan kedua input adalah angka.")

def divide_numbers(a, b):
    try:
        result = a / b
        print(f"Hasil pembagian {a} dengan {b} adalah {result}")
    except TypeError as e:
        print(f"TypeError: {e}. Pastikan kedua input adalah angka.")
    except ZeroDivisionError as e:
        print(f"ZeroDivisionError: {e}. Pembagian dengan nol tidak diperbolehkan.")

def concatenate_strings(a, b):
    try:
        result = a + b
        print(f"Hasil penggabungan '{a}' dan '{b}' adalah '{result}'")
    except TypeError as e:
        print(f"TypeError: {e}. Pastikan kedua input adalah string.")

add_numbers(10, '20')        
multiply_numbers(10, None)   
divide_numbers(10, 0)        
concatenate_strings(10, "20") 