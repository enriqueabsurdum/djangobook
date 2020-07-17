"""My Site views."""

# Python
import datetime

# Django
from django.shortcuts import Http404, HttpResponse

HTML = '''
<!DOCTYPE html>
<html lang="es">
<head>
    <meta http­equiv="content­type" content="text/html; charset=utf­8">
    <meta name="robots" content="NONE,NOARCHIVE">
    <title>Hello, world</title>
    <style type="text/css">
        html * { padding:0; margin:0; }
        body * { padding:10px 20px; }
        body * * { padding:0; }
        body { font:small sans­serif; }
        body>div { border­bottom:1px solid #ddd; }
        h1 { font­weight:normal; }
        #summary { background: #e0ebff; }
    </style>
</head>
<body>
    <div id="summary">
    <h1>Hello, world!</h1>
</div>
</body></html>
'''


def hello_world(request):
    return HttpResponse(HTML)


def current_datetime(request):
    now = datetime.datetime.now()
    html = '''
        <html>
            <body>
                <h1>It is now {}</h1>
            </body>
        </html>
    '''.format(now)
    return HttpResponse(html)


def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()

    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = '''
        <html>
            <body>
                <h1>In {} hour(s), it will be {}.</h1>
            </body>
        </html>
    '''.format(offset, dt)
    return HttpResponse(html)
