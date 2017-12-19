# json 用法

# loads 和 load
> loads是将str转化成dict格式
> load  与文件操作结合
```python
>> import json
# a = '{"2":"a", "1":"c", "3":"d"}'
with open('d:/test/js.json', 'w') as fp:
    json.load(fp)   # 读取json文件
