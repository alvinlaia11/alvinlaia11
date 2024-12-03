def hitung(menit, tarif):
    total = menit * tarif
    return total

class Jam:
    def __init__(self, jam, menit):
        self.jam = jam
        self.menit = menit
    
    def selisih(self, jam_akhir):
        menit_awal = (self.jam * 60) + self.menit
        menit_akhir = (jam_akhir.jam * 60) + jam_akhir.menit
        return menit_akhir - menit_awal

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
                self.tambahPetugas()
            elif pil == "3":
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
                waktu_keluar = input("Waktu CekOut (jj:mm): ")
                kendaraan.status_cekin = False
                print(f"ID Kendaraan : {id_kendaraan}")
                print(f"Waktu CekIn (jj:mm): {kendaraan.waktu_cekin}")
                print(f"Waktu CekOut (jj:mm): {waktu_keluar}")
                print(f"Kendaraan berhasil CekOut")
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
