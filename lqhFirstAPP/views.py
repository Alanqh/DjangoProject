from django.shortcuts import render,HttpResponse
import json
from django.http import JsonResponse

# Create your views here.
def index(request):
    return HttpResponse('Hello,lqh!')


newslist = {'title':'Wonderful boy!','datatime':'2023-03-02 12:56:23'}
def getnews(request):

    newsjs = json.dumps(newslist)
    return HttpResponse(newsjs)

def getmessage(request):
    return JsonResponse(newslist)

def myhome(request):
    return render(request, 'lqhFirstAPP/index.html', {'title': '小华爱编程'})