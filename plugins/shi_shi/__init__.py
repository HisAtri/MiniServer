def handler_request(handler):
    
    handler.send_response(200)
    handler.send_header('Content-type', 'text/plain')
    handler.end_headers()
    handler.wfile.write(b'This is a plain text response.')