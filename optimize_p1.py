from PIL import Image
import os

# Directorio de imágenes
img_dir = r"c:\Users\diego\OneDrive\Documents\1AAA GITHUB WEB\diegosecor.github.io\Images\p1"

# Lista de imágenes PNG usadas en 01.html
png_images = [
    "5aMap.png",
    "3amodel.png",
    "3bmodel.png",
    "4aexplo.png",
    "Asset 290.png",
    "Asset 349.png",
    "Asset 294.png",
    "Asset 347.png",
    "Asset 291.png",
    "Asset 292.png",
    "Asset 293.png"
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
