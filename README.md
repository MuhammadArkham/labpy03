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
![Foto](https://github.com/MuhammadArkham/Foto/blob/main/Screenshot%202024-11-02%20081404.png?raw=true)

## Penjelasan alur algoritma program

__Input:__ Program meminta nilai n dari pengguna untuk menentukan jumlah angka acak.

__Perulangan:__ Program melakukan perulangan while untuk menghasilkan dan menampilkan n angka acak.

__Output:__ Program menampilkan setiap angka acak yang dihasilkan bersama nomor urutannya.

__Akhir:__ Program menampilkan "Selesai" setelah semua angka acak ditampilkan


## Gambar Flowchart
![Foto](https://github.com/MuhammadArkham/Foto/blob/main/latihan1.png?raw=true)


## Latihan 2: latihan2.py
Seorang pengusaha menginvestasikan uangnya untuk memulai usahanya dengan modal
awal 100 juta, pada bulan pertama dan kedua belum mendapatkan laba. pada bulan ketiga
baru mulai mendapatkan laba sebesar 1% dan pada bulan ke 5, pendapatan meningkat 5%,
selanjutnya pada bulan ke 8 mengalami penurunan keuntungan sebesar 2%, sehingga laba
menjadi 3%. Hitung total keuntungan selama 8 bulan berjalan usahanya.

# Kode Program
```python
modal_awal = 100_000_000  

laba_bulan_3 = 0.01 
laba_bulan_5 = 0.05  
laba_bulan_8 = 0.03 

total_keuntungan = 0  

print("Rincian Laba Per Bulan:")
for bulan in range(1, 9):  
    if bulan <= 2:
        laba = 0 
    elif bulan < 5:
        laba = modal_awal * laba_bulan_3  
    elif bulan < 8:
        laba = modal_awal * laba_bulan_5  
    else:
        laba = modal_awal * laba_bulan_8  

    total_keuntungan += laba  
    print(f"Bulan ke-{bulan} => Laba: Rp {laba:,.2f}")

print(f"\nTotal Keuntungan Selama 8 Bulan: Rp {total_keuntungan:,.2f}")

```
## Hasil kode Program
![Foto](https://github.com/MuhammadArkham/Foto/blob/main/Screenshot%202024-11-02%20090657.png?raw=true)

## Penjelasan alur algoritma program

__1. Inisialisasi variabel awal:__

- Modal awal = 100.000.000

- Laba bulan 3 = 1% (0.01)

- Laba bulan 5 = 5% (0.05)

- Laba bulan 8 = 3% (0.03)

Total keuntungan = 0


__2. Program akan melakukan Looping dari bulan 1-8 :__  

- Bulan 1-2: Tidak ada laba (0)

- Bulan 3-4: Laba 1% dari modal awal

- Bulan 5-7: Laba 5% dari modal awal

- Bulan 8: Laba 3% dari modal awal

__3. Lalu hitung laba sesuai kondisi__

__4.Tambahkan laba ke total keuntungan__

__5. Tampilkan laba bulan tersebut__

__6. Setelah perulangan selesai, tampilkan total keuntungan__


## Gambar Flowchart
![Foto](https://github.com/MuhammadArkham/Foto/blob/main/Latihan2.png?raw=true)

## Latihan 3: latihan3.py
Buat program yang mensimulasikan mesin ATM sederhana. Pengguna memiliki saldo awal
sebesar Rp 1.000.000, dan dapat menarik uang hingga saldo habis atau memilih untuk
keluar.

# Kode Program
```python
   print(f"\nSaldo saat ini: Rp {balance}")
    print("1. Tarik Uang")
    print("2. Keluar")

    choice = input("Pilih menu (1/2): ")

    if choice == "1":
        
        amount = int(input("Masukkan jumlah penarikan: "))
        
        if amount <= balance:
            balance -= amount
            print("Penarikan berhasil!")
        else:
            print("Saldo tidak mencukupi!")
        
        if balance == 0:
            print("Saldo habis! Terima kasih telah menggunakan ATM!")
            break

    elif choice == "2":
        
        print("Terima kasih telah menggunakan ATM!")
        break

    else:
        
        print("Pilihan tidak valid, silakan coba lagi.")
```

## Hasil kode Program
![Foto](https://github.com/MuhammadArkham/Foto/blob/main/Screenshot%202024-11-02%20095616.png?raw=true)

## Penjelasan alur algoritma program

__1. Tampilkan saldo saat ini__

__2. Tampilkan menu pilihan__ 

1. Tarik Uang
   
2. Keluar
   
__3. memilih menu :__
Program meminta pengguna untuk memasukkan pilihan menu (1 atau 2).

__4. Jika pilihan = 1 (Tarik Uang):__

- Input jumlah penarikan
- Cek apakah jumlah penarikan <= saldo
- Jika ya: kurangi saldo dan tampilkan pesan sukses
- Jika tidak: tampilkan pesan saldo tidak cukup
- Cek apakah saldo = 0
- Jika ya: tampilkan pesan saldo habis dan keluar


__5. Jika pilihan = 2:__

Tampilkan pesan terima kasih dan keluar


__6. Jika pilihan tidak valid:__

Tampilkan pesan error

## Gambar Flowchart
![Foto](https://github.com/MuhammadArkham/Foto/blob/main/Latihan3%20(1).png?raw=true)
