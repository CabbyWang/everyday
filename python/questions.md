***
# questions
**1. 一行代码实现对列表a中的偶数位置的元素进行加3后求和？**

自我感觉问题有点歧义, 最后是将偶数元素求和还是将所有元素求和, 这里我思考了两种方式,如下

```python
a = [1, 2, 3, 4, 5, 6, 7]
sum(map(lambda x: x + 3 if x%2 == 0 else x, a))   # 求和所有

sum(map(lambda x: x + 3, a[1::2]))                # 求和偶数元素
```

**2. List = [-2, 1, 3, -6]，如何实现以绝对值大小从小到大将 List 中内容排序**
```python
List = [-2, 1, 3, -6]
sorted(List, key=lambda x: abs(x))   # 这是我第一时间想到的方法...有点笨

sorted(List, key=abs)
```

**dd**
