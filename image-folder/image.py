from PIL import Image, ImageFilter

img = Image.open('lion.jpg')


box = (100, 100, 400, 400)
region = img.crop(box)

region.save("lion.png", 'png')
