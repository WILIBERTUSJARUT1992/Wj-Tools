#!/usr/bin/env python3
import random
import shutil
import time

CHARS = "01アイウエオカキクケコサシスセソタチツテト"

def run():
    try:
        width = min(shutil.get_terminal_size((80, 24)).columns, 100)
        print("Efek Matrix berjalan. Tekan Ctrl+C untuk berhenti.")
        while True:
            line = "".join(random.choice(CHARS + "   ") for _ in range(width))
            print("\033[32m" + line + "\033[0m")
            time.sleep(0.07)
    except KeyboardInterrupt:
        print("\nEfek Matrix dihentikan.")

if __name__ == "__main__":
    run()
