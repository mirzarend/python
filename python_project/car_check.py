#mini project tentang pengecekan mobil


#Masukkan def tekanan ban 
def cek_tekanan_ban() :
  tekanan_ban = [30,33,32,28]
  tekanan_std = 33
  
  for i in range(4) :
    print("tekanan ban", i+1 , ":", tekanan_ban[i] , "PSI")
    
    if tekanan_ban[i] < tekanan_std :
      print("tekanan kurang")
    elif tekanan_ban[i] > tekanan_std :
      print("tekanan berlebih")
    else :
      print("tekanan pas")

#def volume oli
def cek_oli():
  volume_std = 4
  volume_oli = int(input("Masukkan data oli mobil anda "))
  
  if volume_oli < volume_std:
    print("volume kurang")
  elif volume_oli > volume_std:
    print("volume berlebih")
  else :
    print("volume pas")

#def cek suhu
def cek_suhu() :
  suhu_mobil = 0
  suhu_std = 90
  
  while suhu_mobil < suhu_std :
    print("suhu saat ini adalah", suhu_mobil , "°C")
    suhu_mobil = suhu_mobil + 10
  print("mesin sudah mencapai suhu kerjanya")

#Buat judul terlebih dahulu
print("="*30)
print("LAPORAN PENGECEKAN KENDARAAN")
print("="*30)
#ini untuk spasi/enter
print(" ")

#masukkan def dan kasih judul
print("\n --- PENGECEKAN BAN --- ")
cek_tekanan_ban()

print(" ")

print("\n --- PENGECEKAN SUHU --- ")
cek_suhu()

print(" ")

print("\n --- PENGECEKAN OLI --- ")
cek_oli()
