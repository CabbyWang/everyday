# 安装

```shell
pip install sqlalchemy
```

# 连接数据库

1. 数据库连接字符串

```shell
mysql://username:password@hostname/database
postgresql://username:password@hostname/database
sqlite:////absolute/path/to/database
sqlite:///c:/absolute/path/to/database
```

2. 创建数据库引擎

```python
from sqlalchemy import create_engine

DB_CONNECT_STRING = 'postgresql://username:password@hostname/database'
engine = create_engine(DB_CONNECT_STRING, echo=True)
# echo为True,会打印所有的sql语句
```

3. 传统方式连接数据库

```python
with engine.connect() as conn:
  rs = conn.execute('select 1')
  data = rs.fetchone()[0]
  print("data: {}".format(data))
```

4. connection事务

```python
with engine.connect() as conn:
	trans = conn.begin()
	try:
		r1 = conn.execute("")
		r2 = con.execute("")
		trans.commit()
	except:
		trans.rollback()
		raise
```

5. session

```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DB_CONNECT_STRING = 'postgresql://username:password@hostname/database'
# 创建数据库引擎
engine = create_engine(DB_CONNECT_STRING, echo=True)

# 创建会话类
DB_Session = sessionmaker(bind=engine)

# 创建会话对象
session = DB_Session()

# do something

session.close()
```

