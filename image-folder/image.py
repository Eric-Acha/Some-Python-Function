from PIL import Image, ImageFilter

img = Image.open('snail.jpg')


box = (100, 100, 300, 300)
region = img.crop(box)

region.save("lion.png", 'png')
