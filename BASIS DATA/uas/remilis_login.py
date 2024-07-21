import mysql.connector as sql

def connection_database():
    try:
        conn = sql.connect(
            host="localhost",
            username="root",
            password = "luthfiku12345",
            database = "project_db"
        )
        return conn
    except sql.Error as e:
        print(e)
def login(username,password):
    conn = connection_database()
    cursor = conn.cursor()
    cursor.execute("Select id_user,nama from user where nama = '{}' and sandi = '{}'".format(username,password))
    nama_user = cursor.fetchone()
    if nama_user is None:
        return "nama atau kata sandi salah"
    else:
        cursor.execute("update user set `status` = 1 where id_user = '{}'".format(nama_user[0]))
        cursor.execute("select status from user where id_user = '{}' ".format(nama_user[0]))
        status = cursor.fetchone()[0]
        conn.commit()
        cursor.close()
        conn.close()
        return nama_user[1],status


def register(username,email,password):
    conn = connection_database()
    cursor = conn.cursor()
    cursor.execute("select gmail from user where gmail = '{}' ".format(email))
    user_data = cursor.fetchone()
    id = generate_id()
    if user_data is None:
        cursor.execute("insert into user(id_user,nama,gmail,sandi,status)values('{}','{}','{}','{}',2)".format(id,username,email,password))
        conn.commit()
        cursor.close()
        conn.close()
        return True
    else:
        return False

def generate_id():
    conn = connection_database()
    cursor = conn.cursor()
    cursor.execute("select count(*) from user")
    id_count = cursor.fetchone()[0]
    id_count += 1
    id_len = len(str(id_count))
    txt = "A0000"
    id_gen = (txt[:5-id_len] + str(id_count))
    return id_gen
