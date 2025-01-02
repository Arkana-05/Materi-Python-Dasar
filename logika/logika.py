#TOKO SERBA ADA
harga = int(input("Masukkan Harga Barang: "))
jumlah = int(input("Masukkan jumlah beli: "))
totalbelanja = harga*jumlah
disc = totalbelanja*0.1
totalbayar = totalbelanja-disc
print("Total Harga = ",totalbelanja)
print("Total Diskon = ",disc)
print("Total Bayar setelah Diskon = ",totalbayar)
uangbyr = int(input("Masukkan Uang Bayar: "))
uangkembali = uangbyr-totalbayar
print("Terimakasih sudah berbalanja. Uang kembalian Anda adalah: ", uangkembali)

# -----------------------------------------------------------------------------------------------
#MAHASISWA  
nim = int(input("Masukkan NIM Anda"))
nama = input("Masukkan Nama Anda")
absen = int(input("Masukkan Nilai Absen"))
tugas = int(input("Masukkan Nilai tugas"))
uts = int(input("Masukkan Nilai uts"))
uas = int(input("Masukkan Nilai uas"))
totalnilai = (absen*0.2) + (tugas*0.25) + (uts*0.25) + (uas*0.3)

print("Total Nilai Mahasiswa", totalnilai)

# -----------------------------------------------------------------------------------------------
# nama = input("Silahkan masukkan nama Anda = ")
# nim = int(input("Silahkan masukkan NIM Anda = "))
# word = ("Termakasih sudah mengikuti aturan saya!")
# print(word, nama)    

# Membuat inputan string dan integer
nama = input("Masukkan Nama Mahasiswa: ")
nim = input("Masukkan NIM Mahasiswa: ")
# Membuat inputan integer
usia = int(input("Masukkan Usia Mahasiswa: "))
# memanggil data berupa string
print("Selamat datang " +str(nama)+ "!")
print("Ini adalah NIM Anda adalah:" +str(nim))
# memanggil data berupa integer
print("Dan ini adalah Usia Anda adalah: ", usia)


# -----------------------------------------------------------------------------------------------
print(list(range(1, 10))) #menampilkan list dari 1-10
print(list(range(3, 14))) #menampilkan list dari 3-14
print(list(range(2, 11, 3))) #menampilkan list dari 2-11 output di tambah 3 hingga hasil di output adalah 2, 5, 8
print(list(range(1,10,2))) #menampilkan bilangan ganjil

# -----------------------------------------------------------------------------------------------
# operator aritmatika
a = int(input("Masukkan bilangan pertama: "))
b = int(input("Masukkan bilangan kedua: "))
jumlah = a+b
kurang = a-b
kali = a*b
print("Hasil penjumlahan bilangan: ", jumlah)
print("Hasil pengurangan bilangan: ", kurang)
print("Hasil perkalian bilangan: ", kali)

# -----------------------------------------------------------------------------------------------
a = int(input("Masukkan bilangan pertama: "))
b = int(input("Masukkan bilangan kedua: "))
jumlah = a+b
kurang = a-b
kali = a*b
print("Hasil penjumlahan bilangan: ", jumlah)
print("Hasil pengurangan bilangan: ", kurang)
print("Hasil perkalian bilangan: ", kali)

# -----------------------------------------------------------------------------------------------

print("NIM : 19241186")
print("Nama : t Nuriyah")
print("------ Tugas Pertemuan 2 ------")

berat = int(input("Masukkan berat kg telur = "))
harga = int(input("Masukkan harga per kg telur = "))
print("Total  Belanja : ", berat*harga)
ongkos = int(input("Masukkan ongkos sekali naik = "))
uang = int(input("Masukkan jumlah uang = "))

total_harga_telur = berat * harga
total_keseluruhan = total_harga_telur + ongkos
hasil = uang - total_keseluruhan
print("Sisa uang belanja: " +str(hasil))

# -----------------------------------------------------------------------------------------------

# PERTEMUAN 3
aldi = int(input("Masukkan Jumlah Kelereng Aldi: "))
budi = aldi-15
anto = 2 * (aldi + budi)
agung = (aldi + budi + anto) - 5

print("Jumlah Kelereng Aldi: ", aldi)
print("Jumlah Kelereng Budi: ", budi)
print("Jumlah Kelereng Anto: ", anto)
print("Jumlah Kelereng Agung: ", agung)

# -----------------------------------------------------------------------------------------------

# TUGAS 3, MENENTUKAN BILANGAN TERBESAR
Bil1 = 60
Bil2 = 20
Bil3 = 100
Bil4 = 40

if Bil2 > Bil1:
    nilai_terbesar = Bil2
elif Bil3 > Bil2:
    nilai_terbesar = Bil3
elif Bil4 > Bil3:
    nilai_terbesar = Bil4

print("Bilangan terbesar adalah ", nilai_terbesar)


# -----------------------------------------------------------------------------------------------

# STUDI KASUS ELIF KODE BAJU
print("Program Pembelian Baju")
kode_baju = input("Masukkan Kode Baju [P/A/S] : ")

# CODE UNTUK MENENTUKAN MERK DAN HARGA
if (kode_baju == "P" or kode_baju == "p"):
    merk = "Polo"
    ukuran = input("Masukkan Ukuran Baju [S/M/L] : ")
    if ukuran == "S" or ukuran == "s" : 
        harga = 150000
    elif ukuran == "M" or ukuran == "m" : 
        harga = 250000
    elif ukuran == "L" or ukuran == "l" : 
        harga = 350000
    else:
        print("Salah Input Ukuran!")

elif (kode_baju == "A" or kode_baju == "a"):
    merk = "Alisan"
    ukuran = input("Masukkan Ukuran Baju [S/M/L] : ")
    if ukuran == "S" or ukuran == "s" : 
        harga = 175000
    elif ukuran == "M" or ukuran == "m" : 
        harga = 275000
    elif ukuran == "L" or ukuran == "l" : 
        harga = 375000
    else:
        print("Salah Input Ukuran!")

elif (kode_baju == "S" or kode_baju == "s"):
    merk = "Stlys"
    ukuran = input("Masukkan Ukuran Baju [S/M/L] : ")
    if ukuran == "S" or ukuran == "s" : 
        harga = 200000
    elif ukuran == "M" or ukuran == "m" : 
        harga = 300000
    elif ukuran == "L" or ukuran == "l" : 
        harga = 400000
    else:
        print("Salah Input Ukuran!")

else:
    merk = "Anda Salah Input Kode Baju"
    harga = 0

jumlah = int(input("Masukkan jumlah beli: "))
total_harga = harga * jumlah

if total_harga > 1000000:
    diskon = total_harga * 0.1
else:
    diskon = total_harga * 0.05

total = total_harga - diskon
    

print("-----------------------------------")
print("Merk Baju    : "+str(merk))
print("Ukuran Baju  : "+str(ukuran))
print("Harga Baju   : Rp.", harga)

print("Total Harga  : Rp.",total_harga)
print("Total Diskon : Rp.",diskon)
print("Total Bayar setelah Diskon : Rp.",total)

# -----------------------------------------------------------------------------------------------

# STUDI KASUS 5, PENGGAJIAN KARYAWAN
print("Program Penggajian Karyawan")
gaji_pokok = int(input("Masukkan Gaji Pokok Karyawan : "))
jam_kerja = int(input("Masukkan Jam Kerja Karyawan : "))

tunjangan = 0.2 * gaji_pokok
pajak =  0.1 * gaji_pokok

if jam_kerja > 200:
    honor_lembur = (jam_kerja - 200) * 20000
else:
    honor_lembur = 0

total = gaji_pokok + tunjangan + honor_lembur - pajak

print("----------------------------------------")
print("     PROGRAM HITUNG GAJI KARYAWAN")
print("----------------------------------------")
print("Honor yang diterima")
print(" Gaji Pokok              : Rp.",gaji_pokok)
print(" Tunjangan               : Rp.",tunjangan)
print(" Honor Lembur            : Rp.",honor_lembur)
print(" Pajak                   : Rp.",pajak)
print("----------------------------------------")
print(" Total Gaji Bersih       : Rp.",total)

# -----------------------------------------------------------------------------------------------

# STUDI KASUS 3
jam = int(input("Masukkan Lama Sewa : "))

if jam <= 3:
    harga = jam * 6000
elif jam > 3:
    harga = (3 * 6000) + (jam - 3) * 5000 
else:
    harga = 0

print("Harga yang harus di bayar : Rp.", harga)

# -----------------------------------------------------------------------------------------------

# STUDI KASUS 4, GAJI SALES
gaji_pokok = 5000000

produk = int(input("Masukkan Jumlah Produk yang Terjual : "))
harga = int(input("Masukkan Harga Produk : Rp."))

omset = produk * harga

if produk > 100:
    bonus = 0.2 * omset
else:
    bonus = 0.1 * omset

gaji = gaji_pokok + bonus

print("Gaji yang diterima : Rp.", gaji)
# -----------------------------------------------------------------------------------------------

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


# LATIHAN LOOPING
for i in range(5,55,5): #i adalah index
    print(i, end=" ")

print()
print("---------------------")

for i in range(100,1,-10): 
    print(i, end=" ")