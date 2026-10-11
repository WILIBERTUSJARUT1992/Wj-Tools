#!/usr/bin/env python3
import os
import platform
import shutil
import socket
import sys

def show():
    print("=== INFORMASI SISTEM ===")
    print(f"Sistem operasi : {platform.system()} {platform.release()}")
    print(f"Arsitektur     : {platform.machine()}")
    print(f"Versi Python   : {sys.version.split()[0]}")
    print(f"Nama perangkat : {platform.node() or 'Tidak tersedia'}")
    print(f"Direktori kerja: {os.getcwd()}")
    print(f"Nama host      : {socket.gethostname()}")
    usage = shutil.disk_usage(os.getcwd())
    print(f"Penyimpanan    : {usage.free // (1024**3)} GB tersedia dari {usage.total // (1024**3)} GB")
    print("\nCatatan: informasi bergantung pada izin dan lingkungan Termux.")

if __name__ == "__main__":
    show()
