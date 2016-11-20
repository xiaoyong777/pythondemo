# -*- coding: utf-8 -*-
from urllib.request import urlopen
from bs4 import BeautifulSoup
import json
import os

def GET():
    try:
        html = urlopen("http://www.ishadowsocks.org")
        bsObj = BeautifulSoup(html.read(),"html.parser")
    except BaseException as e:
        return ("网络链接错误,检查网络和链接地址是否正常",None)
    try:
        bsRow = bsObj.find(id="free").find("div").findAll("div")[2]
        list=[]
        for bsCol in bsRow.findAll("div",{"class":"col-sm-4 text-center"}):
            dict={"server":"","server_port":"","password":"","method":"","remarks":""}
            index = 0
            for bsAccount in bsCol.findAll("h4"):
                val = bsAccount.get_text().split(':')[1]
                if index == 0:
                    dict["server"] = val
                elif index == 1:
                    dict["server_port"] = val
                elif index == 2:
                    dict["password"] = val
                elif index == 3:
                    dict["method"] = val
                elif index ==4:
                    dict["remarks"] = val
                    break
                else:
                    break
                index = index+1
            list.append(dict)
    except BaseException as e:
        return ("解析错误，检查链接和解析规则是否正确",None)
    try:
        BASE_DIR = os.path.dirname(__file__)
        file_path = os.path.join(BASE_DIR, 'gui-config.json')

        fp = open(file_path, 'r')
        dict = json.load(fp)
        fp.close()
    except IOError as e:
        return ("文件读取错误，检查gui-config.json文件是否存在",None)
    try:
        dict["configs"] = list

        fp = open(file_path,'w')
        fp.write(json.dumps(dict))
        fp.close()
    except IOError as e:
        return "文件写入错误"
    return (None,list)

(err,result) = GET()
if err == None:
    print("获取成功 账号信息如下：")
    jsonDumpsIndentStr = json.dumps(result, indent=1);#josn格式化
    print(jsonDumpsIndentStr)
else:
    print(err)
input("")