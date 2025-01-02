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
