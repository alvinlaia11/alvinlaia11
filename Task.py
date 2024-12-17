from GudangM12 import Gudang
import unittest

class testGudang(unittest.TestCase):
    def setUp(self):
        self.gudang = Gudang()
    
    def test_tambah_barang_pertama(self):
        hasil = self.gudang.tambahBarang("Kabel", "USB", "US01", 12000)
        expected = "Jenis Baru\nTipe Baru\nSeri Baru\n"
        self.assertEqual(hasil, expected)
    
    def test_tambah_barang_jenis_sama_tipe_sama(self):
        self.gudang.tambahBarang("Kabel", "USB", "US01", 12000)
        hasil = self.gudang.tambahBarang("Kabel", "USB", "US02", 15000)
        expected = "Jenis Lama\nTipe Lama\nSeri Baru\n"
        self.assertEqual(hasil, expected)
    
    def test_tambah_barang_jenis_sama_tipe_baru(self):
        self.gudang.tambahBarang("Kabel", "USB", "US01", 12000)
        hasil = self.gudang.tambahBarang("Kabel", "LAN", "LN01", 23000)
        expected = "Jenis Lama\nTipe Baru\nSeri Baru\n"
        self.assertEqual(hasil, expected)
    
    def test_tambah_barang_jenis_baru(self):
        self.gudang.tambahBarang("Kabel", "USB", "US01", 12000)
        hasil = self.gudang.tambahBarang("Monitor", "21 Inch", "LG L001", 5100000)
        expected = "Jenis Baru\nTipe Baru\nSeri Baru\n"
        self.assertEqual(hasil, expected)

if __name__ == "__main__":
    gudang = Gudang()
    
    print(gudang.tambahBarang("Kabel", "USB", "US01", 12000))
    print()
    print(gudang.tambahBarang("Kabel", "USB", "US02", 15000))
    print()
    print(gudang.tambahBarang("Kabel", "LAN", "LN01", 23000))
    print()
    print(gudang.tambahBarang("Monitor", "21 Inch", "LG L001", 5100000))
