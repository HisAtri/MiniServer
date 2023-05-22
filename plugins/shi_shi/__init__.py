def handler_request(handler):
    conntype = "Text"
    if conntype == "Text":
        import os
        import random
        import linecache
        #模块获取自身目录
        rootdir = os.path.dirname(os.path.abspath(__file__))
        text_path = os.path.join(rootdir, "sample.txt")
        num_lines = sum(1 for line in open(text_path))
        random_line = random.randint(1, num_lines)
        text = linecache.getline(text_path, random_line)
        textencode = text.encode("utf-8")

    handler.send_response(200)
    handler.send_header('Content-type', 'text/plain')
    handler.end_headers()
    handler.wfile.write(textencode)