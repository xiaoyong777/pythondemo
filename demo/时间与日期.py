import time
import datetime

'''
time.sleep(3)# 程序休眠 单位秒

time.gmtime() # 返回struct_time格式的UTC时间
time.localtime()  # 返回struct_time格式的当地时间, 当地时区根据系统环境决定

>>>st=time.localtime()
time.struct_time(tm_year=2016, tm_mon=11, tm_mday=19, tm_hour=20, tm_min=51, tm_sec=39, tm_wday=5, tm_yday=324, tm_isdst=0)
>>>time.mktime(st)
1479559939.0

t=datetime.datetime(2016,11,19) # t属性：hour, minute, second, microsecond, year, month, day, weekday

>>>t=datetime.datetime(2016,11,19)
>>>t.year
2016
>>>t.month
11

时间格式化
>>>t=time.localtime()
>>>time.strftime("%Y-%m-%d %H:%M:%S",t)
2016-11-19 21:18:42
'''

print()