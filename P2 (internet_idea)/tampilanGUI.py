import mysql.connector
import getpass
import tkinter as tk
from tkinter import messagebox

# Fungsi untuk menyimpan data ke database
def simpan_ke_database():
    uid = int(id_entry.get())
    nama_user = nama_user_entry.get()
    nama_lengkap = nama_lengkap_entry.get()
    password = password_entry.get()
    
    try:
        cn = mysql.connector.connect(host="localhost", user="root", password="")
        myCurr = cn.cursor()
        myCurr.execute("USE MyUPJ")
        
        qry = 'INSERT INTO userTable (userId, userName, Password, NamaLengkap) VALUES (%s, %s, %s, %s)'
        val = (uid, nama_user, password, nama_lengkap)
        myCurr.execute(qry, val)
        
        cn.commit()
        
        # Update data di Listbox
        tampilan_listbox(myCurr)
        
        cn.close()
        
        messagebox.showinfo("Info", "Data berhasil disimpan ke database!")
        
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error: {err}")

# Fungsi untuk memperbarui data di Listbox
def tampilan_listbox(cursor):
    data_listbox.delete(0, tk.END)
    cursor.execute("SELECT * FROM userTable")
    for row in cursor:
        data_listbox.insert(tk.END, row)

# Membuat GUI
root = tk.Tk()
root.title("Form Simpan Data Pengguna")
root.geometry('600x250')  

# Frame untuk masukan data
input_frame = tk.Frame(root)
input_frame.grid(row=0, column=0, padx=10, pady=5, sticky="nsew")

# Label dan Entry untuk input data
id_label = tk.Label(input_frame, text="ID:")
id_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
id_entry = tk.Entry(input_frame)
id_entry.grid(row=0, column=1, padx=10, pady=5)

nama_user_label = tk.Label(input_frame, text="Nama User:")
nama_user_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
nama_user_entry = tk.Entry(input_frame)
nama_user_entry.grid(row=1, column=1, padx=10, pady=5)

nama_lengkap_label = tk.Label(input_frame, text="Nama Lengkap:")
nama_lengkap_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")
nama_lengkap_entry = tk.Entry(input_frame)
nama_lengkap_entry.grid(row=2, column=1, padx=10, pady=5)

password_label = tk.Label(input_frame, text="Password:")
password_label.grid(row=3, column=0, padx=10, pady=5, sticky="w")
password_entry = tk.Entry(input_frame, show="*")
password_entry.grid(row=3, column=1, padx=10, pady=5)

simpan_button = tk.Button(input_frame, text="Tambah", command=simpan_ke_database)
simpan_button.grid(row=4, column=0, columnspan=2, pady=10)

# Frame untuk menampilkan data
data_frame = tk.Frame(root)
data_frame.grid(row=0, column=1, padx=10, pady=5, sticky="nsew")

data_label = tk.Label(data_frame, text="Data di userTable:")
data_label.pack()

# Listbox untuk menampilkan data
data_listbox = tk.Listbox(data_frame, width=40)
data_listbox.pack()

# Membuat koneksi dan menampilkan data awal di Listbox
cn = mysql.connector.connect(host="localhost", user="root", password="")
myCurr = cn.cursor()
myCurr.execute("USE MyUPJ")
tampilan_listbox(myCurr)
cn.close()

root.mainloop()