from os import path
import os
import sys

'''
>>>os.getcwd() # 获取当前文件所在目录
/home/zxy/PycharmProjects/pythondemo/demo

>>>sys.argv[0] # 获取当前文件的局对路径
/home/zxy/PycharmProjects/pythondemo/demo/文件.py

>>>p=sys.argv[0]
>>>path.dirname(p) # 获取路径中的目录
/home/zxy/PycharmProjects/pythondemo/demo

>>>path.basename(p) #获取路径中的文件名
文件.py

>>>path.split(p) #路径拆分为目录和文件名
('/home/zxy/PycharmProjects/pythondemo/demo', '文件.py')

'''
p=sys.argv[0]
print(path.split(p))