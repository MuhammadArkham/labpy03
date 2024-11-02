
balance = 1000000

while True:
   
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
