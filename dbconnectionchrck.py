import pymysql

print("Trying to connect with pymysql...")

try:
    conn = pymysql.connect(
        host='127.0.0.1',
        user='root',
        password='',
        database='invoice_db',
        port=3306,
        connect_timeout=5
    )
    print("CONNECTED with pymysql!")
    conn.close()
except Exception as e:
    print("ERROR:", e)
