from create_table import cookies, users, line_items, orders
from insert import connection
from sqlalchemy import select, join

columns = [orders.c.order_id, users.c.username, users.c.phone,
           cookies.c.cookie_name, line_items.c.quantity,
           line_items.c.extended_cost]
cookiemon_orders = select(columns)
cookiemon_orders = cookiemon_orders.select_from(orders.join(users).join(line_items).join(cookies)).where(users.c.username =='cookiemon')
print(str(cookiemon_orders))

result = connection.execute(cookiemon_orders).fetchall()
for row in result:
    print(row)