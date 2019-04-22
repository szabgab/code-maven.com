from PIL import Image
import sys

in_file = sys.argv[1]

img = Image.open(in_file)
print(img.size)
print(img.size[0])
print(img.size[1])
