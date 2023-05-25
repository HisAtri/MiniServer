from datetime import datetime
import time, pytz
import json

from def_global import remove_first_path, page404, page500


tz = pytz.timezone('Asia/Shanghai')
d_time = datetime.now(tz)
local_time = d_time.strftime('%Y-%m-%d %H:%M:%S.%f%z')

def handle_request(handler):
    pathreq = remove_first_path(handler.path)
    if pathreq == '/':
        timencode = local_time.encode()
        handler.send_response(200)
        handler.send_header('Content-type', 'text/plain')
        handler.end_headers()
        handler.wfile.write(timencode)
    
    elif pathreq == '/json':
        timestamp = time.time()
        u_time = datetime.utcnow()
        utc = u_time.strftime('%Y-%m-%d %H:%M:%S.%f%z')
        timedic = {"Timestamp":timestamp, "Localtime":local_time, "UTC":utc}
        timejson = json.dumps(timedic).encode('utf-8')
        handler.send_response(200)
        handler.send_header('Content-type', 'application/json')
        handler.end_headers()
        handler.wfile.write(timejson)

    else:
        pathreq = pathreq.strip("/")
        print(pathreq)
        try:
            tz = pytz.timezone(pathreq)
            d_time = datetime.now(tz)
            tz_time = d_time.strftime('%Y-%m-%d %H:%M:%S.%f%z')
            timencode = tz_time.encode()
            handler.send_response(200)
            handler.send_header('Content-type', 'text/plain')
            handler.end_headers()
            handler.wfile.write(timencode)

        except pytz.exceptions.UnknownTimeZoneError:
            page404(handler)

        except:
            page500(handler)