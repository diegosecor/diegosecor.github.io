from PIL import Image
import os

# Directorio de imágenes
img_dir = r"c:\Users\diego\OneDrive\Documents\1AAA GITHUB WEB\diegosecor.github.io\Images\p2"

# Lista de imágenes PNG a convertir
png_images = [
    "Asset 259.png",
    "Asset 260.png",
    "Asset 267.png",
    "Asset 268.png",
    "Asset 276.png",
    "Asset 277.png",
    "Asset 278.png",
    "Asset 279.png",
    "Asset 280.png",
    "Asset 281.png",
    "Asset 282.png",
    "Asset 283.png",
    "Asset 284.png",
    "Asset 285.png",
    "Asset 286.png",
    "Asset 287.png"
]

for png_file in png_images:
    png_path = os.path.join(img_dir, png_file)
    webp_file = png_file.replace('.png', '.webp')
    webp_path = os.path.join(img_dir, webp_file)
    
    if os.path.exists(png_path):
        # Abrir imagen PNG
        img = Image.open(png_path)
        
        # Convertir a RGB si tiene canal alpha
        if img.mode in ('RGBA', 'LA', 'P'):
            background = Image.new('RGB', img.size, (255, 255, 255))
            if img.mode == 'P':
                img = img.convert('RGBA')
            background.paste(img, mask=img.split()[-1] if img.mode == 'RGBA' else None)
            img = background
        
        # Guardar como WebP
        img.save(webp_path, 'WEBP', quality=85)
        print(f"Converted: {png_file} -> {webp_file}")
    else:
        print(f"File not found: {png_file}")

print("\nConversion complete!")
