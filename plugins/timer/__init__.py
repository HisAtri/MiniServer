from def_global import remove_first_path, page404, page500



def handle_request(handler):
    import time
    pathreq = remove_first_path(handler.path)
    if pathreq == '/':
        local_time = time.strftime('%Y-%m-%d %H:%M:%S%z', time.localtime())
        timencode = local_time.encode()
        handler.send_response(200)
        handler.send_header('Content-type', 'text/plain')
        handler.end_headers()
        handler.wfile.write(timencode)
    
    elif pathreq == '/json':
        import json
        local_time = time.strftime('%Y-%m-%d %H:%M:%S%z', time.localtime())
        utc = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime())
        timestamp = time.time()
        timedic = {"Timestamp":timestamp, "Localtime":local_time, "UTC":utc}
        timejson = json.dumps(timedic).encode('utf-8')

        handler.send_response(200)
        handler.send_header('Content-type', 'application/json')
        handler.end_headers()
        handler.wfile.write(timejson)

    else:
        import pytz
        pathreq = pathreq.strip("/")
        print(pathreq)
        try:
            from datetime import datetime
            tz = pytz.timezone(pathreq)
            d_time = datetime.now(tz)
            tz_time = d_time.strftime('%Y-%m-%d %H:%M:%S.%f %z')
            timencode = tz_time.encode()
            handler.send_response(200)
            handler.send_header('Content-type', 'text/plain')
            handler.end_headers()
            handler.wfile.write(timencode)

        except pytz.exceptions.UnknownTimeZoneError:
            page404(handler)

        except:
            page500(handler)