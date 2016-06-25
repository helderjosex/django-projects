from django.http import HttpResponse
from django.http import Http404
import datetime


def ola(request):
    return HttpResponse("Olá mundo!")

def data_atual(request):
    now = datetime.datetime.now()
    html = "<em>Agora é %s.</em>" % now
    return HttpResponse(html)

def data_mais(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(days=offset)
    html = "<em>Em %s dia(s), será %s.</em>" % (offset, dt)
    return HttpResponse(html)
