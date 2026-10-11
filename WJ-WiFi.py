#!/usr/bin/env python3
# WJ-WiFi — safe Wi-Fi information and security checklist for Termux.
# No password cracking, credential capture, or network attacks.
import os, platform, shutil, subprocess

CYAN="\033[96m"; GREEN="\033[92m"; YELLOW="\033[93m"; RESET="\033[0m"; BOLD="\033[1m"

def run_command(args):
    try:
        r=subprocess.run(args,capture_output=True,text=True,timeout=5)
        return (r.stdout or r.stderr).strip()
    except (FileNotFoundError, subprocess.TimeoutExpired, OSError):
        return ""

def header():
    os.system("clear")
    print(CYAN+BOLD+r"""
 __        ___      _  _____ _
 \ \      / / |    | |/ ____(_)
  \ \ /\ / /| |    | | |     _  __ _
   \ V  V / | |    | | |    | |/ _` |
    \_/\_/  | |____| | |____| | (_| |
            |______|_|\_____|_|\__,_|
"""+RESET)
    print(GREEN+"WJ-WiFi • Termux Wi-Fi Safety Helper"+RESET)
    print("Pemeriksaan dasar dan panduan keamanan.")
    print(YELLOW+"Tidak membobol kata sandi atau menyerang jaringan."+RESET)
    print("-"*52)

def wait():
    input("\nTekan Enter untuk kembali...")

def device_info():
    header()
    print(BOLD+"INFORMASI PERANGKAT"+RESET)
    print("Sistem:",platform.system(),platform.release())
    print("Python:",platform.python_version())
    print("Arsitektur:",platform.machine())
    print("Termux:",os.environ.get("PREFIX","Tidak terdeteksi"))
    wait()

def wifi_info():
    header()
    print(BOLD+"INFORMASI KONEKSI WI-FI"+RESET)
    if shutil.which("termux-wifi-connectioninfo"):
        out=run_command(["termux-wifi-connectioninfo"])
        print(out if out else "Informasi koneksi tidak tersedia.")
    else:
        print("Perintah Termux:API belum tersedia.")
        print("Opsional: instal aplikasi Termux:API dari sumber yang sama dengan Termux,")
        print("lalu jalankan: pkg install termux-api")
        print("Kemudian coba lagi.")
    print("\nAndroid dapat meminta izin yang diperlukan untuk informasi Wi-Fi.")
    wait()

def checklist():
    header()
    print(BOLD+"CHECKLIST KEAMANAN ROUTER MILIK SENDIRI"+RESET)
    items=[
        "Gunakan WPA2-AES atau WPA3 jika tersedia.",
        "Ganti kata sandi admin bawaan router.",
        "Gunakan kata sandi Wi-Fi kuat dan unik.",
        "Matikan WPS jika tidak diperlukan.",
        "Perbarui firmware router dari sumber resmi.",
        "Tinjau perangkat tersambung melalui aplikasi/admin router resmi.",
        "Gunakan jaringan tamu untuk pengunjung bila tersedia.",
        "Jangan menguji jaringan lain tanpa izin yang jelas.",
    ]
    for i,item in enumerate(items,1): print(f"{CYAN}{i:>2}.{RESET} [ ] {item}")
    print("\nTool ini memberikan panduan; tidak menyerang atau menguji router.")
    wait()

def main():
    while True:
        header()
        print("1. Informasi perangkat")
        print("2. Informasi koneksi Wi-Fi (jika didukung)")
        print("3. Checklist keamanan router sendiri")
        print("0. Keluar")
        c=input("\nPilih menu: ").strip()
        if c=="1": device_info()
        elif c=="2": wifi_info()
        elif c=="3": checklist()
        elif c=="0":
            print("WJ-WiFi ditutup."); break
        else: input("Pilihan tidak valid. Tekan Enter...")

if __name__=="__main__":
    try: main()
    except KeyboardInterrupt: print("\nProgram dihentikan.")
