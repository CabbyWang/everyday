## 登录
```shell
psql -ucabbyw -ppsd -P
```

## 数据库语法
```sql
-- 创建数据库
create database db_test;
create database db_test1 with owner=postgres encoding='utf-8';

-- 修改数据库
alter database db_test rename to db_test2;

alter database db_test connection limit 20;  -- 修改数据表属性

-- 删除数据库
drop database test1;

```

## 数据表语法
```sql
-- 创建数据表
create table student(
	id int;
	name varchar(30),
	birthday date,
	score numeric(5,2)
);

-- 修改数据表
alter table student rename to student1;  -- 修改数据表名

alter table student rename id to bh;  -- 修改表中列名

alter table student alter column name type varchar(40);  -- 修改列数据类型

alter table student drop column birthday;  -- 删除列

alter table student add column address varchar(200);  -- 添加列

-- 删除数据表
drop table student1;
drop table if exists student1;  -- 数据表存在时才会删除，不会报错
```

## 数据类型

### 1. 数值类型
  
  > 整数

  ```
  SMALLINT          // 小范围整数，取值范围：-32768 ~ 32767
  INT(INTEGER)      // 普通大小整数 -214783648 ~ 2147483647
  ```

  > 任意精度浮点数类型

  ```
  REAL              // 6位十进制数字精度
  NUMERIC(m, n)     // 任意精度类型
  ```

### 2. 日期与时间类型

	类型名称|含义|存储需求|举例
	:--: | :--: | :--: | :--:
	TIME | 只用于一日内时间 | 8字节 | 10:05:05
	DATE | 只用于日期 | 4字节 | 1987-04-04
	TIMESTAMP | 日期和时间 | 8字节 | 1987-04-04 10:05:05
	
### 3. 字符串类型

	类型名称 | 说明|
	:--: | :--: 
	CHAR(n)/CHARACTER(n) | 固定长度字符串，不足补空白
	VARCHAR(n)/CHARACTER VARYING(n) | 变长字符串，有长度限制
	TEXT | 变长字符串，无长度限制


## 运算符

### 1. 比较运算符
  
  + =                等于
  + <>(!=)           不等于
  + <=
  + (>=)
  + (>)
  + <
  + LEAST            在有两个或多个参数时，返回最小值
  + GREATEST         在有两个或多个参数时，返回最大值
  + BETWEEN AND      两个值之间(包含两边的值)
  + IN               判断一个值是否是列表中的任意一个值
  + LIKE             通配符匹配    % 匹配任意字符   _匹配单个字符
  
### 2. 逻辑运算符
  
  + NOT(逻辑非)
  + AND(逻辑与)
  + OR(逻辑或)


## 常用函数

### 1. 常用数值函数
   
   函数名 | 函数作用
   :--: | :--:
   AVG() | 返回某列的平均值
   COUNT() | 返回某列的行数
   MAX() | 返回某列的最大值
   MIN() | 返回某列的最小值
   SUM() | 返回某列的值之和

### 2. 常用字符串函数
   
   函数名 | 函数作用
   :--: | :--:
   LENGTH(s) | 计算字符串长度
   CONCAT(s1,s2,s3,···) | 字符串合并函数
   RTRIM(s)/LTRIM(s)/TRIM(s) | 删除字符串空格函数
   REPLACE(s, s1, s2) | 字符串替换
   SUBSTRING(s, n, len) | 获取子串

### 3. 常用日期时间函数
   
   函数名 | 函数作用
   :--: | :--:
   EXTRACT(type FROM d) | 获取日期指定值函数
   CURRENT_DATE | 获取当前日期
   CURRENT_TIME | 获取当前时间
   NOW() | 获取当前日期时间

   ```sql
   --  
   select hireDate, extract(year from hireDate), extract(month from hireDate), extract(day from hireDate) from employee;
   ```


## 索引

### 1. 索引的分类

   索引名称 | 使用场景
   :--: | :--:
   B-tree 索引 | 适合处理那些能够按顺序存储数据
   Hash 索引 | 只能处理简单的等于比较
   GiST 索引 | 一种索引架构
   GIN 索引 | 反转索引，处理包含多个值的键

### 2. 创建索引

```sql
create index emp_name_index on employee(e_name);
-- emp_name_index为索引名称， employee为表名， e_name为列名
```

### 3. 删除索引

```sql
drop index emp_name_index;
```

### 4. 优缺点

+ 优点：
  - 提高数据的查询速度
  - 加速表与表之间的连接
+ 缺点：
  - 创建和维护索引需要耗费时间
  - 需要占用磁盘空间


## 视图

> 将复杂的sql操作封装为视图，使查询简单化

- 简单化
- 安全性
- 逻辑数据独立性

### 1. 创建视图

```sql
create view v_emp_dev as select e_no, e_name, e_salary, e_hireDate from employee where dept_no=10 order by e_salary desc;
```

### 2. 使用视图

```sql
select * from v_emp_dev;
```

### 3. 删除视图

```sql
drop view v_emp_dev;
```



## 数据库操作
### 1. 简单数据插入

- 插入单行

```shell
insert into ${table} (column1, column2)
values
	(value1, value2)
```

- 插入多行

```shell
insert into ${table} (column1, column2)
values
	(value1, value2),
	(value1, value2),
	(value1, value2);
```

- 从其他表结果中插入

```shell
insert into ${table} (column1, column2)
select column1, column2
from ${another_table}
where	${condition};
```

### 2. 数据更新

```sql
update student set name = '李四' where id = 2;
```

### 3. 数据删除

```sql
delete from student where id = 1;  -- 删除id为1的数据

truncate table student;  -- 清空表数据
```

  '| DELETE | TRUNCATE
   :--: | :--: | :--:
   执行速度 | 慢 | 快
   可指定条件 | 可以 | 不可以
   语句分类 | DML | DDL
   可以回滚事务 | 可以 | 不可以
   删除操作记录日志 | 记录 | 不记录


## 主键约束

```sql
create table emp(
	id int primary key,    -- 直接指定主键
	name varchar(30),
	salary numeric(9,2)
);

create table emp1(
	id int;
	name varchar(30),
	salary numeric(9,2),
	constraint pk_emp1 primary key(id)
)
```


## 非空约束、唯一约束、默认值约束
- 维护数据的完整性
- 在业务层面保证数据正确性

```sql
create table emp2(
	id int primary key,
	name varchar(30) not null,       -- 非空约束
	phone varchar(30) unique,        -- 唯一约束
	salary numeric(9,2) default 0.00  -- 默认值约束
);
```


## 数据查询操作

### 1. 简单数据查询

```sql
select * from employee;

select e_no, e_name, e_hireDate from employee;

select employee.e_no, employee.e_name, employee.e_hireDate from employee;  -- 表名.字段

select e.e_no, e.e_name, e.e_hireDate from employee as e;

select e.e_no, e.e_name, e.e_hireDate from employee e;  -- as可以省略

select e.e_no as a, e.e_name as b, e.e_hireDate as c from employee e;  -- 修改字段别名

select e.e_no a, e.e_name b, e.e_hireDate c from employee e;  -- as可以省略
```

### 2. 单表指定条件查询操作

```sql
select * from employee where e_salary < 5000;

select * from employee where e_salary = 5000;

-- in 关键字
select * from employee where dept_no in (20, 30);

-- not in
select * from employee where dept_no not in (20, 30);

-- between and
select * from employee where e_hireDate between '2010-01-01' and '2010-01-04';

-- like
select * from employee where e_name like '李%';   -- % 匹配任意长度字符
select * from employee where e_name like '李_';   -- _ 匹配单个字符

```

### 3. 单表指定条件复杂查询操作

```sql
select * from employee where dept_no in (20, 30) and e_name like '李%' order by e_name desc nulls first;
-- nulls first 空值优先

-- 只查询5条数据
select * from employee limit 5;

-- 忽略前5条数据，从第6条开始，显示前5条数据
select * from employee limit 5 offset 5;
```

### 4. 多表连接查询

```sql
-- 隐式内连接查询
select e_no, e_name, dept_no, d_no, d_name, d_location from employee, dept where dept_no = d_no;

-- 显示内连接查询
select e_no, e_name, dept_no, d_no, d_name, d_location from employee inner join dept on dept_no = d_no;

-- left join 左连接: 返回左边数据表的所有内容和右表匹配内容
select e_no, e_name, dept_no, d_no, d_name, d_location from employee left join dept on dept_no = d_no;

-- left outer join 左外连接: 和左连接一样，可以在结果表的基础上加条件语句
select e_no, e_name, dept_no, d_no, d_name, d_location from employee left outer join dept on dept_no = d_no where dept_no = 10;
```

### 5. 子查询操作

```sql
-- exists: 当exists后的条件中，存在值，则返回前面的查询语句，否则不返回
select * from employee where exists (select d_no from dept where d_name = '开发部');

select * from employee where exists (select d_no from dept where d_name = '开发部' and d_no = dept_no); -- 返回开发部所有员工信息

-- not exists
select * from employee where not exists (select d_no from dept where d_name = '开发部' and d_no = dept_no); -- 返回非开发部所有员工信息

-- in
select * from employee where dept_no in (select d_no from dept where d_name = '开发部')

-- 标量子查询
select e_no, e_name, (select d_name || ' ' || d_location from dept where dept_no = d_no) as address from employee;
```


### 6. 查询结果集合并操作

- UNION ALL : 合并操作效率更高
- UNION : 可以去除重复记录

```sql
-- union all ，使用union all会直接合并两个结果集
select e_no, e_name, dept_no, e_salary from employee where dept_no in (10, 20)
union all
select e_no, e_name, dept_no, e_salary from employee where e_salary > 5000;

-- union ， 使用union会将结果集中的重复记录去除
select e_no, e_name, dept_no, e_salary from employee where dept_no in (10, 20)
union all
select e_no, e_name, dept_no, e_salary from employee where e_salary > 5000;

-- 字段数量不一致时， 可以用null来占位
select e_no, e_name, dept_no, e_salary, e_hireDate from employee where dept_no in (10, 20)
union all
select e_no, e_name, dept_no, e_salary, null from employee where e_salary > 5000;
```

' | UNION | UNION ALL
:--: | :--: | :--:
去除重复记录 | 可以 | 不可以
执行速度 | 慢 | 快
