---
title: "[DB] Mysql Basics"
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
%sql mysql+mysqldb://root:<passwd>@35.201.196.222/kaka_test
```

```python
%%sql

SELECT * FROM entries;
```

```
 * mysql+mysqldb://root:***@35.201.196.222/kaka_test
2 rows affected.
```

| guestName | content | entryID |
| -- | -- | -- |
| first guest | I got here | 1 |
| second guest | Me too! | 2 |

## MySQL Version

```python
%sql SHOW VARIABLES LIKE '%version%';
```

```
 * mysql+mysqldb://root:***@35.201.196.222/kaka_test
8 rows affected.
```

![](../images/mysql_version.png)
![](/images/db/mysql_version.png)

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

```
 * mysql+mysqldb://root:***@35.201.196.222/kaka_test
0 rows affected.
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
 * mysql+mysqldb://root:***@35.201.196.222/kaka_test
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
 * mysql+mysqldb://root:***@35.201.196.222/kaka_test
2 rows affected.
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
```

```
 * mysql+mysqldb://root:***@35.201.196.222/kaka_test
1 rows affected.
[]
```

```python
%%sql

SELECT * FROM persons;
```

```
 * mysql+mysqldb://root:***@35.201.196.222/kaka_test
2 rows affected.
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
 * mysql+mysqldb://root:***@35.201.196.222/kaka_test
1 rows affected.
[]
```

```python
%%sql

SELECT * FROM persons;
```

```
 * mysql+mysqldb://root:***@35.201.196.222/kaka_test
3 rows affected.
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
 * mysql+mysqldb://root:***@35.201.196.222/kaka_test
1 rows affected.
[]
```

```python
%%sql

SELECT * FROM persons;
```

```
 * mysql+mysqldb://root:***@35.201.196.222/kaka_test
2 rows affected.
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
 * mysql+mysqldb://root:***@35.201.196.222/kaka_test
7 rows affected.
[]
```

```python
%%sql

SELECT * FROM persons
```

```
 * mysql+mysqldb://root:***@35.201.196.222/kaka_test
9 rows affected.
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
 * mysql+mysqldb://root:***@35.201.196.222/kaka_test
3 rows affected.
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
 * mysql+mysqldb://root:***@35.201.196.222/kaka_test
2 rows affected.
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
 * mysql+mysqldb://root:***@35.201.196.222/kaka_test
9 rows affected.
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
 * mysql+mysqldb://root:***@35.201.196.222/kaka_test
5 rows affected.
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
WHERE  age IN (26, 28);
```

```
 * mysql+mysqldb://root:***@35.201.196.222/kaka_test
5 rows affected.
```

| person_id | firstname | lastname | age | height | weight | city |
| -- | -- | -- | -- | -- | -- | -- |
| 10 | kaka | Lin | 28 | 175.0 | 68.0 | Taipei |
| 12 | Albert | Lin | 28 | 160.0 | 70.0 | Taipei |
| 16 | David | Kang | 26 | 175.0 | 65.0 | Washington |
| 17 | Matt | Wang | 26 | 172.0 | 72.0 | Taipei |
| 18 | kaka-ideal | Lin | 28 | 178.0 | 70.0 | Janpan |

### Not


```python
%%sql

SELECT *
FROM   persons
WHERE  age != 28;
```

```
 * mysql+mysqldb://root:***@35.201.196.222/kaka_test
6 rows affected.
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
 * mysql+mysqldb://root:***@35.201.196.222/kaka_test
9 rows affected.
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
WHERE  city LIKE '%pei%';
```

```
 * mysql+mysqldb://root:***@35.201.196.222/kaka_test
6 rows affected.
```

| person_id | firstname | lastname | age | height | weight | city |
| -- | -- | -- | -- | -- | -- | -- |
| 10 | kaka | Lin | 28 | 175.0 | 68.0 | Taipei |
| 11 | kiwi | Li | 30 | 173.0 | 70.0 | Taipei |
| 12 | Albert | Lin | 28 | 160.0 | 70.0 | Taipei |
| 13 | Andy | Wei | 24 | 175.0 | 72.0 | Taipei |
| 15 | kevin | Wei | 27 | 178.0 | 65.0 | Taipei |
| 17 | Matt | Wang | 26 | 172.0 | 72.0 | Taipei |

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

```
     * mysql+mysqldb://root:***@35.201.196.222/kaka_test
    0 rows affected.
    9 rows affected.
    9 rows affected.
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
 * mysql+mysqldb://root:***@35.201.196.222/kaka_test
0 rows affected.
[]
```
