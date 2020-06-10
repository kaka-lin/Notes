---
title: "Mysql Basics"
date: 2020-06-10
tags: [Database, MySQL]
categories: [Database]
---

# MySQL - Basics

- [SQL Tutorial](https://www.w3schools.com/sql/default.asp)
- [MySQL Documentation](https://dev.mysql.com/doc/refman/5.7/en/create-table.html)
- [MySQL - Tutorial](https://www.tutorialspoint.com/mysql/index.htm)
- [Quickstart for Cloud SQL for MySQL](https://cloud.google.com/sql/docs/mysql/quickstart)

## Load ipython-sql

`ipython-sql`:

    - 是jupyter notebook的extension，用來擴充jupyter對SQL的支援
    - 其底層是使用SQLAlchemy


```python
%load_ext sql
# for engines that do not support autocomit
%config SqlMagic.autocommit=False
```

## Connect Database

Because `ipython-sql` is based on `SQLAlchemy`, 
we use the SQLAlchemy's DBAPI to connect the MySQL database via the mysqlclient 
(maintained fork of MySQL-Python) driver.

[SQLAlchemy - MySQL DBAPI](https://docs.sqlalchemy.org/en/13/dialects/mysql.html#module-sqlalchemy.dialects.mysql.pymysql)


```bash
mysql+mysqldb://<user>:<password>@<host>[:<port>]/<dbname>
```


```python
%sql mysql+mysqldb://root:abc123456@35.201.196.222/kaka_test
```


```python
%%sql

SELECT * FROM entries;
```

     * mysql+mysqldb://root:***@35.201.196.222/kaka_test
    2 rows affected.





<table>
    <tr>
        <th>guestName</th>
        <th>content</th>
        <th>entryID</th>
    </tr>
    <tr>
        <td>first guest</td>
        <td>I got here!</td>
        <td>1</td>
    </tr>
    <tr>
        <td>second guest</td>
        <td>Me too!</td>
        <td>2</td>
    </tr>
</table>



## MySQL Version


```python
%sql SHOW VARIABLES LIKE '%version%';
```

     * mysql+mysqldb://root:***@35.201.196.222/kaka_test
    8 rows affected.





<table>
    <tr>
        <th>Variable_name</th>
        <th>Value</th>
    </tr>
    <tr>
        <td>innodb_version</td>
        <td>5.7.25</td>
    </tr>
    <tr>
        <td>protocol_version</td>
        <td>10</td>
    </tr>
    <tr>
        <td>slave_type_conversions</td>
        <td></td>
    </tr>
    <tr>
        <td>tls_version</td>
        <td>TLSv1,TLSv1.1,TLSv1.2</td>
    </tr>
    <tr>
        <td>version</td>
        <td>5.7.25-google-log</td>
    </tr>
    <tr>
        <td>version_comment</td>
        <td>(Google)</td>
    </tr>
    <tr>
        <td>version_compile_machine</td>
        <td>x86_64</td>
    </tr>
    <tr>
        <td>version_compile_os</td>
        <td>Linux</td>
    </tr>
</table>



## Create Table

- [MySQL - Data Type](https://www.tutorialspoint.com/mysql/mysql-data-types.htm)


```python
%%sql
CREATE TABLE persons(
    PRIMARY KEY (person_id),
    person_id INT          NOT NULL AUTO_INCREMENT,
    firstname VARCHAR(255) NOT NULL,
    lastname  VARCHAR(255),
    age       INT,
    height    FLOAT,
    weight    FLOAT,
    city      VARCHAR(255)
);
```

     * mysql+mysqldb://root:***@35.201.196.222/kaka_test
    0 rows affected.





    []



## CRUD for Data

- C: Create
- R: Read
- U: Update
- D: Delete

![](https://raw.githubusercontent.com/kaka-lin/Notes/master/DB/images/crud.png)

### Create Data: SQL INSERT INTO


```python
%%sql
INSERT INTO persons
VALUES (10, 'kaka','Lin', 28, 175, 70, 'Taipei');

INSERT INTO persons (firstname, lastname, age, height, weight, city) 
VALUES ('kiwi','Li', 30, 173, 70, 'Taipei');
```

     * mysql+mysqldb://root:***@35.201.196.222/kaka_test
    1 rows affected.
    1 rows affected.





    []



### Read Data: SQL SELECT


```python
%%sql

SELECT * FROM persons; 
```

     * mysql+mysqldb://root:***@35.201.196.222/kaka_test
    2 rows affected.





<table>
    <tr>
        <th>person_id</th>
        <th>firstname</th>
        <th>lastname</th>
        <th>age</th>
        <th>height</th>
        <th>weight</th>
        <th>city</th>
    </tr>
    <tr>
        <td>10</td>
        <td>kaka</td>
        <td>Lin</td>
        <td>28</td>
        <td>175.0</td>
        <td>70.0</td>
        <td>Taipei</td>
    </tr>
    <tr>
        <td>11</td>
        <td>kiwi</td>
        <td>Li</td>
        <td>30</td>
        <td>173.0</td>
        <td>70.0</td>
        <td>Taipei</td>
    </tr>
</table>



### Update Data: SQL UPDATE


```python
%%sql

UPDATE persons
SET    weight = 68
WHERE  firstname = 'kaka';
```

     * mysql+mysqldb://root:***@35.201.196.222/kaka_test
    1 rows affected.





    []




```python
%%sql

SELECT * FROM persons;
```

     * mysql+mysqldb://root:***@35.201.196.222/kaka_test
    2 rows affected.





<table>
    <tr>
        <th>person_id</th>
        <th>firstname</th>
        <th>lastname</th>
        <th>age</th>
        <th>height</th>
        <th>weight</th>
        <th>city</th>
    </tr>
    <tr>
        <td>10</td>
        <td>kaka</td>
        <td>Lin</td>
        <td>28</td>
        <td>175.0</td>
        <td>68.0</td>
        <td>Taipei</td>
    </tr>
    <tr>
        <td>11</td>
        <td>kiwi</td>
        <td>Li</td>
        <td>30</td>
        <td>173.0</td>
        <td>70.0</td>
        <td>Taipei</td>
    </tr>
</table>



### Delete Data: SQL DELETE

Before we delete data,
we first add the data that we want to delete.


```python
%%sql

INSERT INTO persons
VALUES (3, 'albert','Lin', 28, 180, 70, 'Taipei');
```

     * mysql+mysqldb://root:***@35.201.196.222/kaka_test
    1 rows affected.





    []




```python
%%sql

SELECT * FROM persons;
```

     * mysql+mysqldb://root:***@35.201.196.222/kaka_test
    3 rows affected.





<table>
    <tr>
        <th>person_id</th>
        <th>firstname</th>
        <th>lastname</th>
        <th>age</th>
        <th>height</th>
        <th>weight</th>
        <th>city</th>
    </tr>
    <tr>
        <td>3</td>
        <td>albert</td>
        <td>Lin</td>
        <td>28</td>
        <td>180.0</td>
        <td>70.0</td>
        <td>Taipei</td>
    </tr>
    <tr>
        <td>10</td>
        <td>kaka</td>
        <td>Lin</td>
        <td>28</td>
        <td>175.0</td>
        <td>68.0</td>
        <td>Taipei</td>
    </tr>
    <tr>
        <td>11</td>
        <td>kiwi</td>
        <td>Li</td>
        <td>30</td>
        <td>173.0</td>
        <td>70.0</td>
        <td>Taipei</td>
    </tr>
</table>




```python
%%sql

DELETE FROM persons
WHERE persion_id = 3;
```

     * mysql+mysqldb://root:***@35.201.196.222/kaka_test
    (MySQLdb._exceptions.OperationalError) (1054, "Unknown column 'persion_id' in 'where clause'")
    [SQL: DELETE FROM persons WHERE persion_id = 3;]
    (Background on this error at: http://sqlalche.me/e/e3q8)



```python
%%sql

SELECT * FROM persons;
```

     * mysql+mysqldb://root:***@35.201.196.222/kaka_test
    3 rows affected.





<table>
    <tr>
        <th>person_id</th>
        <th>firstname</th>
        <th>lastname</th>
        <th>age</th>
        <th>height</th>
        <th>weight</th>
        <th>city</th>
    </tr>
    <tr>
        <td>3</td>
        <td>albert</td>
        <td>Lin</td>
        <td>28</td>
        <td>180.0</td>
        <td>70.0</td>
        <td>Taipei</td>
    </tr>
    <tr>
        <td>10</td>
        <td>kaka</td>
        <td>Lin</td>
        <td>28</td>
        <td>175.0</td>
        <td>68.0</td>
        <td>Taipei</td>
    </tr>
    <tr>
        <td>11</td>
        <td>kiwi</td>
        <td>Li</td>
        <td>30</td>
        <td>173.0</td>
        <td>70.0</td>
        <td>Taipei</td>
    </tr>
</table>



## SQL WHERE


```python
%%sql
    
INSERT INTO persons (firstname, lastname, age, height, weight, city) 
VALUES ('Albert', 'Lin', 28, 160, 70, 'Taipei'),
       ('Andy', 'Wei', 24, 175, 72, 'Teipei'),
       ('kevin', 'Wang', 30, 174, 63, 'San Francisco'),
       ('kevin', 'Wei', 27, 178, 65, 'Taipei'),
       ('David', 'Kang', 26, 175, 65, 'Washington'),
       ('Matt', 'Wang', 26, 172, 72, 'Taipei'),
       ('kaka-ideal', 'Lin', 28, 178, 70, 'Janpan');
```

     * mysql+mysqldb://root:***@35.201.196.222/kaka_test
    7 rows affected.





    []




```python
%%sql

SELECT * FROM persons
```

     * mysql+mysqldb://root:***@35.201.196.222/kaka_test
    10 rows affected.





<table>
    <tr>
        <th>person_id</th>
        <th>firstname</th>
        <th>lastname</th>
        <th>age</th>
        <th>height</th>
        <th>weight</th>
        <th>city</th>
    </tr>
    <tr>
        <td>3</td>
        <td>albert</td>
        <td>Lin</td>
        <td>28</td>
        <td>180.0</td>
        <td>70.0</td>
        <td>Taipei</td>
    </tr>
    <tr>
        <td>10</td>
        <td>kaka</td>
        <td>Lin</td>
        <td>28</td>
        <td>175.0</td>
        <td>68.0</td>
        <td>Taipei</td>
    </tr>
    <tr>
        <td>11</td>
        <td>kiwi</td>
        <td>Li</td>
        <td>30</td>
        <td>173.0</td>
        <td>70.0</td>
        <td>Taipei</td>
    </tr>
    <tr>
        <td>12</td>
        <td>Albert</td>
        <td>Lin</td>
        <td>28</td>
        <td>160.0</td>
        <td>70.0</td>
        <td>Taipei</td>
    </tr>
    <tr>
        <td>13</td>
        <td>Andy</td>
        <td>Wei</td>
        <td>24</td>
        <td>175.0</td>
        <td>72.0</td>
        <td>Teipei</td>
    </tr>
    <tr>
        <td>14</td>
        <td>kevin</td>
        <td>Wang</td>
        <td>30</td>
        <td>174.0</td>
        <td>63.0</td>
        <td>San Francisco</td>
    </tr>
    <tr>
        <td>15</td>
        <td>kevin</td>
        <td>Wei</td>
        <td>27</td>
        <td>178.0</td>
        <td>65.0</td>
        <td>Taipei</td>
    </tr>
    <tr>
        <td>16</td>
        <td>David</td>
        <td>Kang</td>
        <td>26</td>
        <td>175.0</td>
        <td>65.0</td>
        <td>Washington</td>
    </tr>
    <tr>
        <td>17</td>
        <td>Matt</td>
        <td>Wang</td>
        <td>26</td>
        <td>172.0</td>
        <td>72.0</td>
        <td>Taipei</td>
    </tr>
    <tr>
        <td>18</td>
        <td>kaka-ideal</td>
        <td>Lin</td>
        <td>28</td>
        <td>178.0</td>
        <td>70.0</td>
        <td>Janpan</td>
    </tr>
</table>




```python
%%sql

SELECT *
FROM   persons
WHERE  age = 28;
```

     * mysql+mysqldb://root:***@35.201.196.222/kaka_test
    4 rows affected.





<table>
    <tr>
        <th>person_id</th>
        <th>firstname</th>
        <th>lastname</th>
        <th>age</th>
        <th>height</th>
        <th>weight</th>
        <th>city</th>
    </tr>
    <tr>
        <td>3</td>
        <td>albert</td>
        <td>Lin</td>
        <td>28</td>
        <td>180.0</td>
        <td>70.0</td>
        <td>Taipei</td>
    </tr>
    <tr>
        <td>10</td>
        <td>kaka</td>
        <td>Lin</td>
        <td>28</td>
        <td>175.0</td>
        <td>68.0</td>
        <td>Taipei</td>
    </tr>
    <tr>
        <td>12</td>
        <td>Albert</td>
        <td>Lin</td>
        <td>28</td>
        <td>160.0</td>
        <td>70.0</td>
        <td>Taipei</td>
    </tr>
    <tr>
        <td>18</td>
        <td>kaka-ideal</td>
        <td>Lin</td>
        <td>28</td>
        <td>178.0</td>
        <td>70.0</td>
        <td>Janpan</td>
    </tr>
</table>



## SQL AND, OR and NOT

### AND


```python
%%sql

SELECT *
FROM   persons
WHERE  age = 28
AND    height > 170;
```

     * mysql+mysqldb://root:***@35.201.196.222/kaka_test
    3 rows affected.





<table>
    <tr>
        <th>person_id</th>
        <th>firstname</th>
        <th>lastname</th>
        <th>age</th>
        <th>height</th>
        <th>weight</th>
        <th>city</th>
    </tr>
    <tr>
        <td>3</td>
        <td>albert</td>
        <td>Lin</td>
        <td>28</td>
        <td>180.0</td>
        <td>70.0</td>
        <td>Taipei</td>
    </tr>
    <tr>
        <td>10</td>
        <td>kaka</td>
        <td>Lin</td>
        <td>28</td>
        <td>175.0</td>
        <td>68.0</td>
        <td>Taipei</td>
    </tr>
    <tr>
        <td>18</td>
        <td>kaka-ideal</td>
        <td>Lin</td>
        <td>28</td>
        <td>178.0</td>
        <td>70.0</td>
        <td>Janpan</td>
    </tr>
</table>



### OR


```python
%%sql

SELECT *
FROM   persons
WHERE  age = 28
OR     height > 170;
```

     * mysql+mysqldb://root:***@35.201.196.222/kaka_test
    10 rows affected.





<table>
    <tr>
        <th>person_id</th>
        <th>firstname</th>
        <th>lastname</th>
        <th>age</th>
        <th>height</th>
        <th>weight</th>
        <th>city</th>
    </tr>
    <tr>
        <td>3</td>
        <td>albert</td>
        <td>Lin</td>
        <td>28</td>
        <td>180.0</td>
        <td>70.0</td>
        <td>Taipei</td>
    </tr>
    <tr>
        <td>10</td>
        <td>kaka</td>
        <td>Lin</td>
        <td>28</td>
        <td>175.0</td>
        <td>68.0</td>
        <td>Taipei</td>
    </tr>
    <tr>
        <td>11</td>
        <td>kiwi</td>
        <td>Li</td>
        <td>30</td>
        <td>173.0</td>
        <td>70.0</td>
        <td>Taipei</td>
    </tr>
    <tr>
        <td>12</td>
        <td>Albert</td>
        <td>Lin</td>
        <td>28</td>
        <td>160.0</td>
        <td>70.0</td>
        <td>Taipei</td>
    </tr>
    <tr>
        <td>13</td>
        <td>Andy</td>
        <td>Wei</td>
        <td>24</td>
        <td>175.0</td>
        <td>72.0</td>
        <td>Teipei</td>
    </tr>
    <tr>
        <td>14</td>
        <td>kevin</td>
        <td>Wang</td>
        <td>30</td>
        <td>174.0</td>
        <td>63.0</td>
        <td>San Francisco</td>
    </tr>
    <tr>
        <td>15</td>
        <td>kevin</td>
        <td>Wei</td>
        <td>27</td>
        <td>178.0</td>
        <td>65.0</td>
        <td>Taipei</td>
    </tr>
    <tr>
        <td>16</td>
        <td>David</td>
        <td>Kang</td>
        <td>26</td>
        <td>175.0</td>
        <td>65.0</td>
        <td>Washington</td>
    </tr>
    <tr>
        <td>17</td>
        <td>Matt</td>
        <td>Wang</td>
        <td>26</td>
        <td>172.0</td>
        <td>72.0</td>
        <td>Taipei</td>
    </tr>
    <tr>
        <td>18</td>
        <td>kaka-ideal</td>
        <td>Lin</td>
        <td>28</td>
        <td>178.0</td>
        <td>70.0</td>
        <td>Janpan</td>
    </tr>
</table>



#### SQL IN Operator

The IN operator allows you to specify multiple values in a WHERE clause.


```python
%%sql

SELECT *
FROM   persons
WHERE  age = 28 OR age = 26;
```

     * mysql+mysqldb://root:***@35.201.196.222/kaka_test
    6 rows affected.





<table>
    <tr>
        <th>person_id</th>
        <th>firstname</th>
        <th>lastname</th>
        <th>age</th>
        <th>height</th>
        <th>weight</th>
        <th>city</th>
    </tr>
    <tr>
        <td>3</td>
        <td>albert</td>
        <td>Lin</td>
        <td>28</td>
        <td>180.0</td>
        <td>70.0</td>
        <td>Taipei</td>
    </tr>
    <tr>
        <td>10</td>
        <td>kaka</td>
        <td>Lin</td>
        <td>28</td>
        <td>175.0</td>
        <td>68.0</td>
        <td>Taipei</td>
    </tr>
    <tr>
        <td>12</td>
        <td>Albert</td>
        <td>Lin</td>
        <td>28</td>
        <td>160.0</td>
        <td>70.0</td>
        <td>Taipei</td>
    </tr>
    <tr>
        <td>16</td>
        <td>David</td>
        <td>Kang</td>
        <td>26</td>
        <td>175.0</td>
        <td>65.0</td>
        <td>Washington</td>
    </tr>
    <tr>
        <td>17</td>
        <td>Matt</td>
        <td>Wang</td>
        <td>26</td>
        <td>172.0</td>
        <td>72.0</td>
        <td>Taipei</td>
    </tr>
    <tr>
        <td>18</td>
        <td>kaka-ideal</td>
        <td>Lin</td>
        <td>28</td>
        <td>178.0</td>
        <td>70.0</td>
        <td>Janpan</td>
    </tr>
</table>




```python
%%sql

SELECT *
FROM   persons
WHERE  age IN (26, 28);
```

     * mysql+mysqldb://root:***@35.201.196.222/kaka_test
    6 rows affected.





<table>
    <tr>
        <th>person_id</th>
        <th>firstname</th>
        <th>lastname</th>
        <th>age</th>
        <th>height</th>
        <th>weight</th>
        <th>city</th>
    </tr>
    <tr>
        <td>3</td>
        <td>albert</td>
        <td>Lin</td>
        <td>28</td>
        <td>180.0</td>
        <td>70.0</td>
        <td>Taipei</td>
    </tr>
    <tr>
        <td>10</td>
        <td>kaka</td>
        <td>Lin</td>
        <td>28</td>
        <td>175.0</td>
        <td>68.0</td>
        <td>Taipei</td>
    </tr>
    <tr>
        <td>12</td>
        <td>Albert</td>
        <td>Lin</td>
        <td>28</td>
        <td>160.0</td>
        <td>70.0</td>
        <td>Taipei</td>
    </tr>
    <tr>
        <td>16</td>
        <td>David</td>
        <td>Kang</td>
        <td>26</td>
        <td>175.0</td>
        <td>65.0</td>
        <td>Washington</td>
    </tr>
    <tr>
        <td>17</td>
        <td>Matt</td>
        <td>Wang</td>
        <td>26</td>
        <td>172.0</td>
        <td>72.0</td>
        <td>Taipei</td>
    </tr>
    <tr>
        <td>18</td>
        <td>kaka-ideal</td>
        <td>Lin</td>
        <td>28</td>
        <td>178.0</td>
        <td>70.0</td>
        <td>Janpan</td>
    </tr>
</table>



### Not


```python
%%sql

SELECT *
FROM   persons
WHERE  age != 28;
```

     * mysql+mysqldb://root:***@35.201.196.222/kaka_test
    6 rows affected.





<table>
    <tr>
        <th>person_id</th>
        <th>firstname</th>
        <th>lastname</th>
        <th>age</th>
        <th>height</th>
        <th>weight</th>
        <th>city</th>
    </tr>
    <tr>
        <td>11</td>
        <td>kiwi</td>
        <td>Li</td>
        <td>30</td>
        <td>173.0</td>
        <td>70.0</td>
        <td>Taipei</td>
    </tr>
    <tr>
        <td>13</td>
        <td>Andy</td>
        <td>Wei</td>
        <td>24</td>
        <td>175.0</td>
        <td>72.0</td>
        <td>Teipei</td>
    </tr>
    <tr>
        <td>14</td>
        <td>kevin</td>
        <td>Wang</td>
        <td>30</td>
        <td>174.0</td>
        <td>63.0</td>
        <td>San Francisco</td>
    </tr>
    <tr>
        <td>15</td>
        <td>kevin</td>
        <td>Wei</td>
        <td>27</td>
        <td>178.0</td>
        <td>65.0</td>
        <td>Taipei</td>
    </tr>
    <tr>
        <td>16</td>
        <td>David</td>
        <td>Kang</td>
        <td>26</td>
        <td>175.0</td>
        <td>65.0</td>
        <td>Washington</td>
    </tr>
    <tr>
        <td>17</td>
        <td>Matt</td>
        <td>Wang</td>
        <td>26</td>
        <td>172.0</td>
        <td>72.0</td>
        <td>Taipei</td>
    </tr>
</table>



## SQL ORDER BY

```
SELECT column1, column2, ...
    FROM table_name
    ORDER BY column1, column2, ... ASC|DESC;
```

- Default: ASC


```python
%%sql

SELECT *
FROM   persons
ORDER BY age;
```

     * mysql+mysqldb://root:***@35.201.196.222/kaka_test
    10 rows affected.





<table>
    <tr>
        <th>person_id</th>
        <th>firstname</th>
        <th>lastname</th>
        <th>age</th>
        <th>height</th>
        <th>weight</th>
        <th>city</th>
    </tr>
    <tr>
        <td>13</td>
        <td>Andy</td>
        <td>Wei</td>
        <td>24</td>
        <td>175.0</td>
        <td>72.0</td>
        <td>Teipei</td>
    </tr>
    <tr>
        <td>16</td>
        <td>David</td>
        <td>Kang</td>
        <td>26</td>
        <td>175.0</td>
        <td>65.0</td>
        <td>Washington</td>
    </tr>
    <tr>
        <td>17</td>
        <td>Matt</td>
        <td>Wang</td>
        <td>26</td>
        <td>172.0</td>
        <td>72.0</td>
        <td>Taipei</td>
    </tr>
    <tr>
        <td>15</td>
        <td>kevin</td>
        <td>Wei</td>
        <td>27</td>
        <td>178.0</td>
        <td>65.0</td>
        <td>Taipei</td>
    </tr>
    <tr>
        <td>3</td>
        <td>albert</td>
        <td>Lin</td>
        <td>28</td>
        <td>180.0</td>
        <td>70.0</td>
        <td>Taipei</td>
    </tr>
    <tr>
        <td>10</td>
        <td>kaka</td>
        <td>Lin</td>
        <td>28</td>
        <td>175.0</td>
        <td>68.0</td>
        <td>Taipei</td>
    </tr>
    <tr>
        <td>12</td>
        <td>Albert</td>
        <td>Lin</td>
        <td>28</td>
        <td>160.0</td>
        <td>70.0</td>
        <td>Taipei</td>
    </tr>
    <tr>
        <td>18</td>
        <td>kaka-ideal</td>
        <td>Lin</td>
        <td>28</td>
        <td>178.0</td>
        <td>70.0</td>
        <td>Janpan</td>
    </tr>
    <tr>
        <td>11</td>
        <td>kiwi</td>
        <td>Li</td>
        <td>30</td>
        <td>173.0</td>
        <td>70.0</td>
        <td>Taipei</td>
    </tr>
    <tr>
        <td>14</td>
        <td>kevin</td>
        <td>Wang</td>
        <td>30</td>
        <td>174.0</td>
        <td>63.0</td>
        <td>San Francisco</td>
    </tr>
</table>



## SQL LIKE Operator

The LIKE operator is used in a WHERE clause to search for a specified pattern in a column.

There are two wildcards often used in conjunction with the LIKE operator:

- % : The percent sign represents zero, one, or multiple characters
- _ : The underscore represents a single character


```python
%%sql

SELECT *
FROM   persons
WHERE  city LIKE '%pei%';
```

     * mysql+mysqldb://root:***@35.201.196.222/kaka_test
    7 rows affected.





<table>
    <tr>
        <th>person_id</th>
        <th>firstname</th>
        <th>lastname</th>
        <th>age</th>
        <th>height</th>
        <th>weight</th>
        <th>city</th>
    </tr>
    <tr>
        <td>3</td>
        <td>albert</td>
        <td>Lin</td>
        <td>28</td>
        <td>180.0</td>
        <td>70.0</td>
        <td>Taipei</td>
    </tr>
    <tr>
        <td>10</td>
        <td>kaka</td>
        <td>Lin</td>
        <td>28</td>
        <td>175.0</td>
        <td>68.0</td>
        <td>Taipei</td>
    </tr>
    <tr>
        <td>11</td>
        <td>kiwi</td>
        <td>Li</td>
        <td>30</td>
        <td>173.0</td>
        <td>70.0</td>
        <td>Taipei</td>
    </tr>
    <tr>
        <td>12</td>
        <td>Albert</td>
        <td>Lin</td>
        <td>28</td>
        <td>160.0</td>
        <td>70.0</td>
        <td>Taipei</td>
    </tr>
    <tr>
        <td>13</td>
        <td>Andy</td>
        <td>Wei</td>
        <td>24</td>
        <td>175.0</td>
        <td>72.0</td>
        <td>Teipei</td>
    </tr>
    <tr>
        <td>15</td>
        <td>kevin</td>
        <td>Wei</td>
        <td>27</td>
        <td>178.0</td>
        <td>65.0</td>
        <td>Taipei</td>
    </tr>
    <tr>
        <td>17</td>
        <td>Matt</td>
        <td>Wang</td>
        <td>26</td>
        <td>172.0</td>
        <td>72.0</td>
        <td>Taipei</td>
    </tr>
</table>



## MySQL -  Functions

- [MySQL Function](https://www.w3schools.com/sql/sql_ref_mysql.asp)

### Modify Table: SQL ALTER TABLE

- Add a new column in an existing table
    
    ```
    ALTER TABLE table_name ADD column_name datatype; 
    ```


```python
%%sql

ALTER TABLE persons
ADD height_meters REAL;

UPDATE persons
SET    height_meters = round(height / 100, 2);

SELECT * FROM persons;
```

     * mysql+mysqldb://root:***@35.201.196.222/kaka_test
    0 rows affected.
    10 rows affected.
    10 rows affected.





<table>
    <tr>
        <th>person_id</th>
        <th>firstname</th>
        <th>lastname</th>
        <th>age</th>
        <th>height</th>
        <th>weight</th>
        <th>city</th>
        <th>height_meters</th>
    </tr>
    <tr>
        <td>3</td>
        <td>albert</td>
        <td>Lin</td>
        <td>28</td>
        <td>180.0</td>
        <td>70.0</td>
        <td>Taipei</td>
        <td>1.8</td>
    </tr>
    <tr>
        <td>10</td>
        <td>kaka</td>
        <td>Lin</td>
        <td>28</td>
        <td>175.0</td>
        <td>68.0</td>
        <td>Taipei</td>
        <td>1.75</td>
    </tr>
    <tr>
        <td>11</td>
        <td>kiwi</td>
        <td>Li</td>
        <td>30</td>
        <td>173.0</td>
        <td>70.0</td>
        <td>Taipei</td>
        <td>1.73</td>
    </tr>
    <tr>
        <td>12</td>
        <td>Albert</td>
        <td>Lin</td>
        <td>28</td>
        <td>160.0</td>
        <td>70.0</td>
        <td>Taipei</td>
        <td>1.6</td>
    </tr>
    <tr>
        <td>13</td>
        <td>Andy</td>
        <td>Wei</td>
        <td>24</td>
        <td>175.0</td>
        <td>72.0</td>
        <td>Teipei</td>
        <td>1.75</td>
    </tr>
    <tr>
        <td>14</td>
        <td>kevin</td>
        <td>Wang</td>
        <td>30</td>
        <td>174.0</td>
        <td>63.0</td>
        <td>San Francisco</td>
        <td>1.74</td>
    </tr>
    <tr>
        <td>15</td>
        <td>kevin</td>
        <td>Wei</td>
        <td>27</td>
        <td>178.0</td>
        <td>65.0</td>
        <td>Taipei</td>
        <td>1.78</td>
    </tr>
    <tr>
        <td>16</td>
        <td>David</td>
        <td>Kang</td>
        <td>26</td>
        <td>175.0</td>
        <td>65.0</td>
        <td>Washington</td>
        <td>1.75</td>
    </tr>
    <tr>
        <td>17</td>
        <td>Matt</td>
        <td>Wang</td>
        <td>26</td>
        <td>172.0</td>
        <td>72.0</td>
        <td>Taipei</td>
        <td>1.72</td>
    </tr>
    <tr>
        <td>18</td>
        <td>kaka-ideal</td>
        <td>Lin</td>
        <td>28</td>
        <td>178.0</td>
        <td>70.0</td>
        <td>Janpan</td>
        <td>1.78</td>
    </tr>
</table>



## Drop Table


```python
%%sql

DROP TABLE persons;
```

     * mysql+mysqldb://root:***@35.201.196.222/kaka_test
    0 rows affected.





    []


