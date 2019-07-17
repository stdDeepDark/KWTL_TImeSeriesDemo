from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.core import serializers
from django.http import JsonResponse
import json



# Create your views here.
@require_http_methods(["GET"])
def load_data(request):
    response = {}
    try:
        f = open(r"./traffic/raw/"+request.GET['file'], "r")  # 打开文件
        fr = f.read()  # 读取文件
        fr = fr.split(' ', fr.count(' '))
        response['info'] = 'info :'
        for i in fr:
            if (i.count('.') != 1):
                response['info'] += (i + ',')
                fr.remove(i)
        for i in range(43200 - len(fr)):
            fr.append(fr[-1])
        response['size'] = len(fr)
        response['msg'] = fr
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)
