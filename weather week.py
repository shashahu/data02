# -*- coding: utf-8 -*-
"""
Created on Sun Jun  3 09:47:06 2018

@author: lenovo
"""

import json
import urllib.request as r
city=input("请输入城市的拼音:")
address='http://api.openweathermap.org/data/2.5/forecast?q={},cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996 '
info=r.urlopen(address.format(city)).read().decode('utf-8','ignore')
#print(info)
data=json.loads(info)
print("未来五天不同时间的天气")

for i in range(0,38,4):
    print("城市"+str(data['city']['name'])+"\n时间："+str(data['list'][i]['dt_txt'])+"\n温度:"+str(data['list'][i]['main']['temp'])+"\n天气:"+str(data['list'][i]['weather'][0]['description'])+"\n气压:"+str(data['list'][i]['main']['pressure']))
    