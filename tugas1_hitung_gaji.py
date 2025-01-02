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
    honor_lembur = 0

tunjangan = tunjangan_jabatan + tunjangan_pendidikan
total = (gaji_pokok+tunjangan+honor_lembur)

# OUTPUT
print("----------------------------------------")
print("     PROGRAM HITUNG GAJI KARYAWAN")
print("----------------------------------------")
print("Karyawan yang bernama    : "+str(nama_karyawan))
print("Honor yang diterima")
print(" Tunjangan Jabatan       : Rp.",tunjangan_jabatan)
print(" Tunjangan Pendidikan    : Rp.",tunjangan_pendidikan)
print(" Honor Lembur            : Rp.",honor_lembur)
print("----------------------------------------")
print(" Total Gaji              : Rp.",total)