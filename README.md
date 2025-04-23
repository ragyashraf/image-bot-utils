
# 🖼️ image-bot-utils

A collection of powerful and beginner-friendly Python tools for image processing.  
This repo includes standalone scripts that can be used as CLI utilities or integrated into bots (Discord, Telegram, etc.)

## ✨ Features

- ✅ Rotate, Flip (Horizontal/Vertical)
- ✅ Convert to Grayscale
- ✅ Blur, Invert, Compress
- ✅ Resize images
- ✅ CLI usage & easy to extend

## 📂 Folder Structure
```
image-bot-utils/
├── main.py
├── utils/
│   ├── rotate.py
│   ├── grayscale.py
│   ├── compress.py
│   └── invert.py
├── examples/
│   └── sample.png
└── README.md
```

## 📦 Requirements

- Python 3.8+
- [Pillow (PIL)](https://pillow.readthedocs.io/en/stable/)

Install via pip:
```bash
pip install pillow
```

## 🚀 Usage

### CLI (from terminal)
```bash
python main.py --action rotate --input path/to/image.png
```

### As a module:
```python
from utils.rotate import rotate_image
rotate_image("input.png", "output.png", 90)
```

## 🤖 Integration Ideas
- Discord bot command: `!rotate 90`
- Telegram image handler
- Drag-and-drop GUI

## 📸 Example
Before → ![Before](examples/sample.png)  
After → *(processed images to be added)*

---

Created with 💻 by [Ragy Ashraf](https://github.com/ragyashraf)
