"""
Script para optimizar imágenes de las carpetas p6-p11 a WebP con alta calidad
"""
from PIL import Image
import os

# Configuración
MAX_WIDTH = 1920  # Ancho máximo
WEBP_QUALITY = 85  # Calidad WebP

# Lista de imágenes a optimizar (p6-p11)
images_to_optimize = [
    # p6 - Convertir AVIF a WebP
    (r"Images\p6\06-02.avif", r"Images\p6\06-02.webp"),
    (r"Images\p6\06-03.avif", r"Images\p6\06-03.webp"),
    (r"Images\p6\06-04.avif", r"Images\p6\06-04.webp"),
    (r"Images\p6\06-05.avif", r"Images\p6\06-05.webp"),
    (r"Images\p6\06-06.avif", r"Images\p6\06-06.webp"),
    (r"Images\p6\06-07.avif", r"Images\p6\06-07.webp"),
    (r"Images\p6\06-08.avif", r"Images\p6\06-08.webp"),
    (r"Images\p6\06-09.avif", r"Images\p6\06-09.webp"),
    (r"Images\p6\06-10.avif", r"Images\p6\06-10.webp"),
    (r"Images\p6\06-11.avif", r"Images\p6\06-11.webp"),
    (r"Images\p6\06-12.avif", r"Images\p6\06-12.webp"),
    (r"Images\p6\06-13.avif", r"Images\p6\06-13.webp"),
    (r"Images\p6\06-14.avif", r"Images\p6\06-14.webp"),
    (r"Images\p6\06-15.avif", r"Images\p6\06-15.webp"),
    
    # p7 - Convertir JPG/PNG a WebP
    (r"Images\p7\07-01.jpg", r"Images\p7\07-01.webp"),
    (r"Images\p7\07-02.png", r"Images\p7\07-02.webp"),
    (r"Images\p7\07-03.jpg", r"Images\p7\07-03.webp"),
    (r"Images\p7\07-04.png", r"Images\p7\07-04.webp"),
    (r"Images\p7\07-05.jpg", r"Images\p7\07-05.webp"),
    (r"Images\p7\07-06.png", r"Images\p7\07-06.webp"),
    
    # p8 - Convertir PNG/GIF a WebP
    (r"Images\p8\08-01.png", r"Images\p8\08-01.webp"),
    (r"Images\p8\08-02.png", r"Images\p8\08-02.webp"),
    (r"Images\p8\08-03.png", r"Images\p8\08-03.webp"),
    (r"Images\p8\08-04.png", r"Images\p8\08-04.webp"),
    (r"Images\p8\08-05.png", r"Images\p8\08-05.webp"),
    (r"Images\p8\08-06.png", r"Images\p8\08-06.webp"),
    (r"Images\p8\08-07.png", r"Images\p8\08-07.webp"),
    (r"Images\p8\08-08.png", r"Images\p8\08-08.webp"),
    (r"Images\p8\08-09.png", r"Images\p8\08-09.webp"),
    (r"Images\p8\08-10.png", r"Images\p8\08-10.webp"),
    (r"Images\p8\08-11.gif", r"Images\p8\08-11.webp"),
    
    # p9 - Convertir JPG/PNG a WebP
    (r"Images\p9\09-01.jpg", r"Images\p9\09-01.webp"),
    (r"Images\p9\09-02.png", r"Images\p9\09-02.webp"),
    (r"Images\p9\09-03.jpg", r"Images\p9\09-03.webp"),
    
    # p10 - Convertir JPG/PNG a WebP
    (r"Images\p10\10-01.jpg", r"Images\p10\10-01.webp"),
    (r"Images\p10\10-02.png", r"Images\p10\10-02.webp"),
    (r"Images\p10\10-03.png", r"Images\p10\10-03.webp"),
    
    # p11 - Convertir JPG/PNG a WebP
    (r"Images\p11\11-01.jpg", r"Images\p11\11-01.webp"),
    (r"Images\p11\11-02.png", r"Images\p11\11-02.webp"),
    (r"Images\p11\11-03.jpg", r"Images\p11\11-03.webp"),
    (r"Images\p11\11-04.png", r"Images\p11\11-04.webp"),
    (r"Images\p11\11-05.jpg", r"Images\p11\11-05.webp"),
    (r"Images\p11\11-06.jpg", r"Images\p11\11-06.webp"),
    (r"Images\p11\11-07.jpg", r"Images\p11\11-07.webp"),
    (r"Images\p11\11-08.jpg", r"Images\p11\11-08.webp"),
    (r"Images\p11\11-09.jpg", r"Images\p11\11-09.webp"),
    (r"Images\p11\11-10.jpg", r"Images\p11\11-10.webp"),
    (r"Images\p11\11-11.png", r"Images\p11\11-11.webp"),
]

def get_file_size_mb(filepath):
    """Obtiene el tamaño de archivo en MB"""
    return os.path.getsize(filepath) / (1024 * 1024)

def optimize_image(input_path, output_path):
    """Optimiza una imagen a WebP"""
    print(f"\n🔄 Procesando: {input_path}")
    
    try:
        # Abrir imagen (soporta PNG, JPG, GIF, AVIF si pillow-avif-plugin está instalado)
        img = Image.open(input_path)
        
        # Convertir a RGB si es necesario (para GIF o imágenes con transparencia)
        if img.mode in ('RGBA', 'LA', 'P'):
            # Mantener transparencia si la tiene
            pass
        elif img.mode != 'RGB':
            img = img.convert('RGB')
        
        # Si la imagen es más ancha que MAX_WIDTH, redimensionar
        if img.width > MAX_WIDTH:
            ratio = MAX_WIDTH / img.width
            new_height = int(img.height * ratio)
            img = img.resize((MAX_WIDTH, new_height), Image.Resampling.LANCZOS)
            print(f"   📐 Redimensionada a {MAX_WIDTH}x{new_height}px")
        else:
            print(f"   📐 Tamaño: {img.width}x{img.height}px")
        
        # Guardar como WebP
        img.save(output_path, 'WEBP', quality=WEBP_QUALITY, method=6)
        
        # Mostrar resultados
        original_size = get_file_size_mb(input_path)
        optimized_size = get_file_size_mb(output_path)
        reduction = ((original_size - optimized_size) / original_size) * 100
        
        print(f"   📦 Original:   {original_size:.2f} MB")
        print(f"   ✅ Optimizada: {optimized_size:.2f} MB")
        print(f"   💾 Reducción:  {reduction:.1f}%")
        
    except Exception as e:
        print(f"   ❌ Error: {str(e)}")

def main():
    print("=" * 60)
    print("🖼️  OPTIMIZADOR DE IMÁGENES P6-P11")
    print("=" * 60)
    print(f"Configuración:")
    print(f"  - Ancho máximo: {MAX_WIDTH}px")
    print(f"  - Calidad WebP: {WEBP_QUALITY}%")
    print(f"  - Imágenes a procesar: {len(images_to_optimize)}")
    
    total_original = 0
    total_optimized = 0
    processed = 0
    
    for input_path, output_path in images_to_optimize:
        if os.path.exists(input_path):
            size_before = get_file_size_mb(input_path)
            optimize_image(input_path, output_path)
            if os.path.exists(output_path):
                total_original += size_before
                total_optimized += get_file_size_mb(output_path)
                processed += 1
        else:
            print(f"\n⚠️  No encontrado: {input_path}")
    
    print("\n" + "=" * 60)
    print("📊 RESUMEN TOTAL")
    print("=" * 60)
    print(f"Imágenes procesadas:     {processed}/{len(images_to_optimize)}")
    print(f"Tamaño original total:   {total_original:.2f} MB")
    print(f"Tamaño optimizado total: {total_optimized:.2f} MB")
    if total_original > 0:
        print(f"Reducción total:         {((total_original - total_optimized) / total_original) * 100:.1f}%")
        print(f"Espacio ahorrado:        {total_original - total_optimized:.2f} MB")
    print("\n✨ ¡Optimización completada!")

if __name__ == "__main__":
    main()
