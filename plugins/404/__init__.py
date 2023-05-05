def handle_request(handler):
    handler.send_response(404)
    handler.send_header('Content-type', 'text/html')
    handler.end_headers()
    html = "<html><head><title>404 Not Found</title></head><body><h1>404 Not Found</h1></body></html>"
    handler.wfile.write(html.encode('utf-8'))