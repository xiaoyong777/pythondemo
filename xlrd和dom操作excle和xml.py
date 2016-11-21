import xlrd
from xml.dom import minidom

# 从excle 读取数据 写入xml
impl = minidom.getDOMImplementation()
dom = impl.createDocument(None, None, None)
root = dom.createElement("array") # 获取根节点
data = xlrd.open_workbook('.\\ExpressCode.xls')
table = data.sheets()[0]
nrows = table.nrows
for i in range(nrows):
    code = table.cell(i, 0).value
    name = table.cell(i, 1).value
    print(name)
    skill = dom.createElement('express') # 新建一个节点
    skill.setAttribute('code', str(code)) # 设置属性
    skillVal = dom.createTextNode(str(name))  # 创建节点的值
    skill.appendChild(skillVal)  # 设置值
    root.appendChild(skill) # 新建的节点添加进根节点
dom.appendChild(root)
f = open('.\\ExpressCode.xml', 'w')
dom.writexml(f, ' ', ' ', '\n', "gb2312")
f.close()
