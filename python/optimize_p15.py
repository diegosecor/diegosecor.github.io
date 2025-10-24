"""
Optimiza y renombra imágenes en Images/p15/

Genera archivos WebP con nombres p15-01.webp, p15-02.webp, ...
Mantiene los originales PNGs por seguridad.

Uso: python optimize_p15.py
"""
from PIL import Image
import os

SRC_DIR = os.path.join('Images', 'p15')
OUT_PREFIX = 'p15-'
MAX_WIDTH = 1920
QUALITY = 85

def get_file_size_mb(path):
    return os.path.getsize(path) / (1024*1024)

def main():
    if not os.path.isdir(SRC_DIR):
        print(f"No existe el directorio: {SRC_DIR}")
        return

    files = [f for f in os.listdir(SRC_DIR) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
    files.sort()
    if not files:
        print('No hay imágenes para procesar en', SRC_DIR)
        return

    total_orig = 0.0
    total_opt = 0.0

    for i, fname in enumerate(files, start=1):
        in_path = os.path.join(SRC_DIR, fname)
        out_name = f"{OUT_PREFIX}{i:02d}.webp"
        out_path = os.path.join(SRC_DIR, out_name)

        print(f"Procesando {in_path} -> {out_path}")
        img = Image.open(in_path)
        if img.width > MAX_WIDTH:
            ratio = MAX_WIDTH / img.width
            new_h = int(img.height * ratio)
            img = img.resize((MAX_WIDTH, new_h), Image.Resampling.LANCZOS)
            print(f"  Redimensionada a {MAX_WIDTH}x{new_h}")
        else:
            print(f"  Tamaño original: {img.width}x{img.height}")

        img.save(out_path, 'WEBP', quality=QUALITY, method=6)

        orig_mb = get_file_size_mb(in_path)
        opt_mb = get_file_size_mb(out_path)
        total_orig += orig_mb
        total_opt += opt_mb
        red = (orig_mb - opt_mb) / orig_mb * 100 if orig_mb > 0 else 0
        print(f"  Original: {orig_mb:.2f} MB, Optimizada: {opt_mb:.2f} MB, Reducción: {red:.1f}%")

    print("\nResumen:")
    print(f"  Original total: {total_orig:.2f} MB")
    print(f"  Optimizado total: {total_opt:.2f} MB")
    if total_orig > 0:
        print(f"  Ahorro total: {(total_orig-total_opt):.2f} MB ({(total_orig-total_opt)/total_orig*100:.1f}%)")

if __name__ == '__main__':
    main()
