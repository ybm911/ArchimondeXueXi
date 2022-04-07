"""
作者：Elli0t
2022.04.07
如要运行需要修改三处代码
""" 
import requests
import time
import random


url = "http://osscache.vol.jxmfkj.com/pub/vol/volClass/join?accessToken="


# 第一处：修改班级人数 1-43 人
for i in range(1,44):
  i = str(i)
  i = i.rjust(2,'0')


  # 第二处：修改班级编号：2112 班
  peopleNumber = "2112" + i
  # 第三处：修改 nid ，具体查看 README.md
  payload = '''{"course":"7","subOrg":null,"nid":"N0014000210021029","cardNo":"'''+ peopleNumber +'''"}'''
  

  headers = {
    'Host': 'osscache.vol.jxmfkj.com',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'X-Requested-With': 'XMLHttpRequest',
    'Accept-Language': 'zh-cn',
    'Accept-Encoding': 'gzip, deflate',
    'Content-Type': 'application/json;charset=UTF-8',
    'Origin': 'http://osscache.vol.jxmfkj.com',
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_8_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.18(0x1800123c) NetType/WIFI Language/zh_CN',
    'Connection': 'keep-alive',
    'Referer': 'http://osscache.vol.jxmfkj.com/html/h5_index.html'
  }
  response = requests.request("POST", url, headers=headers, data=payload)
  print(peopleNumber)
  print(response.text)
  time.sleep( random.randint(1,10) )
