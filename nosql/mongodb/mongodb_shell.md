# mongodb基本操作

## database

```shell
# 查看数据库
show dbs
show databases

# 查看当前所在数据库
db

# 切换/创建数据库
use db_name

# 删除当前数据库
db.dropDatabase()
```

## collection

1. collection操作

   ```shell
   # 查看collections
   show collections  # 更准确
   show tables
   
   # 创建collection
   db.createCollection("abc")
   db.col.insert({"name": "cabbyw"})  # 插入数据自动创建collection
   document = ({"name": "ls"})
   db.col.save(document)  # 不指定_id字段和insert()方法类似，指定_id字段，则更新该_id的数据
   
   # 删除collection
   db.abc.drop()
   ```

2. 增

   ```shell
   db.col.insert({name: "cabbyw", age: 25})
   ```
   
   ```shell
# 定义一个变量document
   document = ({name: "cabbyw", age: 24})
   
   # insert
db.col.insert(document)
   
   # insertOne
   db.col.insertOne(document)
   
   # insertMany
   db.col.insertMany([document, document])
   ```
   
3. 删

   a. remove

   ```shell
   # 语法
   db.collection.remove(
   	<query>,
   	<justOne>  # 默认False(删除所有匹配项)
   )
   # Or
   db.collection.remove(
   	<query>,
   	{
   		justOne: <boolean>,  # 默认False(删除所有匹配项)
   		writeConcern: <document>,
   		collation: <document>
   	}
   )
   ```

   b. deleteOne

   ```shell
   # 语法
   db.collection.deleteOne(
   	<filter>,
   	{
   		writeConcert: <document>,
   		collation: <document>
   	}
   )
   ```

   c. deleteMany

   ```shell
   # 语法
   db.collection.deleteMany(
   	<filter>,
   	{}
   )
   ```

   

   ```shell
   db.col.remove({name: "cabbyw"}, true)  # 只删除一个name=cabbyw的记录
   db.col.remove({name: "cabbyw"})  # 删除所有name=cabbyw的记录
   db.col.deleteOne({name: "cabbyw"})  # 只删除一个name=cabbyw的记录
   db.col.deleteMany({name: "cabbyw"})  # 删除所有name=cabbyw的记录
   ```

4. 查

   ```shell
   db.col.find({name: "cabbyw"})  # 查找name=cabbyw的记录
   db.col.find({"name": "cabbyw"})  # 同上
   db.col.find({"a.b.c": 1})  # 嵌套查找value[a][b][c]=1的记录
   
   # 数值比较
   db.col.find(age: {$gt: 24})  # 查找age > 24的记录
   db.col.find(age: {$gte: 24})  # 查找age >= 24的记录
   db.col.find(age: {$lt: 24})  # 查找age < 24的记录
   db.col.find(age: {$lte: 24})  # 查找age <= 24的记录
   
   # 组合查询
   db.col.find({age: {$gt: 24}, gender: "male"})  # 查找age > 24 且是男性的记录
   
   # 数组相关
   # db.col.insertMany([
   #    { item: "journal", qty: 25, tags: ["blank", "red"], dim_cm: [ 14, 21 ] },
   #    { item: "notebook", qty: 50, tags: ["red", "blank"], dim_cm: [ 14, 21 ] },
   #    { item: "paper", qty: 100, tags: ["red", "blank", "plain"], dim_cm: [ 14, 21 ] },
   #    { item: "planner", qty: 75, tags: ["blank", "red"], dim_cm: [ 22.85, 30 ] },
   #    { item: "postcard", qty: 45, tags: ["blue"], dim_cm: [ 10, 15.25 ] }
   # ]);
   db.col.find({tags: ["red", "blank"]})  # 查找tags数组为["red", "blank"]的记录, 数组元素顺序要一致
   db.col.find({tags: {$all: ["red", "blank"]}})  # 查找tags数组中包含"red"和"blank"的记录, both包含
   db.col.find({dim_cm: {$gt: 24}})  # 查找dim_cm数组中存在大于24的记录
   db.col.find({dim_cm: {$elemMatch: {$gt: 23, $lt: 30}}})  # 查找dim_cm书中中存在>23 <30的记录
   db.col.find({dim_cm: {$size: 3}})  # 查找dim_cm数组大小为3的记录
   db.col.find({dim_cm.1: {$gt: 24}})  # 查找dim_cm数组索引为1的元素大于24的记录
   
   # 继续嵌套...以后遇到在研究，大致类似
   ```

5. 改

   ```shell
   # updateOne语法
   db.col.updateOne(
   	<filter>,
   	<update>,
   	{
   		upsert: <boolean>,  # 如果没有匹配项，是否插入  默认False，不插入
       writeConcern: <document>,
       collation: <document>,
       arrayFilters: [ <filterdocument1>, ... ],
       hint:  <document|string>
   	}
   )
   # updateMany语法
   db.col.updateMany(
   	<filter>,
   	<update>,
   	{
   		upsert: <boolean>,
       writeConcern: <document>,
       collation: <document>,
       arrayFilters: [ <filterdocument1>, ... ],
       hint:  <document|string>
   	}
   )
   # replace
   db.col.replace(
   	<filter>,
   	<update>,
   	{
   		upsert: <boolean>,
       writeConcern: <document>,
       collation: <document>,
       hint:  <document|string>
   	}
   )
   ```

