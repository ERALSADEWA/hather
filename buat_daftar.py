#!/usr/bin/env python3
"""Membuat md/index.json (daftar dokumen untuk dokumen.html).

Jalankan setiap kali menambah, menghapus, atau mengganti nama berkas .md:
    cd /var/www/html && python3 buat_daftar.py

Aturan:
- Semua berkas *.md di dalam folder md/ (termasuk subfolder) dimasukkan.
- Judul diambil dari baris '# ' pertama; kalau tidak ada, dari nama berkas.
- Grup diambil dari nama subfolder; berkas langsung di md/ masuk grup "Ringkasan".
- Urutan grup dan berkas bisa diatur lewat daftar URUTAN_GRUP dan URUTAN_BERKAS di bawah.
"""
import json
import os
import re
import sys

DASAR = os.path.dirname(os.path.abspath(__file__))
FOLDER = os.path.join(DASAR, "md")

NAMA_GRUP = {
    "": "Ringkasan", "proyek": "Proyek", "tim": "Tim", "panduan": "Panduan langkah",
    "desain": "Rancangan", "internal": "Internal",
}
URUTAN_GRUP = ["", "tim", "panduan", "desain", "proyek", "internal"]
URUTAN_BERKAS = [
    "penjelasan.md",
    "tim/PEMBAGIAN_TUGAS.md", "tim/LINIMASA_KELOMPOK.md", "tim/RENCANA_VIDEO.md",
    "panduan/LINIMASA_PC.md", "panduan/PANDUAN_LENGKAP.md", "panduan/RESET_MYSQL_DARI_NOL.md",
    "panduan/LANGKAH_MIGRASI.md", "panduan/LANGKAH_BACKUP.md", "panduan/LANGKAH_PELAPISAN.md",
]


def judul_dari(jalur, nama):
    try:
        with open(jalur, encoding="utf-8-sig") as f:
            dalam_kode = False
            for baris in f:
                if baris.lstrip().startswith("```"):
                    dalam_kode = not dalam_kode
                    continue
                if not dalam_kode:
                    m = re.match(r"#\s+(.+?)\s*#*\s*$", baris)
                    if m:
                        return m.group(1).strip()
    except OSError:
        pass
    return os.path.splitext(os.path.basename(nama))[0].replace("_", " ")


def main():
    if not os.path.isdir(FOLDER):
        sys.exit("Folder md/ tidak ditemukan di " + DASAR)
    daftar = []
    for akar, _, berkas in os.walk(FOLDER):
        for b in berkas:
            if not b.lower().endswith(".md"):
                continue
            jalur = os.path.join(akar, b)
            rel = os.path.relpath(jalur, FOLDER).replace(os.sep, "/")
            grup_kode = rel.split("/")[0] if "/" in rel else ""
            daftar.append({
                "berkas": rel,
                "judul": judul_dari(jalur, rel),
                "grup": NAMA_GRUP.get(grup_kode, grup_kode.replace("_", " ").title()),
                "_g": grup_kode,
            })

    def kunci(d):
        g = URUTAN_GRUP.index(d["_g"]) if d["_g"] in URUTAN_GRUP else len(URUTAN_GRUP)
        b = URUTAN_BERKAS.index(d["berkas"]) if d["berkas"] in URUTAN_BERKAS else len(URUTAN_BERKAS)
        return (g, d["_g"], b, d["berkas"].lower())

    daftar.sort(key=kunci)
    for d in daftar:
        d.pop("_g")
    with open(os.path.join(FOLDER, "index.json"), "w", encoding="utf-8") as f:
        json.dump({"versi": 1, "dokumen": daftar}, f, ensure_ascii=False, indent=2)
        f.write("\n")
    print("md/index.json dibuat: %d dokumen" % len(daftar))
    for d in daftar:
        print("  [%s] %s  (%s)" % (d["grup"], d["judul"], d["berkas"]))


if __name__ == "__main__":
    main()
