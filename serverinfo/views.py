from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from .models import serverList
# from django.template import loader
from django.http import Http404
from django.shortcuts import get_object_or_404

# def index(request):
#     return HttpResponse('hello world.')

def ipinfo(request, ip):
    return HttpResponse('ip %s' % ip)

def index(request):
    idList = serverList.objects.order_by('id')
    # output = ','.join([l.instance for l in id_list])
    # return HttpResponse(output)
    # template = loader.get_template('serverinfo/index.html')
    context = {
        'idList': idList
    }
    # return HttpResponse(template.render(context, request))
    return render(request, 'serverinfo/index.html', context)

# def detail(request, serverId):
#     try:
#         server = serverList.objects.get(id=serverId)
#     except server.DoesNotExist:
#         raise Http404('server does not exist')
#     return render(request, 'serverinfo/detail.html', {'server': server})

#shortcut:get_object_or_404,等同于上面detail方法,判断是否为空，还有判断列表的get_list_or_404
def detail(request, ip):
    server = get_object_or_404(serverList, ip=ip)
    return render(request, 'serverinfo/detail.html', {'server': server})