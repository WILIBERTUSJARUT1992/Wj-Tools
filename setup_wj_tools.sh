#!/data/data/com.termux/files/usr/bin/bash
set -e

# WJ-Tools setup/update untuk Termux.
# Tidak menyimpan username, password, atau token GitHub di dalam file.

REPO_URL="https://github.com/WILIBERTUSJARUT1992/WJ-Tools.git"
PROJECT_DIR="$HOME/WJ-Tools"

echo "[1/3] Memasang kebutuhan dasar..."
pkg update
pkg install git python -y

echo "[2/3] Mengambil atau memperbarui WJ-Tools..."
if [ -d "$PROJECT_DIR/.git" ]; then
    git -C "$PROJECT_DIR" pull --ff-only
elif [ -e "$PROJECT_DIR" ]; then
    echo "Folder $PROJECT_DIR sudah ada tetapi bukan repositori Git."
    echo "Pindahkan/ubah nama folder itu terlebih dahulu, lalu jalankan ulang."
    exit 1
else
    git clone "$REPO_URL" "$PROJECT_DIR"
fi

echo "[3/3] Menyiapkan dependensi opsional..."
if [ -f "$PROJECT_DIR/requirements.txt" ]; then
    python -m pip install -r "$PROJECT_DIR/requirements.txt"
fi

echo
echo "WJ-Tools siap di: $PROJECT_DIR"
echo "Untuk menjalankan menu utama, ketik:"
echo "cd ~/WJ-Tools && python hacker_toolkit.py"
echo
echo "Catatan: repositori publik tidak memerlukan login. Jangan simpan password"
echo "atau token GitHub di dalam skrip. Untuk repositori privat, gunakan autentikasi resmi GitHub."
