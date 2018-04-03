***
# python -m

`run library module as a script(terminates option list)`    
意思是将库中的python模块用作脚本运行相当于    
`import xxx.py`


```python
python xxx.py       # 直接运行，main方法
python -m xxx.py    # 相当于import xxx.py，不执行main方法
```
***

# list遍历删除的正确方式
遍历时删除list中的元素会粗线`IndexError`的问题，这是因为在删除list中
的元素后，list的实际长度(len)变小了，但是循环次数不会减少(该循环多少次由刚开始的list决定)，
依然按照之前的次数遍历，就会造成索引溢出(IndexError)的问题

- 拷贝一份进行操作(比较笨的办法)
```python
num_list = [1, 2, 3, 4, 5]
for i in num_list[:]:         # 这里使用切片代替拷贝
    if i == 2:
        num_list.remove(2)
    else:
        print(i)
```

- 倒序遍历(自我感觉比较pythonic的方式)
````python
num_list = [1, 2, 3, 4, 5]
for i in reversed(num_list):
    if i == 2:
        num_list.remove(i)
    else:
        print(i)
````

- 如果list特别大, 使用reversed感觉有些不合适
```python
num_list = [1, 2, 3, 4, 5]
for i in range(len(num_list), -1, -1):      # 这里使用range的后两个参数进行倒序遍历
    if i == 2:
        num_list.remove(i)
    else:
        print(i)
```

- filter实现删除
```python
num_list = [1, 2, 3, 4, 5]
list(filter(num_list, lambda x: x != 2))
```
倒序循环删除和正序删除的区别(自己画了一个草图)
![xx](https://raw.githubusercontent.com/CabbyWang/everyday/master/image/reversed.jpg)

markdown显示本地图片语法   
`![xxx](../image/reversed.jpg)`
