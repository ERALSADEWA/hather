# Linimasa dan Dokumen Kelompok PDP (GitHub Pages)

Situs statis: tidak butuh server, PHP, atau database. Isi: `index.html` (linimasa), `dokumen.html` (pembaca semua `.md`), `md/` (dokumen), `status.json` (status bersama), `alur.png`, `assets/` (pustaka lokal, tanpa CDN), `buat_daftar.py`, `.nojekyll`.

## Pasang di GitHub Pages
1. Buat repo baru di GitHub, misalnya `linimasa-pdp`.
2. Unggah isi folder ini ke repo. Untuk berkas banyak, lebih mudah: di PC, ekstrak zip, lalu `git init`, `git add .`, `git commit -m "situs"`, `git branch -M main`, `git remote add origin https://github.com/AKUN/linimasa-pdp.git`, `git push -u origin main`. Berkas `.nojekyll` harus ikut (berkas tersembunyi).
3. Buka **Settings → Pages**. Pada "Build and deployment" pilih **Deploy from a branch**, branch `main`, folder `/ (root)`, lalu **Save**.
4. Setelah 1 sampai 2 menit, alamatnya: `https://AKUN.github.io/linimasa-pdp/`.
5. Beri akses edit ke Reza dan Hafiz: **Settings → Collaborators → Add people**.

## Cara status dibagikan
1. Ubah status di halaman (tersimpan dulu di perangkatmu). Pilih nama di kolom "Saya" supaya tercatat.
2. Klik **Salin status**.
3. Klik **Edit di GitHub** (muncul otomatis di alamat `github.io`), pilih semua isi `status.json`, tempel, lalu **Commit changes**.
4. Orang lain melihatnya setelah memuat ulang. GitHub Pages bisa menunda beberapa menit. Halaman memeriksa `status.json` tiap menit.
5. Kalau dua orang mengubah di waktu berdekatan, klik **Salin status** lagi sebelum menempel. Entri yang lebih baru (menurut waktu) menang.
6. **Impor** menempel JSON dari anggota lain tanpa lewat GitHub.

## Menambah atau mengganti dokumen
- Taruh `.md` di folder `md/` (subfolder = nama grup). Gambar ditaruh di folder yang sama dan ditulis dengan jalur relatif.
- Setelah menambah, menghapus, atau mengganti nama dokumen: jalankan `python3 buat_daftar.py` (atau `python buat_daftar.py` di Windows) di folder ini, lalu commit juga `md/index.json`. Mengganti isi dokumen yang sudah ada tidak perlu menjalankannya.
- Judul yang diawali `[ ]` dan daftar `- [ ]` menjadi kotak centang yang tersimpan di browser masing-masing. Blok ```` ```mermaid ```` digambar sebagai diagram.

## Kata sandi halaman
Bawaan: `OnnoPurbo`. Untuk menggantinya:
```
python -c "import hashlib;print(hashlib.sha256(b'KataSandiBaru').hexdigest())"
```
Salin hasilnya ke `HASH_SANDI` di `assets/konfig.js`, lalu commit.

## PENTING: situs ini publik
- Repo dan situs GitHub Pages bersifat **publik** (repo privat dengan Pages butuh paket berbayar). Kata sandi di halaman hanyalah pintu di browser, bukan pengaman: semua `.md` dan `status.json` tetap bisa dibuka langsung lewat alamat berkasnya, dan isi halaman terbaca lewat "View source".
- **Sebelum diunggah, tinjau isi `md/`.** Folder `md/internal/` (bahan diskusi kelompok dan perbandingan dengan paket anggota lain) sengaja TIDAK disertakan di paket ini; jangan ditambahkan kembali ke repo publik. Dokumen rancangan (`md/desain/`) dan panduan langkah juga akan terbaca siapa pun, termasuk tim lain, sebelum batas kirim. Hapus yang tidak ingin dibuka.
- Jangan pernah mengunggah dataset, dump SQL, kunci, file keyring, backup, atau password. Folder ini tidak memuat satu pun.
- Jangan menulis hal sensitif di kolom catatan.
- Nama Eral, Reza, Hafiz terlihat publik.
