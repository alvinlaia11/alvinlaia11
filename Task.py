def hitung(menit, tarif):
    tarif_dasar = 5000 if isinstance(tarif, Mobil) else 30000
    if menit <= 60: return tarif_dasar
    jam = (menit - 1) // 60 + 1
    return tarif_dasar + ((jam - 1) * 2000)

class Jam:
    def __init__(self, jam, menit):
        self.jam, self.menit = jam, menit
    
    def selisih(self, jam_akhir):
        menit_awal = (self.jam * 60) + self.menit
        menit_akhir = (jam_akhir.jam * 60) + jam_akhir.menit
        selisih = menit_akhir - menit_awal
        return selisih if selisih >= 0 else selisih + 24 * 60

class AdapterKendaraan:
    def __init__(self):
        self.id = input("ID : ")
        self.nama = input("Nama : ")
        self.status_cekin = False
        self.waktu_cekin = None

class Mobil:
    def __init__(self):
        print("Tambah Mobil")
        self.kendaraan = AdapterKendaraan()
        self.transmisi = input("Transmisi (AT/MT) : ")
        self.jumlahRoda = input("Jumlah Roda : ")
    
    def __getattr__(self, name):
        return getattr(self.kendaraan, name)

class Excavator:
    def __init__(self):
        print("Tambah Excavator\n")
        self.kendaraan = AdapterKendaraan()
        self.att = input("Jenis Atachment (Bucket, Grapple, Breaker): ")
        self.jenisRoda = input("Jenis Roda (Crawler/Wheeled): ")
    
    def __getattr__(self, name):
        return getattr(self.kendaraan, name)

class Petugas:
    def __init__(self):
        print("\nTambah Petugas")
        self.id = input("ID : ")
        self.nama = input("Nama : ")

class Parkir:
    def __init__(self, id, jam, tarif):
        self.id, self.jam, self.tarif = id, jam, tarif
    
    def hitungBiaya(self, waktukeluar):
        try:
            waktu_masuk = [int(x) for x in self.jam.split(':')]
            waktu_keluar = [int(x) for x in waktukeluar.replace('.', ':').split(':')]
            
            durasi = Jam(*waktu_masuk).selisih(Jam(*waktu_keluar))
            return {
                'durasi_jam': durasi // 60,
                'durasi_menit': durasi % 60,
                'biaya': hitung(durasi, self.tarif)
            }
        except (ValueError, IndexError):
            return None

class Garasi:
    def __init__(self):
        self.listKendaraan = []
        self.listParkir = []
        self.petugas = None
    
    def tampilkanInfo(self, kendaraan):
        info = [
            f"ID Kendaraan   : {kendaraan.id}",
            f"Nama Kendaraan : {kendaraan.nama}",
            f"Status         : {'CekIn' if kendaraan.status_cekin else 'Tersedia'}"
        ]
        
        if isinstance(kendaraan, Mobil):
            info.extend([
                f"Jenis          : Mobil",
                f"Transmisi      : {kendaraan.transmisi}",
                f"Jumlah Roda    : {kendaraan.jumlahRoda}"
            ])
        else:
            info.extend([
                f"Jenis          : Excavator",
                f"Attachment     : {kendaraan.att}",
                f"Jenis Roda     : {kendaraan.jenisRoda}"
            ])
        
        if kendaraan.status_cekin:
            info.append(f"Waktu CekIn    : {kendaraan.waktu_cekin}")
        
        print("\n".join(info))

    def tambahPetugas(self):
        self.petugas = Petugas()
        print(f"Petugas dengan ID: {self.petugas.id} berhasil ditambahkan")

    def tambahKendaraan(self):
        print("\nMenu\n1. Mobil\n2. Excavator")
        kendaraan = Mobil() if input("Pilihan : ") == "1" else Excavator()
        self.listKendaraan.append(kendaraan)

    def cekInParkir(self):
        id_kendaraan = input("\nID Kendaraan : ")
        waktu = input("Waktu CekIn (jj:mm): ").replace('.', ':')
        
        for kendaraan in self.listKendaraan:
            if kendaraan.id == id_kendaraan:
                if not kendaraan.status_cekin:
                    kendaraan.status_cekin = True
                    kendaraan.waktu_cekin = waktu
                    self.listParkir.append(Parkir(id_kendaraan, waktu, kendaraan))
                    return print("Parkir telah ditambahkan")
                return print(f"Kendaraan {id_kendaraan} sudah CekIn Parkir")
        print(f"Kendaraan {id_kendaraan} tidak ditemukan")

    def cekOutParkir(self):
        id_kendaraan = input("\nID Kendaraan : ")
        parkir = next((p for p in self.listParkir if p.id == id_kendaraan), None)
        kendaraan = next((k for k in self.listKendaraan if k.id == id_kendaraan), None)
        
        if not parkir or not kendaraan or not kendaraan.status_cekin:
            return print(f"Kendaraan {id_kendaraan} tidak valid untuk checkout")
        
        hasil = parkir.hitungBiaya(input("Waktu CekOut (jj:mm): "))
        if hasil:
            tarif_dasar = 5000 if isinstance(kendaraan, Mobil) else 30000
            print(f"\nID Kendaraan : {id_kendaraan}")
            print(f"Durasi : {hasil['durasi_jam']} jam {hasil['durasi_menit']} menit")
            print(f"Tarif Dasar : {tarif_dasar}")
            print(f"Total Biaya : {hasil['biaya']}")
            
            kendaraan.status_cekin = False
            kendaraan.waktu_cekin = None
            self.listParkir.remove(parkir)
        else:
            print("Format waktu tidak valid (gunakan jj:mm)")

    def mulai(self):
        if not self.petugas:
            return self.tambahPetugas()
        
        print("\nData Petugas:")
        print(f"ID: {self.petugas.id}, Nama: {self.petugas.nama}")
        
        if not self.listKendaraan:
            return print("\nBelum ada kendaraan")
        
        print("\nData Kendaraan:")
        for kendaraan in self.listKendaraan:
            print("\n" + "-"*34)
            self.tampilkanInfo(kendaraan)
            print("-"*34)

    def daftarParkir(self):
        print("\nDaftar Parkir:")
        if not self.listParkir:
            return print("- Belum ada kendaraan yang parkir")
        for p in self.listParkir:
            print(f"ID: {p.id}, Waktu CekIn: {p.jam}")

if __name__ == "__main__":
    obj = Garasi()
    menu = {
        "1": ("Mulai(Facade Pattern)", obj.mulai),
        "2": ("Tambah Petugas", obj.tambahPetugas),
        "3": ("Tambah Kendaraan", obj.tambahKendaraan),
        "4": ("CekIn Kendaraan", obj.cekInParkir),
        "5": ("CekOut Kendaraan", obj.cekOutParkir),
        "6": ("Daftar Kendaraan", obj.mulai),
        "7": ("Daftar Parkir", obj.daftarParkir),
    }
    
    while True:
        print("\nMenu")
        for key, (label, _) in menu.items():
            print(f"{key}. {label}")
        print("0. Keluar")
        
        pil = input("\nPilihan : ")
        if pil == "0":
            print("\nTerima kasih telah menggunakan sistem parkir!")
            break
        
        if pil in menu:
            menu[pil][1]()
            input("\nTekan Enter untuk melanjutkan...")
