# 定义一些全局常用的模块


#去掉路径的首段
def remove_first_path(path):
    import os
    if not path.endswith("/"):
        path += "/"

    first, _, rest = path.lstrip("/").partition("/")
    pathstr = os.path.normpath(os.path.join("/", rest)).replace('\\', '/')

    if pathstr == "/":
        return pathstr

    if first:
        pathstr = os.path.join("/", pathstr.lstrip(first).lstrip(os.sep)).replace('\\', '/')

    return pathstr

def get_first_path(path):
    # 去除开头和结尾的空格
    path = path.strip()
    # 去除结尾的斜杠
    path = path.rstrip('/')
    # 拆分路径
    path_components = path.split('/')
    # 返回第一个非空路径
    for component in path_components:
        if component != '':
            return component
    return '/'

def page404(self):
    import importlib
    mod404 = importlib.import_module("404")
    mod404.handle_request(self)

def page500(self):
    import importlib
    mod404 = importlib.import_module("500")
    mod404.handle_request(self)

def page301(self, host):
    self.send_response(301)
    self.send_header('Location', "http://" + host)
    self.end_headers()