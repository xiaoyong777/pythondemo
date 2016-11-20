from os import path
import os
import sys
import  shutil
import  glob

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

>>>path.join('/', 'home', 'zxy', 'PycharmProjects','pythondemo', 'demo') # 路径拼接
/home/zxy/PycharmProjects/pythondemo/demo

>>>path.exists(p) # 查询文件是否存在
>>>path.isfile(p) # 是否为文件
>>>path.isdir(p)  # 是否为文件夹
>>>path.getsize(p) # 获取文件大小


>>>glob.glob('/home/zxy/PycharmProjects/pythondemo/*') #列出路径文件列表
['/home/zxy/PycharmProjects/pythondemo/README.md', '/home/zxy/PycharmProjects/pythondemo/demo']

>>>os.mkdir(path)    # 创建文件夹
>>>os.rmdir(path)    # 删除空的目录
>>>os.listdir(path)  # 获取目录下的文件列表

'''
p="/home/zxy/PycharmProjects/pythondemo/demo/demo.txt"
with open(p,'w') as file: # open(p,"a")为追加写入
    file.write("12343\n") #写文件

with open(p,'r') as f:
    #print(f.read()) #读文件 read()可带一次读写文件大小参数 f.read(1024)
   print(f.readline())
os.rename(p,'/home/zxy/PycharmProjects/pythondemo/t.txt') # 文件重命名 包括路径 第二个参数为新的文件路径
shutil.copyfile('/home/zxy/PycharmProjects/pythondemo/t.txt','/home/zxy/t.txt') # 文件复制 第二个参数为新的文件路径
#shutil.move('/home/zxy/PycharmProjects/pythondemo/t.txt','/home/zxy/t.txt')  # 文件移动
os.remove('/home/zxy/PycharmProjects/pythondemo/t.txt') #文件删除  文件夹删除用removedirs()
os.remove('/home/zxy/t.txt')



