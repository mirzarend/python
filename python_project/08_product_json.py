import json

dataProduk = [
  {
  "nama" : "Pepsodent",
  "harga" : 15000,
  "stok" : 250
  },
  {
  "nama" : "Royco",
  "harga" : 1000,
  "stok" : 2000
  },
  {
  "nama" : "Lada",
  "harga" : 8000,
  "stok" : 240
  }
 ]
with open("dataProduk.json", "w") as file :
  json.dump(dataProduk,file)
with open("dataProduk.json", "r") as file :
  hasil = json.load(file)

def tampilkan_produk(barang) :
  for produk in barang :
    print("="*30)
    print(f"Nama : {produk["nama"]}")
    print(f"Harga : {produk["harga"]}")
    print(f"Stok : {produk["stok"]}")
    print("="*30)

tampilkan_produk(hasil)
