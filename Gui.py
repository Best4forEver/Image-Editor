import Optimize
import numpy as np
import Filters
import Image_Editor
import os, sys
from PIL import Image, ImageFilter, ImageFont, ImageEnhance, ImageDraw, ImageOps, ImageTk
import tkinter as tk
from tkinter import filedialog  
from tkinter import ttk
from tkinter import messagebox
file_path = None  
saved = False
def on_close(window):
    global saved    
    if saved:
        answer = messagebox.askyesno("Warning", "You haven't saved the file.The progress will be lost.")
        if answer:
            window.destroy()
        else:
            return       
    window.destroy()        

def save(image):
    global saved
    saved = True
    save_path = filedialog.asksaveasfilename(
    title="Save Image",
    defaultextension=".jpg",
    filetypes=[("JPEG", "*.jpg"), ("PNG", "*.png")])
    if save_path:
        image.save(save_path)
        saved = False

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
    global saved
    root.withdraw()  

    editor = tk.Toplevel(root)
    editor.title("Image X - Editor")
    editor.resizable(True, True)
    editor.geometry("1280x720")

    tk.Label(editor, text=f"Editing: {filepath}", fg="gray").pack(pady=10)

    def go_back():
        if saved:
            answer = messagebox.askyesno("Warning", "You haven't saved. Progress will be lost.")
            if not answer:
                return
        editor.destroy()
        root.deiconify()

    s_file = tk.Button(editor, text="Save", command=lambda: save(result))
    s_file.pack(pady=20)
   
    img = Image.open(filepath)
    img.thumbnail((800, 500))
    original = img.copy()
    result = None
    photo = ImageTk.PhotoImage(img)
    
    top_bar   = tk.Frame(editor, bg="#132E23", height=40)
    top_bar.pack(fill=tk.X)

    main_area = tk.Frame(editor, bg="#2E131E")
    main_area.pack(fill=tk.BOTH, expand=True)
    bottom_panel = tk.Frame(main_area,bg="#1A1A2E",width=200)
    bottom_panel.pack(side=tk.BOTTOM, fill=tk.Y, padx=5, pady=5)
    tk.Button(bottom_panel, text="← Go Back", command=go_back).pack(pady=10)
    left_panel  = tk.Frame(main_area, bg="#1A1A2E", width=200)
    left_panel.pack(side=tk.LEFT, fill=tk.Y, padx=5, pady=5)
    right_panel = tk.Frame(main_area,bg="#1A1A2E",width=200)
    right_panel.pack(side=tk.RIGHT, fill=tk.Y, padx=5, pady=5)
    canvas_frame = tk.Frame(main_area, bg="#2E131E")
    canvas_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    
    image_label = tk.Label(canvas_frame, image=photo, bg="#2E131E")
    image_label.image = photo
    image_label.pack(pady=10)

    editor.protocol("WM_DELETE_WINDOW", lambda: on_close(editor))
    

    brightness  = tk.DoubleVar(value=1.0)
    contrast    = tk.DoubleVar(value=1.0)
    exposure    = tk.DoubleVar(value=0.0)
    highlight   = tk.DoubleVar(value=1.0)
    shadow      = tk.DoubleVar(value=1.0)
    temperature = tk.DoubleVar(value=0.0)
    vibrance    = tk.DoubleVar(value=1.0)
    saturation  = tk.DoubleVar(value=1.0)
    grain       = tk.DoubleVar(value=0.0)
    sharpness   = tk.DoubleVar(value=1.0)
    blur        = tk.DoubleVar(value=0.0)
    rotate      = tk.IntVar(value=0)
    img_w, img_h = original.size
    crop_left   = tk.DoubleVar(value=0)
    crop_top    = tk.DoubleVar(value=0)
    crop_right  = tk.DoubleVar(value=img_w)
    crop_bottom = tk.DoubleVar(value=img_h)
    zoom        = tk.IntVar(value=0)
    
    
    def l_make_slider(label_text, variable, from_, to):
        tk.Label(left_panel, text=label_text, bg="#1A1A2E", fg="white").pack(pady=(8,0))
        tk.Scale(left_panel, variable=variable, from_=from_, to=to,
                 resolution=0.1, orient=tk.HORIZONTAL, bg="#1A1A2E", fg="white",
                 troughcolor="#132E23", command=on_change).pack(fill=tk.X, padx=10)
    def r_make_slider(label_text, variable, from_, to):
        tk.Label(right_panel, text=label_text, bg="#1A1A2E", fg="white").pack(pady=(8,0))
        tk.Scale(right_panel, variable=variable, from_=from_, to=to,
                 resolution=0.1, orient=tk.HORIZONTAL, bg="#1A1A2E", fg="white",
                 troughcolor="#132E23", command=update_image).pack(fill=tk.X, padx=10)             
    def b_make_slider(label_text, variable, from_, to):
        tk.Label(bottom_panel, text=label_text, bg="#1A1A2E", fg="white").pack(pady=(8,0))
        tk.Scale(bottom_panel, variable=variable, from_=from_, to=to,
                 resolution=0.1, orient=tk.HORIZONTAL, bg="#1A1A2E", fg="white",
                 troughcolor="#132E23", command=update_image).pack(fill=tk.X, padx=10)          
    def update_image(val=None):
        
        global saved
        nonlocal result
        result = original.copy()
        result = Image_Editor.Crop(result,
                                   crop_left.get(), crop_top.get(),
                                   crop_right.get(), crop_bottom.get())
        result = Optimize.optimize(Image_Editor.Blur,result,blur,0.0)
        result = Optimize.optimize(Image_Editor.Contrast,result,contrast,1.0)
        result = Optimize.optimize(Filters.Exposure,result,exposure,1.0)
        result = Optimize.optimize(Filters.Highlights,result,highlight,1.0)
        result = Optimize.optimize(Filters.Shadows,result,shadow,1.0)
        result = Optimize.optimize(Filters.Temperature,result,temperature,0.0)
        result = Optimize.optimize(Filters.Vibrance,result,vibrance,1.0)
        result = Optimize.optimize(Filters.Grain,result,grain,0.0)
        result = Optimize.optimize(Filters.Saturation,result,saturation,1.0)
        result = Optimize.optimize(Image_Editor.Sharpness,result,sharpness,1.0)
        result = Optimize.optimize(Image_Editor.Brightness,result,brightness,1.0)
        result = Optimize.optimize(Image_Editor.Rotate,result,rotate,0.0)
        result = Optimize.optimize(Image_Editor.zoom,result,zoom,0.0)
        result.thumbnail((800, 500))
        new_photo = ImageTk.PhotoImage(result)
        image_label.config(image=new_photo)
        image_label.image = new_photo
        if img != result:
            saved = True
    on_change = Optimize.debounce(root, update_image)
    l_make_slider("Brightness",   brightness,   0.1, 3.0)
    l_make_slider("Contrast",     contrast,     0.1, 3.0)
    l_make_slider("Exposure",     exposure,     -2.0, 2.0)
    l_make_slider("Highlights",   highlight,     0.0, 3.0)
    l_make_slider("Shadow",        shadow,     0.0, 3.0)
    l_make_slider("Temperature",  temperature,     -50.0, 50.0)
    l_make_slider("Vibrance",     vibrance,     0.1, 3.0)
    l_make_slider("Saturation",     saturation,     0.1, 3.0)
    l_make_slider("Sharpness",    sharpness,    0.1, 3.0)
    l_make_slider("Blur",         blur,         0.0, 10.0)
    l_make_slider("Grain",         grain,         0.0, 10.0)
    r_make_slider("Rotate",       rotate,       0.0, 360)
    r_make_slider("Zoom", zoom, 0.0, 5.0)
    # --- Collapsible Crop Section ---
    crop_frame = tk.Frame(right_panel, bg="#1A1A2E")

    def toggle_crop():
        if crop_frame.winfo_ismapped():
            crop_frame.pack_forget()
            crop_toggle_btn.config(text="▶ Crop")
        else:
            crop_frame.pack(fill=tk.X, padx=5)
            crop_toggle_btn.config(text="▼ Crop")

    crop_toggle_btn = tk.Button(
        right_panel, text="▶ Crop",
        command=toggle_crop,
        bg="#132E23", fg="white",
        relief=tk.FLAT, anchor="w",
        font=("Arial", 9, "bold")
    )
    crop_toggle_btn.pack(fill=tk.X, padx=10, pady=(8, 0))

    def make_crop_slider(label_text, variable, from_, to):
        tk.Label(crop_frame, text=label_text, bg="#1A1A2E", fg="white").pack(pady=(4, 0))
        tk.Scale(crop_frame, variable=variable, from_=from_, to=to,
                 resolution=1, orient=tk.HORIZONTAL, bg="#1A1A2E", fg="white",
                 troughcolor="#132E23", command=update_image).pack(fill=tk.X, padx=10)

    make_crop_slider("Crop Left",   crop_left,   0, img_w)
    make_crop_slider("Crop Top",    crop_top,    0, img_h)
    make_crop_slider("Crop Right",  crop_right,  0, img_w)
    make_crop_slider("Crop Bottom", crop_bottom, 0, img_h)
    # ----------------------------------
    exit_btn2 = tk.Button(bottom_panel, text="Exit", font=("Arial", 9), bg="#1A1A2E", fg="white", command=lambda:on_close(root))
    exit_btn2.pack(pady=10)
    
def exit_app():
    root.quit()
    root.destroy()
    sys.exit()

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