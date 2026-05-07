import os, sys
from PIL import Image, ImageFilter, ImageFont, ImageEnhance, ImageDraw, ImageOps,ImageTk
#FILTERS

def Blur(image, amount):
    blur = image.filter(ImageFilter.GaussianBlur(radius=amount))
    return blur
def Sharpness(image, amount):
    enhancer = ImageEnhance.Sharpness(image)
    sharpened = enhancer.enhance(amount)
    return sharpened
def Contrast(image, amount):
    enhancer = ImageEnhance.Contrast(image)
    result = enhancer.enhance(amount)
    return result
def Brightness(image, amount):
    enhancer = ImageEnhance.Brightness(image)
    return enhancer.enhance(amount)
#Image customization

def Rotate(image, amount):
    rotated = image.rotate(amount)
    return rotated
def Text(image):
    font = ImageFont.load_default()
    draw = ImageDraw.Draw(image)
    draw.text(
    (50, 50),           # (x, y) position
    "Hello World!",     # text
    fill="white",       # color
    font=font)
    return image
def Crop(image, left, top, right, bottom):
    w, h = image.size
    left   = max(0, int(left))
    top    = max(0, int(top))
    right  = min(w, int(right))
    bottom = min(h, int(bottom))
    cropped = image.crop((left, top, right, bottom))
    return cropped

def zoom(image, amount):
    if amount <= 0:
        return image
    w, h = image.size
    scale = 1 / (1 + amount * 0.2)
    new_w, new_h = int(w * scale), int(h * scale)
    left   = (w - new_w) // 2
    top    = (h - new_h) // 2
    right  = left + new_w
    bottom = top  + new_h
    return image.crop((left, top, right, bottom)).resize((w, h), Image.LANCZOS)
