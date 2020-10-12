---
title: "[DB] Sqlite Basics"
date: 2020-06-10
tags: [SQLite]
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

```
* sqlite:///test.db
Done.
```

```
| SQLite Version |
| 3.31.1 |
```

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

```
 * sqlite:///test.db
Done.
[]
```

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

```
 * sqlite:///test.db
1 rows affected.
1 rows affected.
[]
```

### Read Data: SQL SELECT

```python
%%sql

SELECT * FROM persons;
```

```
 * sqlite:///test.db
Done.
```

| person_id | firstname | lastname | age | height | weight | city |
| -- | -- | -- | -- | -- | -- | -- |
| 10 | kaka | Lin | 28 | 175.0 | 70.0 | Taipei |
| 11 | kiwi | Li | 30 | 173.0 | 70.0 | Taipei |

### Update Data: SQL UPDATE

```python
%%sql

UPDATE persons
SET    weight = 68
WHERE  firstname = 'kaka';
-- or WHERE person_id = 1;
```

```
 * sqlite:///test.db
1 rows affected.
0 rows affected.
[]
```

```python
%%sql

SELECT * FROM persons;
```

```
 * sqlite:///test.db
Done.
```

| person_id | firstname | lastname | age | height | weight | city |
| -- | -- | -- | -- | -- | -- | -- |
| 10 | kaka | Lin | 28 | 175.0 | 68.0 | Taipei |
| 11 | kiwi | Li | 30 | 173.0 | 70.0 | Taipei |


### Delete Data: SQL DELETE

Before we delete data,
we first add the data that we want to delete.

```python
%%sql

INSERT INTO persons
VALUES (3, 'albert','Lin', 28, 180, 70, 'Taipei');
```

```
 * sqlite:///test.db
1 rows affected.
[]
```

```python
%%sql

SELECT * FROM persons;
```

```
 * sqlite:///test.db
Done.
```

| person_id | firstname | lastname | age | height | weight | city |
| -- | -- | -- | -- | -- | -- | -- |
| 3 | albert | Lin | 28 | 180.0 | 70.0 | Taipei |
| 10 | kaka | Lin | 28 | 175.0 | 68.0 | Taipei |
| 11 | kiwi | Li | 30 | 173.0 | 70.0 | Taipei |

```python
%%sql

DELETE FROM persons
WHERE person_id = 3;
```

```
 * sqlite:///test.db
1 rows affected.
[]
```

```python
%%sql

SELECT * FROM persons;
```

```
 * sqlite:///test.db
Done.
```

| person_id | firstname | lastname | age | height | weight | city |
| -- | -- | -- | -- | -- | -- | -- |
| 10 | kaka | Lin | 28 | 175.0 | 68.0 | Taipei |
| 11 | kiwi | Li | 30 | 173.0 | 70.0 | Taipei |


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

```
 * sqlite:///test.db
7 rows affected.
[]
```

```python
%%sql

SELECT * FROM persons
```

```
 * sqlite:///test.db
Done.
```

| person_id | firstname | lastname | age | height | weight | city |
| -- | -- | -- | -- | -- | -- | -- |
| 10 | kaka | Lin | 28 | 175.0 | 68.0 | Taipei |
| 11 | kiwi | Li | 30 | 173.0 | 70.0 | Taipei |
| 12 | Albert | Lin | 28 | 160.0 | 70.0 | Taipei |
| 13 | Andy | Wei | 24 | 175.0 | 72.0 | Taipei |
| 14 | kevin | Wang | 30 | 174.0 | 63.0 | San Francisco |
| 15 | kevin | Wei | 27 | 178.0 | 65.0 | Taipei |
| 16 | David | Kang | 26 | 175.0 | 65.0 | Washington |
| 17 | Matt | Wang | 26 | 172.0 | 72.0 | Taipei |
| 18 | kaka-ideal | Lin | 28 | 178.0 | 70.0 | Janpan |

```python
%%sql

SELECT *
FROM   persons
WHERE  age = 28;
```

```
 * sqlite:///test.db
Done.
```

| person_id | firstname | lastname | age | height | weight | city |
| -- | -- | -- | -- | -- | -- | -- |
| 10 | kaka | Lin | 28 | 175.0 | 68.0 | Taipei |
| 12 | Albert | Lin | 28 | 160.0 | 70.0 | Taipei |
| 18 | kaka-ideal | Lin | 28 | 173.0 | 70.0 | Janpan |

## SQL AND, OR and NOT

### AND

```python
%%sql

SELECT *
FROM   persons
WHERE  age = 28
AND    height > 170;
```

```
 * sqlite:///test.db
Done.
```

| person_id | firstname | lastname | age | height | weight | city |
| -- | -- | -- | -- | -- | -- | -- |
| 10 | kaka | Lin | 28 | 175.0 | 68.0 | Taipei |
| 18 | kaka-ideal | Lin | 28 | 178.0 | 70.0 | Janpan |

### OR

```python
%%sql

SELECT *
FROM   persons
WHERE  age = 28
OR     height > 170;
```

```
 * sqlite:///test.db
Done.
```

| person_id | firstname | lastname | age | height | weight | city |
| -- | -- | -- | -- | -- | -- | -- |
| 10 | kaka | Lin | 28 | 175.0 | 68.0 | Taipei |
| 11 | kiwi | Li | 30 | 173.0 | 70.0 | Taipei |
| 12 | Albert | Lin | 28 | 160.0 | 70.0 | Taipei |
| 13 | Andy | Wei | 24 | 175.0 | 72.0 | Taipei |
| 14 | kevin | Wang | 30 | 174.0 | 63.0 | San Francisco |
| 15 | kevin | Wei | 27 | 178.0 | 65.0 | Taipei |
| 16 | David | Kang | 26 | 175.0 | 65.0 | Washington |
| 17 | Matt | Wang | 26 | 172.0 | 72.0 | Taipei |
| 18 | kaka-ideal | Lin | 28 | 178.0 | 70.0 | Janpan |

#### SQL IN Operator

The IN operator allows you to specify multiple values in a WHERE clause.

```python
%%sql

SELECT *
FROM   persons
WHERE  age = 28 OR age = 26;
```

```
 * sqlite:///test.db
Done.
```

| person_id | firstname | lastname | age | height | weight | city |
| -- | -- | -- | -- | -- | -- | -- |
| 10 | kaka | Lin | 28 | 175.0 | 68.0 | Taipei |
| 12 | Albert | Lin | 28 | 160.0 | 70.0 | Taipei |
| 16 | David | Kang | 26 | 175.0 | 65.0 | Washington |
| 17 | Matt | Wang | 26 | 172.0 | 72.0 | Taipei |
| 18 | kaka-ideal | Lin | 28 | 178.0 | 70.0 | Janpan |

```python
%%sql

SELECT *
FROM   persons
WHERE age IN (26, 28);
```

```
 * sqlite:///test.db
Done.
```

| person_id | firstname | lastname | age | height | weight | city |
| -- | -- | -- | -- | -- | -- | -- |
| 10 | kaka | Lin | 28 | 175.0 | 68.0 | Taipei |
| 12 | Albert | Lin | 28 | 160.0 | 70.0 | Taipei |
| 16 | David | Kang | 26 | 175.0 | 65.0 | Washington |
| 17 | Matt | Wang | 26 | 172.0 | 72.0 | Taipei |
| 18 | kaka-ideal | Lin | 28 | 178.0 | 70.0 | Janpan |

### NOT

```python
%%sql

SELECT *
FROM   persons
/* WHERE NOT age = 28; */
WHERE age != 28;
```

```
 * sqlite:///test.db
Done.
```

| person_id | firstname | lastname | age | height | weight | city |
| -- | -- | -- | -- | -- | -- | -- |
| 11 | kiwi | Li | 30 | 173.0 | 70.0 | Taipei |
| 13 | Andy | Wei | 24 | 175.0 | 72.0 | Taipei |
| 14 | kevin | Wang | 30 | 174.0 | 63.0 | San Francisco |
| 15 | kevin | Wei | 27 | 178.0 | 65.0 | Taipei |
| 16 | David | Kang | 26 | 175.0 | 65.0 | Washington |
| 17 | Matt | Wang | 26 | 172.0 | 72.0 | Taipei |

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

```
 * sqlite:///test.db
Done.
```

| person_id | firstname | lastname | age | height | weight | city |
| -- | -- | -- | -- | -- | -- | -- |
| 13 | Andy | Wei | 24 | 175.0 | 72.0 | Taipei |
| 16 | David | Kang | 26 | 175.0 | 65.0 | Washington |
| 17 | Matt | Wang | 26 | 172.0 | 72.0 | Taipei |
| 15 | kevin | Wei | 27 | 178.0 | 65.0 | Taipei |
| 10 | kaka | Lin | 28 | 175.0 | 68.0 | Taipei |
| 12 | Albert | Lin | 28 | 160.0 | 70.0 | Taipei |
| 18 | kaka-ideal | Lin | 28 | 178.0 | 70.0 | Janpan |
| 11 | kiwi | Li | 30 | 173.0 | 70.0 | Taipei |
| 14 | kevin | Wang | 30 | 174.0 | 63.0 | San Francisco |

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

```
 * sqlite:///test.db
Done.
```

| person_id | firstname | lastname | age | height | weight | city |
| -- | -- | -- | -- | -- | -- | -- |
| 10 | kaka | Lin | 28 | 175.0 | 68.0 | Taipei |
| 11 | kiwi | Li | 30 | 173.0 | 70.0 | Taipei |
| 12 | Albert | Lin | 28 | 160.0 | 70.0 | Taipei |
| 13 | Andy | Wei | 24 | 175.0 | 72.0 | Taipei |
| 15 | kevin | Wei | 27 | 178.0 | 65.0 | Taipei |
| 17 | Matt | Wang | 26 | 172.0 | 72.0 | Taipei |

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

```
 * sqlite:///test.db
Done.
9 rows affected.
Done.
```

| person_id | firstname | lastname | age | height | weight | city | height_meters |
| -- | -- | -- | -- | -- | -- | -- | -- |
| 10 | kaka | Lin | 28 | 175.0 | 68.0 | Taipei | 1.75 |
| 11 | kiwi | Li | 30 | 173.0 | 70.0 | Taipei | 1.73 |
| 12 | Albert | Lin | 28 | 160.0 | 70.0 | Taipei | 1.6 |
| 13 | Andy | Wei | 24 | 175.0 | 72.0 | Taipei | 1.75 |
| 14 | kevin | Wang | 30 | 174.0 | 63.0 | San Francisco | 1.74 |
| 15 | kevin | Wei | 27 | 178.0 | 65.0 | Taipei | 1.78 |
| 16 | David | Kang | 26 | 175.0 | 65.0 | Washington | 1.75 |
| 17 | Matt | Wang | 26 | 172.0 | 72.0 | Taipei | 1.72 |
| 18 | kaka-ideal | Lin | 28 | 178.0 | 70.0 | Janpan | 1.78 |

## Drop Table

```python
%%sql

DROP TABLE persons;
```

```
 * sqlite:///test.db
Done.
[]
```

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
