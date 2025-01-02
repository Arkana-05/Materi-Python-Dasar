# LATIHAN PERTEMUAN KETIGA
# OPERATOR AND BITWISE (&)
a = 5 #0101 dalam biner
b = 3 #0011 dalam biner
hasil_and = a & b
print("Hasil Operator AND Bitwise = ", hasil_and)

# OPERATOR AND BITWISE (|)
a = 5 #0101 dalam biner
b = 3 #0011 dalam biner
hasil_or = a | b
print("Hasil Operator OR Bitwise = ", hasil_or)

# OPERATOR XOR BITWISE (|)
a = 5 #0101 dalam biner
b = 3 #0011 dalam biner
hasil_xor = a ^ b
print("Hasil Operator XOR Bitwise = ", hasil_xor)

# OPERATOR NOT BITWISE (|)
a = 5 #0101 dalam biner
hasil_not = ~a
print("Hasil Operator NOT Bitwise = ", hasil_not)

print("------------------------------ BIANGAN BINER------------------------------")
# Bilangan biner yang akan dikonversi
bilangan_biner = "1010"

# Konversi bilangan biner kedesimal
bilangan_desimal = int(bilangan_biner, 2)

# Cetak hasil konversi
print("Bilangan Biner", bilangan_biner, "Setara dengan Desimal", bilangan_desimal)

print("------------------------------OPERATOR KEANGGOTAAN------------------------------")
# Operator in
angka = [1, 2, 3, 4, 5]
hasil_in = 3 in angka 
print("Hasil Operator In = ", hasil_in)

# Operator not in
buah = ['apel', 'mangga', 'pisang']
hasil_notin = "jeruk" not in buah 
print("Hasil Operator Not In = ", hasil_notin)

print("------------------------------OPERATOR IDENTITAS------------------------------")
# Operator is
a = [1, 2, 3]
b = a
hasil_is = a is b
print("Hasil Operator Is = ", hasil_is)

# Operator is not
x = [1, 2, 3]
y = [1, 2, 3]
hasil_isnot =   x is not y
print("Hasil Operator Is Not = ", hasil_isnot)

print("Pesan Pertama")
print("\a") #akan menghasilkan bunyi "bell" atau notifikasi audio
print("Pesan kedua setelah bunyi")