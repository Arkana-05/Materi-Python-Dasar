# import math 
# print(math.sqrt(16))
# perintah untuk melakukan pembagian / akar

# import numpy as np
# print(np.array([1, 2, 3]))

# penggunaan eksepsi
try:
    x = int(input("Masukkan angka: "))
    y = 10 / x
except ZeroDivisionError:
    print("Error: Tidak bisa membagi dengan ini")
except ValueError:
    print("Error: Input harus berupa angka")
else:
    print("Operasi berhasil tanpa error")
finally:
    print("Selesai")