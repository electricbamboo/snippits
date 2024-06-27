import os
import sys
import subprocess
from PIL import Image

def install_pillow():
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pillow"])

try:
    from PIL import Image
except ImportError:
    install = input("Pillow is not installed. Do you want to install it now? (Y/N): ").strip().lower()
    if install == 'y':
        install_pillow()
        from PIL import Image
    else:
        print("Pillow is required to run this script. Exiting.")
        sys.exit(1)

def convert_image_to_webp(input_image_path):
    output_image_path = os.path.splitext(input_image_path)[0] + '.webp'
    if not os.path.exists(output_image_path):
        with Image.open(input_image_path) as img:
            img.save(output_image_path, 'webp')
            print(f"Converted: {input_image_path} -> {output_image_path}")
    else:
        print(f"WebP file already exists for {input_image_path}, skipping conversion.")

def process_directory(directory_path):
    for root, _, files in os.walk(directory_path):
        for file in files:
            if file.lower().endswith(('.jpg', '.jpeg', '.png')):
                file_path = os.path.join(root, file)
                convert_image_to_webp(file_path)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python webpX.py input_file_or_directory")
        sys.exit(1)

    input_path = sys.argv[1]

    if os.path.isfile(input_path):
        if input_path.lower().endswith(('.jpg', '.jpeg', '.png')):
            convert_image_to_webp(input_path)
        else:
            print("The file is not a JPG or PNG. Please provide a valid file.")
    elif os.path.isdir(input_path):
        process_directory(input_path)
    else:
        print("The path provided is neither a file nor a directory. Please provide a valid path.")
