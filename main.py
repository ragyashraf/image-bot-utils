#!/usr/bin/env python3

import argparse
import sys
import os
from utils import rotate_image, grayscale_image, compress_image, invert_image

# Import the Flask app for the web interface
from app import app

def validate_file_path(file_path, check_exists=True):
    if check_exists and not os.path.exists(file_path):
        return f"Error: Input file '{file_path}' does not exist."
    
    directory = os.path.dirname(file_path) or '.'
    if not os.path.exists(directory):
        return f"Error: Directory '{directory}' for the output file does not exist."
    
    return None


def validate_input_output(args):
    input_error = validate_file_path(args.input)
    if input_error:
        return input_error
    
    output_error = validate_file_path(args.output, check_exists=False)
    if output_error:
        return output_error
    
    valid_extensions = ['.jpg', '.jpeg', '.png', '.bmp', '.gif', '.tiff']
    input_ext = os.path.splitext(args.input.lower())[1]
    if input_ext not in valid_extensions:
        return f"Error: Input file must be an image (supported formats: {', '.join(valid_extensions)})"
    
    return None


def main():
    parser = argparse.ArgumentParser(description='Image-Bot-Utils: A toolkit for image processing')
    
    parser.add_argument('--input', '-i', required=True, help='Input image path')
    parser.add_argument('--output', '-o', required=True, help='Output image path')
    
    subparsers = parser.add_subparsers(dest='action', help='Image processing action')
    
    rotate = subparsers.add_parser('rotate', help='Rotate image')
    rotate.add_argument('--angle', '-a', type=float, default=90, help='Rotation angle (default: 90)')
    
    subparsers.add_parser('grayscale', help='Convert to grayscale')
    
    compress = subparsers.add_parser('compress', help='Compress image')
    compress.add_argument('--quality', '-q', type=int, default=60, help='Compression quality (0-100)')
    
    subparsers.add_parser('invert', help='Invert colors')
    
    args = parser.parse_args()
    
    if not args.action:
        parser.print_help()
        return 1
    
    error = validate_input_output(args)
    if error:
        print(error)
        return 1
    
    try:
        if args.action == 'rotate':
            rotate_image(args.input, args.output, args.angle)
            print(f"Image rotated by {args.angle} degrees and saved to {args.output}")
        
        elif args.action == 'grayscale':
            grayscale_image(args.input, args.output)
            print(f"Image converted to grayscale and saved to {args.output}")
        
        elif args.action == 'compress':
            if args.quality < 0 or args.quality > 100:
                print("Error: Quality must be between 0 and 100")
                return 1
            
            compress_image(args.input, args.output, args.quality)
            print(f"Image compressed with quality {args.quality} and saved to {args.output}")
        
        elif args.action == 'invert':
            invert_image(args.input, args.output)
            print(f"Image colors inverted and saved to {args.output}")
    
    except Exception as e:
        print(f"Error processing image: {str(e)}")
        return 1
    
    return 0


if __name__ == "__main__":
    # When run directly, use CLI
    sys.exit(main())
