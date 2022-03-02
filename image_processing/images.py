from PIL import Image, ImageFilter
import pprint
import os
# Sets path to root folder (/data) for first run of main()
dir_path = os.path.dirname(os.path.realpath(__file__))
basepath = f'{dir_path}'

img = Image.open(f'{dir_path}/pokemons/pikachu.jpg')


# # --- Grayscale & crop ---
img_convert = img.convert('L')
box = (100, 100, 400, 400,)
croped = img_convert.crop(box)
croped.save('grayscale_croped.png', 'png')
croped.show()
# # --- *** ---

# # --- Grayscale & resize ---
# img_convert = img.convert('L')
# resize = img_convert.resize((300, 300))
# resize.save('grayscale_resize_300x300.png', 'png')
# resize.show()
# # --- *** ---


# # --- Grayscale & Rotate ---
# img_convert = img.convert('L')
# rotated = img_convert.rotate(90)
# rotated.save('grayscale_rotated.png', 'png')
# rotated.show()
# # --- *** ---


# # --- Grayscale ---
# img_convert = img.convert('L')
# img_convert.save('grayscale.png', 'png')
# img_convert.show()
# # --- *** ---

# # --- Filtered images ---
# img_filtered = img.filter(ImageFilter.BLUR)
# img_filtered.save('blur.png', 'png')
# # --- *** ---

# pprint.pprint(dir(image))
# print(image)
