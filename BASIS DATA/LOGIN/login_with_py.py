import mysql.connector as sql
import mysql.connector.errors as e
import method_of_app as moa
global conn,db
conn =sql.connect(
    host="localhost",
    user="root",
    password="luthfiku12345",
    database="prjk"
)

db = conn.cursor()
user_data = [] #cokiee semenetara
while True:
    print("USER LOGIN NIH BOS")
    print("1.LOGIN")
    print("2.REGISTER")
    print("3.exit")
    print("------------------")
    choice = int(input("select your choice: "))

    if choice == 1:
        username = input("Input your username: ")
        password = input("Input your password: ")
        moa.login(user_data,username,password,db,conn)
    elif choice == 2:
        username = input("Input your username: ")
        password = input("Input your password: ")
        nama = input("Input your name: ")
        moa.register(username,password,nama,conn,db)
    elif choice == 3 :
        moa.Update_logout(user_data[0],db,conn)
        break
    else:
        print("please insert corectly")
db.close()
conn.close()
exit()