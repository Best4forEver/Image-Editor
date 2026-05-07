# 🖼️ Image X — Simple Image Editor

A lightweight desktop image editor built with **Python**, **Tkinter**, and **Pillow (PIL)**. Open any photo and apply real-time adjustments using intuitive sliders — no installation beyond Python required.

---

## ✨ Features

| Feature | Description |
|---|---|
| 🔆 **Brightness** | Lighten or darken your image (0.1× – 3.0×) |
| 🎨 **Contrast** | Boost or reduce contrast (0.1× – 3.0×) |
| ✏️ **Sharpness** | Make details crisp or soft (0.1× – 3.0×) |
| 🌫️ **Blur** | Apply Gaussian blur (0 – 10 radius) |
| 🔄 **Rotate** | Rotate the image 0–360 degrees |
| 🔍 **Zoom** | Zoom into the center of the image |
| ✂️ **Crop** | Interactively crop by Left / Top / Right / Bottom (collapsible panel) |
| 💾 **Save** | Export edited image as `.jpg` or `.png` |
| ⚠️ **Unsaved warning** | Prompts before closing if image hasn't been saved |

---

## 📁 Project Structure

```
Simple Image Editor/
│
├── Gui.py              # Main application — Tkinter GUI and editor window
├── Image_Editor.py     # Backend image processing functions (Pillow)
├── logo.ico            # App icon
└── README.md
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- Pillow

```bash
pip install Pillow
```

### Run the App

```bash
python Gui.py
```

---

## 📦 Dependencies

| Package | Purpose |
|---|---|
| `tkinter` | GUI framework (built into Python) |
| `Pillow` | Image loading, processing, and display |

---

## 🛠️ Built With

- **Python** — Core language
- **Tkinter** — Desktop GUI
- **Pillow (PIL)** — Image manipulation

---

## 📄 License

This project is open source. Feel free to fork, modify, and use it.
