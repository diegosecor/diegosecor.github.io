from PIL import Image
import os

# Ruta de las imágenes
image_folder = "Images/p1"
output_gif = "Images/p1/animation.gif"

# Lista de imágenes en orden (a1 a a28)
images = []
for i in range(1, 29):
    img_path = os.path.join(image_folder, f"a{i}.png")
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
        print(f"Agregada: a{i}.png")
    else:
        print(f"No encontrada: a{i}.png")

if images:
    # Crear GIF (duration en milisegundos, 300ms = más lento)
    images[0].save(
        output_gif,
        save_all=True,
        append_images=images[1:],
        duration=300,  # 300ms por frame (ajusta para más rápido/lento)
        loop=0  # 0 = loop infinito
    )
    print(f"\n✓ GIF creado: {output_gif}")
    print(f"  Total de frames: {len(images)}")
    print(f"  Duración por frame: 300ms")
else:
    print("No se encontraron imágenes para crear el GIF")
