from PIL import Image


def rotate_image(input_path, output_path, angle=90):
    try:
        with Image.open(input_path) as img:
            rotated_img = img.rotate(angle, expand=True)
            
            output_format = output_path.split('.')[-1].upper()
            if output_format == 'JPG':
                output_format = 'JPEG'
            
            rotated_img.save(output_path, format=output_format)
    
    except Exception as e:
        raise Exception(f"Failed to rotate image: {str(e)}")
