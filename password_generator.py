#!/usr/bin/env python3
import secrets
import string

def generate(length=16, symbols=True):
    alphabet = string.ascii_letters + string.digits
    if symbols:
        alphabet += "!@#$%^&*()-_=+"
    return "".join(secrets.choice(alphabet) for _ in range(length))

def main():
    try:
        length = int(input("Panjang kata sandi (8-128, default 16): ").strip() or "16")
        if not 8 <= length <= 128:
            print("Panjang harus antara 8 dan 128.")
            return
        symbols = input("Gunakan simbol? [Y/n]: ").strip().lower() not in ("n", "tidak")
        print("\nKata sandi:", generate(length, symbols))
        print("Simpan di pengelola kata sandi yang aman.")
    except (ValueError, KeyboardInterrupt):
        print("\nDibatalkan atau input tidak valid.")

if __name__ == "__main__":
    main()
