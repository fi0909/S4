import tkinter as tk
from tkinter import ttk, messagebox
from database import Database
import customtkinter as ctk
import time
import datetime

class Main:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplikasi")
        self.root.geometry("800x600")

        self.frame = ctk.CTkFrame(self.root, width=800, height=600, fg_color='#517F9C')
        self.frame.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)

        lblMain = ctk.CTkLabel(self.frame, text="Selamat Datang di Aplikasi Sewa Laptop", font=('Inter',30))
        lblMain.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)

        self.optionValues = ["Form Sewa Laptop", "Tabel Laptop", "Riwayat Sewa Laptop"]
        self.selected_option_value = ctk.StringVar()
        self.optionMenu = ctk.CTkOptionMenu(self.frame, values=self.optionValues, font=('Inter', 13), corner_radius=1, command=self.selected_option, variable=self.selected_option_value)
        self.optionMenu.place(x=0, y=0)
        self.optionMenu.set("Pilih menu")

    def selected_option(self, selected_value):
        if selected_value == "Form Sewa Laptop":
            self.frame.destroy()
            self.frame = ctk.CTkFrame(self.root, width=800, height=600, fg_color='#517F9C')
            self.frame.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)

            lblMain = ctk.CTkLabel(self.frame, text="Form Sewa Laptop", font=('Inter',30))
            lblMain.place(x=10, y=60)

            lblKodeLaptop = ctk.CTkLabel(self.frame, text="Kode Laptop:", font=('Inter',15))
            lblKodeLaptop.place(x=10, y=120)
            kode = Database.get_kode()
            self.kode_strings = [code[0] for code in kode]
            self.selected_kode = ctk.StringVar()
            self.comboKodeLaptop = ctk.CTkComboBox(self.frame, font=('Inter',15),values=self.kode_strings, width=150, variable=self.selected_kode, command=self.update_info)
            self.comboKodeLaptop.place(x=120, y=120)
            self.comboKodeLaptop.set("Pilih Kode Laptop")

            ongoing_rentals = Database.get_list()
            rented_codes = [rental[1] for rental in ongoing_rentals]
            for rented_code in rented_codes:
                if rented_code in self.kode_strings:
                    self.kode_strings.remove(rented_code)
            # Update nilai-nilai ComboBox
            self.comboKodeLaptop.configure(values=self.kode_strings)

            lblJenisLaptop1 = ctk.CTkLabel(self.frame, text="Jenis Laptop:", font=('Inter',15))
            lblJenisLaptop1.place(x=10, y=170)
            self.lblJenisLaptop2 = ctk.CTkLabel(self.frame, text="", font=('Inter',15))
            self.lblJenisLaptop2.place(x=120, y=170)

            lblHargaSewa1 = ctk.CTkLabel(self.frame, text="Harga Sewa:", font=('Inter',15))
            lblHargaSewa1.place(x=10, y=220)
            self.lblHargaSewa2 = ctk.CTkLabel(self.frame, text="", font=('Inter',15))
            self.lblHargaSewa2.place(x=120, y=220)

            btnTambah = ctk.CTkButton(self.frame, text="Tambah", font=('Inter',15), command=self.sewa_laptop)
            btnTambah.place(x=10, y=250)

            lblTabel = ctk.CTkLabel(self.frame, text="Tabel sewa yang berlangsung", font=('Inter',30))
            lblTabel.place(x=10, y=300)

            self.create_table_list()

            btnAkhiri = ctk.CTkButton(self.frame, text="Akhiri Sewa", font=('Inter',15), command=self.akhiri_sewa)
            btnAkhiri.place(x=625, y=550)

            btnBack = ctk.CTkButton(self.frame, text="Back", font=('Inter',20), command=self.back)
            btnBack.place(x=10, y=10)

        elif selected_value == "Tabel Laptop":
            self.frame.destroy()
            self.frame = ctk.CTkFrame(self.root, width=800, height=600, fg_color='#517F9C')
            self.frame.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)

            lblMain = ctk.CTkLabel(self.frame, text="Tabel Laptop", font=('Inter',30))
            lblMain.place(x=325, y=40)

            btnBack = ctk.CTkButton(self.frame, text="Back", font=('Inter',20), command=self.back)
            btnBack.place(x=10, y=10)

            self.create_table()

            btnTambah = ctk.CTkButton(self.frame, text="Tambah Laptop", font=('Inter',20), command=self.tambah_laptop)
            btnTambah.place(x=100, y=450)

            btnHapus = ctk.CTkButton(self.frame, text="Hapus Laptop", font=('Inter',20), command=self.hapus_laptop)
            btnHapus.place(x=550, y=450)

        elif selected_value == "Riwayat Sewa Laptop":
            self.frame.destroy()
            self.frame = ctk.CTkFrame(self.root, width=800, height=600, fg_color='#517F9C')
            self.frame.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)

            lblMain = ctk.CTkLabel(self.frame, text="Riwayat Sewa Laptop", font=('Inter',30))
            lblMain.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)

            btnBack = ctk.CTkButton(self.frame, text="Back", font=('Inter',20), command=self.back)
            btnBack.place(x=10, y=10)

    def back(self):
        self.frame.destroy()
        Main(self.root)

    def create_table(self):
        self.tree = ttk.Treeview(self.frame, show='headings' )
        self.tree['columns'] = ('Kode Laptop','Jenis Laptop', 'Status', 'Harga Sewa')
        self.tree.column('Kode Laptop', width=50, anchor=tk.CENTER)
        self.tree.column('Jenis Laptop', anchor=tk.CENTER)
        self.tree.column('Status', anchor=tk.CENTER)
        self.tree.column('Harga Sewa', anchor=tk.CENTER)
        self.tree.heading('Kode Laptop', text='Kode')
        self.tree.heading('Jenis Laptop', text='Jenis Laptop')
        self.tree.heading('Status', text='Status')
        self.tree.heading('Harga Sewa', text='Harga Sewa')

        data = Database.get_laptops()
        if data:
            for (kode_laptop, jenis_laptop, status, harga_sewa) in data:
                self.tree.insert('', 'end', values=(kode_laptop, harga_sewa, status, jenis_laptop))

        self.tree.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def tambah_laptop(self):
        top = ctk.CTkToplevel(self.root, fg_color='#517F9C')
        top.title("Tambah Laptop")
        top.geometry("400x300")

        lblMain = ctk.CTkLabel(top, text="Tambah Laptop", font=('Inter', 20))
        lblMain.pack(pady=10)

        lblKode = ctk.CTkLabel(top, text="Kode Laptop:", font=('Inter', 15))
        lblKode.place(x=10, y=50)
        self.kode_entry = ctk.CTkEntry(top, font=('Inter', 12))
        self.kode_entry.place(x=150, y=50)

        lblJenis = ctk.CTkLabel(top, text="Jenis Laptop:", font=('Inter', 15))
        lblJenis.place(x=10, y=100)
        self.jenis_entry = ctk.CTkEntry(top, font=('Inter', 12))
        self.jenis_entry.place(x=150, y=100)

        lblHarga = ctk.CTkLabel(top, text="Harga Sewa:", font=('Inter', 15))
        lblHarga.place(x=10, y=150)
        self.harga_entry = ctk.CTkEntry(top, font=('Inter', 12))
        self.harga_entry.place(x=150, y=150)

        btnSubmit = ctk.CTkButton(top, text="Submit", font=('Inter', 15), command=self.submit_laptop)
        btnSubmit.place(x=50, y=250)

        btnClose = ctk.CTkButton(top, text="Close", font=('Inter', 15), command=top.destroy)
        btnClose.place(x=200, y=250)

    def hapus_laptop(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Peringatan", "Pilih laptop yang akan dihapus.")
            return

        confirmation = messagebox.askyesno("Konfirmasi", "Apakah Anda yakin ingin menghapus laptop ini?")
        if confirmation:
            # Hapus laptop dari database
            kode_laptop = self.tree.item(selected_item)['values'][0]
            if Database.delete_laptop(kode_laptop):
                self.tree.delete(selected_item)
                messagebox.showinfo("Info", "Laptop berhasil dihapus.")
            else:
                messagebox.showerror("Error", "Gagal menghapus laptop.")

    def submit_laptop(self):
        kode_laptop = self.kode_entry.get()
        jenis_laptop = self.jenis_entry.get()
        harga_sewa = self.harga_entry.get()

        if not (kode_laptop and jenis_laptop and harga_sewa):
            messagebox.showerror("Error", "Semua kolom harus diisi.")
            return

        if Database.add_laptop(kode_laptop, jenis_laptop, harga_sewa):
            messagebox.showinfo("Info", "Laptop berhasil ditambahkan.")
            self.refresh_table_laptop()
            self.kode_entry.delete(0, ctk.END) 
            self.jenis_entry.delete(0, ctk.END)  
            self.harga_entry.delete(0, ctk.END)
        else:
            messagebox.showerror("Error", "Gagal menambahkan laptop.")

    def refresh_table_laptop(self):
        # Hapus semua entri saat ini dari tabel
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Perbarui tabel dengan data terbaru dari database
        data = Database.get_laptops()
        if data:
            for (kode_laptop, jenis_laptop, status, harga_sewa) in data:
                self.tree.insert('', 'end', values=(kode_laptop, harga_sewa, status, jenis_laptop))

    def update_info(self, selected_kode):
        jenis = Database.get_jenis(selected_kode)
        self.lblJenisLaptop2.configure(text=jenis)

        harga = Database.get_harga(selected_kode)
        self.lblHargaSewa2.configure(text=harga)

    def create_table_list(self):
        self.tree = ttk.Treeview(self.frame, show='headings' )
        self.tree['columns'] = ('Id Sewa','Kode Laptop','Jenis Laptop', 'Harga Sewa/Jam', 'Jam Mulai', 'Tanggal')
        self.tree.column('Id Sewa', width=50, anchor=tk.CENTER)
        self.tree.column('Kode Laptop', width=50, anchor=tk.CENTER)
        self.tree.column('Jenis Laptop', width=100, anchor=tk.CENTER)
        self.tree.column('Harga Sewa/Jam', width=100, anchor=tk.CENTER)
        self.tree.column('Jam Mulai', width=100, anchor=tk.CENTER)
        self.tree.column('Tanggal', anchor=tk.CENTER)
        self.tree.heading('Id Sewa', text='Id Sewa')
        self.tree.heading('Kode Laptop', text='Kode')
        self.tree.heading('Jenis Laptop', text='Jenis Laptop')
        self.tree.heading('Harga Sewa/Jam', text='Harga Sewa/Jam')
        self.tree.heading('Jam Mulai', text='Jam Mulai')
        self.tree.heading('Tanggal', text='Tanggal')

        data = Database.get_list()
        if data:
            for (id_sewa, kode_laptop, jenis_laptop, harga_sewa, jam_mulai, created_at) in data:
                self.tree.insert('', 'end', values=(id_sewa, kode_laptop, jenis_laptop, harga_sewa, jam_mulai, created_at))

        self.tree.place(x=10, y=350)

    def sewa_laptop(self):
        kode_laptop = self.selected_kode.get()
        jenis = self.lblJenisLaptop2.cget("text")
        harga = self.lblHargaSewa2.cget("text")

        if Database.sewa_laptop(kode_laptop, jenis, harga):
            messagebox.showinfo("Sukses", "Laptop berhasil disewa!")
            self.refresh_table_sewa()
            
            # Hapus item terpilih dari daftar nilai ComboBox
            self.kode_strings.remove(kode_laptop)
            # Atur ulang nilai-nilai ComboBox
            self.comboKodeLaptop.configure(values=self.kode_strings)
            self.comboKodeLaptop.set("Pilih Kode Laptop")
        else:
            messagebox.showerror("Error", "Gagal menyewa laptop.")

    def akhiri_sewa(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Peringatan", "Pilih laptop yang akan diakhiri sewanya.")
            return

        confirmation = messagebox.askyesno("Konfirmasi", "Apakah Anda yakin ingin mengakhiri sewa laptop ini?")
        if confirmation:
            # Akhiri sewa laptop dan dapatkan waktu mulai sewa
            kode_laptop = self.tree.item(selected_item)['values'][1]  # Ambil kode laptop dari item terpilih
            jam_mulai = Database.akhiri_sewa(kode_laptop)

            if jam_mulai is not None:
                messagebox.showinfo("Info", "Sewa laptop berhasil diakhiri.")
                self.refresh_table_sewa()

                # Konversi waktu sekarang menjadi datetime
                waktu_sekarang = datetime.datetime.now().time()
                print(jam_mulai)
                # Convert jam_mulai to datetime object
                jam_mulai_datetime = jam_mulai

                # Hitung perbedaan waktu dalam detik
                perbedaan_waktu = (waktu_sekarang.hour - jam_mulai.hour)
                print(perbedaan_waktu)

                # Konversi perbedaan waktu ke dalam jam
                durasi_sewa_jam = perbedaan_waktu // 3600

                # Ambil harga sewa per jam
                harga_sewa_per_jam = int(str(Database.get_harga(kode_laptop)))

                # Hitung total harga
                total_harga = harga_sewa_per_jam * perbedaan_waktu
                print("Total harga yang harus dibayar:", total_harga)  # Output untuk tujuan demonstrasi
            else:
                messagebox.showerror("Error", "Gagal mengakhiri sewa laptop.")




    def refresh_table_sewa(self):
        # Hapus semua entri saat ini dari tabel
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Perbarui tabel dengan data terbaru dari database
        data = Database.get_list()
        if data:
            for (id_sewa, kode_laptop, jenis_laptop, harga_sewa, jam_mulai, created_at) in data:
                self.tree.insert('', 'end', values=(id_sewa, kode_laptop, jenis_laptop, harga_sewa, jam_mulai, created_at))

ctk.set_appearance_mode("dark")
root = ctk.CTk()
app = Main(root)
root.mainloop()