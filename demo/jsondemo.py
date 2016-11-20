import json

'''
dict转json
>>>json.dumps(dict(name='Bob',age='20',score='99'))
{"name": "Bob", "age": "20", "score": "99"}

写入文件
>>>f = open('./tt.txt','a')
>>>json.dump(josn,f)

json转dict
>>>json.loads('{"name": "Bob", "age": "20", "score": "99"}')
{'score': '99', 'name': 'Bob', 'age': '20'}

文件读取
>>>f = open('./tt.txt','r')
>>>json.load(f)

'''
class Student(object):

    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    def __str__(self):
        return 'Student object (%s, %s, %s)' % (self.name, self.age, self.score)

s = Student('Bob', 20, 88)
std_data = json.dumps(s, default=lambda obj: obj.__dict__)      # 对象转json
print('Dump Student:', std_data)
rebuild = json.loads(std_data, object_hook=lambda d: Student(d['name'], d['age'], d['score']))     # json转对象
print(rebuild)