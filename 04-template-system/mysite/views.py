"""My Site views."""

# Python
import datetime

# Django
from django.shortcuts import Http404, render


def current_time(request):
    now = datetime.datetime.now()
    return render(request, 'current-datetime.html', {'now': now})


def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()

    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    return render(request, 'hours-ahead.html', {
        'hour_offset': offset,
        'next_time': dt,
    })
