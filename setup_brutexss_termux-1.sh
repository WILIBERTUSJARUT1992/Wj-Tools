#!/data/data/com.termux/files/usr/bin/bash
set -e

# Setup BruteXSS di Termux.
# Gunakan hanya untuk menguji website milik sendiri atau yang Anda punya izin tertulis.
# Proyek ini memakai Python 2 yang sudah usang; instalasi bisa gagal pada Termux terbaru.

echo "[1/4] Memperbarui paket Termux..."
pkg update
pkg upgrade -y

echo "[2/4] Memasang Git dan Python..."
pkg install git python -y

echo "[3/4] Mengambil repositori BruteXSS..."
cd "$HOME"
if [ -d "$HOME/BruteXSS/.git" ]; then
  echo "Folder BruteXSS sudah ada; mengambil pembaruan..."
  git -C "$HOME/BruteXSS" pull
elif [ -d "$HOME/BruteXSS" ]; then
  echo "Folder $HOME/BruteXSS sudah ada tetapi bukan checkout Git."
  echo "Pindahkan atau ganti nama folder tersebut dahulu, lalu jalankan skrip lagi."
  exit 1
else
  git clone https://github.com/shawarkhanethicalhacker/BruteXSS.git "$HOME/BruteXSS"
fi

echo "[4/4] Selesai."
echo "Periksa README proyek untuk petunjuk dan kompatibilitas."
echo "Catatan: Python 2 sudah tidak didukung; jangan jalankan pada situs tanpa izin."
echo "Folder proyek: $HOME/BruteXSS"
