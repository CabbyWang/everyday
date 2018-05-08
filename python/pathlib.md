***
# 超好用的Pathlib

`Pathlib`有多好用? 可能只能这样解释了: 自从接触了`Pathlib`, 之前用的`os`相关操作, 基本上就不想再用了/笑哭

这里先做部分总结, 在之后的使用中会继续更新`^_^`


```python
from pathlib import Path
p = Path()
# WindowsPath('.')
p.resolve()                     # 文档显示是absolute path, 这里感觉只能用在获取当前绝对路径上
# WindowsPath('C:/Users/Cabby')
```

常用操作
```python
p = Path(r'd:\test\tt.txt.bk')
p.name                          # 获取文件名
# tt.txt.bk
p.stem                          # 获取文件名除后缀的部分
# tt.txt
p.suffix                        # 文件后缀
# .bk
p.suffixs                       # 文件的后缀们...
# ['.txt', '.bk']
p.parent                        # 相当于dirnanme
# WindowsPath('d:/test')
p.parents                       # 返回一个iterable, 包含所有父目录
# <WindowsPath.parents>
for i in p.parents:
	print(i)
# d:\test
# d:\
a.parts                         # 将路径通过分隔符分割成一个元祖
# ('d:\\', 'test', 'tt.txt.bk')
```

另一些常用操作..
```python
p = Path(r'd:\test')
p = Path(p, 'tt.txt')           # 字符串拼接
p.exists()                      # 判断文件是否存在
p.is_file()                     # 判断是否是文件
p.is_dir()                      # 判断是否是目录
```

遍历文件夹
```python
p = Path(r'd:\test')
# WindowsPath('d:/test')
p.iterdir()                     # 相当于os.listdir
p.glob('*')                     # 相当于os.listdir, 但是可以添加匹配条件
p.rglob('*')                    # 相当于os.walk, 也可以添加匹配条件
```

创建文件夹
```python
p = Path(r'd:\test\tt\dd')
p.mkdir(exist_ok=True)          # 创建文件目录(前提是tt目录存在, 否则会报错)
# 一般我会使用下面这种创建方法
p.mkdir((exist_ok=True, parents=True) # 递归创建文件目录
```

文件详细信息(size, createtime...)
```python
p = Path(r'd:\test\tt.txt')
p.stat()                        # 获取详细信息
# os.stat_result(st_mode=33206, st_ino=562949953579011, st_dev=3870140380, st_nlink=1, st_uid=0, st_gid=0, st_size=0, st_atime=1525254557, st_mtime=1525254557, st_ctime=1525254557)
p.stat().st_size                # 文件大小
# 0
p.stat().st_ctime               # 创建时间
# 1525254557.2090347
# 其他的信息也可以通过相同方式获取
p.stat().st_mtime               # 修改时间
```

