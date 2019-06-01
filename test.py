from PIL import Image
import PIL
import config

images1 = [
    "16AM003..PNG",
    #"16KM149..PNG"
]

import os

images = map(lambda image: os.path.join(config.samples_folder, image), images1)

for img, name in zip(images, images1):
    basewidth = 320
    img = Image.open(img)
    wpercent = (basewidth / float(img.size[0]))
    hsize = int((float(img.size[1]) * float(wpercent)))
    img = img.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
    img.save(f'{name}')