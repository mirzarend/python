listSiswa = [
  {
    "nama" : "Mirza",
    "umur" : 18,
    "kelas" : "A"
  },
  {
    "nama" : "Rendika",
    "umur" : 16,
    "kelas" : "B"
  },
  {
    "nama" : "Sari",
    "umur" : 20,
    "kelas" : "C"
  }
  ]

def tampilkan_seluruh_siswa(data):
  for siswa in data :
    print("="*30)
    print(f"Nama : {siswa["nama"]}")
    print(f"Umur : {siswa["umur"]}")
    print(f"Kelas : {siswa["kelas"]}")
    print("="*30)

def siswa_termuda_tertua(data) :
  tertua = data[0]
  termuda = data[0]
  for siswa in data :
    if siswa["umur"] > tertua["umur"] :
      tertua = siswa
    elif siswa["umur"] < termuda["umur"] :
      termuda = siswa
  return tertua,termuda

def cari_nama(data) :
  cari_siswa = input("Cari siapa?")
  found = False
  for siswa in data :
    if cari_siswa == siswa["nama"] :
      found = True
      print("Ketemu !")
      print(f"Nama siswa : {siswa["nama"]}")
      print(f"Umur siswa : {siswa["umur"]}")
      print(f"Kelas siswa : {siswa["kelas"]}")
  if not found :
    print("Tidak ada siswa dengan nama tersebut")

tampilkan_seluruh_siswa(listSiswa)
tertua,termuda= siswa_termuda_tertua(listSiswa)
print(f"Siswa dengan umur tertua adalah :{tertua["nama"]}")
print(f"Siswa dengan umur termuda adalah :{termuda["nama"]}")
print("="*30)
cari_nama(listSiswa)