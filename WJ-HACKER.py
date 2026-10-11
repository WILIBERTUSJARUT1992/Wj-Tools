#!/usr/bin/env python3
# WJ-HACKER — simulasi terminal edukasi
# Dibuat oleh: Wilibertus Jarut (W.B.J.)
# Aman: tidak membobol akun/sistem, tidak mengambil token, dan tidak mengirim data.

import os
import random
import shutil
import string
import sys
import time
from datetime import datetime

RED = "\033[91m"
GREEN = "\033[92m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
WHITE = "\033[97m"
RESET = "\033[0m"
BOLD = "\033[1m"


def clear():
    os.system("clear" if os.name != "nt" else "cls")


def typewrite(text, delay=0.012):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()


def banner():
    print(RED + r"""
 __        ___     _   _   ____   _   _    ____  _____ ____
 \ \      / / |   | | | | | __ ) | | | |  / ___|| ____|  _ \
  \ \ /\ / /| |   | |_| | |  _ \ | |_| | | |  _ |  _| | |_) |
   \ V  V / | |___|  _  | | |_) ||  _  | | |_| || |___|  _ <
    \_/\_/  |_____|_| |_| |____/ |_| |_|  \____||_____|_| \_\
""" + RESET)
    print(CYAN + "             WILIBERTUS JARUT  |  W.B.J." + RESET)
    print(GREEN + "          TERMINAL SIMULATION • EDUCATIONAL" + RESET)
    print("-" * 58)


def device_info():
    print(CYAN + "\n[ INFORMASI PERANGKAT ]" + RESET)
    print(f"Sistem operasi : {sys.platform}")
    print(f"Versi Python   : {sys.version.split()[0]}")
    print(f"Lebar terminal : {shutil.get_terminal_size((80, 20)).columns}")
    print(f"Waktu lokal    : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    input("\nTekan Enter untuk kembali...")


def terminal_simulation():
    clear()
    banner()
    print(YELLOW + "MODE SIMULASI — seluruh keluaran di bawah hanya contoh." + RESET)
    steps = [
        "[SIMULASI] Memulai pemeriksaan lingkungan lokal...",
        "[SIMULASI] Memeriksa konfigurasi contoh...",
        "[SIMULASI] Tidak ada koneksi ke target atau server.",
        "[SIMULASI] Tidak ada akun yang diakses dan tidak ada data yang diambil.",
        "[SELESAI] Simulasi edukasi berhasil dijalankan."
    ]
    for step in steps:
        typewrite(GREEN + step + RESET, 0.018)
        time.sleep(0.35)
    input("\nTekan Enter untuk kembali...")


def password_generator():
    print(CYAN + "\n[ GENERATOR PASSWORD AMAN ]" + RESET)
    try:
        length = int(input("Panjang password (8–64): ").strip())
    except ValueError:
        print(RED + "Masukkan angka yang valid." + RESET)
        input("Tekan Enter...")
        return
    if not 8 <= length <= 64:
        print(RED + "Panjang harus antara 8 dan 64 karakter." + RESET)
        input("Tekan Enter...")
        return
    alphabet = string.ascii_letters + string.digits + "!@#$%^&*()-_=+"
    password = "".join(random.SystemRandom().choice(alphabet) for _ in range(length))
    print(GREEN + "\nPassword yang dibuat:" + RESET)
    print(YELLOW + password + RESET)
    print("Simpan secara pribadi. Jangan bagikan kepada orang lain.")
    input("\nTekan Enter untuk kembali...")


def website_safety_check():
    print(CYAN + "\n[ PEMERIKSAAN DASAR WEBSITE ]" + RESET)
    print("Masukkan domain milik sendiri, misalnya: example.com")
    domain = input("Domain: ").strip()
    if not domain:
        print(RED + "Domain belum diisi." + RESET)
    elif any(ch.isspace() for ch in domain) or "/" in domain:
        print(YELLOW + "Masukkan nama domain saja tanpa spasi atau path." + RESET)
    else:
        print(YELLOW + f"\nChecklist keamanan untuk {domain}:" + RESET)
        print(" [ ] Pastikan HTTPS aktif dan sertifikat masih berlaku.")
        print(" [ ] Perbarui CMS, plugin, dan dependensi.")
        print(" [ ] Aktifkan MFA untuk akun administrator.")
        print(" [ ] Gunakan backup dan pembatasan hak akses.")
        print(" [ ] Lakukan pengujian hanya dengan izin pemilik.")
        print(WHITE + "\nCatatan: tool ini tidak memindai atau menyerang website." + RESET)
    input("\nTekan Enter untuk kembali...")


def about():
    print(CYAN + "\n[ TENTANG WJ-HACKER ]" + RESET)
    print("Nama tool : WJ-HACKER")
    print("Pembuat   : Wilibertus Jarut")
    print("Alias     : W.B.J.")
    print("Platform  : Termux / Python 3")
    print("Jenis     : Simulasi terminal dan edukasi keamanan")
    print("Fitur     : Info perangkat, simulasi, checklist, password")
    input("\nTekan Enter untuk kembali...")


def main():
    while True:
        clear()
        banner()
        print(WHITE + "[1] Informasi perangkat")
        print("[2] Simulasi terminal hacker")
        print("[3] Checklist keamanan website")
        print("[4] Generator password aman")
        print("[5] Tentang pembuat")
        print("[0] Keluar" + RESET)
        choice = input(GREEN + "\nWJ-HACKER >>> " + RESET).strip()

        if choice == "1":
            device_info()
        elif choice == "2":
            terminal_simulation()
        elif choice == "3":
            website_safety_check()
        elif choice == "4":
            password_generator()
        elif choice == "5":
            about()
        elif choice == "0":
            print(GREEN + "\nTerima kasih telah menggunakan WJ-HACKER." + RESET)
            break
        else:
            print(RED + "Pilihan tidak tersedia." + RESET)
            time.sleep(1)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n" + YELLOW + "Program dihentikan." + RESET)
