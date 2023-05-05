from configparser import ConfigParser
import http.server
import os
import socketserver
import http.client
import logging

from def_global import get_first_path

logger = logging.getLogger()
logger.setLevel(logging.INFO)
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
file_handler = logging.FileHandler('log.txt')
file_handler.setLevel(logging.WARNING)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)
logger.addHandler(console_handler)
logger.addHandler(file_handler)

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # 获取请求路径
        path = self.path
        # 获取配置文件中对应的插件
        plugin_name = get_first_path(path)
        # 导入对应的插件模块并处理请求
        try:
            plugin_module = __import__('plugins.' + plugin_name, fromlist=['*'])
            plugin_module.handle_request(self)
        except ModuleNotFoundError:
            plugin_module = __import__('plugins.404', fromlist=['*'])
            plugin_module.handle_request(self)


# 启动Web服务器
PORT = 8080
Handler = MyHandler
httpd = socketserver.TCPServer(("", PORT), Handler)
logger.info("serving at port"+str(PORT))
httpd.serve_forever()