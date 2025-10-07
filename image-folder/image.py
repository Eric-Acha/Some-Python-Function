from PIL import Image, ImageFilter

img = Image.open('snail.jpg')
filtered_img = img.filter(ImageFilter.SMOOTH)

filtered_img.save("smooth.png", 'png')
