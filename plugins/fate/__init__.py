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
font_path2 = os.path.join(rootdir, "font/qkwt.ttf")

def getext():
    fatext = random.choice(["大\n\n吉","中\n\n吉","小\n\n吉","\n吉\n","末\n\n吉","\n凶\n","大\n\n凶"])
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
        "彻夜西风撼破扉\n萧条孤馆一灯微\n家山回首三千里\n断天南无雁飞",
        "无事经年别远公\n帝城钟晓忆西峰\n炉烟消尽寒灯晦\n童子开门雪满松",
        "陇头流水\n鸣声呜咽\n遥望秦川\n心肝断绝",
        "东门之杨\n其叶牂牂\n昏以为期\n明星煌煌",
        "几日喜春晴\n几夜愁春雨\n十二雕窗六曲屏\n题遍伤春句",
        "糟粕所传非粹美\n丹青难写是精神\n区区岂尽高贤意\n独守千秋纸上尘",
        "新来好\n唱得虎头词\n一片冷香唯有梦\n十分清瘦更无诗\n标格早梅知",
        "春风倚棹阖闾城\n水国春寒阴复晴\n细雨湿衣看不见\n闲花落地听无声",
        "古陵在蒿下\n啼乌在蒿上\n陵中人不闻\n行客自惆怅",
        "红藕花香到槛频\n可堪闲忆似花人\n旧欢如梦绝音尘",
        "佳期期未归\n望望下鸣机\n徘徊东陌上\n月出行人稀",
        "好是春风湖上亭\n柳条藤蔓系离情\n黄莺久住浑相识\n欲别频啼四五声",
        "江南倦历览\n江北旷周旋\n怀新道转迥\n寻异景不延",
        "空一缕余香在此\n盼千金游子何之\n证候来时\n正是何时\n灯半昏时\n月半明时"
        "一声画角谯门\n半庭新月黄昏\n雪里山前水滨\n篱茅舍\n淡烟衰草孤村",
        "兴亡千古繁华梦\n诗眼倦天涯\n孔林乔木\n吴宫蔓草\n楚庙寒鸦",
        "叹人间\n美中不足今方信\n纵然是齐眉举案\n到底意难平",
        "庭前落尽梧桐\n水边开彻芙蓉\n解与诗人意同"
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
    outline_color = (255, 255, 255)
    outline_width = 2
    bbox = img_draw.textbbox((0, 0), text, font=font)
    w, h = bbox[2] - bbox[0], bbox[3] - bbox[1]
    text_width, text_height = img_draw.textsize(text, font)
    x = (img.width - text_width) // 2
    y = (img.height - text_height) // 8
    for xo in range(-outline_width, outline_width + 1, 4):
        for yo in range(-outline_width, outline_width + 1, 4):
            img_draw.text((x + xo, y + yo), text, fill=outline_color, font=font)
    img_draw.text((x, y), text, fill=(0, 0, 0), font=font)

    text = getext()
    font = ImageFont.truetype(font_path, size=108)
    bbox = img_draw.textbbox((0, 0), text[0], font=font)
    w, h = bbox[2] - bbox[0], bbox[3] - bbox[1]
    text_width, text_height = img_draw.textsize(text[0], font)
    x = (img.width - text_width) // 2
    y = (img.height - text_height) // 3
    for xo in range(-outline_width, outline_width + 1, 4):
        for yo in range(-outline_width, outline_width + 1, 4):
            img_draw.text((x + xo, y + yo), text[0], fill=outline_color, font=font)
    img_draw.text((x, y), text[0], fill=(255, 0, 0), font=font)

    font = ImageFont.truetype(font_path2, size=54)
    bbox = img_draw.textbbox((0, 0), text[1], font=font)
    w, h = bbox[2] - bbox[0], bbox[3] - bbox[1]
    text_width, text_height = img_draw.textsize(text[1], font)
    x = (img.width - text_width) // 2
    y = (img.height - text_height) * 0.7
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
    random.seed(seed)                   #全局随机数种子

    img = getimg()

    self.send_response(200)
    self.send_header("Content-type", "image/png")
    self.send_header("Content-length", len(img))
    self.end_headers()
    self.wfile.write(img)