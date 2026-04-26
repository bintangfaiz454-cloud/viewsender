# 🔥 VIEW SENDER - PENAMBAH VIEWS WEBSITE

**Tools Termux untuk menambah views / kunjungan website secara otomatis**

> ⚠️ **Peringatan: Hanya untuk website MILIK SENDIRI. Gunakan secara bijak, resiko ditanggung pengguna.**

---

## 📌 APA ITU VIEW SENDER?

View Sender adalah script Python yang **mengirim request HTTP ke website target** secara berulang.

Setiap 1 request yang berhasil = **+1 view** tercatat di server website.

---

## 🎯 FUNGSI UTAMA

| Fungsi | Keterangan |
| :--- | :--- |
| ✅ **Menambah views** | Meningkatkan jumlah kunjungan website |
| ✅ **Menaikkan traffic** | Membuat website terlihat ramai |
| ✅ **Testing performa** | Menguji ketahanan server sendiri |

---

## 🚀 CARA INSTALL LENGKAP (Termux)

Jalankan perintah berikut **satu per satu** di Termux:

```
pkg update && pkg upgrade -y
pkg install git python -y
pip install requests
git clone https://github.com/bintangfaiz454-cloud/viewsender.git
cd viewsender
python viewsender.py

📝 CARA PAKAI

Setelah menjalankan python viewsender.py, ikuti petunjuk di layar:

1. Masukkan URL target
      Contoh: https://bintangtools.diskon.cloud
2. Masukkan jumlah views
      Contoh: 100
3. Tunggu proses selesai
4. Lihat hasil
      ✅ Berapa views berhasil
      ❌ Berapa views gagal

---

📸 CONTOH TAMPILAN

```
┌─[MASUKKAN URL TARGET]
└────► https://bintangtools.diskon.cloud

┌─[MASUKKAN JUMLAH VIEWS]
└────► 50

══════════════════════════════════════════════════════════
 TARGET: https://bintangtools.diskon.cloud
 TOTAL VIEWS: 50
══════════════════════════════════════════════════════════

⏳ MENYIAPKAN MATA SERVER...██████████████████████████████ 100%

✅ VIEW 1/50 BERHASIL
✅ VIEW 2/50 BERHASIL
✅ VIEW 3/50 BERHASIL
...
✅ VIEW 50/50 BERHASIL

══════════════════════════════════════════════════════════
 PROSES SELESAI!
✅ BERHASIL : 50 views
❌ GAGAL    : 0 views
 TARGET   : https://bintangtools.diskon.cloud
══════════════════════════════════════════════════════════


---

⚙️ FITUR YANG TERSEDIA

Fitur Keterangan
✅ Random User-Agent Berpura-pura jadi perangkat berbeda
✅ Loading bar warna-warni Animasi proses pengiriman
✅ Laporan lengkap Berhasil & gagal tampil jelas
✅ Timeout handling Tidak menggantung saat error
✅ Simple input Hanya URL + jumlah views

---

⚠️ BATASAN & TANGGUNG JAWAB

Boleh ✅ Tidak Boleh ❌
Website sendiri Website orang lain
Testing performa server Manipulasi iklan / AdSense
Belajar & riset DDoS / serangan ilegal

Melanggar UU ITE, resiko pidana ditanggung pengguna.

---

🛠️ TROUBLESHOOTING

Masalah Solusi
command not found pkg install git python
No module named 'requests' pip install requests
Permission denied termux-setup-storage
Koneksi timeout / gagal Cek koneksi internet & pastikan URL benar

---

👤 AUTHOR

Bintang
team : BINTANGTOOLS

---

📄 LICENSE

MIT License — Bebas dipakai, dimodifikasi, dan didistribusikan untuk keperluan legal.

```
