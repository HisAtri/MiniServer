import os
import random
from io import BytesIO
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from datetime import datetime

from def_global import remove_first_path

rootdir = os.path.dirname(os.path.abspath(__file__))
image_dir = os.path.join(rootdir, "image")
jpg_img = [filename for filename in os.listdir(image_dir) if filename.endswith('.jpg')]

def getext():
    fatext = random.choice(["大\n\n吉","中\n\n吉","小\n\n吉","末\n\n吉",])
    fatile = random.choice([
        "昔我往矣\n杨柳依依\n今我来思\n雨雪霏霏",
        "有酒有酒\n闲饮东窗\n愿言怀人\n舟车靡从",
    ])

    return fatext, fatile


def getimg():
    random_img = random.choice(jpg_img)
    image_path = os.path.join(image_dir, random_img)
    img = Image.open(image_path)
    # 图片上添加文字
    font = ImageFont.truetype("simhei.ttf", size=84)
    text = "今日运势"
    img_draw = ImageDraw.Draw(img)
    # 文字描边
    outline_color = (255, 255, 255)
    outline_width = 2
    bbox = img_draw.textbbox((0, 0), text, font=font)
    w, h = bbox[2] - bbox[0], bbox[3] - bbox[1]
    text_width, text_height = img_draw.textsize(text, font)
    x = (img.width - text_width) // 2
    y = (img.height - text_height) // 8  # 垂直居中
    for xo in range(-outline_width, outline_width + 1, 4):
        for yo in range(-outline_width, outline_width + 1, 4):
            img_draw.text((x + xo, y + yo), text, fill=outline_color, font=font)
    img_draw.text((x, y), text, fill=(0, 0, 0), font=font)

    text = getext()
    font = ImageFont.truetype("simhei.ttf", size=108)
    # 文字描边
    bbox = img_draw.textbbox((0, 0), text[0], font=font)
    w, h = bbox[2] - bbox[0], bbox[3] - bbox[1]
    text_width, text_height = img_draw.textsize(text[0], font)
    x = (img.width - text_width) // 2
    y = (img.height - text_height) // 3  # 垂直居中
    for xo in range(-outline_width, outline_width + 1, 4):
        for yo in range(-outline_width, outline_width + 1, 4):
            img_draw.text((x + xo, y + yo), text[0], fill=outline_color, font=font)
    img_draw.text((x, y), text[0], fill=(255, 0, 0), font=font)

    font = ImageFont.truetype("simhei.ttf", size=54)
    # 文字描边
    bbox = img_draw.textbbox((0, 0), text[1], font=font)
    w, h = bbox[2] - bbox[0], bbox[3] - bbox[1]
    text_width, text_height = img_draw.textsize(text[1], font)
    x = (img.width - text_width) // 2
    y = (img.height - text_height) * 0.7  # 垂直居中
    for xo in range(-outline_width, outline_width + 1, 2):
        for yo in range(-outline_width, outline_width + 1, 2):
            img_draw.text((x + xo, y + yo), text[1], fill=outline_color, font=font)
    img_draw.text((x, y), text[1], fill=(0, 0, 0), font=font)

    # 转换为字节流
    img_byte_array = BytesIO()
    img.save(img_byte_array, format='JPEG')
    img_byte_array = img_byte_array.getvalue()

    return img_byte_array

def handle_request(self):

    now = datetime.now()
    
    if remove_first_path(self.path) == "/":
        seed = datetime.timestamp(now)
    else:
        date = now.strftime("%Y%m%d")   #20230201格式
        seed = remove_first_path(self.path) + date
    random.seed(seed)               #全局随机数种子

    img = getimg()

    self.send_response(200)
    self.send_header("Content-type", "image/png")
    self.send_header("Content-length", len(img))
    self.end_headers()
    self.wfile.write(img)