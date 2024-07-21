import mysql.connector as sql
user_data = []
#user variabel to use in app:
conn = sql.connect(
    host="localhost",
    username="root",
    password="luthfiku12345",
    database="prjk"
)
db = conn.cursor()

def check_username(username,db):
    qry = "select username from user where username = '{x}'".format(x=username)
    try:
        db.execute(qry)
        check = db.fetchone()
        return check
    except:
        print(Exception)

def register(username,password,nama,conn,db):
    if check_username(username=username,db=db) is None:
        qry = "insert into user(username,pass,nama,tipe_akun) values('{0}','{1}','{2}','user')".format(username,password,nama)
        try:
            db.execute(qry)
            conn.commit()
            print("register sukses")
        except:
            print(Exception)
    else:
        print("your username has been used, please change")

def login (username,password,db,conn):
    qry = "select nama,tipe_akun,`status` from user where username = '{0}' and pass ='{1}'".format(username,password)
    try:
        db.execute(qry)
        user = db.fetchone()
        if user is not None:
            Update_login(username=username,db=db,conn=conn)
            db.execute(qry)
            user = db.fetchone()
            for x in user:
                user_data.append(x)
            print("welcome {0} ,silahkan menggunakan aplikasi sebagai {1} dan anda sudah dinyatakan {2}".format(user_data[0],user_data[1],user_data[2]))
        else:
            print("password is incorrect or you didnt have account")
    except:
        print(Exception)

def Update_login(username,db,conn):
    qry = "update user set `status` = 'aktif' where username = '{0}'".format(username)
    try:
        db.execute(qry)
        conn.commit()
    except:
        print(Exception)

def Update_logout(username,db,conn):
    qry = "update user set `status` = NULL where username = '{0}'".format(username)
    try:
        db.execute(qry)
        conn.commit()
    except:
        print(Exception)
def admin_account(username,password,nama,db,conn):
    if check_username(username=username,db=db) is None:
        qry = "insert into user(username,pass,nama,tipe_akun) values('{0}','{1}','{2}','admin')".format(username,password,nama)
        try:
            db.execute(qry)
            conn.commit()
            print("register sukses")
        except:
            print(Exception)
    else:
        print("your username has been claim, please change")
while True:
    menu_var = "1.login\n2.register\n3.exit\n------------------"
    print(menu_var)
    choice = int(input("select your choice: "))
    if choice == 1:
        print("login menu")
        username = input("input username: ")
        password = input("input password: ")
        login(username,password,db,conn)
    elif choice == 2:
        print("register menu")
        username = input("input username: ")
        password = input("input password: ")
        nama = input("input nama: ")
        register(username,password,nama,conn,db)
    elif choice == 3:
        print("THANKS FOR USING")
        Update_logout(user_data[0],db,conn)
        break
    elif choice == 12345:
        print("admin created account")
        username = input("input username: ")
        password = input("input password: ")
        nama = input("input nama: ")
        admin_account(username,password,nama,db,conn)
    else:
        print("try again")
        input()

conn.close()
exit()
