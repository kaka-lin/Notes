---
title: "Sqlite Basics"
date: 2020-06-10
tags: [Database, SQLite]
categories: [Database]
---

# SQLite - Basics

- [SQL - Tutorial](https://www.w3schools.com/sql/default.asp)
- [SQL As Understood By SQLite(官網)](https://www.sqlite.org/lang.html)
- [SQLite - Tutorial](https://www.tutorialspoint.com/sqlite/index.htm)

## Load ipython-sql

`ipython-sql`:

    - 是jupyter notebook的extension，用來擴充jupyter對SQL的支援
    - 其底層是使用SQLAlchemy


```python
%load_ext sql
```

## Create Database

The concept of creating or dropping a database is not meant for an embedded database engine like SQLite.

If you want to create DB in SQLite, just from the command line: `sqlite3 databasefilename`.

For example: `sqlite3 test.db`

### Create DB in Jupyter

Because `ipython-sql` is based on `SQLAlchemy`, we can create and connect DB as follow:


```python
%sql sqlite:///test.db
```


```python
!ls -al
```

    total 32
    drwxr-xr-x 3 kaka kaka  4096  5月 14 10:16 .
    drwxr-xr-x 7 kaka kaka  4096  5月 14 09:49 ..
    drwxr-xr-x 2 kaka kaka  4096  5月 14 09:52 .ipynb_checkpoints
    -rw-r--r-- 1 kaka kaka   422  5月 14 09:25 README.md
    -rw-r--r-- 1 kaka kaka 15267  5月 14 10:16 sqlite-basics.ipynb
    -rw-r--r-- 1 kaka kaka     0  5月 14 10:16 test.db


## SQLite Version


```python
%sql SELECT sqlite_version() AS 'SQLite Version';
```

     * sqlite:///test.db
    Done.





<table>
    <tr>
        <th>SQLite Version</th>
    </tr>
    <tr>
        <td>3.31.1</td>
    </tr>
</table>



## Create Table

- [SQLite - Data Type](https://www.sqlite.org/lang.html)
- [SQLite - AUTOINCREMENT](https://www.tutorialspoint.com/sqlite/sqlite_using_autoincrement.htm)


```python
%%sql

CREATE TABLE persons(
    person_id INTEGER PRIMARY KEY AUTOINCREMENT,
    firstname VARCHAR(255),
    lastname  VARCHAR(255),
    age       INTEGER,
    height    REAL,
    weight    REAL,
    city      VARCHAR(255)
);
```

     * sqlite:///test.db
    Done.





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

     * sqlite:///test.db
    1 rows affected.
    1 rows affected.





    []



### Read Data: SQL SELECT


```python
%%sql

SELECT * FROM persons; 
```

     * sqlite:///test.db
    Done.





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
-- or WHERE person_id = 1;
```

     * sqlite:///test.db
    1 rows affected.
    0 rows affected.





    []




```python
%%sql

SELECT * FROM persons;
```

     * sqlite:///test.db
    Done.





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

     * sqlite:///test.db
    1 rows affected.





    []




```python
%%sql

SELECT * FROM persons;
```

     * sqlite:///test.db
    Done.





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
WHERE person_id = 3;
```

     * sqlite:///test.db
    1 rows affected.





    []




```python
%%sql

SELECT * FROM persons;
```

     * sqlite:///test.db
    Done.





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

     * sqlite:///test.db
    7 rows affected.





    []




```python
%%sql

SELECT * FROM persons
```

     * sqlite:///test.db
    Done.





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

     * sqlite:///test.db
    Done.





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

     * sqlite:///test.db
    Done.





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

     * sqlite:///test.db
    Done.





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

     * sqlite:///test.db
    Done.





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
WHERE age IN (26, 28);
```

     * sqlite:///test.db
    Done.





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



### NOT


```python
%%sql

SELECT *
FROM   persons
/* WHERE NOT age = 28; */
WHERE age != 28;
```

     * sqlite:///test.db
    Done.





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

     * sqlite:///test.db
    Done.





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
WHERE city LIKE '%pei%';
```

     * sqlite:///test.db
    Done.





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



## SQLite -  Functions

- [SQLite Core Function](https://www.w3resource.com/sqlite/core-functions-round.php)

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
SET height_meters = round(height / 100, 2);

SELECT * FROM persons;
```

     * sqlite:///test.db
    Done.
    9 rows affected.
    Done.





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

     * sqlite:///test.db
    Done.





    []



## Drop Database

If we want to drop DB in SQLite, just delete the file.


```python
!rm -rf test.db
!ls -al
```

    total 32
    drwxr-xr-x 3 kaka kaka  4096  5月 14 10:16 .
    drwxr-xr-x 7 kaka kaka  4096  5月 14 09:49 ..
    drwxr-xr-x 2 kaka kaka  4096  5月 14 09:52 .ipynb_checkpoints
    -rw-r--r-- 1 kaka kaka   422  5月 14 09:25 README.md
    -rw-r--r-- 1 kaka kaka 15267  5月 14 10:16 sqlite-basics.ipynb

