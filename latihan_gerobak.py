# TAMPILAN MENU 
print("   GEROBAK FRIED CHICKEN  ")
print("--------------------------")
print("Kode JenisPotong Harga")
print("--------------------------")
print("D     Dada       Rp. 2500")
print("P     Paha       Rp. 2000")
print("S     Sayap      Rp. 1500")
print("--------------------------")

banyak_jenis = int(input("Banyak Jenis : "))
# LIST UNTUK MENYIMPAN INFORMASI
kode_potong = []
banyak_potong = []
jenis_potong = []
harga = []
jumlah = []

# LOOPING
for i in range(banyak_jenis):
    print("Jenis Ke - " + str(i+1))
    kode_potong.append(input("Kode Potong [D/P/S]: "))
    # APPEND UNTUK MENYIMPAN INFORMASI KE DALAM [] YANG BERADA DI ATAS 
    banyak_potong.append(int(input("Banyak Potong: ")))

    # IF ELSE JENIS & HARGA
    if kode_potong[i] == "D" or kode_potong[i] == "d":
        jenis_potong.append("Dada")
        harga.append("2500")
        jumlah.append(banyak_potong[i]*int("2500"))
    elif kode_potong[i] == "P" or kode_potong[i] == "p":
        jenis_potong.append("Paha")
        harga.append("2000")
        jumlah.append(banyak_potong[i]*int("2000"))
    elif kode_potong[i] == "S" or kode_potong[i] == "s":
        jenis_potong.append("Sayap")
        harga.append("1500")
        jumlah.append(banyak_potong[i]*int("1500"))
    else:
        jenis_potong.append("Kode Salah")
        harga.append("0")
        jumlah.append(banyak_potong[i]*int("0"))     

print()
print("            GEROBAK FRIED CHICKEN  ")
print("----------------------------------------------")
print("No   Jenis     Harga        Banyak    Jumlah")
print("     Potong    Satuan       Beli      Harga ")
print("----------------------------------------------")

# PERULANGAN DETAIL PESANAN 
jumlah_bayar = 0

for i in range(banyak_jenis):
    print("%i.    %s    Rp.%s        %i      Rp.%i" % (i+1,jenis_potong[i], harga[i], banyak_potong[i], jumlah[i]))
    jumlah_bayar = jumlah_bayar + jumlah[i] # MENAMPILKAN JUMLAH BAYAR BERDASARKAN INFORMASI YANG DI SIMPAN DI DALAM []

pajak = jumlah_bayar * 0.1 
total_bayar = jumlah_bayar + pajak
print("----------------------------------------------")
print("Jumlah Bayar Rp. ", jumlah_bayar)
print("Pajak 10 %   Rp. ", pajak)
print("Total Bayar  Rp. ", total_bayar)



# print("GEROBAK FRIED CHICKEN")
# print("-----------------------------")
# print("Kode JenisPotong  Harga")
# print("-----------------------------")
# print("D     Dada        Rp. 2500")
# print("P     Paha        Rp. 2000")
# print("S     Sayap       Rp.  1500")
# print("-----------------------------")

# banyak_jenis = int(input("Banyak Jenis: "))
# kode_potong = []
# banyak_potong = []
# jenis_potong = []
# harga = []
# jumlah = []


# for i in range(banyak_jenis):
#     print("Jenis ke - " + str(i+1))
#     kode_potong = input("Kode Potong [D/P/S]: ")
#     banyak_potong = int(input("Banyak Potong: "))

#     if kode_potong == "D" or kode_potong == "d":
#         jenis_potong = "Dada"
#         harga = 2500
#     elif kode_potong == "P" or kode_potong == "p":
#         jenis_potong = "Paha"
#         harga = 2000
#     elif kode_potong == "S" or kode_potong == "s":
#         jenis_potong = "Sayap"
#         harga = 1500
#     else:
#         jenis_potong = "Kode Potong Salah"
#         harga = 0

#     kode_potong.append(kode_potong)
#     banyak_potong.append(banyak_potong)
#     jenis_potong.append(jenis_potong)
#     harga.append(harga)
#     jumlah.append(harga * banyak_potong)

# print()
# print("GEROBAK FRIED CHICKEN")
# print("-----------------------------")
# print("No.   Jenis     Harga        Banyak    Jumlah")
# print("      Potong    Satuan       Beli      Harga ")
# print("-----------------------------")

# count = 0
# for i in range(banyak_jenis):
#     # print("%i  %s  %s  %i  %i" % (i+1, jenis_potong, harga, banyak_potong, total_harga))
#     print("%i    %s       %s        %i         %i" % (i+1,jenis_potong[i], harga[i], banyak_potong[i], jumlah[i]))
#     count = count + 1
# print("-----------------------------")

# PERULANGAN DETAIL MENGGUNAKAN WHILE 
# a = 0
# while a < banyak_jenis:
#     print("%i    %s       %s        %i         %i" % (i+1,jenis_potong[a], harga[a], banyak_potong[a], jumlah[a]))
#     jumlah_bayar = jumlah_bayar + jumlah[a] # MENAMPILKAN JUMLAH BAYAR BERDASARKAN INFORMASI YANG DI SIMPAN DI DALAM []
#     a = a + 1