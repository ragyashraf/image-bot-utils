from flask import Flask, render_template, request, redirect, url_for, flash, send_from_directory
import os
import secrets
from werkzeug.utils import secure_filename
from utils import rotate_image, grayscale_image, compress_image, invert_image

app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET", secrets.token_hex(16))

# Configure upload folder
UPLOAD_FOLDER = 'uploads'
OUTPUT_FOLDER = 'outputs'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'bmp', 'tiff'}

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['OUTPUT_FOLDER'] = OUTPUT_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max upload size


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


@app.route('/outputs/<filename>')
def processed_file(filename):
    return send_from_directory(app.config['OUTPUT_FOLDER'], filename)


@app.route('/process', methods=['POST'])
def process_image():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    
    file = request.files['file']
    
    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        
        # Get operation and parameters
        operation = request.form.get('operation')
        
        # Generate output filename
        base_name, extension = os.path.splitext(filename)
        output_filename = f"{base_name}_{operation}{extension}"
        output_path = os.path.join(app.config['OUTPUT_FOLDER'], output_filename)
        
        try:
            # Process the image based on the selected operation
            if operation == 'rotate':
                angle = float(request.form.get('angle', 90))
                rotate_image(file_path, output_path, angle)
                flash(f'Image rotated by {angle} degrees')
            
            elif operation == 'grayscale':
                grayscale_image(file_path, output_path)
                flash('Image converted to grayscale')
            
            elif operation == 'compress':
                # Force jpg extension for compressed images
                output_filename = f"{base_name}_compressed.jpg"
                output_path = os.path.join(app.config['OUTPUT_FOLDER'], output_filename)
                quality = int(request.form.get('quality', 60))
                compress_image(file_path, output_path, quality)
                flash(f'Image compressed with quality {quality}')
            
            elif operation == 'invert':
                invert_image(file_path, output_path)
                flash('Image colors inverted')
            
            return render_template('result.html', 
                                   input_image=url_for('uploaded_file', filename=filename),
                                   output_image=url_for('processed_file', filename=output_filename),
                                   operation=operation)
        
        except Exception as e:
            flash(f'Error processing image: {str(e)}')
            return redirect(url_for('index'))
    
    flash('Invalid file type. Allowed types: png, jpg, jpeg, gif, bmp, tiff')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)