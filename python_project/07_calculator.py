try :
 a = int(input("angka pertama"))
 b = int(input("angka kedua"))
 operator = input("Pilih (+,-,*,/) ")
  
 if operator == "+" :
    hasil = a+b 
 elif operator == "-":
    hasil = a-b
 elif operator == "*":
    hasil = a*b 
 elif operator == "/":
    hasil = a/b
 else :
   print("Operator tidak valid!")
   hasil = None
    
 if hasil is not None:
   print(hasil)

except ZeroDivisionError :
  print("Angka tidak boleh 0!")
except ValueError:
  print("harus angka valid!")
