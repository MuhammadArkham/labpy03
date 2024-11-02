
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

