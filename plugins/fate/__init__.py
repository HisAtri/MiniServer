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
font_path = os.path.join(rootdir, "font/font.ttf")
print (font_path)

def getext():
    fatext = random.choice(["大\n\n吉","中\n\n吉","小\n\n吉","末\n\n吉",])
    fatile = random.choice([
        "昔我往矣\n杨柳依依\n今我来思\n雨雪霏霏",
        "有酒有酒\n闲饮东窗\n愿言怀人\n舟车靡从",
        "素裳酌清酒\n看闲云\n好言赴春梦\n醉良宵",
        "山外落了\n不是斜阳\n庭中垂柳\n可乃故人",
        "夜雨悄无声\n阶前漫青苔\n好问东岭客\n可见故人来",
        "遥指东风来处\n不是天涯\n酒旗漫卷风华\n暗了金钗",
        "吹遍春风游子泪\n醉打山门\n便倚茅檐睡",
        "八阵图不见\n七哀诗已成\n但向酒旗处\n醪糟付此生",
        "山花本无语\n开在尘嚣处\n待到风雨夜\n直往蓬莱去",
        "东风本是伤心客\n吹散晨露伴朝晖\n适逢酒楼闲同饮\n漫卷幡动暗香飞",
        "画作斗方中\n山海几千重\n云游峰聚处\n叶落老龙钟",
    ])

    return fatext, fatile


def getimg():
    
    random_img = random.choice(jpg_img)
    image_path = os.path.join(image_dir, random_img)
    img = Image.open(image_path)
    # 图片上添加文字
    font = ImageFont.truetype(font_path, size=84)
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
    font = ImageFont.truetype(font_path, size=108)
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

    font = ImageFont.truetype(font_path, size=54)
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