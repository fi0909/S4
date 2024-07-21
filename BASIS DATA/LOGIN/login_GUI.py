import mysql.connector as sql
import tkinter as tk
from tkinter import messagebox
import threading
from method_of_app import data_base as data,GUI as GUI
#call the gui
def exit_on():
    if messagebox.askokcancel(title="Exit",message="do you want to quit? "):
        #data.Update_logout(username=user_data[0],db=db,conn=con)
        window.destroy()

#window 
window = tk.Tk()
window.title("login")
window.resizable(width=True,height=True)
window.geometry("800x600")
window.rowconfigure([1,2,3],minsize=5,weight=1)
window.columnconfigure([1,2,3],minsize=0,weight=1)

# user data
username = tk.StringVar()
password = tk.StringVar()
user_data = []
con = sql.connect(
    host="localhost",
    user="root",
    password="luthfiku12345",
    database="prjk"
)

db = con.cursor()
#frame1
label_log = tk.Label(master=window,text="Username :",font= "arial")
label_log.grid(row=1,column=1,sticky='e')
ent_log=tk.Entry(master=window,textvariable=username)
ent_log.grid(row=1,column=2,sticky='ew')
lbl_pass = tk.Label(master=window,text="password :",font="arial")
ent_pass=tk.Entry(master=window,textvariable=password)
btn_log_in = tk.Button(master=window,text="LOG IN",font=("arial",18), command=lambda: threading.Thread(target=data.login(username=username.get(),password=password.get(),user_data=user_data,db=db,conn=con)).start())
lbl_pass.grid(row=2,column=1,sticky='e')
ent_pass.grid(row=2,column=2,sticky='ew')
btn_log_in.grid(row=3,column=2,sticky='ew')



window.protocol("WM_DELETE_WINDOW", exit_on)
window.mainloop()
db.close()