from PIL import Image
import os

# Configuration
MAX_WIDTH = 1920
WEBP_QUALITY = 85

# Define the image folder
image_folder = r"c:\Users\diego\OneDrive\Documents\1AAA GITHUB WEB\diegosecor.github.io\Images\p14"

# Get all image files
image_files = [f for f in os.listdir(image_folder) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]

print(f"Found {len(image_files)} images to convert")

# Process each image
for filename in image_files:
    input_path = os.path.join(image_folder, filename)
    
    # Create output filename with .webp extension
    name_without_ext = os.path.splitext(filename)[0]
    output_filename = f"{name_without_ext}.webp"
    output_path = os.path.join(image_folder, output_filename)
    
    try:
        # Open and process image
        img = Image.open(input_path)
        
        # Convert RGBA to RGB if necessary
        if img.mode == 'RGBA':
            background = Image.new('RGB', img.size, (255, 255, 255))
            background.paste(img, mask=img.split()[3])
            img = background
        elif img.mode != 'RGB':
            img = img.convert('RGB')
        
        # Resize if width is larger than MAX_WIDTH
        if img.width > MAX_WIDTH:
            ratio = MAX_WIDTH / img.width
            new_height = int(img.height * ratio)
            img = img.resize((MAX_WIDTH, new_height), Image.Resampling.LANCZOS)
        
        # Save as WebP
        img.save(output_path, 'WEBP', quality=WEBP_QUALITY, method=6)
        
        # Get file sizes
        original_size = os.path.getsize(input_path) / (1024 * 1024)  # MB
        new_size = os.path.getsize(output_path) / (1024 * 1024)  # MB
        reduction = ((original_size - new_size) / original_size) * 100
        
        print(f"✓ {filename} -> {output_filename}")
        print(f"  {original_size:.2f} MB -> {new_size:.2f} MB ({reduction:.1f}% reduction)")
        
    except Exception as e:
        print(f"✗ Error processing {filename}: {str(e)}")

print("\nConversion complete!")
