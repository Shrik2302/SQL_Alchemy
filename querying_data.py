from sqlalchemy.sql import select

from create_table import cookies
from insert import connection

""""
# select method1
s = select([cookies])
rp = connection.execute(s)
result = rp.fetchall()
print(result)
"""

"""
# select method 2
s = cookies.select()
rp = connection.execute(s)
result = rp.fetchall()
print(result)
print("complete")
"""

"""
#select method 3
s = cookies.select()
rp = connection.execute(s)
result = rp.fetchall()

first_row = result[0]
print("first_row",first_row)
name = first_row.cookie_name
print("name : ", name)
print("cookie name : ", first_row[cookies.c.cookie_name])
"""

"""
#select method 4

s = cookies.select()
rp = connection.execute(s)
print("cookie list")
for i in rp:
    print(i.cookie_name)
connection.close()
"""


""" # *Controlling the Columns in the Query* 
s = select([cookies.c.cookie_name, cookies.c.quantity])
rp = connection.execute(s)
print(rp.fetchall())
print(rp.keys())
result = rp.first()
print(result)
"""

"""
# Ordering ACS
s = select([cookies.c.cookie_name, cookies.c.quantity]).order_by(cookies.c.quantity)
rp = connection.execute(s)
for cookie in rp:
    print("{}:{}".format(cookie.quantity, cookie.cookie_name))

print()

# Order by quantity descending
from sqlalchemy import desc
s = select([cookies.c.cookie_name, cookies.c.quantity]).order_by(desc(cookies.c.quantity))
rp = connection.execute(s)
print("Ordering DESC")
for cookie in rp:
    print("{}:{}".format(cookie.quantity, cookie.cookie_name))
"""

""""
# Limiting
s = select([cookies.c.cookie_name, cookies.c.quantity]).order_by(cookies.c.quantity).limit(2)
rp = connection.execute(s)
print("Limit")
for cookie in rp:
    print("{}:{}".format(cookie.quantity, cookie.cookie_name))
"""

"""
# Built-In SQL Functions and Labels
from sqlalchemy.sql import func
s = select([func.sum(cookies.c.quantity)])
rp = connection.execute(s)
print(rp)
print(rp.scalar())
"""

"""
# counting inventory records
# select count(cookie_name) from cookies; --SQL
from sqlalchemy.sql import func
s = select([func.count(cookies.c.cookie_name)])
rp = connection.execute(s)
record = rp.first()
print("inventory count",rp)
print("inventory count(first)",record)
print(record.keys())
print(record.count_1)
"""

"""
# count record as inventory_record
# SELECT COUNT(cookie_name) AS inventory_count FROM cookies;
from sqlalchemy.sql import func
s = select([func.count(cookies.c.cookie_name).label('inventory_count')])
rp = connection.execute(s)
# print(rp)
record = rp.first()
print(record.keys())
print(record.inventory_count)
"""

"""
#Filtering
# SELECT * FROM cookies WHERE cookie_name = 'cholate_chip';
s = select([cookies]).where(cookies.c.cookie_name == 'chocolate chip')
rp = connection.execute(s)
record = rp.first()
print(record)
print(record.items())
"""
"""
# SELECT * FROM cookies WHERE cookie_name LIKE '%chocolate%';
s = select([cookies]).where(cookies.c.cookie_name.like('%chocolate%'))
rp= connection.execute(s)
records = rp.fetchall()
for record in records:
    print(record.cookie_name)
"""


#### ClauseElements ######

""""
## BETWEEN
# SELECT * FROM cookies WHERE quantity BETWEEN 1 AND 30 ;
s = select(cookies).where(cookies.c.quantity.between(1,30))
rp = connection.execute(s)
results = rp.fetchall()
for record in records:
    print(record.cookie_name)
"""

""""
## CONCAT
# SELECT cookie_name, concat(cookie_name, '  -> ', cookie_recipe_url) AS url FROM cookies;
from sqlalchemy.sql import func
s = select([cookies.c.cookie_name, func.concat(cookies.c.cookie_name, " --> ", cookies.c.cookie_recipe_url).label('url')])
rp = connection.execute(s)
results = rp.fetchall()
for result in results:
    print(result.url)
    print(type(result.url))
"""

"""
## DISTINCT
# SELECT DISTINCT cookie_id AS id FROM cookies ORDER BY id;
from sqlalchemy.sql import func
s = select(func.distinct(cookies.c.cookie_id).label('id')).order_by('id')
rp = connection.execute(s)
results = rp.fetchall()
for result in results:
    print(result.id)
print(result)
"""


"""
### Conjunctions ###
# SELECT cookie_name FROM cookies WHERE quantity >10 AND unit_cost <4;
from sqlalchemy import and_,or_,not_
print("AND operation")
s = select(cookies.c.cookie_name).where(and_(cookies.c.quantity > 10,cookies.c.unit_cost < 4))
for row in connection.execute(s):
    print(row.cookie_name)


# SELECT cookie_name FROM cookies WHERE quantity >10 OR unit_cost <4;
print()
print("OR operation")
s = select(cookies.c.cookie_name).where(or_(cookies.c.quantity > 10,cookies.c.unit_cost < 4))
for row in connection.execute(s):
    print(row.cookie_name)

# SELECT cookie_name FROM cookies WHERE NOT quantity < 10 AND NOT unit_cost >1;
print()
print("NOT operation")
s = select(cookies.c.cookie_name).where(not_(cookies.c.quantity < 10),and_(not_(cookies.c.unit_cost > 1)))
for row in connection.execute(s):
    print(row.cookie_name)
"""

"""
### Updating Data ###

# UPDATE cookies SET quantity = quantity - 100 WHERE cookie_name = 'dark chocolate chip';
from sqlalchemy import update

u = update(cookies).where(cookies.c.cookie_name == 'dark chocolate chip').values(quantity=(cookies.c.quantity -10))
result = connection.execute(u)
print(result.rowcount)

s = select([cookies]).where(cookies.c.cookie_name == 'dark chocolate chip')
result = connection.execute(s).first()
for key in result.keys():
    print('{:>20}: {}'.format(key, result[key]))
"""

"""
### Deleting Data ###
from sqlalchemy import delete
d = delete(cookies).where(cookies.c.cookie_name == 'dark chocolate chip')
result = connection.execute(d)
print(result.rowcount)

s = select([cookies]).where(cookies.c.cookie_name == 'dark chocolate chip')
result = connection.execute(s).fetchall()
print(len(result))
"""