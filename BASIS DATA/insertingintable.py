import mysql.connector as sql

database = input("database: ")
table = input("nama table: ")
v1 = input("values1: ")
v2 = input("values2: ")
v3 = input("values3: ")
v4 = input("values4: ")

conn = sql.connect(
    host="localhost",
    username="root",
    password = "luthfiku12345",
    database = "{}".format(database)
)

db = conn.cursor()
qry = "insert into {table} values ('{v1}','{v2}','{v3}','{v4}')".format(table,v1,v2,v3,v4)
db.execute(qry)
conn.commit()
db.close()
conn.commit()