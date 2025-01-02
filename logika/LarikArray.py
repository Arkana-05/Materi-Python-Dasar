# array adalah sebuah variable(menyimpan data) yang dapat menyimpan banyak tipe data. contohnya
# nim = 11111
# jika data berupa tabel, maka data di simpan didalam lalrik. array identik dengan index(dimulai dari 0)

nilai = [1, 2, 3, 4]
for i in range(len(nilai)):
    nilai[i] = 2*i+1
    print(nilai[i])

#Kodingan Program
#deklarasi matrik 4x4
# matriks=([0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0])
# #isi matriks 4x4
# for i in range(4):
#     for j in range(4):
#         if i==j:
#             matriks[i][j]=1
#         if i<j:
#             matriks[i][j]=1
#         if i>j:
#             matriks[i][j]=0
#         #cetak bentuk matriks
# for i in range(4): 
#     print(matriks[i])