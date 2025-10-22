from PIL import Image
import os

# Ruta de las imágenes
image_folder = "Images/p1"
output_gif = "Images/p1/animation_b.gif"

# Lista de imágenes en orden (B1 a B5)
images = []
for i in range(1, 6):
    img_path = os.path.join(image_folder, f"B{i}.png")
    if os.path.exists(img_path):
        img = Image.open(img_path)
        # Convertir a RGB si es necesario (para compatibilidad con GIF)
        if img.mode in ('RGBA', 'LA', 'P'):
            background = Image.new('RGB', img.size, (255, 255, 255))
            if img.mode == 'P':
                img = img.convert('RGBA')
            background.paste(img, mask=img.split()[-1] if img.mode == 'RGBA' else None)
            img = background
        images.append(img)
        print(f"Agregada: B{i}.png")
    else:
        print(f"No encontrada: B{i}.png")

if images:
    # Crear GIF (duration en milisegundos, 200ms)
    images[0].save(
        output_gif,
        save_all=True,
        append_images=images[1:],
        duration=200,  # 200ms por frame
        loop=0  # 0 = loop infinito
    )
    print(f"\n✓ GIF creado: {output_gif}")
    print(f"  Total de frames: {len(images)}")
    print(f"  Duración por frame: 200ms")
else:
    print("No se encontraron imágenes para crear el GIF")
