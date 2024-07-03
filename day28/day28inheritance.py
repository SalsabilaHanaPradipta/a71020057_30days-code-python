class Hewan:
  def __init__(self, nama, spesies):
    self.nama = nama
    self.spesies = spesies

  def makan(self):
    print(f"{self.nama} sedang makan.")

class Kucing(Hewan):
  def __init__(self, nama, spesies, ras):
    super().__init__(nama, spesies)  # Memanggil init dari kelas parent
    self.ras = ras

  def bersuara(self):
    print(f"{self.nama} (Kucing) berkata 'Miaow!'.")

# Buat objek Hewan
hewan = Hewan("Burung", "Hantu")

# Hewan dapat makan
hewan.makan()

# Buat objek Kucing
kucingku = Kucing("Pus", "Kucing Domestik", "Persia")

# Kucing dapat makan dan bersuara
kucingku.makan()
kucingku.bersuara()