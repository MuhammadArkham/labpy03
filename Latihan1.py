from random import random 

n = int(input("Masukkan nilai N: "))

i = 1
while i <= n:
    for _ in range(1):  
        angka = random()  
        print(f"data ke: {i} => {angka}")
        i += 1 
print("Selesai")
