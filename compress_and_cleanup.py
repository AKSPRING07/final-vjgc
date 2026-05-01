import os
import shutil
from PIL import Image

# 1. Cleanup Unused Pages
unused_pages = [
    'cart.html', 'checkout.html', 'domain-services.html', 'faq.html',
    'index-3.html', 'index-4.html', 'index-5.html', 'index-6.html',
    'index-7.html', 'index-8.html', 'project-details-v1.html',
    'project-details-v2.html', 'project-v1.html', 'project-v2.html',
    'project-v3.html', 'shop-details.html', 'shop-grid.html',
    'solar-solutions.html', 'testimonial.html'
]

templates_dir = 'templates'
print("Cleaning up unused templates...")
for page in unused_pages:
    path = os.path.join(templates_dir, page)
    if os.path.exists(path):
        os.remove(path)
        print(f"Removed: {path}")

# Remove public directory
public_dir = 'public'
if os.path.exists(public_dir):
    print("Removing public directory...")
    shutil.rmtree(public_dir)
    print("Removed public directory.")

# 2. Compress Images
static_images_dir = os.path.join('static', 'images')
SIZE_LIMIT_BYTES = 1 * 1024 * 1024  # 1MB
MAX_WIDTH = 1920

print("\nCompressing large images in static/images...")
for root, _, files in os.walk(static_images_dir):
    for file in files:
        if file.lower().endswith(('.jpg', '.jpeg', '.png')):
            filepath = os.path.join(root, file)
            size = os.path.getsize(filepath)
            
            if size > SIZE_LIMIT_BYTES:
                print(f"Optimizing: {filepath} ({size / (1024*1024):.2f} MB)")
                try:
                    with Image.open(filepath) as img:
                        # Convert to RGB if necessary (e.g. RGBA png to jpg)
                        if img.mode in ('RGBA', 'P'):
                            img = img.convert('RGB')
                        
                        # Resize if too large
                        if img.width > MAX_WIDTH:
                            ratio = MAX_WIDTH / img.width
                            new_size = (MAX_WIDTH, int(img.height * ratio))
                            img = img.resize(new_size, Image.Resampling.LANCZOS)
                        
                        # Save with lower quality to reduce size
                        img.save(filepath, format='JPEG', optimize=True, quality=60)
                        
                    new_size = os.path.getsize(filepath)
                    print(f"  -> Reduced to: {new_size / (1024*1024):.2f} MB")
                except Exception as e:
                    print(f"  -> Error optimizing {filepath}: {e}")

print("\nCleanup and compression complete.")
