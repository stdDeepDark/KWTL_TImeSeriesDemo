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

@require_http_methods(["GET"])
def get_map(request):
    response = {}
    try:
        #import os
        roads = json.load(open('./traffic/RTICLINK_BeiJing.json', 'r'))
        f = open(r"./traffic/map_list.txt", "r")  # 打开文件
        fr = f.read()  # 读取文件
        fr.replace(' ','')
        fr = fr.split(',', fr.count(','))
        map = []

        for i in fr:
            i = int(i)
            '''
            id = roads["features"][i]["properties"]["ID"]
            mapid = roads["features"][i]["properties"]["MapID"] + "_" + roads["features"][i]["properties"][
                "Kind"] + "0"*(4 - len(id)) + id;

            if(os.path.exists('./traffic/raw/' + mapid)):'''
            if (roads["features"][i]["properties"]["Kind"] == request.GET['kind']):
                map.append(i);
        response['msg'] = map
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)
