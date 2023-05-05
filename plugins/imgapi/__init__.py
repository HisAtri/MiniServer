import re
import os

import pytz
from user_agents import parse
from io import BytesIO
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from datetime import datetime

from config_global import config_global
from def_global import remove_first_path, page404


#模块获取自身目录
rootdir = os.path.dirname(os.path.abspath(__file__))
config_path = os.path.join(rootdir, "config.ini")

def read_config():
    default_config = {
        'timezone': 'Asia/Shanghai',
        'font': 'font/font.ttf',
        'image': 'image/sample.jpg',
    }

    try:
        with open(config_path, 'r') as f:
            lines = f.readlines()
            config = {}
            for line in lines:
                key, value = line.strip().split('=')
                config[key] = value
    except (FileNotFoundError, ValueError):
        with open('config.ini', 'w') as f:
            for key, value in default_config.items():
                f.write(f"{key}={value}\n")
        config = default_config

    for key in default_config:
        if key not in config:
            config[key] = default_config[key]

    return config


# 获取配置项
config = read_config()
timezone = config["timezone"]
image_path = os.path.join(rootdir, config["image"])
font_path = os.path.join(rootdir, config["font"])

# 加载图片对象
imgopen = Image.open(image_path)


def gettimestr():
    now = datetime.now(pytz.timezone(timezone))
    time_str = now.strftime("%Y年%m月%d日%H时")
    return time_str


def friendly_useragent(ip_address, os, browser):
    # 操作系统映射
    os_map = {
        'Windows NT 10.0': 'Windows 10',
        'Windows NT 6.3': 'Windows 8.1',
        'Windows NT 6.2': 'Windows 8',
        'Windows NT 6.1': 'Windows 7',
        'Windows NT 6.0': 'Windows Vista',
        'Windows NT 5.1': 'Windows XP',
        'Windows NT 5.0': 'Windows 2000',
        'Macintosh': 'Mac OS X',
        'Linux': 'Linux'
    }

    # 浏览器映射
    browser_map = {
        'Chromium': 'Chromium内核的浏览器',
        'Chrome': 'Chrome浏览器',
        'Firefox': 'Firefox浏览器',
        'Safari': 'Safari浏览器',
        'Opera': 'Opera浏览器',
        'MSIE': 'IE浏览器',
        'Edg': 'Edge浏览器',
        'Trident': 'IE浏览器',
        'UCBrowser': 'UC浏览器'
    }

    # 解析OS和Browser信息
    friendly_os = os_map.get(os, os)
    friendly_browser = ''
    for b, v in browser_map.items():
        if b in browser:
            friendly_browser = v
            break
    if not friendly_browser:
        friendly_browser = browser

    nowtime = gettimestr()

    # 返回格式化的字符串
    return f"\n欢迎来自{ip_address}的访客\n现在是{nowtime}\n您的操作系统是{friendly_os}\n您正在使用的是{friendly_browser}\n*以上内容仅供参考*"


def imgfun(ip_address, os, browser, ):
    img = imgopen.copy()

    # 图片上添加文字
    font = ImageFont.truetype(font_path, size=42)
    text = friendly_useragent(ip_address, os, browser)
    img_draw = ImageDraw.Draw(img)
    # 文字描边
    outline_color = (255, 255, 255)
    outline_width = 2
    bbox = img_draw.textbbox((0, 0), text, font=font)
    w, h = bbox[2] - bbox[0], bbox[3] - bbox[1]
    x, y = 20, 20
    for xo in range(-outline_width, outline_width + 1, 2):
        for yo in range(-outline_width, outline_width + 1, 2):
            img_draw.text((x + xo, y + yo), text, fill=outline_color, font=font)

    # 绘制文本
    img_draw.text((x, y), text, fill=(0, 0, 0), font=font)

    # 转换为字节流
    img_byte_array = BytesIO()
    img.save(img_byte_array, format='JPEG')
    img_byte_array = img_byte_array.getvalue()

    return img_byte_array


def get_client_ip(self):
    # 检查X-Forwarded-For获取客户端IP
    xff_header = self.headers.get('X-Forwarded-For')
    if xff_header:
        # 找到最后一个地址为客户端真实IP
        ip_list = xff_header.split(',')
        client_ip = ip_list[-1].strip()
    else:
        # 如果XFF头部不存在，则使用客户端连接的IP
        client_ip = self.client_address[0]
    if ':' in client_ip:
        # 将IPv6地址对象转换为字符串
        client_ip = str(client_ip[0])

        # 去除IPv6地址中的端口信息
        if client_ip.startswith('[') and ']' in client_ip:
            client_ip = client_ip.split(']')[0] + ']'

    return client_ip

def handle_request(self):
    print(remove_first_path(self.path))
    if remove_first_path(self.path) == '/':
        # 获取访问者的IP
        try:
            ip_address = get_client_ip(self)
        except:
            ip_address = "1.14.5.14"

        # 获取UA信息
        user_agent = self.headers.get('User-Agent')
        uaclass = parse(user_agent)

        # 分析系统类型
        try:
            os = uaclass.os.family
        except:
            os = "Windows 98"
        # 分析浏览器类型
        try:
            browser = uaclass.browser.family
            browser_pattern = r'\b(?:Chrome|Chromium|Firefox|Safari|Opera|Edge|IE|Trident|YaBrowser|Maxthon|QQBrowser|UCBrowser)\b(?:\/[\d.]+)?'
            browser_match = re.search(browser_pattern, browser)
            browser = browser_match.group(0)
        except:
            browser = "不知道是什么\n反正肯定是Chromium内核"

        # 调用imgfun函数，生成图片
        img = imgfun(ip_address, os, browser)

        # 设置响应头
        self.send_response(200)
        self.send_header("Content-type", "image/png")
        self.send_header("Content-length", len(img))
        self.end_headers()

        # 发送图片数据
        self.wfile.write(img)

    else:
        page404(self)