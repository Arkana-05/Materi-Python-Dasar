import pandas as pd
# pandaas adalah 
list_nim = []
list_nama = []
list_uts = []
list_uas = []
list_total = [] 

ulang = 1
for i in range(ulang):
    print("Data ke - " + str(i + 1))
    list_nim.append(input("NIM: "))
    list_nama.append(input("Nama: "))
    list_uts.append(int(input("Nilai UTS: ")))
    list_uas.append(int(input("Nilai UAS: ")))

for i in range(ulang):
    list_total.append((list_uas[i] + list_uts[i]) / 2)

tamu = {
    "NIM" : list_nim,
    "Nama" : list_nama,
    "UTS" : list_uts,
    "UAS" : list_uas,
    "Total" : list_total
}

data_tamu = pd.DataFrame(tamu)
print("============= Daftar Nilai =====================")
print(data_tamu)
print("================================================")