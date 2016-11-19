# pytho常用方法
## 一、序列方法
可用于序列(list,tuple,字符串)的内建函数
```python
all([True, 1, "hello!"])         # 是否所有的元素都相当于True值
any(["", 0, False, [], None])    # 是否有任意一个元素相当于True值

sorted([1,5,3])                  # 返回正序的序列，也就是[1,3,5]
reversed([1,5,3])                # 返回反序的序列，也就是[3,5,1]

# s为一个序列
len(s)        # 返回： 序列中包含元素的个数
min(s)        # 返回： 序列中最小的元素
max(s)        # 返回： 序列中最大的元素
all(s)        # 返回： True, 如果所有元素都为True的话
any(s)        # 返回： True, 如果任一元素为True的话
```
主要用于查询的方法，不改变序列本身，可用于list和tuple
```python
sum(s)        # 返回：序列中所有元素的和
# x为元素值，i为下标(元素在序列中的位置)
s.count(x)    # 返回： x在s中出现的次数
s.index(x)    # 返回： x在s中第一次出现的下标
```
由于tuple的元素不可变，下面方法只能用于list
```python
# l为一个表, l2为另一个表

l.extend(l2)  # 在表l的末尾添加表l2的所有元素
l.append(x)   # 在l的末尾附加x元素
l.sort()      # 对l中的元素排序
l.reverse()   # 将l中的元素逆序
l.pop()       # 返回：表l的最后一个元素，并在表l中删除该元素
del l[i]      # 删除该元素

(以上这些方法都是在原来的表的上进行操作，会对原来的表产生影响，而不是返回一个新表。)
```
字符串常用：尽管字符串是定值表的特殊的一种，但字符串(string)类有一些方法是改变字符串的。这些方法的本质不是对原有字符串进行操作，而是删除原有字符串，再建立一个新的字符串，所以并不与定值表的特点相矛盾。
```python
#str为一个字符串，sub为str的一个子字符串。s为一个序列，它的元素都是字符串。width为一个整数，用于说明新生成字符串的宽度。

str.count(sub)   #    返回：sub在str中出现的次数
str.find(sub)    #    返回：从左开始，查找sub在str中第一次出现的位置。如果str中不包含sub，返回 -1
str.index(sub)   #    返回：从左开始，查找sub在str中第一次出现的位置。如果str中不包含sub，举出错误
str.rfind(sub)   #    返回：从右开始，查找sub在str中第一次出现的位置。如果str中不包含sub，返回 -1
str.rindex(sub)  #    返回：从右开始，查找sub在str中第一次出现的位置。如果str中不包含sub，举出错误
str.isalnum()    #    返回：True， 如果所有的字符都是字母或数字
str.isalpha()    #    返回：True，如果所有的字符都是字母
str.isdigit()    #    返回：True，如果所有的字符都是数字
str.istitle()    #    返回：True，如果所有的词的首字母都是大写
str.isspace()    #    返回：True，如果所有的字符都是空格
str.islower()    #    返回：True，如果所有的字符都是小写字母
str.isupper()    #    返回：True，如果所有的字符都是大写字母
str.split([sep, [max]])  #  返回：从左开始，以空格为分割符(separator)，
                         #  将str分割为多个子字符串，总共分割max次。
                         #  将所得的子字符串放在一个表中返回。可以str.split(',')的方式使用逗号或者其它分割符
                         
str.rsplit([sep, [max]]) #  返回：从右开始，以空格为分割符(separator)，
                         #  将str分割为多个子字符串，总共分割max次。
                         #  将所得的子字符串放在一个表中返回。可以str.rsplit(',')的方式使用逗号或者其它分割符
                         
str.join(s)              #   返回：将s中的元素，以str为分割符，合并成为一个字符串。

str.strip([sub])         #   返回：去掉字符串开头和结尾的空格。
                         #   也可以提供参数sub，去掉位于字符串开头和结尾的sub
                         
str.replace(sub, new_sub) # 返回：用一个新的字符串new_sub替换str中的sub
str.capitalize()          # 返回：将str第一个字母大写
str.lower()               # 返回：将str全部字母改为小写
str.upper()               # 返回：将str全部字母改为大写
str.swapcase()            # 返回：将str大写字母改为小写，小写改为大写
str.title()               # 返回：将str的每个词(以空格分隔)的首字母大写
str.center(width)         # 返回：长度为width的字符串，将原字符串放入该字符串中心，其它空余位置为空格。
str.ljust(width)          # 返回：长度为width的字符串，将原字符串左对齐放入该字符串，其它空余位置为空格。
str.rjust(width)          # 返回：长度为width的字符串，将原字符串右对齐放入该字符串，其它空余位置为空格。
```
##数学运算
```python
abs(-5)                          # 取绝对值，也就是5
round(2.6)                       # 四舍五入取整，也就是3.0
pow(2, 3)                        # 相当于2**3，如果是pow(2, 3, 5)，相当于2**3 % 5
cmp(2.3, 3.2)                    # 比较两个数的大小
divmod(9,2)                      # 返回除法结果和余数
max([1,5,2,9])                   # 求最大值
min([9,2,-4,2])                  # 求最小值
sum([2,-1,9,12])                 # 求和
```
##类型转换
```python
int("5")                         # 转换为整数 integer
float(2)                         # 转换为浮点数 float
long("23")                       # 转换为长整数 long integer
str(2.3)                         # 转换为字符串 string
complex(3, 9)                    # 返回复数 3 + 9i

ord("A")                         # "A"字符对应的数值
chr(65)                          # 数值65对应的字符
unichr(65)                       # 数值65对应的unicode字符

bool(0)                          # 转换为相应的真假值，在Python中，0相当于False 
                                 # 在Python中，下列对象都相当于False：
                                 # ** [], (), {}, 0, None, 0.0, '' **

bin(56)                          # 返回一个字符串，表示56的二进制数
hex(56)                          # 返回一个字符串，表示56的十六进制数
oct(56)                          # 返回一个字符串，表示56的八进制数

list((1,2,3))                    # 转换为表 list
tuple([2,3,4])                   # 转换为定值表 tuple
slice(5,2,-1)                    # 构建下标对象 slice
dict(a=1,b="hello",c=[1,2,3])    # 构建词典 dictionary

```
##类、对象、属性
```python
all([True, 1, "hello!"])         # 是否所有的元素都相当于True值
any(["", 0, False, [], None])    # 是否有任意一个元素相当于True值

sorted([1,5,3])                  # 返回正序的序列，也就是[1,3,5]
reversed([1,5,3])                # 返回反序的序列，也就是[3,5,1]
```