# Pilihan pulsa dan paket data
pulsa = {
    1: ("Pulsa 5.000", 5000),
    2: ("Pulsa 10.000", 10000),
    3: ("Pulsa 30.000", 30000),
    4: ("Pulsa 50.000", 50000),
    5: ("Pulsa 100.000", 100000),
}

paket_data = {
    1: ("Paket Data 1GB 1HR", 5000),
    2: ("Paket Data 5GB 3HR", 10000),
    3: ("Paket Data 10GB 7HR", 15000),
    4: ("Paket Data 20GB 30HR", 50000),
    5: ("Paket Data 50GB 30HR", 100000),
}

# Metode pembayaran
metode_pembayaran = {
    1: ("OVO", "123"),
    2: ("DANA", "231"),
    3: ("GoPay", "321")
}

# Daftar provider
providers = {
    1: "Telkomsel",
    2: "Indosat",
    3: "XL",
    4: "Tri",
    5: "Smartfren"
}

# Menampilkan pilihan
def tampilkan_pilihan(menu):
    for key, value in menu.items():
        print(f"{key}. {value[0]} - Rp{value[1]:,}")

# Menghitung total harga dengan pajak
def hitung_total(harga):
    pajak = 1500
    return harga + pajak

# Program utama
def main():
    print("==== Selamat Datang ====")
    
    print("\nPilih Provider:")
    for key, provider in providers.items():
        print(f"{key}. {provider}")
    
    pilihan_provider = int(input("Masukkan pilihan provider: "))
    if pilihan_provider in providers:
        provider = providers[pilihan_provider]
    else:
        print("Pilihan provider tidak valid.")
        return
    
    while True:
        nomor_hp = input("\nMasukkan nomor HP (minimal 10 digit): ")
        if len(nomor_hp) > 10:
            break
        else:
            print("Nomor HP harus lebih dari 10 digit. Silakan coba lagi.")
    
    print("\nPilih jenis produk:")
    print("1. Pulsa")
    print("2. Paket Data")
    
    pilihan_produk = int(input("Masukkan pilihan (1/2): "))
    
    if pilihan_produk == 1:
        print("\nDaftar Pulsa:")
        tampilkan_pilihan(pulsa)
        pilihan = int(input("Masukkan pilihan pulsa: "))
        nama_produk, harga = pulsa[pilihan]
    elif pilihan_produk == 2:
        print("\nDaftar Paket Data:")
        tampilkan_pilihan(paket_data)
        pilihan = int(input("Masukkan pilihan paket data: "))
        nama_produk, harga = paket_data[pilihan]
    else:
        print("Pilihan tidak valid.")
        return
    
    total_harga = hitung_total(harga)
    
    print("\nMetode Pembayaran:")
    for key, metode in metode_pembayaran.items():
        print(f"{key}. {metode[0]}")
    
    metode = int(input("Pilih metode pembayaran (1/2/3): "))
    
    if metode in metode_pembayaran:
        kode_metode, kode_prefix = metode_pembayaran[metode]
        kode_pembayaran = f"{kode_prefix}{nomor_hp}"
        
        print("\n==== Rincian Pembelian ====")
        print(f"Provider         : {provider}")
        print(f"Nomor HP         : {nomor_hp}")
        print(f"Produk           : {nama_produk}")
        print(f"Harga            : Rp{harga:,}")
        print(f"Pajak            : Rp1,500")
        print(f"Total Harga      : Rp{total_harga:,}")
        print(f"Metode Pembayaran: {kode_metode}")
        print(f"Kode Pembayaran  : {kode_pembayaran}")
        print("=============================")
        
        input("\nTekan Enter setelah melakukan pembayaran...")
        print("\nTRANSAKSI SUKSES!! Terima kasih!!.")
    else:
        print("Metode pembayaran tidak valid.")

# Aplikasi Penjualan
if __name__ == "__main__":
    main()
