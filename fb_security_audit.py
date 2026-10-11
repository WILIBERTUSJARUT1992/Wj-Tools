#!/usr/bin/env python3
# WJ-Tools - FB Security Audit
# Safe local checklist and links to official Facebook security resources.
# This script never asks for or stores passwords, OTPs, cookies, or access tokens.

import os
import shutil
import subprocess
import webbrowser

BLUE = "\033[94m"
CYAN = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
BOLD = "\033[1m"
RESET = "\033[0m"

LINKS = {
    "security": "https://www.facebook.com/security/",
    "password": "https://www.facebook.com/settings?tab=security",
    "privacy": "https://www.facebook.com/settings?tab=privacy",
    "help": "https://www.facebook.com/help/",
    "recovery": "https://www.facebook.com/hacked",
}

CHECKS = [
    "Aktifkan autentikasi dua faktor (2FA).",
    "Periksa sesi login dan keluarkan perangkat yang tidak dikenal.",
    "Gunakan kata sandi unik yang tidak dipakai di situs lain.",
    "Pastikan email dan nomor pemulihan masih bisa diakses.",
    "Aktifkan pemberitahuan login jika tersedia.",
    "Hapus aplikasi atau situs terhubung yang tidak dikenal.",
    "Jangan pernah membagikan kode OTP, kode pemulihan, atau kata sandi.",
    "Hindari tautan login dari pesan yang mencurigakan.",
    "Periksa aktivitas dan informasi profil jika ada perubahan tak dikenal.",
]

def clear():
    os.system("clear")

def open_url(url):
    if shutil.which("termux-open-url"):
        try:
            subprocess.run(["termux-open-url", url], check=False)
            return
        except Exception:
            pass
    try:
        webbrowser.open(url)
    except Exception:
        print("Buka tautan ini secara manual:", url)

def header():
    print(CYAN + BOLD + r"""
  ______ ____    _____                 _ _         
 |  ____|  _ \  / ____|               (_) |        
 | |__  | |_) || (___   ___  ___ _   _ _| |_ _   _ 
 |  __| |  _ <  \___ \ / _ \/ __| | | | | __| | | |
 | |____| |_) | ____) |  __/ (__| |_| | | |_| |_| |
 |______|____/ |_____/ \___|\___|\__,_|_|\__|\__, |
                                                __/ |
                                               |___/ 
""" + RESET)
    print(BLUE + BOLD + "WJ-Tools • FB SECURITY AUDIT • TERMUX" + RESET)
    print("-" * 56)
    print(YELLOW + "Pemeriksaan panduan saja — tidak mencoba login atau menebak password." + RESET)
    print("Jangan masukkan password, OTP, cookie, atau token ke program ini.")
    print()

def checklist():
    clear()
    header()
    print(BOLD + "CHECKLIST KEAMANAN AKUN" + RESET)
    for i, item in enumerate(CHECKS, 1):
        print(f"{CYAN}{i:>2}.{RESET} [ ] {item}")
    print("\nPilih halaman resmi untuk meninjau pengaturan:")
    print("1. Keamanan dan login")
    print("2. Privasi")
    print("3. Pusat Bantuan")
    print("4. Pulihkan akun yang diretas")
    print("0. Kembali")
    while True:
        choice = input("\nPilihan: ").strip()
        if choice == "1":
            open_url(LINKS["security"])
        elif choice == "2":
            open_url(LINKS["privacy"])
        elif choice == "3":
            open_url(LINKS["help"])
        elif choice == "4":
            open_url(LINKS["recovery"])
        elif choice == "0":
            return
        else:
            print("Pilihan tidak valid.")

def phishing_tips():
    clear()
    header()
    print(BOLD + "CEK RISIKO PHISHING" + RESET)
    tips = [
        "Periksa alamat situs dengan teliti; situs resmi harus menggunakan domain facebook.com.",
        "Jangan masuk melalui tautan pendek atau pesan yang mendesak/mengancam.",
        "Facebook tidak perlu meminta kode OTP melalui chat.",
        "Jangan menginstal APK atau ekstensi yang menjanjikan akses akun rahasia.",
        "Jika sudah memasukkan kata sandi di situs mencurigakan, buka pengaturan resmi, ganti kata sandi, dan keluar dari sesi asing.",
    ]
    for tip in tips:
        print(f"{YELLOW}•{RESET} {tip}")
    print("\nPanduan pemulihan resmi: " + LINKS["recovery"])
    input("\nTekan Enter untuk kembali...")

def main():
    while True:
        clear()
        header()
        print(f"{GREEN}1.{RESET} Checklist pemeriksaan keamanan")
        print(f"{GREEN}2.{RESET} Buka pengaturan keamanan Facebook")
        print(f"{GREEN}3.{RESET} Cek risiko phishing")
        print(f"{GREEN}4.{RESET} Panduan pemulihan akun diretas")
        print(f"{RED}0.{RESET} Keluar")
        choice = input("\nPilih menu: ").strip()
        if choice == "1":
            checklist()
        elif choice == "2":
            open_url(LINKS["security"])
            input("Tekan Enter untuk kembali...")
        elif choice == "3":
            phishing_tips()
        elif choice == "4":
            open_url(LINKS["recovery"])
            input("Tekan Enter untuk kembali...")
        elif choice == "0":
            print("FB Security Audit ditutup. Jaga keamanan akun!")
            break
        else:
            input("Pilihan tidak valid. Tekan Enter...")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nKeluar dengan aman.")
