from sqlalchemy import create_engine
# To connect database
DB_URL = 'postgresql+psycopg2://postgres:root@localhost/basic'
engine = create_engine(DB_URL)

try:
    conn = engine.connect()
    print("connected")
    print(conn)
except(Exception) as error:
    print("Not connected")
finally:
    if conn:
        conn.close()
        print("connection closed")
