import os
from PIL import Image

resize_method = Image.ANTIALIAS

max_height = 3000
max_width = 3000
extensions = ['JPG']

path = os.path.abspath("F:\\ImageTests\\2016-07-14 Tests\\JPG-HQ")
path_small = os.path.abspath("F:\\ImageTests\\2016-07-14 Tests\\JPG-SMALL")

def adjusted_size(width, height):
    if width > max_width or height > max_width:
        if width > height:
            return max_width, int (max_width * height/width)
        else:
            return int (max_height * width/height), max_height
    else:
        return width, height

if __name__ == "__main__":
    if not os.path.exists(path_small):
        os.makedirs(path_small)
    for f in os.listdir(path):
        if os.path.isfile(os.path.join(path,f)):
            f_text, f_ext = os.path.splitext(f)
            f_ext = f_ext[1:].upper()
            if f_ext in extensions:
                print(f)
                image = Image.open(os.path.join(path,f))
                print(image.size)
                width, height = image.size
                image = image.resize(adjusted_size(width, height))
                print(image.size)
                image.save(os.path.join(path_small,f))
