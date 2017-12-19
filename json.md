# json 用法

## loads 和 load
> loads 将str转化成dict格式
```python
import json
d = {'2':'a', '1':'c', '3':'d'}
with open('d:/test/js.json', 'w') as fp:
    s = json.loads(d)   # 将dict转换为str
    print(s)         # 输出'{"2":"a", "1":"c", "3":"d"}'
```
> load 与文件操作结合
```python
import json
# a = '{"2":"a", "1":"c", "3":"d"}'
with open('d:/test/js.json') as fp:
    json.load(fp)   # 读取json文件
```

## dumps 和 dump
> dumps 将dict转化为str格式
````python
imprt json
d = {0: 'e', 1: 'c', 2: 'a', 3: 'b', 5: 'f'}
s = json.dumps(d)      
# 输出结果为    '{"2": "a", "1": "c", "3": "b", "0": "e", "5": "f"}'   为str
````
> dump 与文件操作结合
```python
import json
d = {'2':'a', '1':'c', '3':'d'}
with open('d:/test/js.json', 'w') as fp:
    json.dump(d, fp, indent=4)
`````
