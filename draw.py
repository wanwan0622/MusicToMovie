from PIL import Image, ImageDraw


def hsv_to_rgb(h, s, v):
    """
    hsvをrgbに変換する

    Parameters
    ----------
    h : int
        0-360の整数
    s : int
        0-255の整数
    v : int
        0-255の整数

    Returns
    ----------
    r : int
        0-255の整数
    g : int
        0-255の整数
    b : int
        0-255の整数
    """

    max = v
    min = max - ((s / 255) * max)
    if 0 <= h < 60:
        r = max
        g = (h / 60) * (max - min) + min
        b = min
    elif 60 <= h < 120:
        r = ((120 - h) / 60) * (max - min) + min
        g = max
        b = min
    elif 120 <= h < 180:
        r = min
        g = max
        b = ((h - 120) / 60) * (max - min) + min
    elif 180 <= h < 240:
        r = min
        g = ((240 - h) / 60) * (max - min) + min
        b = max
    elif 240 <= h < 300:
        r = ((h - 240) / 60) * (max - min) + min
        g = min
        b = max
    elif 300 <= h <= 360:
        r = max
        g = min
        b = ((360 - h) / 60) * (max - min) + min
    else:
        r = 255
        g = 255
        b = 255
    return int(r), int(g), int(b)


MAX_FREQ = 1600
def draw_circle(freq):
    im = Image.new('RGB', (500, 300), (255, 255, 255))
    draw = ImageDraw.Draw(im)
    h = int(freq * (360 / MAX_FREQ))
    r, g, b = hsv_to_rgb(h, 255, 255)
    print(r, g, b)
    draw.ellipse((100, 100, 200, 200), fill=(r, g, b))
    im.show()
    # im.save('./pillow_imagedraw.jpg', quality=95)   # jpgで保存したい場合
