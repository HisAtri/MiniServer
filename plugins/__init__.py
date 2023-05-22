def handle_request(handler, content):
    handler.send_response(200)
    handler.send_header('Content-type', 'text/html')
    handler.send_header('Content-length', len(content))
    handler.end_headers()
    handler.wfile.write(content)