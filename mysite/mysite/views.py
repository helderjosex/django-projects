from django.http import HttpResponse
from django.http import Http404
from django.template.loader import get_template
from django.template import Context
import datetime


def ola(request):
    return HttpResponse("Olá mundo!")

def data_atual(request):
    now = datetime.datetime.now()
    t = get_template('data_atual.html')
    html = t.render(Context({'data_atual': now}))
    return HttpResponse(html)

def data_mais(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(days=offset)
    html = "<em>Em %s dia(s), será %s.</em>" % (offset, dt)
    return HttpResponse(html)
