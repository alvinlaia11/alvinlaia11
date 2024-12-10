def hitung(menit, jenis_kendaraan):
    # Konversi menit ke jam (pembulatan ke atas)
    jam = (menit + 59) // 60  # Pembulatan ke atas
    
    # Set tarif dasar berdasarkan jenis kendaraan
    if isinstance(jenis_kendaraan, Adaptorpendorong):
        tarif_dasar = 5000
    else:  # Excavator
        tarif_dasar = 30000
    
    # Hitung total biaya
    if jam <= 1:
        return tarif_dasar
    else:
        # Tarif dasar + (jumlah jam tambahan * 2000)
        return tarif_dasar + ((jam - 1) * 2000)

class Jam:
    def __init__(self, jam, menit):
        self.jam = jam
        self.menit = menit
    
    def selisih(self, jam_akhir):
        menit_awal = (self.jam * 60) + self.menit
        menit_akhir = (jam_akhir.jam * 60) + jam_akhir.menit
        selisih = menit_akhir - menit_awal
        if selisih < 0:
            selisih += 24 * 60
        return selisih

class Alat:
    def __init__(self, twatt, twift):
        pass

class Adaptorpendorong:
    def __init__(self):
        print("\nTambah Mobil")
        self.id = input("ID : ")
        self.nama = input("Nama : ")
        self.transmisi = input("Transmisi (AT/MT) : ")
        self.jumlahRoda = input("Jumlah Roda : ")
        self.status_cekin = False
        self.waktu_cekin = None

class Excavator:
    def __init__(self):
        print("\nTambah Excavator")
        self.id = input("ID : ")
        self.nama = input("Nama : ")
        self.att = input("Jenis Attachment (Bucket, Grapple, Breaker): ")
        self.jumlahRoda = input("Jenis Roda (Crawler/Wheeled): ")
        self.status_cekin = False
        self.waktu_cekin = None

class Petugas:
    def __init__(self):
        print("\nTambah Petugas")
        self.id = input("ID : ")
        self.nama = input("Nama : ")

# Implementasi Facade Pattern
class RentalFacade:
    def __init__(self, rental):
        self.rental = rental

    def tampilkanStatus(self):
        print("\n=== Status Rental ===")
        print("\nDaftar Petugas:")
        if len(self.rental.listPetugas) == 0:
            print("- Belum ada petugas")
        else:
            for petugas in self.rental.listPetugas:
                print(f"- ID: {petugas.id}, Nama: {petugas.nama}")

        print("\nDaftar Kendaraan:")
        if len(self.rental.listKendaraan) == 0:
            print("- Belum ada kendaraan")
        else:
            for kendaraan in self.rental.listKendaraan:
                status = "CekIn" if kendaraan.status_cekin else "Tersedia"
                print(f"- ID: {kendaraan.id}, Nama: {kendaraan.nama}, Status: {status}")

class Rental:
    def __init__(self):
        self.listKendaraan = []
        self.listPetugas = []
        self.facade = RentalFacade(self)
        self.tarif_per_menit = 1000 
    
    def mulai(self):
        print("\n=== Sistem Rental Kendaraan ===")
        self.facade.tampilkanStatus()
    
    def tampilMenuUtama(self):
        while True:
            print("\n1. Mulai(Facade Pattern)")
            print("2. Tambah Petugas")
            print("3. Tambah Kendaraan")
            print("4. CekIn Kendaraan")
            print("5. CekOut Kendaraan")
            print("6. Daftar Kendaraan")
            print("7. Daftar Parkir")
            print("0. Keluar")
            
            pil = input("\nPilihan : ")
            if pil == "0":
                print("\nTerima kasih telah menggunakan sistem rental!")
                break
            elif pil == "1":
                self.mulai()
            elif pil == "2":
                # Cek jika sudah ada petugas
                if len(self.listPetugas) > 0:
                    print("\nPetugas sudah ada! Silahkan tambah kendaraan.")
                    self.tambahKendaraan()
                else:
                    self.tambahPetugas()
            elif pil == "3":
                # Cek jika belum ada petugas
                if len(self.listPetugas) == 0:
                    print("\nHarap tambahkan petugas terlebih dahulu!")
                    self.tambahPetugas()
                self.tambahKendaraan()
            elif pil == "4":
                self.cekInKendaraan()
            elif pil == "5":
                self.cekOutKendaraan()
            elif pil == "6":
                self.daftarKendaraan()
            elif pil == "7":
                self.daftarParkir()
            
            if pil != "0":
                input("\nEnter untuk Lanjut")

    def tambahPetugas(self):
        petugas = Petugas()
        self.listPetugas.append(petugas)
        print(f"Petugas dengan ID: {petugas.id} berhasil ditambahkan")

    def tambahKendaraan(self):
        print("\nMenu")
        print("1. Mobil")
        print("2. Excavator")
        pilihan = input("Pilihan : ")
        
        if pilihan == "1":
            kendaraan = Adaptorpendorong()
            self.listKendaraan.append(kendaraan)
        elif pilihan == "2":
            kendaraan = Excavator()
            self.listKendaraan.append(kendaraan)

    def cekInKendaraan(self):
        id_kendaraan = input("\nID Kendaraan : ")
        waktu = input("Waktu CekIn (jj:mm): ")
        waktu = waktu.replace('.', ':') 
        
        for kendaraan in self.listKendaraan:
            if kendaraan.id == id_kendaraan:
                if not kendaraan.status_cekin:
                    kendaraan.status_cekin = True
                    kendaraan.waktu_cekin = waktu
                    print("Parkir telah ditambahkan")
                    return
                else:
                    print(f"Kendaraan {id_kendaraan} sudah CekIn Parkir")
                    return
        print(f"Kendaraan {id_kendaraan} tidak ditemukan")

    def cekOutKendaraan(self):
        id_kendaraan = input("\nID Kendaraan : ")
        for kendaraan in self.listKendaraan:
            if kendaraan.id == id_kendaraan:
                if not kendaraan.status_cekin:
                    print(f"Kendaraan {id_kendaraan} belum CekIn Parkir")
                    return
                
                waktu_keluar_input = input("Waktu CekOut (jj:mm): ")
                waktu_keluar_input = waktu_keluar_input.replace('.', ':')  
                waktu_masuk = kendaraan.waktu_cekin.split(':')
                waktu_keluar = waktu_keluar_input.split(':')
                
                try:
                    jam_masuk = int(waktu_masuk[0])
                    menit_masuk = int(waktu_masuk[1])
                    jam_keluar = int(waktu_keluar[0])
                    menit_keluar = int(waktu_keluar[1])
                    
                    waktu_masuk_obj = Jam(jam_masuk, menit_masuk)
                    waktu_keluar_obj = Jam(jam_keluar, menit_keluar)
                    
                    durasi = waktu_masuk_obj.selisih(waktu_keluar_obj)
                    # Hitung jam dan menit untuk display
                    jam = durasi // 60
                    menit = durasi % 60
                    
                    # Tentukan tarif dasar
                    tarif_dasar = 5000 if isinstance(kendaraan, Adaptorpendorong) else 30000
                    biaya = hitung(durasi, kendaraan)
                    
                    kendaraan.status_cekin = False
                    kendaraan.waktu_cekin = None
                    
                    print(f"\nID Kendaraan : {id_kendaraan}")
                    print(f"Waktu CekOut (jj:mm): {':'.join(waktu_keluar)}")
                    print(f"Waktu : {jam}.{menit} jam {menit} menit dengan tarif dasar {tarif_dasar}")
                    print(f"{biaya}")
                    print(f"Kendaraan {id_kendaraan} berhasil Cek Out dengan biaya : {biaya}")
                    return
                except (ValueError, IndexError):
                    print("Format waktu tidak valid. Gunakan format jj:mm")
                    return
                
        print(f"Kendaraan {id_kendaraan} tidak ditemukan")

    def daftarKendaraan(self):
        print("\nDaftar Kendaraan:")
        if len(self.listKendaraan) == 0:
            print("- Belum ada kendaraan")
        else:
            for kendaraan in self.listKendaraan:
                print(f"ID: {kendaraan.id}, Nama: {kendaraan.nama}")

    def daftarParkir(self):
        print("\nDaftar Parkir:")
        ada_parkir = False
        for kendaraan in self.listKendaraan:
            if kendaraan.status_cekin:
                print(f"ID: {kendaraan.id}, Waktu CekIn: {kendaraan.waktu_cekin}")
                ada_parkir = True
        if not ada_parkir:
            print("- Belum ada kendaraan yang parkir")


if __name__ == "__main__":
    rental = Rental()
    rental.tampilMenuUtama()
