#!/data/data/com.termux/files/usr/bin/bash
set -e

echo "[WJ-Tools] Memeriksa Python..."
if ! command -v python >/dev/null 2>&1; then
  pkg install python -y
fi

echo "[WJ-Tools] Memasang dependensi..."
python -m pip install --upgrade pip
python -m pip install colorama

echo "[WJ-Tools] Selesai. Jalankan: python hacker_toolkit.py"
