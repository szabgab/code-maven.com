from PIL import Image

in_file = 'images/code-maven-workshops-1600x900.png'  # 1600, 900
out_file = 'new.png'

img = Image.open(in_file)

size = (img.size[0]/2,  img.size[1]/2)
img.thumbnail(size)

img.save(out_file)

