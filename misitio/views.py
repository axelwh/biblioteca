import datetime

from django.shortcuts import render
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse, Http404

def hola(request):
    return HttpResponse('Hola')

def fecha_actual(request):
    hora_actual = datetime.datetime.now()
    # template = get_template('fecha_actual.html')
    # context = Context({"fecha_actual": hora_actual})
    # html = template.render(context)
    # html = '<h1>%s</h1>' % hora_actual
    # return HttpResponse(html)
    return render(request,'fecha_actual.html',{'fecha_actual': hora_actual})
def fecha_adelantada(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    assert False
    dt = datetime.datetime.now()+datetime.timedelta(hours=offset)
    html = "<h1>En %s hora(s) seran %s</h1>" % (offset, dt)
    return HttpResponse(html)
