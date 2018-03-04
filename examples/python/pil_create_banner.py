from PIL import Image, ImageDraw, ImageFont

img = Image.new('RGB', (460, 60), color = (73, 109, 137))

fnt = ImageFont.truetype('/Library/Fonts/Arial.ttf', 20)
d = ImageDraw.Draw(img)
d.text((20 ,10), "Would you like to support the Code Maven site?", font=fnt, fill=(255, 255, 0))

d.line((0, 0) + img.size, fill=128)

img.save('support-code-maven.png')