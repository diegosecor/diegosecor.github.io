"""
Optimiza y renombra imágenes en Images/p3.1/

Genera archivos WebP con nombres p3.1-01.webp, p3.1-02.webp, ...
Mantiene los originales por seguridad.

Uso: python optimize_p15.py
"""
from PIL import Image
import os

SRC_DIR = os.path.join('Images', 'p3.1')
OUT_PREFIX = 'p3.1-'
MAX_WIDTH = 1920
QUALITY = 85

def get_file_size_mb(path):
    return os.path.getsize(path) / (1024 * 1024)

def main():
    if not os.path.isdir(SRC_DIR):
        print(f"No existe el directorio: {SRC_DIR}")
        return

    files = [
        f for f in os.listdir(SRC_DIR)
        if f.lower().endswith(('.png', '.jpg', '.jpeg'))
    ]
    files.sort()

    if not files:
        print('No hay imágenes para procesar en', SRC_DIR)
        return

    total_orig = total_opt = 0.0

    for i, fname in enumerate(files, start=1):
        in_path = os.path.join(SRC_DIR, fname)
        out_path = os.path.join(SRC_DIR, f"{OUT_PREFIX}{i:02d}.webp")

        print(f"Procesando {in_path} -> {out_path}")

        with Image.open(in_path) as source:
            img = source.convert('RGB')

            if img.width > MAX_WIDTH:
                ratio = MAX_WIDTH / img.width
                new_h = int(img.height * ratio)
                img = img.resize(
                    (MAX_WIDTH, new_h),
                    Image.Resampling.LANCZOS
                )
                print(f"  Redimensionada a {MAX_WIDTH}x{new_h}")
            else:
                print(f"  Tamaño original: {img.width}x{img.height}")

            img.save(out_path, 'WEBP', quality=QUALITY, method=6)

        orig_mb = get_file_size_mb(in_path)
        opt_mb = get_file_size_mb(out_path)
        total_orig += orig_mb
        total_opt += opt_mb

        red = (orig_mb - opt_mb) / orig_mb * 100 if orig_mb else 0
        print(
            f"  Original: {orig_mb:.2f} MB, "
            f"Optimizada: {opt_mb:.2f} MB, "
            f"Reducción: {red:.1f}%"
        )

    print("\nResumen:")
    print(f"  Original total: {total_orig:.2f} MB")
    print(f"  Optimizado total: {total_opt:.2f} MB")
    if total_orig:
        ahorro = total_orig - total_opt
        print(f"  Ahorro total: {ahorro:.2f} MB ({ahorro / total_orig * 100:.1f}%)")

if __name__ == '__main__':
    main()