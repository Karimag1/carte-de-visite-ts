"""Génère le QR code qui ouvre la carte : python3 make_qr.py https://adresse-de-la-carte/"""
import sys
import segno

url = sys.argv[1] if len(sys.argv) > 1 else "https://exemple.github.io/carte-louis-hage/"
out = sys.argv[2] if len(sys.argv) > 2 else "."
qr = segno.make(url, error="M", micro=False)
qr.save(f"{out}/qr-carte.png", scale=30, border=4, dark="#0f1d5a", light="#ffffff")
qr.save(f"{out}/qr-carte.svg", scale=10, border=4, dark="#0f1d5a", light="#ffffff")
print(f"QR code généré pour {url} -> {out}/qr-carte.png et qr-carte.svg")
