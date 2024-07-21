from tkinter import *
import matplotlib.pyplot as plt
from tkinter import messagebox

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplikasi")
        self.root.geometry("230x80")

        window = Frame(self.root)
        window.grid(row=0, column=0)

        self.lblMain = Label(window, text='Selamat datang di aplikasi')
        self.lblMain.grid(row=0, column=0, columnspan=10, padx=5, pady=5)
        
        self.btnGaris = Button(window, text='Garis', command=self.frame_garis)
        self.btnGaris.grid(row=5, column=2, padx=5, pady=5)

        self.btnPersegiPanjang = Button(window, text='Persegi Panjang', command=self.frame_persegi_panjang)
        self.btnPersegiPanjang.grid(row=5, column=3, padx=5, pady=5)

        self.btnLingkaran = Button(window, text='Lingkaran', command=self.frame_circle)
        self.btnLingkaran.grid(row=5, column=4, padx=5, pady=5)

        self.btnActive = None

    def frame_garis(self):
        if self.btnActive is not None:
            messagebox.showinfo("Info", "Tombol lain sudah aktif.")
            return
        
        self.btnActive = self.btnGaris
        self.new_window = Toplevel(self.root)
        self.new_window.title("Buat Garis")
        self.new_window.geometry("300x200")

        lblStart = Label(self.new_window, text="Titik Awal (x,y):")
        lblStart.grid(row=0, column=0, padx=5, pady=5, sticky='w')
        self.entryStart = Entry(self.new_window)
        self.entryStart.grid(row=0, column=1, padx=5, pady=5)

        lblEnd = Label(self.new_window, text="Titik Akhir (x,y):")
        lblEnd.grid(row=1, column=0, padx=5, pady=5, sticky='w')
        self.entryEnd = Entry(self.new_window)
        self.entryEnd.grid(row=1, column=1, padx=5, pady=5)

        lblTebal = Label(self.new_window, text="Tebal Garis:")
        lblTebal.grid(row=2, column=0, padx=5, pady=5, sticky='w')
        self.entryTebal = Entry(self.new_window)
        self.entryTebal.grid(row=2, column=1, padx=5, pady=5)

        lblColor = Label(self.new_window, text="Warna Garis:")
        lblColor.grid(row=3, column=0, padx=5, pady=5, sticky='w')
        self.listbox_color = Listbox(self.new_window, height=3)
        self.listbox_color.grid(row=3, column=1, padx=5, pady=5)
        colors = ["red", "green", "blue"]
        for color in colors:
            self.listbox_color.insert(END, color)

        btnCreate = Button(self.new_window, text="Buat Garis", command=self.create_line)
        btnCreate.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

        btnClose = Button(self.new_window, text="Close", command= self.on_window_close)
        btnClose.grid(row=4, column=2, padx=5, pady=5)

        self.new_window.protocol("WM_DELETE_WINDOW", self.on_window_close)
    
    def frame_persegi_panjang(self):
        if self.btnActive is not None:
            messagebox.showinfo("Info", "Tombol lain sudah aktif.")
            return

        self.btnActive = self.btnPersegiPanjang
        self.new_window = Toplevel(self.root)
        self.new_window.title("Buat Persegi Panjang")
        self.new_window.geometry("300x300")

        lblStart = Label(self.new_window, text="Titik Awal (x,y):")
        lblStart.grid(row=0, column=0, padx=5, pady=5, sticky='w')
        self.entryStart = Entry(self.new_window)
        self.entryStart.grid(row=0, column=1, padx=5, pady=5)

        lblLebar = Label(self.new_window, text="Lebar:")
        lblLebar.grid(row=2, column=0, padx=5, pady=5, sticky='w')
        self.entryLebar = Entry(self.new_window)
        self.entryLebar.grid(row=2, column=1, padx=5, pady=5)

        lblTinggi = Label(self.new_window, text="Tinggi:")
        lblTinggi.grid(row=3, column=0, padx=5, pady=5, sticky='w')
        self.entryTinggi = Entry(self.new_window)
        self.entryTinggi.grid(row=3, column=1, padx=5, pady=5)

        lblColor = Label(self.new_window, text="Warna Garis:")
        lblColor.grid(row=4, column=0, padx=5, pady=5, sticky='w')
        self.listbox_edgecolor = Listbox(self.new_window, height=3, exportselection=0)
        self.listbox_edgecolor.grid(row=4, column=1, padx=5, pady=5)
        edgecolors = ["red", "green", "blue"]
        for color in edgecolors:
            self.listbox_edgecolor.insert(END, color)

        label_fill_color = Label(self.new_window, text="Warna Fill:")
        label_fill_color.grid(row=5, column=0, padx=5, pady=5, sticky='w')
        self.listbox_fill_color = Listbox(self.new_window, height=3, exportselection=0)
        self.listbox_fill_color.grid(row=5, column=1, padx=5, pady=5)
        fill_colors = ["red", "green", "blue"]
        for color in fill_colors:
            self.listbox_fill_color.insert(END, color)

        btnCreate = Button(self.new_window, text="Buat Persegi Panjang", command=self.create_rectangle)
        btnCreate.grid(row=6, column=0, columnspan=2, padx=5, pady=5)

        btnClose = Button(self.new_window, text="Close", command=self.on_window_close)
        btnClose.grid(row=6, column=2, padx=5, pady=5)

        self.new_window.protocol("WM_DELETE_WINDOW", self.on_window_close)

    def frame_circle(self):
        if self.btnActive is not None:
            messagebox.showinfo("Info", "Tombol lain sudah aktif.")
            return
        
        self.btnActive = self.btnLingkaran
        self.new_window = Toplevel(self.root)
        self.new_window.title("Buat Lingkaran")
        self.new_window.geometry("300x200")

        lblCenter = Label(self.new_window, text="Titik Tengah (x,y):")
        lblCenter.grid(row=0, column=0, padx=5, pady=5, sticky='w')
        self.entryCenter = Entry(self.new_window)
        self.entryCenter.grid(row=0, column=1, padx=5, pady=5)

        lblRadius = Label(self.new_window, text="Radius:")
        lblRadius.grid(row=1, column=0, padx=5, pady=5, sticky='w')
        self.entryRadius = Entry(self.new_window)
        self.entryRadius.grid(row=1, column=1, padx=5, pady=5)

        lblColor = Label(self.new_window, text="Warna Lingkaran:")
        lblColor.grid(row=2, column=0, padx=5, pady=5, sticky='w')
        self.listbox_color = Listbox(self.new_window, height=3)
        self.listbox_color.grid(rentryRadiusow=2, column=1, padx=5, pady=5)
        colors = ["red", "green", "blue"]
        for color in colors:
            self.listbox_color.insert(END, color)

        btnCreate = Button(self.new_window, text="Buat Lingkaran", command=self.create_circle)
        btnCreate.grid(row=3, column=0, columnspan=2, padx=5, pady=5)
        
        btnClose = Button(self.new_window, text="Close", command=self.on_window_close)
        btnClose.grid(row=3, column=2, padx=5, pady=5)

        self.new_window.protocol("WM_DELETE_WINDOW", self.on_window_close)
    
    def create_line(self):
        try:
            start = eval(self.entryStart.get())
            end = eval(self.entryEnd.get())
            tebal = int(self.entryTebal.get())
            color_index = self.listbox_color.curselection()
            if not color_index:
                raise ValueError("Pilih warna garis.")
            color = self.listbox_color.get(color_index)
            
            plt.plot([start[0], end[0]], [start[1], end[1]], color=color, linewidth=tebal)
            plt.show()

        except Exception as e:
            messagebox.showerror("Error", str(e))

    def create_rectangle(self):
        try:
            start = eval(self.entryStart.get())
            lebar = int(self.entryLebar.get())
            tinggi = int(self.entryTinggi.get())

            edgecolor_index = self.listbox_edgecolor.curselection()
            if not edgecolor_index:
                raise ValueError("Pilih warna garis.")
            edgecolor = self.listbox_edgecolor.get(edgecolor_index)

            fill_color_index = self.listbox_fill_color.curselection()
            if not fill_color_index:
                raise ValueError("Pilih warna fill.")
            fill_color = self.listbox_fill_color.get(fill_color_index)

            rectangle = plt.Rectangle(start, lebar, tinggi, edgecolor=edgecolor, linewidth=2, fill=True, facecolor=fill_color)
            plt.gca().add_patch(rectangle)
            plt.axis('equal')
            plt.show()

        except Exception as e:
            messagebox.showerror("Error", str(e))


    def create_circle(self):
        try:
            center = eval(self.entryCenter.get())
            radius = float(self.entryRadius.get())
            color_index = self.listbox_color.curselection()
            if not color_index:
                raise ValueError("Pilih warna lingkaran.")
            color = self.listbox_color.get(color_index)
            
            circle = plt.Circle(center, radius, facecolor=color, linewidth=2, fill=True)
            plt.gca().add_patch(circle)
            plt.axis('equal')
            plt.show()

        except Exception as e:
            messagebox.showerror("Error", str(e))

    def on_window_close(self):
        self.btnActive = None
        self.new_window.destroy()

root = Tk()
app = App(root)
root.mainloop()
