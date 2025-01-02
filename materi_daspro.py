# PERTEMUAN PERTAMA
print("Hello World!!")
print("Hari Pertama Saya Belajar Python")
print("Semoga Hari ini Menyenangkan")

a = 10
if a > 6:
    print("Anda Lulus!")
else:
    print("Anda tidak lulus")

# LATIHAN 1 DI PERTEMUAN PERTAMA
print("=============================")
print("Nama : Arka Nuriyah")
print("Kelas : 19.1B.13")
print("NIM : 19241186")
print("Jurusan : Sistem Informasi")
print("=============================")


# PERTEMUAN KEDUA
# TANDA KUTIP DI PYTHON
kata = 'Kuliah'
kalimat = "BSI Aja!"
paragraf = """
==============
Kuliah..?
BSI Aja!
==============
"""
print(kata)
print(kalimat)
print(paragraf)

# LATIHAN 2 PERTEMUAN KEDUA
# INPUT 
print("=+=+=+=+ Data Diri Mahasiswa =+=+=+=+")
nim = input("NIM : ")
nama = input("Nama Lengkap : ")
jurusan = input("Jurusan : ")
kelas = input("Kelas : ")
alamat = input("Alamat : ")

print("===============================")
print("Hasil cetak data diatas adalah")
print("===============================")
print("Nim : " +str(nim))
print("Nama : " +str(nama))
print("Jurusan : " +str(jurusan))
print("Kelas : " +str(kelas))
print("Alamat : " +str(alamat))

# CONTOH CARA MEGHITUNG USIA DI PYTHON
# perintah input
print("=== APLIKASI MENGHITUNG USIA ===")
tahun_sekarang = 2024
tahun_lahir = int(input("Masukkan Tahun Lahir: "))

# perintah proses
usia = tahun_sekarang - tahun_lahir
print("==============================")
print("Usia Anda saat ini adalah " +str(usia)+ " Tahun")


# PERTEMUAN KE 3
var1 = 'Hello Python'
var2 = "Programming with Python"
print(var1)
print(var2)

# AKSES NILAI STRING
var1 = 'Hello Python'
var2 = "I Love Python"
print("var1[0]", var1[0])
print("var2[2:6]", var2[2:6])

# UPDATE STRING
var1 = 'Hello Python'
var2 = var1[:6]
print(var1)
print("Sring Update: - ", var1[:6] + 'World')

# MENGGABUNGKAN STRING
str1 =  'Hello'
str2 =  'Python'
# menggunakan +
print('str1 + str2', str1 + str2)
# menggunakan *
print('str1 * 3', str1 * 3)

# LEN STRING (MENGETAHUI PANJANG)
string = 'I Love Python'
print(len(string))

# KARAKTER ESCAPE
# menggunakan kutip 3
print('''He Said, "What's there?"''')
# menggunakan kutip tunggal
print('He Said, "What\'s there?"')
# menggunakan kutip ganda
print("He Said, \"What's there?\"")

print("Ini adalah baris pertama\nDan ini adalah baris kedua")
print("Ini adalah \x48\x45\x58")
# RAW STRING MENGABAIKAN ESCAPE
print("This is \x61 \ngood example")
print(r"This is \x61 \ngood example")

# MENGGUNAKAN POSISI DEFAULT
default_order = "{}, {} dan {}".format("Budi", "Galih", "Ratna")
print('\n--- Urutan default ---')
print(default_order)

# MENGGUNAKAN ARGUMENT POSISI
PERSONAL_order = "{1}, {0} dan {2}".format("Budi", "Galih", "Ratna")
print('\n--- Urutan default ---')
print(PERSONAL_order)

# FORMAT INTEGER
print("{0} bila diubah jadi biner menjadi {0:b}".format(12))
# FORMAT FLOAT
print("Fromat eksponensial: {0:e}".format(1566.345))
# PEMBULATAN
print("Sepertiga sama dengan: {0:.3f}".format(1/3))
# MERATAKAN STRING
print("|{:<10}|{:^10}|{:>10}".format('beras', 'gula', 'garam'))

x = 12.3456789
print('Nillai x = %3.2f' %x)
print('Nillai x = %3.4f' %x)

# FUNGSI BAWAAN PYTHON
print("Universitas Bina Sarana Informatika".lower())
print("Universitas Bina Sarana Informatika".upper())
print("I Love Programming in Python".split())
print("I Love Python".startswith("I"))
print("Saya Belajar Python".endswith("on"))
print(' - '.join(['I', 'Love', 'You']))
print("Belajar Java di BSI".replace('Java', 'Python'))

# JENIS BILANGAN
print(int(2.5))
print(int(3.8))
print(float(5))

# STUDI KASUS ELIF BAJU
kode_baju = input("Masukkan Kode Baju [SP/AD] : ")
ukuran_baju = input("Masukkan Ukuran Baju [S/M] : ")

if kode_baju == "SP" or kode_baju == "sp" :
    merk = "SuperDry"
    if ukuran_baju == "S" or ukuran_baju == "s" : 
        harga = 450000
    elif ukuran_baju == "M" or ukuran_baju == "m" : 
        harga = 500000
    else:
        harga = 0
elif kode_baju == "AD" or kode_baju == "ad" :
    merk = "Adidas"
    if ukuran_baju == "S" or ukuran_baju == "s" : 
        harga = 650000
    elif ukuran_baju == "M" or ukuran_baju == "m" : 
        harga = 700000
    else:
        harga = 0

else:
    merk = "Anda Salah Input Kode Merk"
    harga = 0

print("-----------------------------------")
print("Merk Baju    : "+str(merk))
print("Harga Baju   : Rp.", harga)


# STUDI KASUS PENJUALAN TIKET 
nama_pembeli = input("Input Nama Pembeli    : ")
no_hand = input("Input No. Handphone        : ")
jurusan = input("Input Jurusan [SBY/BL/LMP] : ")
jumlah_beli = int(input("Masukkan Jumlah Beli   : "))

# PROSES FILTER JURUSAN
if jurusan == "SBY" or jurusan == "sby" or jurusan == "surabaya" :
    nama_kota = "Surabaya"
    harga = 300000
elif jurusan == "BL" or jurusan == "bl" or jurusan == "bali"  :
    nama_kota = "Bali"
    harga = 350000
elif jurusan == "LMP" or jurusan == "lmp" or jurusan == "lampung"  :
    nama_kota = "Lampung"
    harga = 500000

else:
    nama_kota = "Anda Salah Memasukkan Nama Jurusan"
    harga = 0

# PROSES POTONGAN
if jumlah_beli >= 3 :
    potongan = (jumlah_beli*harga)*0.1
else:
    potongan = 0

total = (jumlah_beli*harga)-potongan

print("----------------------------------------")
print("         PENJUALAN TIKET BUS")
print("                XX")
print("----------------------------------------")
print("Nama Pembeli     : "+str(nama_pembeli))
print("No. Handphone    : "+str(no_hand))
print("Kode Jurusan     : "+str(jurusan))
print("Nama Kota Tujuan : "+str(nama_kota))
print("Harga Tiket      : ", harga)
print("Jumlah Beli      : ", jumlah_beli)
print("----------------------------------------")
print("Potongan         : ", potongan)
print("Total Bayar      : ", total)

uang_bayar = int(input("Masukkan Uang Bayar : "))
uang_kembali = uang_bayar-total

print("Uang Kembali     : ", uang_kembali)


# LATIHAN PERTEMUAN 4
# STUDI KASUS PENDAFTARAN MAHASISWA BARU

nis_mahasiswa = input("Masukkan NIS Calon Mahasiswa : ")
nama_mahasiswa = input("Masukkan Nama Calon Mahasiswa : ")
jurusan = input("Masukkan Jurusan yang di tuju [SI/SIA] : ")

if jurusan == "SI" or jurusan == "si" or jurusan == "sistem informasi":
    nama_prodi = "Sistem Informasi"
    harga = 2400000
elif jurusan == "SIA" or jurusan == "sia" or jurusan == "sistem informasi akuntansi" :
    nama_prodi = "Sistem Informasi Akuntansi"
    harga = 2000000
else:
    nama_prodi = "Jurusan yang Anda masukkan salah"
    harga = 0

print("----------------------------------------")
print("     PENDAFTARAN MAHASISWA BARU")
print("----------------------------------------")
print("NIS Calon Mahasiswa    : "+str(nama_mahasiswa))
print("Nama Calon Mahasiswa   : "+str(nis_mahasiswa))
print("Kode Jurusan           : "+str(jurusan))
print("Nama Prodi Jurusan     : "+str(nama_prodi))
print("Biaya Kuliah           : ", harga)
print("----------------------------------------")


# TUGAS 1
# STUDI KASUS PROGRAM HITUNG GAJI KARYAWAN

gaji_pokok = 300000

nama_karyawan = input("Nama Karyawan : ") 
golongan = input(" Golongan Jabatan [1/2/3] : ") 
pendidikan = input(" Pendidikan [SMA/D1/D3/S1] : ") 
jam_kerja = int(input(" Jumlah Jam Kerja : ") )

# PROSES FILTER GOLONGAN JABATAN 
if golongan == "1":
    tunjangan_jabatan = 0.05*gaji_pokok
elif golongan == "2":
    tunjangan_jabatan = 0.1*gaji_pokok
elif golongan == "3":
    tunjangan_jabatan = 0.15*gaji_pokok
else:
    tunjangan_jabatan = 0


# PROSES FILTER PENDIDIKAN
if pendidikan == "SMA" or pendidikan == "sma":
    tunjangan_pendidikan = 0.025*gaji_pokok
elif pendidikan == "D1" or pendidikan == "d1":
    tunjangan_pendidikan = 0.05*gaji_pokok
elif pendidikan == "D3" or pendidikan == "d3":
    tunjangan_pendidikan = 0.2*gaji_pokok
elif pendidikan == "S1" or pendidikan == "s1":
    tunjangan_pendidikan = 0.3*gaji_pokok
else:
    tunjangan_pendidikan = 0


# PROSES FILTER JAM LEMBUR 
jam_kerja_normal = 8
honor_perjam = 3500

if jam_kerja > jam_kerja_normal :
    jam_lembur = jam_kerja - jam_kerja_normal 
    honor_lembur = jam_lembur*honor_perjam
else:
    tambahan = 0

tunjangan = tunjangan_jabatan + tunjangan_pendidikan
total = (gaji_pokok+tunjangan+honor_lembur)

# OUTPUT
print("----------------------------------------")
print("     PROGRAM HITUNG GAJI KARYAWAN")
print("----------------------------------------")
print("Karyawan yang bernama    : "+str(nama_karyawan))
print("Honor yang diterima      : ", gaji_pokok)
print(" Tunjangan Jabatan       : ", tunjangan_jabatan)
print(" Tunjangan Pendidikan    : ", tunjangan_pendidikan)
print(" Honor Lembur            : ", honor_lembur)
print(" Total Gaji              : ", total)
print("----------------------------------------")


# ==================================================================
# Program untuk menemukan jumlah bilangan dalam satu list
# List number
numbers = [7, 5, 9, 8, 9, 0, 8, 4, 0]
# variable untukmenyimpan jumlah

sum = 0

# iterasi
for each in numbers:
    sum = sum + each

print("Jumla semuanya: ", sum)

# ------------- FOR
# Program untuk iterasi list mmenggunakan pengindeksan
mapel = ['Matematika', 'Fisika', 'Kimia']

# iterasi list menggunakan indeks
for i in range(len(mapel)):
    print("Saya suka", mapel[i])

# ------------- WHILE
count = 0
while (count < 5):
    print('The count is:', count)
    count = count + 1
print('Good bye!')

# -------------- BREAK
# contoh penggunaan statement break
for letter in "PythohnProgramming":
    if letter == 'g':
        break
    print("Huruf sekarang:", letter)
print("Good bye!")

# -------------- WHILE ELSE
count = 0
while (count < 8):
    print(count, "Kurang dari 8")
    count = count + 1
else:
    print(count, "Tidak kurang dari 8")

# -------------- LATIHAN PERULANGAN
ulang = 2
for i in range(ulang):
    print("Data ke - " + str(i+1))
    nim = input("Masukkan NIM Anda: ")
    nama = input("Masukkan Nama Anda: ")
    uts = int(input("Masukkan Nilai UTS Anda: "))
    uas = int(input("Masukkan Nilai UAS Anda: "))
    print("Nim Anda adalah %s, Nama Anda adalah %s, Nilai UTS Anda adalah %i, Nilai UAS Anda adalah %i" % (nim, nama, uts, uas))
    print("============================\n")



# MENGHITUNG JUMLAH BILANNGAN GANJIL DARI 1 - 100
total = 0
for i in range(1, 101, 2):
    total += i
print("Jumlah bilangan ganjil dari 1 hingga 100 adalah: ", total)

# MENCARI KARAKTER
vowels = "aiueo"
for char in "universitas":
    if char in vowels:
        print(char)


# ==================================================================
# PERTEMUAN 6 (LIST & TUPLE)
my_list = ["I", "love", "python", "programming", 2017]
#output: I
my_list[0]
#output: python
my_list[2]

#list dlam list
your_list = ["Hello", [1, 2, 3], "python"]

#output 1
print(your_list[1][0])
#output 3
print(your_list[1][2])

# indexError
my_list[6]

# ----------------
#LIST INDEX NEGATIF
my_list = ['p', 'y', 't', 'h', 'o', 'n']

# output n
print(my_list[-1])
# output h
print(my_list[-3])

my_list = ['p', 'y', 't', 'h', 'o', 'n', 'i', 'n', 'd', 'o']

# anggota list dari 3 s/d 5 (dari h s/d n)
print(my_list[3:6])
# anggota list dari 4 s/d yang terakhir
print(my_list[4:])
# anggota list dari 0 s/d 4
print(my_list[:5])
# indeks dari belakang dari -1 s/d -4
print(my_list[-1:-5])

# ------------
# MENGUBAH ANGGOTA LIST
# MISAL ADAL NILAI YANG SALAH 
ganjil = [1, 3, 4, 7, 9]

# ubah item ke 3 (indeks ke 2)
ganjil[2] = 5
print(ganjil)

#mengubah sekali banyak
ganjil[2:5] = [11, 13, 15]
print(ganjil) 

# -----------------
# MENAMBAHKAN ANGGOTA LIST
ganjil = [1, 3, 5, 7]
# code untuk menambahkan angka 9 pada list
ganjil.append(9)
print(ganjil)
# code untuk menambahkan angka 11, 13, 15 pada list
ganjil.extend([11, 13, 15])
print(ganjil)

# menambahkan list menggunakan operator
genap = [2, 4, 6]
print(genap + [8, 10, 12])
print(['p', 'y'] * 2)

# ------------
# MENYISIPKAN ANGGOTA LIST
ganjil = [5, 7, 11, 13, 15]
# code untuk menyisipkan angka 9 setelah 7
ganjil.insert(2, 9)
print(ganjil)

# ---------------
# MENGHAPUS ANGGOTA LIST
my_list = ['p', 'y', 't', 'h', 'o', 'n', 'i', 'n', 'd', 'o']
my_list.remove('p')

# output ['y', 't', 'h', 'o', 'n', 'i', 'n', 'd', 'o']
print(my_list)

my_list.remove('n')
# remove hanya menghapus elemen pertama yang dijumpai

# output 'y'
print(my_list.pop(1))

del my_list[2]
print(my_list)

my_list.clear()
#output []
print(my_list)

# ----------------
# MENGURUTKAN ANGGOTA LIST
# Pada saat kita perlu mengurutkan atau menyortir anggota list, kita bisa menggunakan metode sort(). Untuk membalik dengan urutan sebaliknya bisa dengan menggunakan argumen reverse=True.
alfabet = ['a', 'b', 'd', 'f', 'e', 'c', 'h', 'g', 'j', 'i']
alfabet.sort()
print(alfabet)

alfabet.sort(reverse=True)
print(alfabet)

# --------------
# MEMBALIK URUTAN LIST
alfabet = ['a', 'c', 'd', 'e', 'b']
alfabet.reverse()
print(alfabet)

# ----------------
# TUPLE
# membuat tuple kosong
my_tuple = ()
print(my_tuple)

# tuple dengan 1 elemen
# output : (1)
my_tuple = (1,)
print(my_tuple)

# tuple berisi integer
my_tuple = (1, 2, 3)
print(my_tuple)

# tuple bersarang
my_tuple = ("hello", [1, 2, 3], (4, 5, 6))
print(my_tuple)

# tuple bisa tidakmenggunakan tanda ()
my_tuple = 1, 2, 3

# memasukkan anggta tuple ke variabel yang bersesuaian
# a akan berisi 1, b berisi 2, dan c berisi 3
a, b, c = my_tuple
print(a, b, c)

#--------------
# MENGAKSES ANGGOTA TUPLE
my_tuple = ('p', 'r', 'o', 'g', 'r', 'a', 'm', 'm', 'i', 'n', 'g')
# akses dari indeks 0 s/d 2
print(my_tuple[:3])
# akses dari indeks 2 s/d 5
print(my_tuple[2:6])
# akses dari indeks 3 sampai akhir
print(my_tuple[3:])

# ----------
# MENGUBAH ANGGOTA TUPLE 
my_tuple = (2, 3, 4, [5, 6])
# kita tdak bisa mengubah anggota tuple
# bila kita hilangkan tanda komentar # pada baris ke 6
# akan muncul error: # TypeError: 'tuple' object does

# my_tuple[1] = 8

# tapi list di dalam tuple bsa di ubah
my_tuple[3][0] = 7
print(my_tuple)

# tuple bisa dianti secara keseluruhan dengan penugasan kembali
my_tuple = ('p', 'y', 't', 'h', 'o', 'n')
print(my_tuple)

# anggta tuple juga tidak bisa dihapus menggunakan del, perintah berikut aka menghasilkan error kalo anda menghilangkan tanda komentar

# del my_tuple[0]

# kita bisa menghapus tuple keseluruhan

del my_tuple

# ---------------
# MENGUJI KEANGGOTAAN TUPLE
my_tuple = (1, 2, 3, 'a', 'b', 'c')

# menggunakan in, output else
print('3' in my_tuple)
print('e' in my_tuple)
print('k' not in my_tuple)

# ---------------
# ITERASI PADA TUPLE
nama = ('Galih', 'Ratna')
for name in nama:
    print('Hi', name)


# ------------
# METODE DAN FUNGSI BAWAAN TUPLE
my_tuple = ('p', 'y', 't', 'o', 'n', 'i', 'n', 'd', 'o')
print(my_tuple.count('n'))

print(my_tuple.index('n'))

#====================================
# PERTEMUAN 7 MATRIKS & PANDAS
# MATRIKS DENGAN UKURAN 2X2
matriksA = [[1,0], [0,1]]
print(matriksA)
# MATRIKS DENGAN UKURAN 3X3
matriksB = [[1,0,1], [0,1,0], [1,0,1]]
print(matriksB)
# MATRIKS DENGAN UKURAN 4x4
matriksC = [[1,0,1,0], [0,1,0,1], [1,0,1,0], [0,1,0,1]]
print(matriksC)

matrix = [
    [5, 0],
    [2, 6]
]

matrix1 = [
    [5, 0, 8],
    [2, 6, 7],
    [1, 3, 4]
]

matrix2 = [
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1]
]


# PENJUMLAHAN MATRIKS
mat1 = [
    [9, 0],
    [3, 6]
]

mat2 = [
    [6, 0],
    [7, 2]
]

for x in range(0, len(mat1[0])):
    for y in range(0, len(mat1[0])):
        print(mat1[x][y] + mat2[x][y], end=' '),
        # JIKA INGIN MELAKUKAN PENGURANGAN / OPERASI ARITMATIKA LAINNYA, KALIAN HANYA TINGGAL MENGGANTI OPERATOR - + DLL MENJADI OPERATOR YANG DI INGINKAN
        # HANYA BERLAKU UNTUK  + -
    print


# MATRIK PERKALIAN
mat1 = [
    [9, 0],
    [3, 6]
]

mat2 = [
    [6, 0],
    [7, 2]
]

mat3 = []

for x in range(0, len(mat1)):
    row = []
    for y in range(0, len(mat1[0])):
        total = 0
        for z in range(0, len(mat1)):
            total = total + (mat1[x][z] * mat2[z][y])
        row.append(total)
    mat3.append(row)

for x in range(0, len(mat3)):
    for y in range(0, len(mat3[0])):
        print(mat3[x][y], end=' '),
    print()


# warna = ('Merah', 'Hijau', 'Biru')
# for warna in warna:
#     print('Balon ini memiliki warna ', warna)

matriks = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

baris  = len(matriks)
kolom  = len(matriks[0])
print("Dimensi Matriks:", baris, "x", kolom)



# ----------------------------------------------------
# def hitung_luas(panjang, lebar):
#     luas = 2 * (panjang + lebar)
#     return luas

# # contoh penggunaan
# panjang = 10
# lebar = 5
# luas = hitung_luas(panjang, lebar)
# print(f"Keliling persegi panjang dengan panjang {panjang} dan lebar {lebar}, dengan keliling adalah adalah {luas}")

# def konversi(suhu_celcius):
#     """Mengonvrsi suhu dari celcius ke Fahrenheit"""
#     suhu_fan = (suhu_celcius * 9/5) + 32
#     return suhu_fan

# suhu_celcius = 25
# suhu_fan = konversi(suhu_celcius)
# print(f"{suhu_celcius}℃ sama dengan {suhu_fan}℉")

# a = 10 #variable lobal
# def hitung():
#     b = 5 #variable lokal
#     hasil = a + b #mengakses var globaal a dan var lokal b 
#     print(hasil)

# print(f"Hasil penjumlahan adalah ")
# hitung()