import os
import sys

# Kode warna ANSI untuk visualisasi terminal yang menarik
GREEN, YELLOW, RED, BLUE, CYAN, BOLD, RESET = "\033[92m", "\033[93m", "\033[91m", "\033[94m", "\033[96m", "\033[1m", "\033[0m"

class Node:
    """Kelas Node mewakili satu pasien dalam Linked List."""
    def __init__(self, no_pasien, nama, keluhan):
        self.no_pasien = no_pasien
        self.nama = nama
        self.keluhan = keluhan
        self.next = None

class Queue:
    """Kelas Queue FIFO menggunakan manual Singly Linked List dengan head dan tail."""
    def __init__(self):
        self.head = self.tail = None
        self.size = 0
        self.max_size = 5
        self.counter = 0
        self.history = []

    def is_empty(self): return self.size == 0
    def is_full(self): return self.size >= self.max_size

    def enqueue(self, nama, keluhan):
        if self.is_full(): return False
        self.counter += 1
        new_node = Node(str(self.counter), nama, keluhan)
        if self.is_empty():
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1
        return new_node.no_pasien

    def dequeue(self):
        if self.is_empty(): return None
        removed = self.head
        self.head = self.head.next
        if not self.head: self.tail = None
        self.size -= 1
        self.history.append(Node(removed.no_pasien, removed.nama, removed.keluhan))
        return removed

    def get_info(self):
        return {"jumlah": self.size, "depan": self.head, "belakang": self.tail}

    def get_history(self): return self.history

    def cari_pasien(self, kata_kunci):
        hasil, current, kw = [], self.head, kata_kunci.lower()
        while current:
            if kw in current.no_pasien.lower() or kw in current.nama.lower():
                hasil.append(current)
            current = current.next
        return hasil

    def tampilkan_semua(self):
        daftar, current = [], self.head
        while current:
            daftar.append(current)
            current = current.next
        return daftar

def cetak_pasien(pasien, index):
    print(f"   {CYAN}┌──────────────────────────────────────────────┐{RESET}\n"
          f"     {BOLD}Urutan    : {index}{RESET}\n"
          f"     {BOLD}No. Pasien: {YELLOW}{pasien.no_pasien}{RESET}\n"
          f"     Nama      : {pasien.nama}\n"
          f"     Keluhan   : {pasien.keluhan}\n"
          f"   {CYAN}└──────────────────────────────────────────────┘{RESET}")

def main():
    antrean_klinik = Queue()
    menu_headers = {
        '1': "TAMBAH PASIEN (ENQUEUE)", '2': "PANGGIL PASIEN BERIKUTNYA (DEQUEUE)",
        '3': "CARI DATA PASIEN", '4': "TAMPILKAN SELURUH ANTREAN",
        '5': "INFORMASI DETAIL ANTREAN", '6': "RIWAYAT PASIEN TERPANGGIL"
    }

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"{CYAN}{BOLD}============================================================\n"
              f"          🏥  SISTEM ANTREAN INSTIKI HOSPITAL  🏥        \n"
              f"============================================================{RESET}")
        
        pb = f"[{GREEN}{'● ' * antrean_klinik.size}{RESET}{'○ ' * (antrean_klinik.max_size - antrean_klinik.size)}]"
        print(f" 📊 {BOLD}STATUS ANTREAN:{RESET}\n"
              f"   • Kapasitas  : {pb} ({antrean_klinik.size}/{antrean_klinik.max_size} Pasien)")
        if not antrean_klinik.is_empty():
            print(f"   • Terdepan   : {YELLOW}{BOLD}{antrean_klinik.head.nama} (No. {antrean_klinik.head.no_pasien}){RESET}\n"
                  f"   • Terbelakang: {BLUE}{antrean_klinik.tail.nama} (No. {antrean_klinik.tail.no_pasien}){RESET}")
        else:
            print(f"   • Terdepan   : {YELLOW}- (Antrean Kosong){RESET}")
        
        print(f"""{CYAN}┌──────────────────────────────────────────────────────────┐
│ {BOLD}📋 MENU UTAMA:{RESET}                                           {CYAN}│
├──────────────────────────────────────────────────────────┤
│ {GREEN}[1]{RESET} Tambah Pasien Baru (Enqueue)                         {CYAN}│
│ {GREEN}[2]{RESET} Panggil Pasien Berikutnya (Dequeue)                  {CYAN}│
│ {GREEN}[3]{RESET} Cari Data Pasien                                     {CYAN}│
│ {GREEN}[4]{RESET} Tampilkan Daftar Antrean                             {CYAN}│
│ {GREEN}[5]{RESET} Informasi Detail Antrean                             {CYAN}│
│ {GREEN}[6]{RESET} Riwayat Pasien Terpanggil                            {CYAN}│
│ {RED}[7]{RESET} Keluar Aplikasi                                      {CYAN}│
└──────────────────────────────────────────────────────────┘{RESET}""")
        
        pilihan = input(f"{BOLD}Pilih menu [1-7]: {RESET}").strip()
        if pilihan in menu_headers:
            print(f"\n{GREEN}{BOLD}>>> {menu_headers[pilihan]}{RESET}\n" + "-" * 50)
            
        if pilihan == '1':
            if antrean_klinik.is_full():
                print(f"{RED}⚠️ Antrean Penuh! Batas maksimal adalah {antrean_klinik.max_size} pasien.{RESET}")
            else:
                nama, keluhan = input("Masukkan Nama Pasien: ").strip(), input("Masukkan Keluhan Pasien: ").strip()
                if nama and keluhan:
                    no = antrean_klinik.enqueue(nama, keluhan)
                    print(f"\n{GREEN}✔ Sukses! Pasien {BOLD}{nama}{RESET}{GREEN} terdaftar dengan {BOLD}Nomor Pasien: {no}{RESET}")
                else:
                    print(f"{RED}❌ Gagal! Nama dan Keluhan tidak boleh kosong.{RESET}")
        elif pilihan == '2':
            pasien = antrean_klinik.dequeue()
            if pasien:
                print(f"📢 {BOLD}{YELLOW}MEMANGGIL PASIEN:{RESET}\n"
                      f"   Nomor Pasien: {BOLD}{YELLOW}{pasien.no_pasien}{RESET}\n"
                      f"   Nama Pasien : {BOLD}{pasien.nama}{RESET}\n"
                      f"   Keluhan     : {pasien.keluhan}\n\n"
                      f"{GREEN}✔ Pasien telah dipanggil dan keluar dari antrean aktif.{RESET}")
            else:
                print(f"{YELLOW}⚠️ Antrean Kosong! Tidak ada pasien untuk dipanggil.{RESET}")
        elif pilihan == '3':
            if antrean_klinik.is_empty():
                print(f"{YELLOW}⚠️ Antrean Kosong!{RESET}")
            else:
                keyword = input("Masukkan Nomor Pasien atau Nama: ").strip()
                if keyword:
                    hasil = antrean_klinik.cari_pasien(keyword)
                    if hasil:
                        print(f"\n{GREEN}✔ Ditemukan {len(hasil)} pasien:{RESET}")
                        for idx, p in enumerate(hasil, 1): cetak_pasien(p, idx)
                    else:
                        print(f"{RED}❌ Pasien dengan kata kunci '{keyword}' tidak ditemukan.{RESET}")
                else:
                    print(f"{RED}❌ Kata kunci pencarian tidak boleh kosong.{RESET}")
        elif pilihan == '4':
            daftar = antrean_klinik.tampilkan_semua()
            if not daftar:
                print(f"{YELLOW}⚠️ Antrean Kosong!{RESET}")
            else:
                print(f"{BOLD}Daftar Pasien di Antrean (Depan -> Belakang):{RESET}")
                for idx, p in enumerate(daftar, 1): cetak_pasien(p, idx)
        elif pilihan == '5':
            print(f"• Total pasien mengantre : {GREEN}{antrean_klinik.size}{RESET} orang")
            if not antrean_klinik.is_empty():
                print(f"• Pasien Terdepan (Head) : {YELLOW}{BOLD}{antrean_klinik.head.nama}{RESET} (No. {antrean_klinik.head.no_pasien})\n"
                      f"• Pasien Terakhir (Tail) : {BLUE}{antrean_klinik.tail.nama}{RESET} (No. {antrean_klinik.tail.no_pasien})")
            else:
                print(f"• Status: {YELLOW}Antrean Kosong.{RESET}")
        elif pilihan == '6':
            riwayat = antrean_klinik.get_history()
            if not riwayat:
                print(f"{YELLOW}⚠️ Belum ada riwayat pasien dipanggil oleh dokter.{RESET}")
            else:
                print(f"{BOLD}Daftar Riwayat Terpanggil (Terbaru -> Terlama):{RESET}")
                for idx, p in enumerate(reversed(riwayat), 1): cetak_pasien(p, idx)
        elif pilihan == '7':
            print(f"\n{GREEN}Terima kasih. Program selesai.{RESET}")
            sys.exit(0)
        else:
            print(f"\n{RED}❌ Pilihan tidak valid! Silakan masukkan 1 sampai 7.{RESET}")
            
        input(f"\n{YELLOW}Tekan Enter untuk kembali ke menu...{RESET}")

if __name__ == '__main__':
    main()
