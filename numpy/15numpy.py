import numpy as np

#dtype = Data Types

array = np.array([1, 2, 3, 4, 5])

print(array)
print(array.dtype) #int64
print(f"{array.nbytes} bytes") #--> 8 bits = 1 byte (40 bytes)

# Mengubah Data Types

# Angka
array = np.array([1, 2, 3, 4, 5], dtype=np.int32)

print(array)
print(array.dtype) #int32
print(f"{array.nbytes} bytes") #20 bytes

#Huruf / String / Boolean / Object (Harus menggunakan Underscore agar dihitung dtype Numpy)

#String
array = np.array(["apple", "orange", "banana"], dtype=np.str_)

print(array)
print(array.dtype) #<U6 mengambil huruf terbanyak
print(f"{array.nbytes} bytes") # 72 bytes

#Manipulation dtype String
array = np.array(["apple", "orange", "banana"], dtype="<U4")

print(array)
print(array.dtype) #<U4 akan terpotong karena kita ambil 4 huruf saja
print(f"{array.nbytes} bytes") # 48 bytes

#Boolean 
array = np.array([0, 1, 0, 1, 1], dtype=np.bool_)

print(array)
print(array.dtype) #bool = 0 adalah False, 1 adalah True
print(f"{array.nbytes} bytes") # 5 bytes

#  Object = Untuk mencampur campur semua data types

array = np.array([1,"apple", "orange", "banana", False, 0, 10], dtype=np.object_)

print(array)
print(array.dtype) # object
print(f"{array.nbytes} bytes") # 56 bytes

# Mengubah dtype menggunakan astype()
array = np.array([1.1, 2.2, 3.3, 4.4, 5.5]) #float

#Mengubah float menjadi int16
array = array.astype(np.int16)

print(array)
print(array.dtype) #int16 
print(f"{array.nbytes} bytes") # 10 bytes

#==================================================================

# Multidimensional arrays

# 0 Dimensi
array = np.array("A")

print(array.ndim) #ndim = Number of Dimension (0)

# 1 Dimensi
array = np.array(["A", "B", "C"])

print(array.ndim) # 1

#2 Dimensi / Matriks
array = np.array([["A", "B", "C"],
                  ["D", "E", "F"],
                  ["G", "H", "I"]])

print(array.ndim) #2

# 3 Dimensi

array = np.array([[["A", "B", "C"],["D", "E", "F"],["G", "H", "I"]],
                  [["J", "K", "L"],["M", "N", "O"],["P", "Q", "R"]],
                  [["S", "T", "U"],["V", "W", "X"],["Y", "Z", " "]]])

print(array.ndim) #3

print(array.shape) #(3, 3, 3) = (Lapisan, Baris, Kolom)

# Multidimensional Indexing = index mulai dari 0

print(array[0, 0, 0]) # A

# Membuat sebuah kata

kata = array[0, 2, 1] + array[0, 0, 0] + array[0, 2, 2] # HAI

print(kata)

#=================================================
# reshape

# 2 dimensi
array = np.array([1,2,3,4,5,6,7,8,9,10,11,12])

array = array.reshape(4, 3) # 4 baris, 3 kolom = 12

print(array)

# 3 dimensi
array = np.array([1,2,3,4,5,6,7,8,9,10,11,12])

array = array.reshape(3, 2, 2) # 3 layer, 2 baris, 2 kolom = 12

print(array)

# -1 = Hitung Otomatis (hanya boleh 1)

array = np.array([1,2,3,4,5,6,7,8,9,10,11,12])

array = array.reshape(-1, 2, 2) # hitung otomatis layer, 2 baris, 2 kolom = 12

print(array)











