from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.core import serializers
from django.http import JsonResponse
import json
from app1 import lstm,LSTM2

# Create your views here.


@require_http_methods(['GET'])
def heatmap_data(request):
    response = {}
    try:
        types = request.GET['type']
        times = request.GET['time']
        filesup = '' if types != 'pattern' else 'mint'
        with open('./backend/backend/hmap/' + types + '/' + filesup + str(int(times) * 60) + '.json', 'r') as fp:
            data = json.load(fp)
            print(types, str(int(times) * 60))
            response['data'] = data['data']
    except Exception as e:
        response['msg'] = str(e)

    res = JsonResponse(response)
    res["Access-Control-Allow-Origin"] = "*"
    return res


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

@require_http_methods(["GET"])
def get_lstm(request):
    response = {}
    try:
        #LSTM2.setdata('65.08,65.08,65.08,65.08,68.59,63.45,63.45,61.9,61.9,65.08,66.79,66.79,66.79,66.79,68.59,70.5,68.59,70.5,70.5,70.5,68.59,68.59,68.59,65.08,61.9,61.9,61.9,65.08,68.59,70.5,68.59,66.79,65.08,66.79,66.79,66.79,68.59,65.08,65.08,65.08,65.08,66.79,70.5,68.59,68.59,68.59,68.59,70.5,70.5,70.5,70.5,68.59,65.08,66.79,66.79,66.79,68.59,68.59,66.79,68.59,66.79,66.79,68.59,66.79,68.59')
        #LSTM2.train_lstm()
        #response['msg'] = LSTM2.prediction([66.94, 69.77, 68.8, 68.8, 68.8], num=4)
#        lstm.setdata(request.GET['mapid'])
#        lstm.train_lstm()
        import subprocess
        '''output = ''
        p = subprocess.Popen('python app1\\LSTM2.py -d '+request.GET['data']+' -n '+request.GET['num'], stdout=subprocess.PIPE, bufsize=1)
        for line in iter(p.stdout.readline, b''):
            output+=line
            print(line),
        p.stdout.close()
        p.wait()'''
        output = subprocess.getoutput('python app1\\LSTM2.py -d '+request.GET['data']+' -n '+request.GET['num'] +' -e '+request.GET['epoch'])
        print(output)
        output = output[output.find("output:")+9:-1].split(',')
        print(output)
        response['msg'] = output#LSTM2.prediction(10)#request.GET['num'])
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)
#LSTM2.setdata([66.94, 69.77, 68.8, 68.8, 68.8])
#LSTM2.train_lstm()
#print(LSTM2.prediction(4))
#
#LSTM2.setdata('65.08,65.08,65.08,65.08,68.59,63.45,63.45,61.9,61.9,65.08,66.79,66.79,66.79,66.79,68.59,70.5,68.59,70.5,70.5,70.5,68.59,68.59,68.59,65.08,61.9,61.9,61.9,65.08,68.59,70.5,68.59,66.79,65.08,66.79,66.79,66.79,68.59,65.08,65.08,65.08,65.08,66.79,70.5,68.59,68.59,68.59,68.59,70.5,70.5,70.5,70.5,68.59,65.08,66.79,66.79,66.79,68.59,68.59,66.79,68.59,66.79,66.79,68.59,66.79,68.59')
#LSTM2.train_lstm()
#response['msg'] = LSTM2.prediction([66.94, 69.77, 68.8, 68.8, 68.8], num=4)
#        lstm.setdata(request.GET['mapid'])
#        lstm.train_lstm()
#print(LSTM2.prediction(10))
#print(LSTM2.prediction(10))#request.GET['num'])
#LSTM2.setdata('65.08,65.08,65.08,65.08,68.59,63.45,63.45,61.9,61.9,65.08,66.79,66.79,66.79,66.79,68.59,70.5,68.59,70.5,70.5,70.5,68.59,68.59,68.59,65.08,61.9,61.9,61.9,65.08,68.59,70.5,68.59,66.79,65.08,66.79,66.79,66.79,68.59,65.08,65.08,65.08,65.08,66.79,70.5,68.59,68.59,68.59,68.59,70.5,70.5,70.5,70.5,68.59,65.08,66.79,66.79,66.79,68.59,68.59,66.79,68.59,66.79,66.79,68.59,66.79,68.59')

#print(LSTM2.prediction(10))
