#posgresql 连表查询

- JOIN连接分为**内连接**和**外连接**，而外连接又分为**左外连接**，**右外连接**，**全外连接**

###一、内连接

INNER JOIN，其中INNER可以省略。

语法：

A INNER JOIN B ON （A.a = B.b）

如果ON条件中两张表的字段名称相同，还可以简单一点

A INNER JOIN B USING（a = b）

内连接的结果如下图中红色部分

![img](https://images2015.cnblogs.com/blog/763932/201606/763932-20160626174655063-1124636759.png)

示例:查询选课情况

```
postgres=# select * from tbl_student_course join tbl_student using(stu_id) join tbl_course using(course_id);
 course_id | stu_id | stu_name | course_name 
-----------+--------+----------+-------------
         2 |      1 | 张三     | 大学英语
         4 |      1 | 张三     | 电影欣赏
         4 |      2 | 李四     | 电影欣赏
         4 |      3 | 王五     | 电影欣赏
(4 rows)
```

###二、左外连接

左外连接其实是一个内连接然后加上左表独有的数据行，结果集中右表的字段自动补充NULL。

LEFT OUTTER JOIN ，其中OUTTER可以省略。

语法：

A LEFT JOIN B ON （A.a=B.b） 

A LEFT JOIN B USING(a)

左外连接的结果如下图红色部分

![img](https://images2015.cnblogs.com/blog/763932/201606/763932-20160626175813938-65081717.png)

 

示例：查询所有学生的选课信息，包括没选课的学生

```
postgres=# select * from tbl_student left join tbl_student_course using(stu_id) left join tbl_course using(course_id);
 course_id | stu_id | stu_name | course_name 
-----------+--------+----------+-------------
         2 |      1 | 张三     | 大学英语
         4 |      1 | 张三     | 电影欣赏
         4 |      2 | 李四     | 电影欣赏
         4 |      3 | 王五     | 电影欣赏
      NULL |      4 | 麻子     | NULL
(5 rows)
```

###三、右外连接

右外连接其实是一个内连接然后加上右表独有的数据行，结果集中左表的字段自动补充NULL。

RIGHT OUTTER JOIN ，其中OUTTER可以省略。

语法：

A RIGHT JOIN B ON （A.a=B.b） 

A RIGHT JOIN B USING(a)

右外连接的结果如下图红色部分

 ![img](https://images2015.cnblogs.com/blog/763932/201606/763932-20160626180427141-436322306.png)

示例：查询所有课程被选情况

```
postgres=# select * from tbl_student right join tbl_student_course using(stu_id) right join tbl_course using(course_id);
 course_id | stu_id | stu_name | course_name 
-----------+--------+----------+-------------
         2 |      1 | 张三     | 大学英语
         4 |      1 | 张三     | 电影欣赏
         4 |      2 | 李四     | 电影欣赏
         4 |      3 | 王五     | 电影欣赏
         3 |   NULL | NULL     | 大学物理
         1 |   NULL | NULL     | 高等数学
(6 rows)
```

###四、全表连接

全外连接其实是一个内连接然后加上左表和右表独有的数据行，左表独有的数据行右表的字段补充NULL，右表独有的数据行左表字段补充NULL。

FULL OUTTER JOIN，其中OUTTER可以省略。

语法：

A FULL OUTTER JOIN B ON (A.a = B.b)

A FULL OUTTER JOIN B USING(a)

全外连接的结果如下图红色部分

![img](https://images2015.cnblogs.com/blog/763932/201606/763932-20160626181152516-1327099894.png)

 

示例：查询所有学生和课程的选课信息

```
test=# select * from tbl_student full join tbl_student_course using(stu_id) full join tbl_course using(course_id);
 course_id | stu_id | stu_name | course_name 
-----------+--------+----------+-------------
         2 |      1 | 张三     | 大学英语
         4 |      1 | 张三     | 电影欣赏
         4 |      2 | 李四     | 电影欣赏
         4 |      3 | 王五     | 电影欣赏
      NULL |      4 | 麻子     | NULL
         3 |   NULL | NULL     | 大学物理
         1 |   NULL | NULL     | 高等数学
(7 rows)
```

查询只在左表存在的数据

![img](https://images2015.cnblogs.com/blog/763932/201606/763932-20160626181929453-1220270358.png)

 

示例：查询没有选课的学生

```
test=# select * from tbl_student left join tbl_student_course using(stu_id) where tbl_student_course.stu_id is null;
 stu_id | stu_name | course_id 
--------+----------+-----------
      4 | 麻子     |      NULL
(1 row)
```

 

NOT IN存在很大的性能瓶颈，除NOT EXISTS外，也可以使用这种查询方式作为替代方案。

查询只在右表中存在的数据

![img](https://images2015.cnblogs.com/blog/763932/201606/763932-20160626182134422-2105633296.png)

 

示例：查询没有被选的课程

```
test=# select * from tbl_student_course right join tbl_course using(course_id) where tbl_student_course.course_id is null;
 course_id | stu_id | course_name 
-----------+--------+-------------
         1 |   NULL | 高等数学
         3 |   NULL | 大学物理
(2 rows)
```

 

 

查询只在左表或只在右表存在的数据

![img](https://images2015.cnblogs.com/blog/763932/201606/763932-20160626182811031-1614053124.png)

 

示例：查询没有选课的学生和没有被选的课程

```
test=# select * from tbl_student full join tbl_student_course using(stu_id) full join tbl_course using(course_id) 
where tbl_student.stu_id is null or tbl_course.course_id is null;

 course_id | stu_id | stu_name | course_name 
-----------+--------+----------+-------------
      NULL |      4 | 麻子     | NULL
         3 |   NULL | NULL     | 大学物理
         1 |   NULL | NULL     | 高等数学
(3 rows)
```

 

所有的JOIN查询，只要理解了下面的图，一切就OK了！

![img](https://images2015.cnblogs.com/blog/763932/201606/763932-20160626183020922-14133775.png)

 