import Image_Editor
import Filters
import Image_Editor
import os, sys
from PIL import Image, ImageFilter, ImageFont, ImageEnhance, ImageDraw, ImageOps, ImageTk
import tkinter as tk
from tkinter import filedialog  
from tkinter import ttk
from tkinter import messagebox

after_id = None

after_id = None

def debounce(root, callback):
    global after_id

    def handler(val=None):
        global after_id

        if after_id is not None:
            root.after_cancel(after_id)

        after_id = root.after(45, callback)

    return handler

def optimize(file, result, gets, default_v):
    if abs(gets.get() - default_v) > 0.01:  # ✅ small tolerance for float precision
        return file(result, gets.get())
    return result