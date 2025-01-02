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
print("NIS Calon Mahasiswa    : "+str(nis_mahasiswa))
print("Nama Calon Mahasiswa   : "+str(nama_mahasiswa))
print("Kode Jurusan           : "+str(jurusan))
print("Nama Prodi Jurusan     : "+str(nama_prodi))
print("Biaya Kuliah           : ", harga)
print("----------------------------------------")