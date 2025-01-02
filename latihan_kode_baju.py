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
print("Ukuran Baju    : "+str(ukuran_baju))
print("Harga Baju   : Rp.", harga)