from PIL import Image, ImageFilter

img = Image.open('./Lessons/Images/pikachu.jpg')
filtered_img = img.filter(ImageFilter.BLUR)
filtered_img.save("blur", 'png' )
filtered_img.rotate 