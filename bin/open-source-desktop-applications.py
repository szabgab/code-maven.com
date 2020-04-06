import os
from PIL import Image, ImageDraw, ImageFont

root = os.path.dirname(os.path.dirname(__file__))

def heb(txt):
    rev = txt[::-1]
    return rev

def embed_image(img, filename, box, size=None, mask=False):
    emb_img_path = os.path.join(root, 'static', 'img', filename)
    emb_img = Image.open(emb_img_path, 'r')
    #size = (emb_img.size[0] / 2, emb_img.size[1] / 2)
    if size:
        emb_img.thumbnail(size)
    if mask:
       img.paste(emb_img, box=box, mask=emb_img)
    else:
       img.paste(emb_img, box=box)

def main():
    width  = 250
    height = 250
    #background_color = '#eb8634'
    #background_color = '#ebb434'
    #background_color = '#f540dd'
    #background_color = '#67f23d'
    background_color = '#ffffff'

    #print(root)

    png_filename = os.path.splitext(os.path.basename(__file__))[0] + '.png'
    #print(png_filename)

    png_filepath = os.path.join(root, 'static', 'img', png_filename)
    #print(png_filepath)

    img = Image.new('RGB', (width, height), color=background_color)

    # Code-Maven Workshop

    font_text = ImageFont.truetype('Pillow/Tests/fonts/FreeMono.ttf', 40)
    font = ImageFont.truetype('Pillow/Tests/fonts/FreeSansBold.ttf', 25)
    draw = ImageDraw.Draw(img)
    draw.text(
        text="Desktop\n\n         Applications",
        xy=(10, 150),
        fill=(0, 0, 0),
        font=font,
    )

    #isize = 250
    #embed_image(img=img, filename='gabor2_612x612.jpg', size=(isize, isize), box=(width-isize-10, height-isize-10))
    embed_image(img=img, filename='open_source_550x389.jpeg', size=(250, 250), box=(0, 0), mask=True)

    img.save(png_filepath)
    img.show()


main()
