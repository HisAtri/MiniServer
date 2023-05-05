# MiniServer

## MiniServer：可拓展的Python服务器

为对接nonebot2插件建立的服务器。

### 插件功能

- [x] 欢迎图片
- [ ] 一言（纯文本）
- [ ] 随机图片
- [ ] 漂流瓶

## 本地搭建方法

Python>=3.7

1.克隆本项目到本地

`git clone https://github.com/HisAtri/MiniServer.git`

2.安装依赖

```
cd MiniServer
pip install -r requirements.txt
```

视实际情况可能需要

`pip3 install -r requirements.txt`

3.（可选）修改配置

```python
#config_global.py
#目前用得到的暂时只有server["port"]
config_global = {
    "database":{
        "type":"mysql",
        "version":"sqlite3",
        "path":"sqlite3.db",
        "host":"localhost",
        "port":3306,
        "dbname":"miniserver",
        "user":"miniserver",
        "password":"password"
    }
}
server={
    "port":8181,
}
```

4.启动项目

`python main.py`

或者

`python3 main.py`

或者使用Supervisor

```
command=python /path/to/MiniServer/main.py	#或者Python3
directory=/path/to/MiniServer
```

5.访问项目

通过http://host:port/plugin_name访问对应模块

例如http://127.0.0.1:8181/imgapi

也可通过Nginx等建立反向代理，访问http://domain.com/plugin_name

