# rekursif memiliki 4 contoh, fungsi pangkat, faktorial, fibonancy dan menara hanoi
# FUNGSI PANGKAT SECARA REKURSIF
# DEF ADALAH FUNGSI UNTUK MENDEFINISIKAN ATAU MEMBUAT SUATU FUNGSI
print("PANGKAT")
def pangkat(x, y):
    if y == 0:
        return 1
    else:
        return x * pangkat(x, y - 1)
    
x = int(input("Masukkan Nilai X: "))
y = int(input("Masukkan Nilai Y: "))

print("%d dipangaktkan %d = %d" % (x, y, pangkat(x, y)))

# print()

# FUNGSI FAKTORIAL SECARA REKURSIF 
# faktorial adalah bilangan dengan ! atau bisa di tulis fakt(n). aturan faktorial adalah 0! = 1. sedangkan jika fakt(n) = N * fak(N -1). faktorial 5 rekursif nya itu 5 x 4 x 3 x 2 x 1 x 0.
print("FAKTORIAL")
def faktorial(a):
    if a == 1:
        return (a)
    else:
        return(a * faktorial(a - 1))
    
bil = int(input("Masukkan Bilangan: "))

print("%d! = %d" % (bil, faktorial(bil)))

print()

# FUNGSI FIBONACCI SECARA REKURSIF
# fubonacci ada nilai tetapnya, yaitu fibo deret pertama = 0, deret kedua itu 1, fibo selanjutnya / fibo(n) = fibo(n - 1) + fibo (n - 2)
print("FIBONACCI")
def fibonacci(n):
    if n == 0 or n == 1:
        return n
    else:
        return(fibonacci(n - 1) + fibonacci(n - 2))
    
x = int(input("Masukkan Batas Deret Bilangan Fibonacci: "))

print("Deret Fibonacci")
for i in range(x):
    print(fibonacci(i), end=' ')

# MENARA HANOI - di cari berapa banyak langkahnya 
# ibaratnya sebagai piringan yang di susun, di menara hanoi kalian di minta memindahkan piringan pada menara tujuan
# piringan yang lebih kecil tidak boleh di pindahkan di bawah yang lebih besar 
#  rumusnya yaitu 2pangkat(n-1)

