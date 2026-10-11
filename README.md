# WJ-Tools

Toolkit terminal sederhana untuk **Termux**. Berisi efek Matrix, banner, informasi sistem, dan generator kata sandi. Semua fitur bersifat lokal dan tidak melakukan akses tanpa izin ke perangkat atau jaringan lain.

## Fitur
- `banner.py` — tampilan banner WJ-Tools
- `matrix_effect.py` — animasi Matrix di terminal
- `system_info.py` — informasi dasar perangkat/lingkungan
- `password_generator.py` — membuat kata sandi acak
- `hacker_toolkit.py` — menu utama untuk menjalankan fitur
- `install.sh` — pemasangan dependensi dasar

## Instalasi di Termux

```bash
pkg update
pkg install python git -y
git clone https://github.com/WILIBERTUSJARUT1992/WJ-Tools.git
cd WJ-Tools
chmod +x install.sh
./install.sh
python hacker_toolkit.py
```

Jika repositori belum diunggah ke GitHub, unduh ZIP proyek ini lalu ekstrak di Termux, kemudian masuk ke foldernya dan jalankan `python hacker_toolkit.py`.

## Menjalankan fitur langsung

```bash
python banner.py
python matrix_effect.py
python system_info.py
python password_generator.py
```

## Catatan keamanan
Gunakan toolkit ini hanya pada perangkat sendiri atau perangkat yang Anda punya izin untuk kelola. Proyek ini tidak berisi pencurian kredensial, eksploitasi, pemindaian target, atau akses jarak jauh.
