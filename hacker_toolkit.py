#!/usr/bin/env python3
from banner import show_banner
import subprocess
import sys

def run_script(name):
    try:
        subprocess.run([sys.executable, name], check=False)
    except KeyboardInterrupt:
        print("\nKembali ke menu.")

def main():
    while True:
        show_banner()
        print("[1] Efek Matrix")
        print("[2] Informasi sistem")
        print("[3] Generator kata sandi")
        print("[0] Keluar")
        choice = input("\nPilih menu: ").strip()
        if choice == "1":
            run_script("matrix_effect.py")
        elif choice == "2":
            run_script("system_info.py")
        elif choice == "3":
            run_script("password_generator.py")
        elif choice == "0":
            print("Terima kasih telah menggunakan WJ-Tools.")
            break
        else:
            print("Pilihan tidak dikenal.")
        input("\nTekan Enter untuk kembali ke menu...")

if __name__ == "__main__":
    main()
