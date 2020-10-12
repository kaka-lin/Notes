---
title: "[DB] Sqlalchemy Basics"
date: 2020-06-10
tags: [SQLAlchemy]
categories: [Database]
---

# SQLAlchemy - basics

[SQLAlchemy - Tutorial](https://www.tutorialspoint.com/sqlalchemy/index.htm)

```python
import sqlalchemy
from sqlalchemy import create_engine, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, ForeignKey, Integer, String, Numeric
from sqlalchemy.orm import sessionmaker

sqlalchemy.__version__
```

## Connect Database

```python
# SQLite
#connect_db = 'sqlite:///test.db'
# MySQL
connect_db = 'mysql+mysqldb://root:<passwd>@35.201.196.222/kaka_test'

''' create_engine

此時只有建立SQLAlchemy Engine instance(實例)
此時還沒真正真正連到資料庫
只有第一個SQL指令被下達時，才會真正連到資料庫
'''
engine = create_engine(connect_db, echo=True, encoding="utf8")
```

```python
!ls -al
```

    total 80
    drwxr-xr-x   5 kakalin  staff    160 May  8 17:19 [1m[36m.[m[m
    drwxr-xr-x  11 kakalin  staff    352 May  6 15:51 [1m[36m..[m[m
    drwxr-xr-x   3 kakalin  staff     96 May  8 13:56 [1m[36m.ipynb_checkpoints[m[m
    -rw-r--r--   1 kakalin  staff    264 May  8 14:10 README.md
    -rw-r--r--   1 kakalin  staff  33194 May  8 17:19 sqlalchemy-basics.ipynb

## Create Table: Declare Mapping

[SQLAlchemy ORM - Declaring Mapping](https://www.tutorialspoint.com/sqlalchemy/sqlalchemy_orm_declaring_mapping.htm)

在使用ORM時，我們要先描述資料庫表格，然後定義我們要映射(mapping)到這些表格的類別(classes)

### Create base class

- 我們使用[declarative_base()](https://docs.sqlalchemy.org/en/13/orm/extensions/declarative/api.html)來建立一個基礎類別

```python
Base = declarative_base()
```

### Defines a class (table)

[Column and Data Types](https://docs.sqlalchemy.org/en/13/core/type_basics.html)

```python
class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    firstname = Column(String(255))
    lastname = Column(String(255))
    age = Column(Integer)
    height = Column(Numeric)
    weight = Column(Numeric)
    city = Column(String(255))

    def __init__(self, id, firstname, lastname, age, height, weight, city):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.height = height
        self.weight = weight
        self.city = city

    def __repr__(self):
        return "<User({}, name: {} {}, age: {}, H: {}, W: {}, city: {})>".format(
            self.id, self.firstname, self.lastname,
            self.age, int(self.height), int(self.weight),
            self.city)
```

### Create Table

```
Each Table object is a member of a larger collection known as MetaData
and this object is available using the .metadata attribute of a declarative base class.
```

The `MetaData.create_all()` method is, passing in our Engine as a source of database connectivity.

For all tables that haven’t been created yet, it issues `CREATE TABLE` statements to the database.

```python
Base.metadata.create_all(engine)
```

    2020-05-08 17:20:20,005 INFO sqlalchemy.engine.base.Engine SHOW VARIABLES LIKE 'sql_mode'
    2020-05-08 17:20:20,011 INFO sqlalchemy.engine.base.Engine ()
    2020-05-08 17:20:20,051 INFO sqlalchemy.engine.base.Engine SHOW VARIABLES LIKE 'lower_case_table_names'
    2020-05-08 17:20:20,052 INFO sqlalchemy.engine.base.Engine ()
    2020-05-08 17:20:20,189 INFO sqlalchemy.engine.base.Engine SELECT DATABASE()
    2020-05-08 17:20:20,190 INFO sqlalchemy.engine.base.Engine ()
    2020-05-08 17:20:20,281 INFO sqlalchemy.engine.base.Engine show collation where `Charset` = 'utf8mb4' and `Collation` = 'utf8mb4_bin'
    2020-05-08 17:20:20,288 INFO sqlalchemy.engine.base.Engine ()
    2020-05-08 17:20:20,354 INFO sqlalchemy.engine.base.Engine SELECT CAST('test plain returns' AS CHAR(60)) AS anon_1
    2020-05-08 17:20:20,357 INFO sqlalchemy.engine.base.Engine ()
    2020-05-08 17:20:20,397 INFO sqlalchemy.engine.base.Engine SELECT CAST('test unicode returns' AS CHAR(60)) AS anon_1
    2020-05-08 17:20:20,398 INFO sqlalchemy.engine.base.Engine ()
    2020-05-08 17:20:20,437 INFO sqlalchemy.engine.base.Engine SELECT CAST('test collated returns' AS CHAR CHARACTER SET utf8mb4) COLLATE utf8mb4_bin AS anon_1
    2020-05-08 17:20:20,438 INFO sqlalchemy.engine.base.Engine ()
    2020-05-08 17:20:20,578 INFO sqlalchemy.engine.base.Engine DESCRIBE `user`
    2020-05-08 17:20:20,578 INFO sqlalchemy.engine.base.Engine ()
    2020-05-08 17:20:20,616 INFO sqlalchemy.engine.base.Engine ROLLBACK
    2020-05-08 17:20:20,661 INFO sqlalchemy.engine.base.Engine
    CREATE TABLE user (
    	id INTEGER NOT NULL AUTO_INCREMENT,
    	firstname VARCHAR(255),
    	lastname VARCHAR(255),
    	age INTEGER,
    	height NUMERIC,
    	weight NUMERIC,
    	city VARCHAR(255),
    	PRIMARY KEY (id)
    )


    2020-05-08 17:20:20,662 INFO sqlalchemy.engine.base.Engine ()
    2020-05-08 17:20:20,724 INFO sqlalchemy.engine.base.Engine COMMIT

```python
!ls -al
```

    total 80
    drwxr-xr-x   5 kakalin  staff    160 May  8 17:19 [1m[36m.[m[m
    drwxr-xr-x  11 kakalin  staff    352 May  6 15:51 [1m[36m..[m[m
    drwxr-xr-x   3 kakalin  staff     96 May  8 13:56 [1m[36m.ipynb_checkpoints[m[m
    -rw-r--r--   1 kakalin  staff    264 May  8 14:10 README.md
    -rw-r--r--   1 kakalin  staff  33194 May  8 17:19 sqlalchemy-basics.ipynb

## SQLAlchemy ORM - Creating Session

```
In order to interact with the database, we need to obtain its handle.
A session object is a handle to the database.
```

- Session class is defined using `sessionmaker()`:

    a configurable session factory method which is bound to the engine object created earlier.

```python
Session = sessionmaker(bind=engine)
session = Session()
```

## CRUD for Data

### SQLAlchemy ORM - Adding Objects: SQL INSERT INTO

We have declared a Customer class that has been mapped to the customer's table.

We have to declare an object of this class and persistently add it to the table by `add()` method of the session object.

```python
user_1 = User(1, 'kaka', 'Lin', 28, 175, 70, 'Taipei')
user_2 = User(2, 'kiwi', 'Li', 30, 173, 70, 'Taipei')

session.add_all([
    user_1,
    user_2
])
```

Note that this `transaction` is pending until the same is flushed using `commit()` method.

```python
session.commit()
```

    2020-05-08 17:20:20,988 INFO sqlalchemy.engine.base.Engine BEGIN (implicit)
    2020-05-08 17:20:20,995 INFO sqlalchemy.engine.base.Engine INSERT INTO user (id, firstname, lastname, age, height, weight, city) VALUES (%s, %s, %s, %s, %s, %s, %s)
    2020-05-08 17:20:21,005 INFO sqlalchemy.engine.base.Engine ((1, 'kaka', 'Lin', 28, 175, 70, 'Taipei'), (2, 'kiwi', 'Li', 30, 173, 70, 'Taipei'))
    2020-05-08 17:20:21,098 INFO sqlalchemy.engine.base.Engine COMMIT

### SQLAlchemy ORM - Using Query: SQL SELECT

All `SELECT statements` generated by SQLAlchemy ORM are constructed by `Query object`.

```python
"""Equivalent

SELECT * FROM user
"""
resutl = session.query(User).all()
resutl
```

    2020-05-08 17:20:21,217 INFO sqlalchemy.engine.base.Engine BEGIN (implicit)
    2020-05-08 17:20:21,220 INFO sqlalchemy.engine.base.Engine SELECT user.id AS user_id, user.firstname AS user_firstname, user.lastname AS user_lastname, user.age AS user_age, user.height AS user_height, user.weight AS user_weight, user.city AS user_city
    FROM user
    2020-05-08 17:20:21,223 INFO sqlalchemy.engine.base.Engine ()

    [<User(1, name: kaka Lin, age: 28, H: 175, W: 70, city: Taipei)>,
     <User(2, name: kiwi Li, age: 30, H: 173, W: 70, city: Taipei)>]

### SQLAlchemy ORM - Updating Objects: SQL UPDATE

```python
x = session.query(User).get(1)
x
```

    <User(1, name: kaka Lin, age: 28, H: 175, W: 70, city: Taipei)>

```python
x.weight = 68
session.commit()
```

    2020-05-08 17:20:21,319 INFO sqlalchemy.engine.base.Engine UPDATE user SET weight=%s WHERE user.id = %s
    2020-05-08 17:20:21,323 INFO sqlalchemy.engine.base.Engine (68, 1)
    2020-05-08 17:20:21,386 INFO sqlalchemy.engine.base.Engine COMMIT

```python
session.query(User).all()
```

    2020-05-08 17:20:21,487 INFO sqlalchemy.engine.base.Engine BEGIN (implicit)
    2020-05-08 17:20:21,495 INFO sqlalchemy.engine.base.Engine SELECT user.id AS user_id, user.firstname AS user_firstname, user.lastname AS user_lastname, user.age AS user_age, user.height AS user_height, user.weight AS user_weight, user.city AS user_city
    FROM user
    2020-05-08 17:20:21,497 INFO sqlalchemy.engine.base.Engine ()

    [<User(1, name: kaka Lin, age: 28, H: 175, W: 68, city: Taipei)>,
     <User(2, name: kiwi Li, age: 30, H: 173, W: 70, city: Taipei)>]

### SQLAlchemy ORM - Deleting Related Objects: SQL DELETE

```python
user_3 = User(3, 'albert', 'Lin', 28, 180, 70, 'Taipei')
session.add(user_3)
session.commit()
```

    2020-05-08 17:20:21,561 INFO sqlalchemy.engine.base.Engine INSERT INTO user (id, firstname, lastname, age, height, weight, city) VALUES (%s, %s, %s, %s, %s, %s, %s)
    2020-05-08 17:20:21,568 INFO sqlalchemy.engine.base.Engine (3, 'albert', 'Lin', 28, 180, 70, 'Taipei')
    2020-05-08 17:20:21,624 INFO sqlalchemy.engine.base.Engine COMMIT

```python
session.query(User).all()
```

    2020-05-08 17:20:21,740 INFO sqlalchemy.engine.base.Engine BEGIN (implicit)
    2020-05-08 17:20:21,743 INFO sqlalchemy.engine.base.Engine SELECT user.id AS user_id, user.firstname AS user_firstname, user.lastname AS user_lastname, user.age AS user_age, user.height AS user_height, user.weight AS user_weight, user.city AS user_city
    FROM user
    2020-05-08 17:20:21,748 INFO sqlalchemy.engine.base.Engine ()

    [<User(1, name: kaka Lin, age: 28, H: 175, W: 68, city: Taipei)>,
     <User(2, name: kiwi Li, age: 30, H: 173, W: 70, city: Taipei)>,
     <User(3, name: albert Lin, age: 28, H: 180, W: 70, city: Taipei)>]

```python
x = session.query(User).get(3)
session.delete(x)
session.commit()
```

    2020-05-08 17:20:21,819 INFO sqlalchemy.engine.base.Engine DELETE FROM user WHERE user.id = %s
    2020-05-08 17:20:21,822 INFO sqlalchemy.engine.base.Engine (3,)
    2020-05-08 17:20:21,866 INFO sqlalchemy.engine.base.Engine COMMIT

```python
session.query(User).all()
```

    2020-05-08 17:20:21,962 INFO sqlalchemy.engine.base.Engine BEGIN (implicit)
    2020-05-08 17:20:21,966 INFO sqlalchemy.engine.base.Engine SELECT user.id AS user_id, user.firstname AS user_firstname, user.lastname AS user_lastname, user.age AS user_age, user.height AS user_height, user.weight AS user_weight, user.city AS user_city
    FROM user
    2020-05-08 17:20:21,970 INFO sqlalchemy.engine.base.Engine ()

    [<User(1, name: kaka Lin, age: 28, H: 175, W: 68, city: Taipei)>,
     <User(2, name: kiwi Li, age: 30, H: 173, W: 70, city: Taipei)>]

## SQLAlchemy ORM - Applying Filter: SQL WHERE

```python
user_4 = User(4, 'Albert', 'Lin', 28, 160, 70, 'Taipei')
user_5 = User(5, 'Andy', 'Wei', 24, 175, 72, 'Teipei')
user_6 = User(6, 'kevin','Wang', 30, 174, 63, 'San Francisco')
user_7 = User(7, 'kevin', 'Wei', 27, 178, 65, 'Taipei')
user_8 = User(8, 'David','Kang', 26, 175, 65, 'Washington')
user_9 = User(9, 'Matt','Wang', 26, 172, 72, 'Taipei')
user_10 = User(10, 'kaka-ideal', 'Lin', 28, 178, 70, 'Janpan')

session.add_all([
    user_4,
    user_5,
    user_6,
    user_7,
    user_8,
    user_9,
    user_10,
])
session.commit()
```

    2020-05-08 17:20:22,049 INFO sqlalchemy.engine.base.Engine INSERT INTO user (id, firstname, lastname, age, height, weight, city) VALUES (%s, %s, %s, %s, %s, %s, %s)
    2020-05-08 17:20:22,050 INFO sqlalchemy.engine.base.Engine ((4, 'Albert', 'Lin', 28, 160, 70, 'Taipei'), (5, 'Andy', 'Wei', 24, 175, 72, 'Teipei'), (6, 'kevin', 'Wang', 30, 174, 63, 'San Francisco'), (7, 'kevin', 'Wei', 27, 178, 65, 'Taipei'), (8, 'David', 'Kang', 26, 175, 65, 'Washington'), (9, 'Matt', 'Wang', 26, 172, 72, 'Taipei'), (10, 'kaka-ideal', 'Lin', 28, 178, 70, 'Janpan'))
    2020-05-08 17:20:22,095 INFO sqlalchemy.engine.base.Engine COMMIT

```python
session.query(User).all()
```

    2020-05-08 17:20:22,182 INFO sqlalchemy.engine.base.Engine BEGIN (implicit)
    2020-05-08 17:20:22,187 INFO sqlalchemy.engine.base.Engine SELECT user.id AS user_id, user.firstname AS user_firstname, user.lastname AS user_lastname, user.age AS user_age, user.height AS user_height, user.weight AS user_weight, user.city AS user_city
    FROM user
    2020-05-08 17:20:22,188 INFO sqlalchemy.engine.base.Engine ()

    [<User(1, name: kaka Lin, age: 28, H: 175, W: 68, city: Taipei)>,
     <User(2, name: kiwi Li, age: 30, H: 173, W: 70, city: Taipei)>,
     <User(4, name: Albert Lin, age: 28, H: 160, W: 70, city: Taipei)>,
     <User(5, name: Andy Wei, age: 24, H: 175, W: 72, city: Teipei)>,
     <User(6, name: kevin Wang, age: 30, H: 174, W: 63, city: San Francisco)>,
     <User(7, name: kevin Wei, age: 27, H: 178, W: 65, city: Taipei)>,
     <User(8, name: David Kang, age: 26, H: 175, W: 65, city: Washington)>,
     <User(9, name: Matt Wang, age: 26, H: 172, W: 72, city: Taipei)>,
     <User(10, name: kaka-ideal Lin, age: 28, H: 178, W: 70, city: Janpan)>]


```python
results = session.query(User).filter(User.age == 28)

for row in results:
    print(row)
```

    2020-05-08 17:20:22,299 INFO sqlalchemy.engine.base.Engine SELECT user.id AS user_id, user.firstname AS user_firstname, user.lastname AS user_lastname, user.age AS user_age, user.height AS user_height, user.weight AS user_weight, user.city AS user_city
    FROM user
    WHERE user.age = %s
    2020-05-08 17:20:22,316 INFO sqlalchemy.engine.base.Engine (28,)
    <User(1, name: kaka Lin, age: 28, H: 175, W: 68, city: Taipei)>
    <User(4, name: Albert Lin, age: 28, H: 160, W: 70, city: Taipei)>
    <User(10, name: kaka-ideal Lin, age: 28, H: 178, W: 70, city: Janpan)>

## SQLAlchemy ORM - Filter Operators

[SQLAlchemy ORM - Filter Operators](https://www.tutorialspoint.com/sqlalchemy/sqlalchemy_orm_filter_operators.htm)

### AND

```python
results = session.query(User).filter(User.age == 28, User.height > 170)

for row in results:
    print(row)
```

    2020-05-08 17:20:22,411 INFO sqlalchemy.engine.base.Engine SELECT user.id AS user_id, user.firstname AS user_firstname, user.lastname AS user_lastname, user.age AS user_age, user.height AS user_height, user.weight AS user_weight, user.city AS user_city
    FROM user
    WHERE user.age = %s AND user.height > %s
    2020-05-08 17:20:22,414 INFO sqlalchemy.engine.base.Engine (28, 170)
    <User(1, name: kaka Lin, age: 28, H: 175, W: 68, city: Taipei)>
    <User(10, name: kaka-ideal Lin, age: 28, H: 178, W: 70, city: Janpan)>

### OR

```python
from sqlalchemy import or_

results = session.query(User).filter(or_(User.age == 28, User.height > 170))

for row in results:
    print(row)
```

    2020-05-08 17:20:22,485 INFO sqlalchemy.engine.base.Engine SELECT user.id AS user_id, user.firstname AS user_firstname, user.lastname AS user_lastname, user.age AS user_age, user.height AS user_height, user.weight AS user_weight, user.city AS user_city
    FROM user
    WHERE user.age = %s OR user.height > %s
    2020-05-08 17:20:22,497 INFO sqlalchemy.engine.base.Engine (28, 170)
    <User(1, name: kaka Lin, age: 28, H: 175, W: 68, city: Taipei)>
    <User(2, name: kiwi Li, age: 30, H: 173, W: 70, city: Taipei)>
    <User(4, name: Albert Lin, age: 28, H: 160, W: 70, city: Taipei)>
    <User(5, name: Andy Wei, age: 24, H: 175, W: 72, city: Teipei)>
    <User(6, name: kevin Wang, age: 30, H: 174, W: 63, city: San Francisco)>
    <User(7, name: kevin Wei, age: 27, H: 178, W: 65, city: Taipei)>
    <User(8, name: David Kang, age: 26, H: 175, W: 65, city: Washington)>
    <User(9, name: Matt Wang, age: 26, H: 172, W: 72, city: Taipei)>
    <User(10, name: kaka-ideal Lin, age: 28, H: 178, W: 70, city: Janpan)>

### IN

```python
results = session.query(User).filter(User.age.in_([28, 26]))

for row in results:
    print(row)
```

    2020-05-08 17:20:22,578 INFO sqlalchemy.engine.base.Engine SELECT user.id AS user_id, user.firstname AS user_firstname, user.lastname AS user_lastname, user.age AS user_age, user.height AS user_height, user.weight AS user_weight, user.city AS user_city
    FROM user
    WHERE user.age IN (%s, %s)
    2020-05-08 17:20:22,579 INFO sqlalchemy.engine.base.Engine (28, 26)
    <User(1, name: kaka Lin, age: 28, H: 175, W: 68, city: Taipei)>
    <User(4, name: Albert Lin, age: 28, H: 160, W: 70, city: Taipei)>
    <User(8, name: David Kang, age: 26, H: 175, W: 65, city: Washington)>
    <User(9, name: Matt Wang, age: 26, H: 172, W: 72, city: Taipei)>
    <User(10, name: kaka-ideal Lin, age: 28, H: 178, W: 70, city: Janpan)>

### LIKE

```python
results = session.query(User).filter(User.city.like('%pei'))

for row in results:
    print(row)
```

    2020-05-08 17:20:22,641 INFO sqlalchemy.engine.base.Engine SELECT user.id AS user_id, user.firstname AS user_firstname, user.lastname AS user_lastname, user.age AS user_age, user.height AS user_height, user.weight AS user_weight, user.city AS user_city
    FROM user
    WHERE user.city LIKE %s
    2020-05-08 17:20:22,644 INFO sqlalchemy.engine.base.Engine ('%pei',)
    <User(1, name: kaka Lin, age: 28, H: 175, W: 68, city: Taipei)>
    <User(2, name: kiwi Li, age: 30, H: 173, W: 70, city: Taipei)>
    <User(4, name: Albert Lin, age: 28, H: 160, W: 70, city: Taipei)>
    <User(5, name: Andy Wei, age: 24, H: 175, W: 72, city: Teipei)>
    <User(7, name: kevin Wei, age: 27, H: 178, W: 65, city: Taipei)>
    <User(9, name: Matt Wang, age: 26, H: 172, W: 72, city: Taipei)>

## SQLAlchemy ORM - Clossing Session

Closes current session by clearing all items and ending any transaction in progress

```python
session.close()
```

    2020-05-08 17:20:22,729 INFO sqlalchemy.engine.base.Engine ROLLBACK

## Drop Table

```python
User.__table__.drop(engine)
```

    2020-05-08 17:20:22,794 INFO sqlalchemy.engine.base.Engine
    DROP TABLE user
    2020-05-08 17:20:22,795 INFO sqlalchemy.engine.base.Engine ()
    2020-05-08 17:20:22,853 INFO sqlalchemy.engine.base.Engine COMMIT

## Drop Database

If we want to drop DB in SQLite, just delete the file.

```python
!rm -rf test.db
!ls -al
```

    total 80
    drwxr-xr-x   5 kakalin  staff    160 May  8 17:19 [1m[36m.[m[m
    drwxr-xr-x  11 kakalin  staff    352 May  6 15:51 [1m[36m..[m[m
    drwxr-xr-x   3 kakalin  staff     96 May  8 13:56 [1m[36m.ipynb_checkpoints[m[m
    -rw-r--r--   1 kakalin  staff    264 May  8 14:10 README.md
    -rw-r--r--   1 kakalin  staff  33194 May  8 17:19 sqlalchemy-basics.ipynb
