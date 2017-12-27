from PIL import Image, ImageFilter
import sys
import os

# add a line accress the image
# ass some text to an image
# move the image a few pixels to the right/left/up/down
# rotate the image a bit
# get the size of the image


filename = sys.argv[1] 
# file, ext = os.path.splitext(filename)
img = Image.open(filename)
print(img.size)
#img.show()
#img.save(new_filename)


#img.thumbnail(200, 200)
#img.save(...)

#img.rotate(90).save()
#img.convert(mode='L')   # to turn black-and-white
# img.filter(ImageFilter.GaussianBlur(15)).save(..)
