from PIL import Image, ImageDraw

def draw_circle():
    im = Image.new('RGB', (500, 300), (255, 255, 255))
    draw = ImageDraw.Draw(im)
    draw.ellipse((100, 100, 200, 200), fill=(255, 0, 0))
    im.show()
    # im.save('./pillow_imagedraw.jpg', quality=95)   # jpgで保存したい場合

draw_circle()
