buah = ["apel", "jeruk", "mangga"]
buah.append("pisang")
print(buah)

buah = ["apel", "jeruk", "mangga"]
buah[1] = "anggur"
print(buah)

buah = ["apel", "jeruk", "mangga"]
buah.extend(["strawberry", "durian", "pisang"])
print(buah)

# LATIHAN PERTEMUAN 6
list_nim = []
list_uts = []
list_uas = []
list_total = []
ulang = 2

for i in range(ulang):
    print ("data Ke - " + str(i+1))
    list_nim.append(input("Masukkan NIM Anda: "))
    list_uts.append(int(input("Masukkan Nilai UTS: ")))
    list_uas.append(int(input("Masukkan Nilai UAS: ")))

#proses
for i in range(ulang):
    list_total.append((list_uas[i] + list_uts[i]) / 2)

#Cetak
N