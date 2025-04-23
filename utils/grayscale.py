from PIL import Image


def grayscale_image(input_path, output_path):
    try:
        with Image.open(input_path) as img:
            grayscale_img = img.convert('L')
            
            output_format = output_path.split('.')[-1].upper()
            if output_format == 'JPG':
                output_format = 'JPEG'
            
            grayscale_img.save(output_path, format=output_format)
    
    except Exception as e:
        raise Exception(f"Failed to convert image to grayscale: {str(e)}")
