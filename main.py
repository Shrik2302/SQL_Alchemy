from sqlalchemy import create_engine
from sqlalchemy import Table, MetaData

engine = create_engine("postgresql+psycopg2://postgres:root@localhost/basic")

try:
    connection = engine.connect()
    meta = MetaData(engine)
    employee_table = Table('employee', meta, autoload=True, autoload_with=engine)

    # #Insert statement
    # insert_statement = employee_table.insert().values(emp_id=16,
    #                                                   emp_name='sushant',
    #                                                   role='tester',
    #                                                   joining_date='2022-06-09',
    #                                                   end_time='16:00:00',
    #                                                   details={"name":"sushant","role":"tester"}
    #                                                   )
    # connection.execute(insert_statement)
    # print("insert completed")

    #select statement
    select_statement = employee_table.select()
    result_set = connection.execute(select_statement)
    for r in result_set:
        print(r)

    print()
    print("select with where clause")
    select_statement = employee_table.select().where(employee_table.c.emp_id==10)
    result_set = connection.execute(select_statement)
    for r in result_set:
        print(r)

    print()
    print("select with perticular column")
    select_statement = employee_table.select()
    result_set = connection.execute(select_statement)
    for r in result_set:
        print(r)

except (Exception) as error:
    print("ERROR")
    print(error)

finally:
    if connection:
        connection.close()
        print("connection closed")

