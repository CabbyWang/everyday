***
# strip(X)

````python
a = 'abcd_342_erw'
a.strip('eawrb')
[out] 'cd_342_'
````
`分析：python对字符串X的处理是一个set（又单个字母组成的set），如果a中包含任意set中的字符，都会被strip掉，直到遇到第一个不在set中的字符`
***

# 字符串编码(chardet)
````python
import chardet     # 分析字符串编码
import sys
text = '你好'
orig_encoding = charset.detect(text)['encoding']          # charset.detect()输出的是一个字典
term_encoding = sys.stdout.encoding                       # 获取终端编码格式
print(text.decode(orig_encoding).encode(term_encoding))   # 将字符串编码转换
````
***

# pip安装flask-sqlalchemy
`出现premission或者unnicode问题`
## 解决办法[https://segmentfault.com/q/1010000008071661](https://segmentfault.com/q/1010000008071661)
### 打开pip目录下pip\compat\__init__.py约75行`return s.decode('utf_8')`改为`return s.decode('cp936')`(cp936即为gbk)
***
