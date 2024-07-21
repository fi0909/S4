import tkinter.messagebox
class data_base:
    def check_username(username,db):
        qry = "select username from user where username = '{x}'".format(x=username)
        try:
            db.execute(qry)
            check = db.fetchone()
            return check
        except:
            print(Exception)

    def register(username,password,nama,conn,db):
        if data_base.check_username(username=username,db=db) is None:
            qry = "insert into user(username,pass,nama,tipe_akun) values('{0}','{1}','{2}','user')".format(username,password,nama)
            try:
                db.execute(qry)
                conn.commit()
                print("register sukses")
            except:
                print(Exception)
        else:
            print("your username has been used, please change")

    def login (user_data,username,password,db,conn):
        qry = "select nama,tipe_akun,`status` from user where username = '{0}' and pass ='{1}'".format(username,password)
        try:
            db.execute(qry)
            user = db.fetchone()
            if user is not None:
                data_base.Update_login(username=username,db=db,conn=conn)
                db.execute(qry)
                user = db.fetchone()
                for x in user:
                    user_data.append(x)
                tkinter.messagebox.showinfo(None,"welcome {0} ,silahkan menggunakan aplikasi sebagai {1} dan anda sudah dinyatakan {2}".format(user_data[0],user_data[1],user_data[2]))
                print("welcome {0} ,silahkan menggunakan aplikasi sebagai {1} dan anda sudah dinyatakan {2}".format(user_data[0],user_data[1],user_data[2]))
            else:
                tkinter.messagebox.showinfo(None,"password is incorrect or you didnt have account")
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
        if data_base.check_username(username=username,db=db) is None:
            qry = "insert into user(username,pass,nama,tipe_akun) values('{0}','{1}','{2}','admin')".format(username,password,nama)
            try:
                db.execute(qry)
                conn.commit()
                print("register sukses")
            except:
                print(Exception)
        else:
            print("your username has been claim, please change")


class GUI:
    def exit_on_close(window):
        ans = tkinter.messagebox.askyesno(title="EXIT", message='ingin keluar?')
        if ans:
            window.destroy()