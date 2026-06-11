# Mini Project - Python

Perkenalkan nama saya **Muhammad Mirza Rendika**

di dalam repo ini akan berisi beberapa project saya dalam belajar python.

## Cara menjalankan program

1. Pastikan anda sudah mendownload **python**
2. Buka terminal dan masuk ke folder tempat file ini disimpan.
3. jalankan seperti ini :

```bash
python nama_file.py
```

# Project 01 - Sistem pengecekan keadaan mobil sederhana

Project berikut adalah projek pertama saya belajar python, saya masih menggunakan hp di projek ini dengan menggunakan aplikasi Acode.

**Fungsi:** melakukan pengecekan kendaraan seperti pengecekan ban, simulasi kenaikan suhu dalam upaya pengecekan suhu, dan terakhir pengecekan volume oli melalui input pengguna.

# Project 02 - Sistem pengecekan nilai siswa

**Fungsi:** melakukan pengecekan nilai nilai siswa menggunakan *input*. yang terdiri dari :

1. Nilai tertinggi
2. Nilai terendah 
3. Penentuan *grade* siswa serta daftar siswa yang dinyatakan lulus

# Project 03 - Sistem analisis kalimat input

**Fungsi:** melakukan beberapa analisis terhadap *input* yang diberikan terhadap sistem.

## Hal - hal yang dianalisis oleh project ini adalah :
1. Vokal
2. Konsonan
3. Kalimat terpanjang

# Project 04 - Manajemen Produk Sistem

**Fungsi:** Menyusun secara rapi data - data produk dari sebuah warung. Output dari sistem ini adalah :

1. Menunjukkan data - data produk yang meliputi Nama, Harga, Stok
2. Menunjukkan produk termahal serta yang termurah
3. Serta memberikan informasi tentang seluruh stok produk yang tersisa

# Project 05 - Sistem Perekomendasian Film

**Fungsi:** Menyusun secara rapi film film yang tersedia, Menyesuaikan film sesuai *input* genre dan memberikan data film terbaik.  Output dari sistem ini adalah :

1. Menampilkan film - film yang tersedia
2. Menampilkan Film dengan rating tertinggi
3. Meminta *input* genre

# Project 06 - Sistem Pendataan Siswa

**Fungsi:** Menampilkan data data siswa, Bisa menjadi tempat pencarian nama siswa, serta mengetahui data siswa yang dicari. Output dari sistem ini adalah :

1. Menampilkan data data siswa
2. Menampilkan siswa yang termuda dan tertua
3. Meminta *input* untuk mencari siswa tertentu sesuai dengan nama siswa yang dicari

# Project 07 - Kalkulator

**Fungsi:** Selayaknya kalkulator biasa, namun kalkulator ini mempunyai fitur *error handling*, sehingga apabila kode error sistem tidak akan berhenti saja, namun mmeberikan peringatan kepada *user*. Kelebihan dari sistem ini adalah :

1. Menghitung angka yang di berikan
2. Apabila operator yang di input tidak benar maka sistem akan memberi peringatan
3. Apabila *input* memberikan angka 0 dan memilih operator bagi *(ZeroDivisionError)* maka akan diperingatkan oleh sistem
4. Apabila *input* memberikan input kosong, huruf, dan lain lain kecuali huruf, maka sistem akan memperingatkan *(ValueError)*

# Project 08 - Sistem File Handling JSON

**Fungsi:** Menyusun produk yang ada dengan menggunakan metode *file handling*, dengan menggunakan metode ini kode lebih sedikit dan efisien untuk data yang banyak.

Membuat file JSON

```
with open("dataProduk.json", "w") as file :
  json.dump(dataProduk,file)
```

Membaca File JSON yang telah dibuat
```
with open("dataProduk.json", "r") as file :
  hasil = json.load(file)
```


*Repositori ini akan terus diperbarui seiring dengan perkembangan proses belajar saya*