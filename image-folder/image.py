from PIL import Image, ImageFilter

img = Image.open('cypic.webp')

img.resize((500, 300))


img.save('cypic.png', 'png')

# img.thumbnail((50, 50))

# img.save('profile4.png')


# img.filter(ImageFilter.SMOOTH)

# img = img.save('profile3.png', 'png')


# box = (100, 100, 300, 300)
# region = img.crop(box)

# region.save("profile.png", 'png')
