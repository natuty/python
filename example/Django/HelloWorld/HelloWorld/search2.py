# -*- coding: utf-8 -*-
import sys
from django.shortcuts import render
from django.views.decorators import csrf
reload(sys)   
sys.setdefaultencoding('utf8') 
# 接收POST请求数据
def search_post(request):
    ctx ={}
    if request.POST:
        ctx['rlt'] = request.POST['q']
    return render(request, "post.html", ctx)