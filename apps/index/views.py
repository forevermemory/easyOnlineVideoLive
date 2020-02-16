import datetime
import json
import os
import time
from os import path
import hashlib
import requests
from PIL import Image

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.http import require_http_methods
from django.views.generic import View
 
 
 
# @method_decorator(login_required, name='dispatch')
class HomeListView(View):
    '''获取所有可用的直播平台'''
    def pingtai(self):
        url = 'http://api.hclyz.com:81/mf/json.txt'
        response = requests.get(url)
        self.pingtai = json.loads(response.text)['pingtai']
        return self.pingtai
    def get(self, request):
        return render(request,'index/home.html',{'pingtai':self.pingtai})
 
# @method_decorator(login_required, name='dispatch')
class liveRoomView(View):
    '''某个平台下面的存在主播'''
    def get(self, request):
        address = request.GET.get('address')
        title = request.GET.get('title')
        zhubo = str("http://api.hclyz.com:81/mf/" + address)
        response = requests.get(zhubo)
        # print(response.text)
        liveroom = json.loads(response.text)['zhubo']

        return render(request, 'index/liveRoom.html',{"room_title":title,"anchors":liveroom} )
 
# @method_decorator(login_required, name='dispatch')
class anchor(View):
    '''直播视频页面'''
    def get(self, request):
        title1 = request.GET.get('title1')
        title2 = request.GET.get('title2')
        address = request.GET.get('address')
        return render(request, 'index/anchor.html', {'anchor_name':title1,'room_title':title2, 'anchor_address':address})



