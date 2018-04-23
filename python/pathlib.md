***
```python
from pathlib import Path
p = Path()
# WindowsPath('.')
p.resolve()                     # 文档显示是absolute path, 这里感觉只能用在获取当前绝对路径上
# WindowsPath('C:/Users/Cabby')

p = Path(r'd:\test')
# WindowsPath('d:/test')
p.iterdir()                     # 相当于os.listdir
p.glob('*')                     # 相当于os.listdir, 但是可以添加匹配条件
p.rglob('*')                    # 相当于os.walk, 也可以添加匹配条件
```
