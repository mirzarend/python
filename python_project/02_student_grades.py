#input pengguna
inputNama = input("Masukkan nama anda =")
inputUmur = int(input("Masukkan Umur anda ="))

#input 5 nilai
listNilai = []
for nilai in range(5) :
  inputNilai = int(input("masukkan 5 nilai anda ="))
  listNilai.append(inputNilai)

#nama besar semua
namaBesar = inputNama.upper()

#umur cukup/tidak
if inputUmur >= 18 :
  umur = "sudah dewasa"
else :
  umur = "belum cukup umur"

def analisis_nilai(data) :
  #nilai tertinggi
  nilaiTertinggi = data[0]
  nilaiTerendah = data[0]
  rata2 = sum(data)/len(data)
  for nilai in data :
    if nilai > nilaiTertinggi :
      nilaiTertinggi = nilai
    elif nilai < nilaiTerendah :
      nilaiTerendah = nilai
  
  if rata2 >= 95 :
    grade = "A"
  elif rata2 >=75 :
    grade = "B"
  elif rata2 >=60 :
    grade = "C"
  else :
    grade = "D"

  JumlahNilai = 0 
  for nilai in data :
    if nilai >= 60 :
      JumlahNilai += 1 

  hasil =(nilaiTertinggi,nilaiTerendah,rata2,grade,JumlahNilai)

  return hasil

hasil = analisis_nilai(listNilai)
print("="*30)
print(f"Halo, {namaBesar}")
print(f"Umur anda {inputUmur}, dan anda {umur}")
print("="*30)
print("-------DATA NILAI ANDA :------")
print("="*30)
print(f"Nilai Tertinggi : {hasil[0]}")
print(f"Nilai Terendah : {hasil[1]}")
print(f"Rata rata nilai : {hasil[2]}")
print(f"Grade anda : {hasil[3]}")
print(f"Jumlah nilai yang lulus : {hasil[4]}")
print("="*30)
