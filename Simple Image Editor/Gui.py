
import Image_Editor
import os, sys
from PIL import Image, ImageFilter, ImageFont, ImageEnhance, ImageDraw, ImageOps, ImageTk
import tkinter as tk
from tkinter import filedialog  

file_path = None  

def selection():
    global file_path 
    file_path = filedialog.askopenfilename(  
        title="Select a File",
        filetypes=[
            ("Image files", "*.jpg *.jpeg *.png *.gif")
        ])

    if file_path:  
        open_editor(file_path) 

def open_editor(filepath):
    root.withdraw()  

    editor = tk.Toplevel(root)
    editor.title("Image X - Editor")
    editor.geometry("1280x720")

    tk.Label(editor, text=f"Editing: {filepath}", fg="gray").pack(pady=10)

    def go_back():
        editor.destroy()
        root.deiconify()  

    tk.Button(editor, text="← Go Back", command=go_back).pack(pady=10)

    # ── Load Image ──────────────────────────────
    img = Image.open(filepath)
    img.thumbnail((800, 500))
    original = img.copy()           # keep original for adjustments

    photo = ImageTk.PhotoImage(img)
    # ── Layout Frames ────────────────────────────
    top_bar   = tk.Frame(editor, bg="#132E23", height=40)
    top_bar.pack(fill=tk.X)

    main_area = tk.Frame(editor, bg="#2E131E")
    main_area.pack(fill=tk.BOTH, expand=True)

    left_panel  = tk.Frame(main_area, bg="#1A1A2E", width=200)
    left_panel.pack(side=tk.LEFT, fill=tk.Y, padx=5, pady=5)

    canvas_frame = tk.Frame(main_area, bg="#2E131E")
    canvas_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    # ── Image Display ────────────────────────────
    image_label = tk.Label(canvas_frame, image=photo, bg="#2E131E")
    image_label.image = photo
    image_label.pack(pady=10)

    # ── Sliders ──────────────────────────────────
    brightness  = tk.DoubleVar(value=1.0)
    contrast    = tk.DoubleVar(value=1.0)
    sharpness   = tk.DoubleVar(value=1.0)
    blur        = tk.DoubleVar(value=0.0)
    rotate      = tk.DoubleVar(value=0.0)
    img_w, img_h = original.size
    crop_left   = tk.DoubleVar(value=0)
    crop_top    = tk.DoubleVar(value=0)
    crop_right  = tk.DoubleVar(value=img_w)
    crop_bottom = tk.DoubleVar(value=img_h)

    def make_slider(label_text, variable, from_, to):
        tk.Label(left_panel, text=label_text, bg="#1A1A2E", fg="white").pack(pady=(8,0))
        tk.Scale(left_panel, variable=variable, from_=from_, to=to,
                 resolution=0.1, orient=tk.HORIZONTAL, bg="#1A1A2E", fg="white",
                 troughcolor="#132E23", command=update_image).pack(fill=tk.X, padx=10)

    def update_image(val=None):
        result = original.copy()
        result = Image_Editor.Crop(result,
                                   crop_left.get(), crop_top.get(),
                                   crop_right.get(), crop_bottom.get())
        result = Image_Editor.Blur(result, blur.get())
        result = Image_Editor.Contrast(result, contrast.get())
        result = Image_Editor.Sharpness(result, sharpness.get())
        result = Image_Editor.Brightness(result, brightness.get())
        result = Image_Editor.Rotate(result, rotate.get())
        result.thumbnail((800, 500))
        new_photo = ImageTk.PhotoImage(result)
        image_label.config(image=new_photo)
        image_label.image = new_photo

    make_slider("Brightness",   brightness,   0.1, 3.0)
    make_slider("Contrast",     contrast,     0.1, 3.0)
    make_slider("Sharpness",    sharpness,    0.1, 3.0)
    make_slider("Blur",         blur,         0.0, 10.0)
    make_slider("Rotate",       rotate,       0.0, 360)
    make_slider("Crop Left",    crop_left,    0,   img_w)
    make_slider("Crop Top",     crop_top,     0,   img_h)
    make_slider("Crop Right",   crop_right,   0,   img_w)
    make_slider("Crop Bottom",  crop_bottom,  0,   img_h)
def exit_app():
    root.destroy()

# --- Main Window ---
root = tk.Tk()
root.title("Image X")
root.geometry("1280x720")
root.resizable(True, True)
root.iconbitmap("logo.ico")
root.config(background="#2E131E")

label = tk.Label(root, text="Image X", font=("Arial", 16), fg="blue", bg="#2E131E")
label.pack(pady=20)

image_sel = tk.Button(root, text="Import Photo", command=selection, bg="#132E23", fg="white", width=30, height=4)
image_sel.pack(pady=5)

exit_btn = tk.Button(root, text="Exit", command=exit_app, bg="#132E23", fg="white", width=30, height=4)
exit_btn.pack(pady=5)

root.mainloop()