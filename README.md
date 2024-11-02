# Praktikum3

Muhammad Arkhamullah Rifai Asshidiq

Bahasa pemrograman

312410545

## Latihan 1: latihan1.py
1. Tampilkan n bilangan acak yang lebih kecil dari 0.5.
2. nilai n diisi pada saat runtime
3. anda bisa menggunakan kombinasi while dan for untuk menyelesaikannya
4. gunakan fungsi random() yang dapat diimport terlebih dahulu

## Kode Program
```python
from random import random 

n = int(input("Masukkan nilai N: "))

i = 1
while i <= n:
    for _ in range(1):  
        angka = random()  
        print(f"data ke: {i} => {angka}")
        i += 1 
print("Selesai")

```
## Hasil kode Program
![Foto](
