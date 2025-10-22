"""
Script para optimizar imágenes PNG a WebP con alta calidad
Reduce el tamaño de archivo manteniendo excelente calidad visual
"""
from PIL import Image
import os

# Configuración
MAX_WIDTH = 1920  # Ancho máximo (suficiente para pantallas 4K)
WEBP_QUALITY = 85  # Calidad WebP (80-90 es óptimo)

# Lista de imágenes a optimizar
images_to_optimize = [
    (r"Images\p1\AA1.png", r"Images\p1\AA1.webp"),
    (r"Images\p2\AA2.png", r"Images\p2\AA2.webp"),
    (r"Images\p3\AA3.png", r"Images\p3\AA3.webp"),
    (r"Images\p4\AA4.png", r"Images\p4\AA4.webp"),
    (r"Images\p5\AA5.png", r"Images\p5\AA5.webp"),
]

def get_file_size_mb(filepath):
    """Obtiene el tamaño de archivo en MB"""
    return os.path.getsize(filepath) / (1024 * 1024)

def optimize_image(input_path, output_path):
    """Optimiza una imagen PNG a WebP"""
    print(f"\n🔄 Procesando: {input_path}")
    
    # Abrir imagen
    img = Image.open(input_path)
    
    # Si la imagen es más ancha que MAX_WIDTH, redimensionar
    if img.width > MAX_WIDTH:
        ratio = MAX_WIDTH / img.width
        new_height = int(img.height * ratio)
        img = img.resize((MAX_WIDTH, new_height), Image.Resampling.LANCZOS)
        print(f"   📐 Redimensionada a {MAX_WIDTH}x{new_height}px")
    else:
        print(f"   📐 Tamaño original: {img.width}x{img.height}px")
    
    # Guardar como WebP
    img.save(output_path, 'WEBP', quality=WEBP_QUALITY, method=6)
    
    # Mostrar resultados
    original_size = get_file_size_mb(input_path)
    optimized_size = get_file_size_mb(output_path)
    reduction = ((original_size - optimized_size) / original_size) * 100
    
    print(f"   📦 Original:   {original_size:.2f} MB")
    print(f"   ✅ Optimizada: {optimized_size:.2f} MB")
    print(f"   💾 Reducción:  {reduction:.1f}%")

def main():
    print("=" * 60)
    print("🖼️  OPTIMIZADOR DE IMÁGENES")
    print("=" * 60)
    print(f"Configuración:")
    print(f"  - Ancho máximo: {MAX_WIDTH}px")
    print(f"  - Calidad WebP: {WEBP_QUALITY}%")
    print(f"  - Imágenes a procesar: {len(images_to_optimize)}")
    
    total_original = 0
    total_optimized = 0
    
    for input_path, output_path in images_to_optimize:
        if os.path.exists(input_path):
            optimize_image(input_path, output_path)
            total_original += get_file_size_mb(input_path)
            total_optimized += get_file_size_mb(output_path)
        else:
            print(f"\n⚠️  No encontrado: {input_path}")
    
    print("\n" + "=" * 60)
    print("📊 RESUMEN TOTAL")
    print("=" * 60)
    print(f"Tamaño original total:   {total_original:.2f} MB")
    print(f"Tamaño optimizado total: {total_optimized:.2f} MB")
    print(f"Reducción total:         {((total_original - total_optimized) / total_original) * 100:.1f}%")
    print(f"Espacio ahorrado:        {total_original - total_optimized:.2f} MB")
    print("\n✨ ¡Optimización completada!")

if __name__ == "__main__":
    main()
