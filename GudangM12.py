class Gudang:
    def __init__(self):
        self.barang = {}
        
    def tambahBarang(self, jenis, tipe, seri, harga):
        kode = f"{jenis}-{tipe}-{seri}"
        self.barang[kode] = {
            "jenis": jenis,
            "tipe": tipe,
            "seri": seri,
            "harga": harga
        }
        
        # Format output sesuai dengan yang diminta
        output = f"Jenis {'Baru' if jenis not in [b['jenis'] for b in self.barang.values()][:-1] else 'Lama'}\n"
        output += f"Tipe {'Baru' if tipe not in [b['tipe'] for b in self.barang.values()][:-1] else 'Lama'}\n"
        output += f"Seri Baru\n"
        return output 
