from PIL import Image, ImageFilter, ImageFont, ImageEnhance, ImageDraw, ImageOps,ImageTk
import numpy as np

def Exposure(image, value=0.0):     # value: -1.0 to +1.0
    image = image.convert("RGB")
    arr   = np.array(image, dtype=np.float32)
    arr   = arr * (2 ** value)      # -1 = half brightness, +1 = double
    return Image.fromarray(np.clip(arr, 0, 255).astype(np.uint8))


def Highlights(image, value=1.0):      
    arr = np.array(image, dtype=np.float64)
    mask = arr / 255.0                 
    arr  = arr + (value - 1) * 100 * mask
    return Image.fromarray(np.clip(arr, 0, 255).astype(np.uint8)) 

def Shadows(image, value=1.0):         
    arr  = np.array(image, dtype=np.float64)
    mask = 1 - (arr / 255.0)          
    arr  = arr + (value - 1) * 100 * mask
    return Image.fromarray(np.clip(arr, 0, 255).astype(np.uint8))   

def Temperature(image, value=0):       # + = warm, - = cool
    arr = np.array(image, dtype=np.float64)
    arr[:,:,0] = np.clip(arr[:,:,0] + value, 0, 255)   # red
    arr[:,:,2] = np.clip(arr[:,:,2] - value, 0, 255)   # blue
    return Image.fromarray(arr.astype(np.uint8))

def Vibrance(image, value=1.0):        # boosts dull colors more than vivid
    arr  = np.array(image, dtype=np.float64)
    avg  = arr.mean(axis=2, keepdims=True)
    diff = arr - avg
    arr  = avg + diff * value
    return Image.fromarray(np.clip(arr, 0, 255).astype(np.uint8))

def Grain(image, value=20):            # adds film grain
    arr   = np.array(image, dtype=np.float64)
    noise = np.random.normal(0, value, arr.shape)
    arr   = arr + noise
    return Image.fromarray(np.clip(arr, 0, 255).astype(np.uint8))

def Saturation(image, value=1.0):      # 0=grayscale, 1=normal, 2=vivid
    return ImageEnhance.Color(image).enhance(value)    