inputKalimat = input("Masukkan kalimat :")

def analisis_kalimat(data):
  vokal = ["a","i","u","e","o"]
  jumlahVokal = 0
  jumlahKonsonan = 0
  for kata in data :
    if kata in vokal :
      jumlahVokal += 1
    elif kata.isalpha():
      jumlahKonsonan += 1
  
  panjangKalimat = data.split()
  kalimatTerpanjang = panjangKalimat[0]
  for kalimat in panjangKalimat :
    if len(kalimat)> len(kalimatTerpanjang):
      kalimatTerpanjang = kalimat 
  
  hasil =(jumlahVokal,jumlahKonsonan,kalimatTerpanjang)
  return hasil
  
hasil = analisis_kalimat(inputKalimat)

print("="*30)
print("-------analisis kalimat------".upper())
print("="*30)
print(f"1. Jumlah vokal pada kalimat : {hasil[0]}")
print(f"2. Jumlah konsonan pada kalimat : {hasil[1]}")
print(f"3. Kalimat terpanjang : {hasil[2]}")
print("="*30)

