# for letter in "PythonProgramming":
#     print("Huruf Sekarang: ", letter)
#     if letter == "g":
#         break

# bil = 6
# for i in range(0, 10):
#     print(i, end=",")
#     if i is bil:
#         break

# CONTINUE
# bil = 0
# pilihan = "y"
# while(pilihan!= "n"):
#     bil = int(input(""))

# NESTED LOOP
n = 5 #nilai awal
i = 1 #batas akhir (range)
while n >= i:
    j = 5 #untuk perulangan dalam perulangan
    while j >= n:
        print(j, end=" ")
        j = j - 1
    print()
    n = n - 1
print("-------------")

# NESTED NAIK
i = 1
while(i < 6):
    j = 1
    while(j <= i):
        print(j, end=" ")
        j = j + 1
    print()
    i = i + 1
print("-------------")

# NESTED NAIK
i = 1
while(i < 6):
    j = 1
    while(j <= i):
        print(i, end=" ")
        j = j + 1
    print()
    i = i + 1
print("-------------")