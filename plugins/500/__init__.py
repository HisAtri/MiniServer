def handle_request(handler):
    handler.send_response(404)
    handler.send_header('Content-type', 'text/html')
    handler.end_headers()
    html = '''
    <!DOCTYPE html>
    <html lang="zh-CN">
    <head>
        <meta charset="UTF-8">
        <title>500 Internal Server Error</title>
        <meta name="description" content="使用Python搭建的多种API接口，">
        <meta name="author" content="HisAtri">
        <style type="text/css">
            .container {
                color: #2c2a33;
                max-width: 1280px;
                margin: 0 auto;
                text-align: center;
            }
            button {
                display: block;
                margin: 0 auto;
                padding: 10px 20px;
                border: none;
                border-radius: 5px;
                background-color: #4CAF50;
                color: #ffffff;
                font-size: 18px;
                cursor: pointer;
                transition: background-color 0.3s ease;
            }
            button:hover {
                background-color: #3e8e41;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>The MiniServer</h1>
            <h1>500 Internal Server Error</h1>
            <p>Sorry, something went wrong on our end.</p>
            <button onclick="window.location.href='/'">Go Back to Homepage</button>
        </div>
    </body>
        <footer class="container">
        <p>&copy; 2023 H.A. All rights reserved.</p>
        <a href="https://github.com/HisAtri/MiniServer" target="_blank">Github MiniServer</a>
    </footer>
    </html>
    '''
    handler.wfile.write(html.encode('utf-8'))