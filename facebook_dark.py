#!/usr/bin/env python3
# WJ-Tools: Facebook Dark (Termux)
# Menu keamanan lokal; tidak meminta atau menyimpan kata sandi/token.
import os
import shutil
import subprocess
import sys
import textwrap
import webbrowser

BLUE = "\033[94m"
CYAN = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
RESET = "\033[0m"
BOLD = "\033[1m"

URLS = {
    "security": "https://www.facebook.com/security/",
    "password": "https://www.facebook.com/settings?tab=security",
    "sessions": "https://www.facebook.com/settings?tab=security",
    "privacy": "https://www.facebook.com/settings?tab=privacy",
    "help": "https://www.facebook.com/help/",
}

def clear():
    os.system("clear")

def open_url(url):
    # Prefer Termux's Android URL handler; fall back to Python browser handler.
    if shutil.which("termux-open-url"):
        try:
            subprocess.run(["termux-open-url", url], check=False)
            return
        except Exception:
            pass
    try:
        webbrowser.open(url)
    except Exception:
        print(f"Silakan buka manual: {url}")

def header():
    print(CYAN + BOLD + r"""
 __        __     _____  _  _   _____
 \ \      / /    |  ___|| || | |  ___|
  \ \ /\ / /_____| |_   | || |_| |_   Facebook
   \ V  V /______|  _|  |__   _|  _|  DARK
    \_/\_/       |_|      |_| |_| 
""" + RESET)
    print(BLUE + "WJ-Tools • Facebook Dark • Termux" + RESET)
    print("Tema gelap terminal + pemeriksaan keamanan akun\n")
    print(YELLOW + "PENTING: jangan masukkan kata sandi, kode OTP, atau token ke tool ini." + RESET)
    print("-" * 58)

def checklist():
    clear()
    header()
    items = [
        "Aktifkan autentikasi dua faktor (2FA).",
        "Periksa tempat/perangkat yang sedang login; keluarkan sesi asing.",
        "Ganti kata sandi jika pernah dibagikan atau dipakai ulang.",
        "Gunakan kata sandi unik dan simpan di pengelola kata sandi tepercaya.",
        "Pastikan email dan nomor pemulihan masih milik Anda.",
        "Aktifkan pemberitahuan login jika tersedia.",
        "Periksa aplikasi/situs yang terhubung dan hapus yang tidak dikenal.",
        "Jangan bagikan kode OTP atau klik tautan login yang mencurigakan.",
        "Jika akun diambil alih, gunakan pemulihan resmi Facebook.",
    ]
    done = 0
    for i, item in enumerate(items, 1):
        print(f"{CYAN}{i:>2}.{RESET} [ ] {item}")
    print("\nPilih nomor untuk membuka halaman resmi terkait.")
    print("  1 = keamanan/2FA  2 = kata sandi & sesi  3 = privasi")
    print("  4 = Pusat Bantuan  0 = kembali")
    while True:
        choice = input("\nPilihan: ").strip()
        if choice == "0":
            return
        if choice == "1":
            open_url(URLS["security"])
        elif choice == "2":
            open_url(URLS["password"])
        elif choice == "3":
            open_url(URLS["privacy"])
        elif choice == "4":
            open_url(URLS["help"])
        else:
            print("Pilihan tidak valid.")

def main():
    while True:
        clear()
        header()
        print(f"{GREEN}1.{RESET} Pemeriksaan keamanan akun (checklist)")
        print(f"{GREEN}2.{RESET} Buka pengaturan keamanan Facebook")
        print(f"{GREEN}3.{RESET} Buka pengaturan privasi Facebook")
        print(f"{GREEN}4.{RESET} Buka Pusat Bantuan Facebook")
        print(f"{RED}0.{RESET} Keluar")
        choice = input("\nPilih menu: ").strip()
        if choice == "1":
            checklist()
            input("\nTekan Enter untuk kembali...")
        elif choice == "2":
            open_url(URLS["security"])
            input("Jika browser belum terbuka, buka: " + URLS["security"] + "\nTekan Enter...")
        elif choice == "3":
            open_url(URLS["privacy"])
            input("Jika browser belum terbuka, buka: " + URLS["privacy"] + "\nTekan Enter...")
        elif choice == "4":
            open_url(URLS["help"])
            input("Jika browser belum terbuka, buka: " + URLS["help"] + "\nTekan Enter...")
        elif choice == "0":
            print("WJ-Tools Facebook Dark ditutup. Tetap jaga keamanan akun!")
            break
        else:
            print("Pilihan tidak valid.")
            input("Tekan Enter untuk lanjut...")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nKeluar dengan aman.")
