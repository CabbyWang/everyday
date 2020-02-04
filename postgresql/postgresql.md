```shell
psql -ucabbyw -ppsd -P
```



## insert

1. 插入单行

```shell
insert into ${table} (column1, column2)
values
	(value1, value2)
```

2. 插入多行

```shell
insert into ${table} (column1, column2)
values
	(value1, value2),
	(value1, value2),
	(value1, value2);
```

3. 从其他表结果中插入

```shell
insert into ${table} (column1, column2)
select column1, column2
from ${another_table}
where	${condition};
```

