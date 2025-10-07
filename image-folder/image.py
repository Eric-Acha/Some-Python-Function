from PIL import Image, ImageFilter

img = Image.open('snail.jpg')
filtered_img = img.convert('L')
resize = filtered_img.resize((710, 640))

resize.save("Grey.png", 'png')
