
# 🖼️ image-bot-utils

A powerful Python toolkit with both a **command-line interface (CLI)** and a **web interface** for basic image processing.

Built with ❤️ using **Python 3.11**, **Pillow**, **Flask**, and **Bootstrap**.

---

## ⚙️ Features

✅ Rotate images (custom angles)  
✅ Convert to grayscale  
✅ Compress images with quality control  
✅ Invert image colors  
✅ Run from terminal or browser  
✅ Upload, preview, and download edited images

---

## 💻 Tech Stack

- Python 3.11
- Pillow (PIL)
- Flask (Web)
- Bootstrap (Styling)
- Replit (Dev)

---

## 🚀 CLI Usage

Run directly from the terminal:

```bash
# Rotate an image
python main.py --input input.png --output rotated.png rotate --angle 90

# Convert to grayscale
python main.py --input input.png --output grayscale.png grayscale

# Compress with custom quality
python main.py --input input.png --output compressed.jpg compress --quality 80

# Invert image colors
python main.py --input input.png --output inverted.png invert
```

### 🔧 Help Menu
```bash
python main.py --help
```

---

## 🌐 Web Interface

- Launches Flask app via `app.py`
- Upload images via browser
- Preview before/after
- Works with `.png`, `.jpg`, `.jpeg`

---

## 🖼️ Screenshots

<p float="left">
  <img src="screenshots/upload-form.png" width="300" />
  <img src="screenshots/result-preview.png" width="300" />
</p>

---

## 📦 Installation

```bash
pip install pillow flask
```

> Python 3.8 or higher is recommended.

---

## 👨‍💻 Created By

**Ragy Ashraf**  
Python dev | Discord bot engineer | Game systems nerd  
[GitHub Profile →](https://github.com/ragyashraf)

