from PIL import Image, ImageOps


def invert_image(input_path, output_path):
    try:
        with Image.open(input_path) as img:
            if img.mode == 'RGBA':
                r, g, b, a = img.split()
                rgb_image = Image.merge('RGB', (r, g, b))
                inverted_rgb = ImageOps.invert(rgb_image)
                r, g, b = inverted_rgb.split()
                inverted_img = Image.merge('RGBA', (r, g, b, a))
            else:
                if img.mode not in ['RGB', 'L']:
                    img = img.convert('RGB')
                
                inverted_img = ImageOps.invert(img)
            
            output_format = output_path.split('.')[-1].upper()
            if output_format == 'JPG':
                output_format = 'JPEG'
            
            inverted_img.save(output_path, format=output_format)
    
    except Exception as e:
        raise Exception(f"Failed to invert image: {str(e)}")
