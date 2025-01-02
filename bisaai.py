# INTEGER
ini_variable = 250
print(ini_variable)
print('Tipe data variable ini = '+str(type(ini_variable)))

# FLOAT
ini_variable = 11.33
variable_int = int(ini_variable)
print(ini_variable)
print(variable_int)
print('Tipe data variable ini = '+str(type(ini_variable)))

# COMPLEX NUMBER
ini_variable = 1 + 4
print(ini_variable)
print('Tipe data variable ini = '+str(type(ini_variable)))

# STRING
s = 'String dengan kutip tunggal'
t =  "String dengan kutip ganda"
m = '''Ini merupakan string munti-lane 
kita coba untuk menulis tanda kutip '" 
ini baris ketiga dan tidak error'''
print(s)
print(t)
print(m)
print(s+' dan '+t)
print(s[3])
print(s[7:15])

# LIST
var_list = [3, 'test', 7.5, 'b', 1, 6, 4]
print(var_list[2])
print(var_list[-2]) #memanggil dengan indeks negatif
print(var_list[1:4])
print(var_list[:4])
print(var_list[-2:])
print(var_list[1:6:2])

# MENAMBAHKAN ELEMEN LIST
hewan = ['kucing', 'burung', 'kelinci', 'anjing']
warna = ['merah', 'kuning']
hewan.append(warna)
print(hewan)

# Pertama, dengan menggunakan method append, dengan menggunaan metode append, maka kita akan menambahkan elemen baru kedalam list pada urutan terakhir.

hewan2 = ['kucing', 'burung', 'kelinci']
warna = ['merah', 'kuning'] 
hewan2.extend(warna)
print(hewan2)

# Kedua, menggunakan method extend, dengan method ini, jika kita menambahkan elemen list berupa tipe data list juga, maka semua elemen list yang baru akan dijadikan satu dengan elemen list yang ada.

hewan3 = ['kucing', 'burung', 'kelinci']
print(hewan3)

hewan3.insert(0, 'kuda')
print(hewan3)
# =====
hewan4 = ['kucing', 'burung', 'kelinci']
print(hewan4)

hewan4[0] = 'anjing'
print(hewan4)
# Ketiga, dengan menggunakan method insert, dengan menggunakan method ini, kita dapat menentukan pada index ke berapa elemen baru yang akan kita tambahkan diletakkan dalam 


# MENGHAPUS ELEMEN LIST
# pertama, menggunakan del, menghapus elemen berdasarkan index
hewan = ['kucing', 'burung', 'kelinci']
print(hewan)

del hewan[2]
print(hewan)

# kedua, remove, menghapus elemen berdasarkan nama
hewan = ['kucing', 'burung', 'kelinci']
print(hewan)

hewan.remove('kelinci')
print(hewan)

# ketika, pop. Karena list merupakan tipe data yang bersifat mutable, maka kita dapat mengubah elemen dalam list, menambahkan ataupun menghapus elemen.
hewan = ['kucing', 'burung', 'kelinci']
print(hewan)

out = hewan.pop(0)
print(hewan)
print(out)

hewan = ['kucing', 'burung', 'kelinci']
angka = [1, 2, 3, 8]

# mengitung elemen pada banyaknya list
print(len(hewan))

# mengetahui index pada elemen tertentu
print(hewan.index('burung'))

# menghitung elemen 
print(angka.count(2))

# mengurutkan elemen
hewan.sort()
print(hewan)

# mengurutkan descending
hewan.sort(reverse=True)
print(hewan)

# menggabungkan operator
print(hewan+angka)

# mereplikasi 
print(angka*2)


# TUPLE
# Tuple dideklarasikan dengan tanda kurung () dan elemen didalamnya masih dipisahkan dengan koma.
var_tuple = ('a', 5, 's', 'r', 6)
print(type(var_tuple))
# proses slicing
print (var_tuple[2]) #memanggil dengan indeks 2
print (var_tuple[1:4])
print (var_tuple[:5])

# SET
# Set merupakan tipe data kumpulan elemen yang bersifat tidak terurut atau unordered collection. Karena merupakan tipe data yang tidak terurut, maka kita tidak bisa melakukan proses slicing. Set dideklarasikan dengan kurung kurawal {}, elemen dalam set dipisahkan dengan koma.
var_set = {1, 8, 2, 'a', 5, 4, 'b', 7, 4, 4, 4}
print(var_set)
print(type(var_set))

var_set1 = {1, 8, 2, 'a', 5, 4, 'b', 7, 4, 4, 4}
var_set2 = {1, 8, 2, 4, 4, 'a'}
print(var_set1.intersection(var_set2))
# mendeteksi kesamaan antar elemen yang akan muncul di output
print(var_set1.union(var_set2))
# mengurutkan 
print(var_set1.difference(var_set2))
# mendeteksi erbedaan antar kedua variable

var_set = {1, 8, 2, 4, 4}
print(var_set)

# hapus elemen set berdasarkan nama elemennya 
var_set.remove(2)
print(var_set)

# tambah elamen set
var_set.add(10)
print(var_set)

# DICTONARY
# Dictionary merupakan tipe data pada Python yang memiliki pasangan kunci dan nilai (key-value pairs). Untuk mengakses elemen pada dictionary, kita perlu mengetahui key pada elemen tersebut. Dictionary merupakan tipe data yang bersifat mutable, artinya elemen berupa value dalam dictionary dapat diubah tetapi key-nya tidak dapat diubah, karena key bersifat unik. Selain unik, key pada dictionary dapat menggunakan tipe data yang bervariasi untuk mengubah key terdapat beberapa pendekatan khusus. Dictionary dideklarasikan dengan tanda kurung kurawal {} dengan elemen pasangan key dan value-nya dipisahkan dengan koma. Pemisah antara key dan value menggunakan titik dua (key : value). 
var_set = {1, 8, 2, 4, 4}
print(var_set)

# hapus elemen set berdasarkan nama elemennya 
var_set.remove(2)
print(var_set)

# tambah elamen set
var_set.add(10)
print(var_set)


# KONVERSI
var_int = 3
var_float = 3.4
var_string = '-10'
# konverai int to float
print(float(var_int))
print(int(var_float))
print(type(str(var_float)))
print(int(var_string))
# =============================
var_list  = [1, 2, 3, 4, 5, 6]
var_tuple  = (1, 2, 4, 3, 5, 6)
var_set  = {9, 2, 4, 3, 5, 6}

print(tuple(var_list))
print(set(var_list))
print(list(var_tuple))
print(set(var_tuple))
print(list(var_set))
print(tuple(var_set))


# IF ELSE
# IF
kondisi = True
if kondisi:
    print('Statement yang dieksekusi jika kondisi terpenuhi')

# contoh kasus
nilai = 80
if nilai >= 80:
    print('Lulus')

# ELSE
nilai = 80 
if nilai > 80:
    print('Lulus')
else: 
    print('Tidak lulus')

# ELIF
nilai = 60

if nilai >= 50 and nilai < 60:
    print('Grade D')
elif nilai >= 60 and nilai < 70:
    print('Grade C')
elif nilai >= 70 and nilai < 80:
    print('Grade B')
elif nilai >= 80 and nilai <= 100:
    print('Grade A')
else :
    print('Tidak Lulus')

# NESTED IF ELSE
jumlah_kaki = 4
suara = 'meong'
kategori = 'mamalia'

if jumlah_kaki == 4 :
    print('Kemungkinan kucing = 25%')
    print('Kemungkinan buaya = 25%')
    print('Kemungkinan anjing = 25%')
    print('========================= Kondisi Pertama ===========================')

    if kategori == 'mamalia':
        print('Kemungkinan kucing = 75%')
        print('Kemungkinan anjing = 75%')
        print('========================= Kondisi Kedua ===========================')

        if suara == 'meong':
            print('Kemungkinan Kucing = 100%')

# FOR LOOP
for i in range(0, 10):
    print("angka yang ke " + str(i))
# contohlain
array = ['mobil', 'motor', 'kereta']
for i in array:
    print(i)

# WHILE LOPOP
i = 1
while i < 10:
    print(i)
    i += 1

number = 7
while number > 0:
    print(number)
    number = number - 1

for x in range(5):
    if x == "2":
        continue
    print(x)


# DEF
def halaman_utama():
    print("Hello World")

halaman_utama()

# ARGUMENT IN FUNCTION
def calculator_tambah(angka1, angka2):
    hasil = angka1 + angka2
    print(hasil)

calculator_tambah(10, 20)

# RETURN VALUE IN FUNCTION
def calculator_tambah(angka1, angka2):
    hasil = angka1 + angka2
    return hasil

nomor = calculator_tambah(10, 20)
print(nomor)

def perhitungan_nilai(angka):
    if angka > 0 and angka <= 50:
        print("D")
    elif angka > 50 and angka <= 70:
        print("C")
    elif angka > 70 and angka <= 85:
        print("B")
    elif angka > 85 and angka <= 100:
        print("A")
    else:
        print("Nilai tidak valid")

perhitungan_nilai(0.1)

def identitas(name, age=20):
    print(name, age)
identitas('Agus', 25)

import re
txt = "Belajar Bahasa ppemrogramamn Python"
x = re.split("\s", txt)
print(x)


def factorial(n):
    if n == 0:
        return 1
    else:
        return(n * factorial(n - 1))
    
n = int(input("Masukkan bilangan: "))
hasil = factorial(n)
print(f"Faktorial dari {n} adalah {hasil}")

n = int(input("Masukkan bilangan: "))

def faktor_bilangan(n):
    faktor = []
    for i in range(1, n + 1):
        if n % i == 0:
            faktor.append(i)
    return faktor
    
hasil = faktor_bilangan(n)
print("Faktor bilangan dari " + str(n) + " adalah", hasil)





# KALKULATOR
def kalkulator():
    print("Pilih operasi matematika:")
    print("1. Penjumlahan (+)")
    print("2. Pengurangan (-)")
    print("3. Perkalian (*)")
    print("4. Pembagian (/)")

    # Meminta input operasi dari pengguna
    operasi = input("Masukkan pilihan (1/2/3/4): ")

    # Meminta input dua angka dari pengguna
    try:
        angka1 = float(input("Masukkan angka pertama: "))
        angka2 = float(input("Masukkan angka kedua: "))
    except ValueError:
        print("Input tidak valid! Masukkan angka yang benar.")
        return

    # Melakukan operasi yang dipilih
    if operasi == '1':
        hasil = angka1 + angka2
        print(f"Hasil: {angka1} + {angka2} = {hasil}")
    elif operasi == '2':
        hasil = angka1 - angka2
        print(f"Hasil: {angka1} - {angka2} = {hasil}")
    elif operasi == '3':
        hasil = angka1 * angka2
        print(f"Hasil: {angka1} * {angka2} = {hasil}")
    elif operasi == '4':
        if angka2 != 0:
            hasil = angka1 / angka2
            print(f"Hasil: {angka1} / {angka2} = {hasil}")
        else:
            print("Kesalahan! Tidak dapat membagi dengan nol.")
    else:
        print("Pilihan operasi tidak valid!")

# Menjalankan fungsi kalkulator
kalkulator()
