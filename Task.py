import os

def clr():
    os.system('cls')

class Mahasiswa:
    def __init__(self, nim, nama, jurusan):
        self.nim, self.nama, self.jurusan = nim, nama, jurusan
        
    def __str__(self):
        return f"NIM: {self.nim}, Nama: {self.nama}, Jurusan: {self.jurusan}"

class Dosen:
    def __init__(self, nip, nama, bidang):
        self.nip, self.nama, self.bidang = nip, nama, bidang
        
    def __str__(self):
        return f"NIP: {self.nip}, Nama: {self.nama}, Bidang: {self.bidang}"

class Perkuliahan:
    def __init__(self):
        self.daftar_dosen = []
        self.daftar_mahasiswa = []
        self.status_kelas = False
        
    def tambah_dosen(self):
        print("\n=== Tambah Dosen ===")
        nip = input("NIP: ").strip()
        nama = input("Nama: ").strip()
        bidang = input("Bidang: ").strip()
        
        if not all([nip, nama, bidang]):  # Validasi input kosong
            print("Data dosen tidak boleh kosong!")
            return
            
        self.daftar_dosen.append(Dosen(nip, nama, bidang))
        print("Dosen berhasil ditambahkan!")
        
    def tambah_mahasiswa(self):
        print("\n=== Tambah Mahasiswa ===")
        nim = input("NIM: ").strip()
        nama = input("Nama: ").strip()
        jurusan = input("Jurusan: ").strip()
        
        if not all([nim, nama, jurusan]):  # Validasi input kosong
            print("Data mahasiswa tidak boleh kosong!")
            return
            
        self.daftar_mahasiswa.append(Mahasiswa(nim, nama, jurusan))
        print("Mahasiswa berhasil ditambahkan!")
        
    def detail_kelas(self):
        print("\n=== Detail Kelas ===")
        print("Daftar Dosen:", *self.daftar_dosen, sep="\n")
        print("\nDaftar Mahasiswa:", *self.daftar_mahasiswa, sep="\n")
            
    def tap_in(self):
        if not (self.daftar_dosen and self.daftar_mahasiswa):
            print("\nBelum ada data dosen atau mahasiswa!")
            return
        if not self.status_kelas:
            print("\nDosen membuka perkuliahan Toeri\nMelakukan Absensi\nDosen memaparkan materi\nMelakukan Diskusi\nDosen Menutup Perkuliahan")
            self.status_kelas = True
            print("\nPerkuliahan Dimulai!")
        else:
            print("\nKelas sudah dimulai!")
            
    def tap_out(self):
        if not (self.daftar_dosen and self.daftar_mahasiswa):
            print("\nBelum ada data dosen atau mahasiswa!")
            return
        if self.status_kelas:
            print("\nDosen menutup perkuliahan")
            self.status_kelas = False
        else:
            print("\nTidak ada perkuliahan yang sedang berlangsung!")
    
    def tampilkan_template(self):
        print("\nTemplate Pattern")
        print("\n# Template Kelas Teori:")
        print("Dosen Membuka perkuliahan Teori")
        print("Melakukan Absensi")
        print("Dosen memaparkan materi")
        print("Melakukan Diskusi")
        print("Dosen menutup perkuliahan")
        
        print("\n# Template Kelas Praktek:")
        print("Dosen Membuka perkuliahan")
        print("Melakukan Absensi")
        print("Mahasiswa mengerjakan Latihan")
        print("Dosen menutup perkuliahan")

class Teori(Perkuliahan):
    def __init__(self):
        super().__init__()
        self.jenis = "Teori"
    
    def jalankan_kelas(self):
        print("Dosen Membuka perkuliahan Teori")
        print("Melakukan Absensi")
        print("Dosen memaparkan materi")
        print("Melakukan Diskusi")
        print("Dosen menutup perkuliahan")

class Praktek(Perkuliahan):
    def __init__(self):
        super().__init__()
        self.jenis = "Praktek"
    
    def jalankan_kelas(self):
        print("Dosen Membuka perkuliahan")
        print("Melakukan Absensi")
        print("Mahasiswa mengerjakan Latihan")
        print("Dosen menutup perkuliahan")

clr()
ob = Perkuliahan()

while True:
    print("\nMenu\n=====")
    print("1. Tambah Dosen\n2. Tambah Mahasiswa\n3. Detail Kelas\n4. Tap In\n5. Tap Out\n6. Template Pattern\n0. Keluar")
    
    match input("Pilihan: "):
        case "1": ob.tambah_dosen()
        case "2": ob.tambah_mahasiswa()
        case "3": ob.detail_kelas()
        case "4": ob.tap_in()
        case "5": ob.tap_out()
        case "6": ob.tampilkan_template()
        case "0": 
            print("\nTerima kasih!")
            break
        case _: print("\nPilihan tidak valid!")
    
    input("\nTekan enter untuk lanjut...")
    clr()