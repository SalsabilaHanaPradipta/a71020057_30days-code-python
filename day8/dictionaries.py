mahasiswa = {'nama':'salsa','umur':19} 
mahasiswa['umur'] = 19 
mahasiswa['alamat'] = 'karawang' 
mahasiswa['angkatan'] = 2023
print(mahasiswa) 
print(mahasiswa.pop('angkatan')) 
print(mahasiswa) 
print('nama' in mahasiswa) 
print(len(mahasiswa)) 
print(sorted(mahasiswa)) 
mahasiswa.clear() 
print(mahasiswa)