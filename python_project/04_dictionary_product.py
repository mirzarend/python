produk = [
  {
    "nama" : "Sabun",
    "harga" : 20000,
    "stok" : 150
  },
  {
    "nama" : "Korek",
    "harga" : 2000,
    "stok" : 100
  },
  {
    "nama" : "Sikat Gigi",
    "harga" : 18000,
    "stok" : 200
  }
  ]
  
def daftar_produk(x) :
  for barang in x :
    print("="*30)
    print(f"Nama : {barang['nama']}")
    print(f"Harga : {barang['harga']}")
    print(f"Stok : {barang['stok']}")
    print("="*30)

def produk_termahal_dan_termurah(x) :
  termahal = x[0]
  termurah = x[0]
  for barang in x :
    if barang['harga'] > termahal['harga'] :
      termahal = barang
    elif barang['harga'] < termurah['harga'] :
      termurah = barang
  return termahal,termurah
  
def total_stok(x) :
  total = 0 
  for t in x  :
    total += t['stok']
  return total
 
print("="*30)
print("-------------- DATA PRODUK --------------")
print("="*30)
daftar_produk(produk)
termahal,termurah = produk_termahal_dan_termurah(produk)
print(f"Barang termahal : {termahal['nama']}, Harga : {termahal["harga"]}")
print(f"Barang termurah : {termurah['nama']}, Harga : {termurah["harga"]}")
print("="*30)
total = total_stok(produk)
print(f"Total stok : {total}")
print("="*30)
