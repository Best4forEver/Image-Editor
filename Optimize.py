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
def debounce(root, callback):
    global after_id
    def handler(val=None):
        global after_id

        if after_id is not None:
            root.after_cancel(after_id)

        after_id = root.after(45, callback)

    return handler
def undo(history_index,history, result):
    history_index, result

    if history_index > 0:
        history_index -= 1

        result = history[history_index].copy()

        return show_image(result)
def redo(history_index,history, result):

    if history_index < len(history) - 1:
        history_index += 1

        result = history[history_index].copy()

        return show_image(result)        
def optimize(file, result, gets, default_v):
    if abs(gets.get() - default_v) > 0.01:  # ✅ small tolerance for float precision
        return file(result, gets.get())
    return result