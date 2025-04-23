from PIL import Image


def compress_image(input_path, output_path, quality=60):
    try:
        with Image.open(input_path) as img:
            if img.mode == 'RGBA':
                background = Image.new('RGB', img.size, (255, 255, 255))
                background.paste(img, mask=img.split()[3])
                img = background
            elif img.mode != 'RGB':
                img = img.convert('RGB')
            
            img.save(output_path, format='JPEG', quality=quality, optimize=True)
    
    except Exception as e:
        raise Exception(f"Failed to compress image: {str(e)}")
