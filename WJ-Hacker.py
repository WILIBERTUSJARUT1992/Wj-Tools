#!/usr/bin/env python3
# WJ-Hacker: safe terminal hacking-style simulation for Android Termux.
# SIMULATION ONLY: no network scanning, exploitation, account access, or data collection.

import os
import random
import shutil
import sys
import time

GREEN = "\033[92m"
LIME = "\033[32m"
CYAN = "\033[96m"
BLUE = "\033[94m"
YELLOW = "\033[93m"
RED = "\033[91m"
DIM = "\033[2m"
BOLD = "\033[1m"
RESET = "\033[0m"

def clear():
    os.system("clear")

def pause():
    input(f"\n{DIM}Tekan Enter untuk kembali ke menu...{RESET}")

def type_out(text, delay=0.012, color=GREEN):
    sys.stdout.write(color)
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write(RESET + "\n")

def progress(label, seconds=1.5, width=28):
    print(f"{CYAN}{label}{RESET}")
    steps = 28
    for i in range(steps + 1):
        filled = int(width * i / steps)
        bar = "█" * filled + "░" * (width - filled)
        pct = int(100 * i / steps)
        sys.stdout.write(f"\r{GREEN}[{bar}] {pct:3d}%{RESET}")
        sys.stdout.flush()
        time.sleep(seconds / steps)
    print("\n")

def banner():
    print(GREEN + BOLD + r"""
 __        ______     _   _            _
 \ \      / / ___|   | | | | __ _  ___| | _____ _ __
  \ \ /\ / /\___ \   | |_| |/ _` |/ __| |/ / _ \ '__|
   \ V  V /  ___) |  |  _  | (_| | (__|   <  __/ |
    \_/\_/  |____/   |_| |_|\__,_|\___|_|\_\___|_|
""" + RESET)
    print(CYAN + "WJ-Hacker • TERMUX TERMINAL SIMULATION" + RESET)
    print(YELLOW + "SIMULASI VISUAL SAJA — tidak ada peretasan sungguhan." + RESET)
    print("-" * 56)

def fake_console():
    clear()
    banner()
    type_out("[SIMULASI] Menginisialisasi terminal virtual...", 0.018)
    progress("Memuat modul visual", 1.4)
    type_out("[SIMULASI] Membuat koneksi fiktif ke server latihan...", 0.012, CYAN)
    time.sleep(0.5)
    progress("Menjalankan animasi visual", 1.8)
    for _ in range(12):
        line = "".join(random.choice("0123456789ABCDEF") for _ in range(48))
        print(f"{LIME}{line}{RESET}")
        time.sleep(0.07)
    type_out("[SIMULASI SELESAI] Tidak ada perangkat atau akun yang diakses.", 0.015, YELLOW)
    pause()

def matrix_rain():
    clear()
    banner()
    print("Tekan Ctrl+C untuk menghentikan efek Matrix.\n")
    try:
        while True:
            width = shutil.get_terminal_size((70, 20)).columns
            line = "".join(random.choice("01アイウエオカキクケコサシスセソ") for _ in range(min(width, 90)))
            print(GREEN + line + RESET)
            time.sleep(0.06)
    except KeyboardInterrupt:
        print(RESET + "\nEfek Matrix dihentikan.")
        time.sleep(0.5)

def fake_log():
    clear()
    banner()
    events = [
        ("[DEMO]", "Memulai sesi latihan lokal"),
        ("[DEMO]", "Memuat antarmuka terminal"),
        ("[INFO]", "Tidak ada permintaan jaringan yang dibuat"),
        ("[INFO]", "Tidak ada kredensial yang diminta atau disimpan"),
        ("[OK]", "Mode simulasi aman aktif"),
    ]
    for tag, msg in events:
        color = GREEN if tag == "[OK]" else CYAN
        print(f"{color}{time.strftime('%H:%M:%S')} {tag:<8}{RESET} {msg}")
        time.sleep(0.5)
    pause()

def main():
    while True:
        clear()
        banner()
        print(f"{GREEN}1.{RESET} Simulasi peretasan (visual)")
        print(f"{GREEN}2.{RESET} Efek Matrix")
        print(f"{GREEN}3.{RESET} Log terminal demo")
        print(f"{GREEN}4.{RESET} Tentang dan batasan keamanan")
        print(f"{RED}0.{RESET} Keluar")
        choice = input("\nPilih menu: ").strip()
        if choice == "1":
            fake_console()
        elif choice == "2":
            matrix_rain()
            pause()
        elif choice == "3":
            fake_log()
        elif choice == "4":
            clear()
            banner()
            print("WJ-Hacker adalah simulasi visual untuk belajar terminal.")
            print("Tidak memindai jaringan, mengeksploitasi sistem,")
            print("mengakses akun, atau mengumpulkan data.")
            pause()
        elif choice == "0":
            print("WJ-Hacker ditutup. Tetap gunakan teknologi secara bertanggung jawab.")
            break
        else:
            input("Pilihan tidak valid. Tekan Enter...")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(RESET + "\nProgram dihentikan dengan aman.")
