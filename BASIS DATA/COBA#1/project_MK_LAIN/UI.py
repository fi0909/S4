import tkinter as tk
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import threading

def garis_plot(x,y,lw,color):
    plt.title("gambar garis dari titik {},{} dan {},{}".format(x[0],y[0],x[1],y[1]))
    x1=x
    y1=y
    plt.plot(x1,y1, linewidth=lw, c=color)
    plt.show()

def persegi_plot(x_arr,y_arr,lw,color,color2):
    x=x_arr #[1,5]
    y=y_arr #[1,2]
    x_fix=[x[0],x[1],x[2],x[3],x[0]]
    y_fix=[y[0],y[1],y[2],y[3],y[0]]
    fig, ax = plt.subplots()
    plt.title("gambar persegi panjang dari 4 titik")
    ax.fill(x_fix,y_fix,color=color2)
    plt.plot(x_fix,y_fix,linewidth=lw,c=color)
    plt.show()

def lingkaran_plot(center,r,color):
    
    
    plt.figure(figsize=(8,6.5))
    xy=[center[0],center[1]]
    circle1= patches.Circle(xy,r,color=color)
    fig,ax=plt.subplots()

    ax.add_patch(circle1)
    plt.xlim(0,20)
    plt.ylim(0,20)
    plt.show()

def garis_menu():
    for child in frame1.winfo_children():
        child.destroy()
    
    #row configure
    frame1.rowconfigure([1,2,3,4,5],weight=1)
    frame1.columnconfigure([1,2,3],weight=1)
    frame1.pack(ipadx=500,ipady=500,fill="both")
    
    #variables
    grs_titik_awal = tk.StringVar()
    grs_titik_awal1 = tk.StringVar()
    grs_titik_akhir = tk.StringVar()
    grs_titik_akhir1 = tk.StringVar()
    x_garis = []
    y_garis = []
    warna = ''
    lebar = tk.StringVar()

    # label_garis
    lbl_titik_awal=tk.Label(master=frame1,text="koordinat titik awal")
    lbl_titik_awal.grid(row=1,column=1,sticky='w')
    lbl_titik_akhir =tk.Label(master=frame1,text="koordinat titik akhir")
    lbl_titik_akhir.grid(row=2,column=1,sticky='w')
    lbl_lebar_garis = tk.Label(master=frame1,text="lebar garis").grid(row=3,column=1,sticky='w')
    lbl_warna_garis =tk.Label(master=frame1,text="warna garis").grid(row=4,column=1,sticky='w')
    

    #entry garis
    ent_titik_awal = tk.Entry(master=frame1,textvariable=grs_titik_awal).grid(row=1,column=2,sticky='w',ipadx=65,ipady=0)
    ent_titik_awa2 = tk.Entry(master=frame1,textvariable=grs_titik_awal1).grid(row=1,column=3,sticky='w',ipadx=65,ipady=0)
    ent_titik_akhir = tk.Entry(master=frame1,textvariable=grs_titik_akhir).grid(row=2,column=2,sticky='w',ipadx=65,ipady=0)
    ent_titik_akhir2 = tk.Entry(master=frame1,textvariable=grs_titik_akhir1).grid(row=2,column=3,sticky='w',ipadx=65,ipady=0)
    ent_lebar_garis = tk.Entry(master=frame1,textvariable=lebar).grid(row=3,column=2,columnspan=3,sticky='ew')

    #list
    list_warna_garis = tk.Listbox(master=frame1,selectmode="single",activestyle="dotbox")
    list_warna_garis.insert(1,"red")
    list_warna_garis.insert(2,"blue")
    list_warna_garis.insert(3,"yellow")
    list_warna_garis.insert(4,"magenta")
    list_warna_garis.insert(5,"white")
    list_warna_garis.grid(row=4,column=2,columnspan=2,sticky='ew')
    
    #btn
    btn_garis = tk.Button(master=frame1,text="continue",command=lambda: threading.Thread(
        target=garis_plot(
            x=[int(grs_titik_awal.get()),int(grs_titik_akhir.get())],
            y=[int(grs_titik_awal1.get()),int(grs_titik_akhir1.get())],
            lw=int(lebar.get()),
            color=list_warna_garis.get(list_warna_garis.curselection()))
        ).start()).grid(row=5,columnspan=4,rowspan=2,sticky='sew')

def persegi_panjang():
    for child in frame1.winfo_children():
        child.destroy()
    
    #frame1 configure
    frame1.rowconfigure([1,2,3,4],weight=1)
    frame1.rowconfigure(5,weight=1)
    frame1.rowconfigure(6,weight=2)

    #label
    lbl_titik_persegi1      = tk.Label(master=frame1,text="koordinat titik ke-1").grid(row=1,column=1,sticky='w')
    lbl_titik_persegi2      = tk.Label(master=frame1,text="koordinat titik Ke-2").grid(row=2,column=1,sticky='w')
    lbl_titik_persegi3      = tk.Label(master=frame1,text="koordinat titik Ke-3").grid(row=3,column=1,sticky='w')
    lbl_titik_persegi4      = tk.Label(master=frame1,text="koordinat titi ke-4").grid(row=4,column=1,sticky='w')
    lbl_lebar_garis_persegi = tk.Label(master=frame1,text="lebar garis").grid(row=5,column =1,sticky='w')

    #variabel
    titik_persegi1      = tk.StringVar()
    titik_persegi1_2    = tk.StringVar()
    titik_persegi2      = tk.StringVar()
    titik_persegi2_2    = tk.StringVar()
    titik_persegi3      = tk.StringVar()
    titik_persegi3_2    = tk.StringVar()
    titik_persegi4      = tk.StringVar()
    titik_persegi4_2    = tk.StringVar()
    lebar_garis_persegi = tk.StringVar()

    #entry
    ent_titik_persegi1      = tk.Entry(master=frame1,textvariable=titik_persegi1).grid(row=1,column=2,sticky='w',ipadx=65,ipady=0)
    ent_titik_persegi1_2    = tk.Entry(master=frame1,textvariable=titik_persegi1_2).grid(row=1,column=3,sticky='w',ipadx=65,ipady=0)
    ent_titik_persegi2      = tk.Entry(master=frame1,textvariable=titik_persegi2).grid(row=2,column=2,sticky='w',ipadx=65,ipady=0)
    ent_titik_persegi2_1    = tk.Entry(master=frame1,textvariable=titik_persegi2_2).grid(row=2,column=3,sticky='w',ipadx=65,ipady=0)
    ent_titik_persegi3      = tk.Entry(master=frame1,textvariable=titik_persegi3).grid(row=3,column=2,sticky='w',ipadx=65,ipady=0)
    ent_titik_persegi3_1    = tk.Entry(master=frame1,textvariable=titik_persegi3_2).grid(row=3,column=3,sticky='w',ipadx=65,ipady=0)
    ent_titik_persegi4      = tk.Entry(master=frame1,textvariable=titik_persegi4).grid(row=4,column=2,sticky='w',ipadx=65,ipady=0)
    ent_titik_persegi4_1    = tk.Entry(master=frame1,textvariable=titik_persegi4_2).grid(row=4,column=3,sticky='w',ipadx=65,ipady=0)
    ent_lebar_garis_persegi = tk.Entry(master=frame1,textvariable=lebar_garis_persegi).grid(row=5,column=2,columnspan=2,sticky='w',ipadx=230,ipady=0)


    #frame & list
    frame_warna = tk.Frame(master=frame1)
    frame_warna.rowconfigure([1,2],weight=1)
    frame_warna.columnconfigure([1,2],weight=1)
    frame_warna.grid(row=6,columnspan=2,column=1,sticky='ew')

    lbl_warna_persegi = tk.Label(master=frame_warna,text="warna_garis").grid(row=1,column=1,sticky='ew')

    list_warna_garis = tk.Listbox(master=frame_warna,selectmode="browse",activestyle="dotbox",exportselection=False)
    list_warna_garis.insert(1,"red")
    list_warna_garis.insert(2,"blue")
    list_warna_garis.insert(3,"yellow")
    list_warna_garis.insert(4,"magenta")
    list_warna_garis.insert(5,"white")
    list_warna_garis.grid(row=2,column=1,sticky='')

    lbl_isi_persegi = tk.Label(master=frame_warna,text="warna persegi").grid(row=1,column=2,sticky='ew')

    list_isi_persegi = tk.Listbox(master=frame_warna,selectmode="browse",activestyle="dotbox",exportselection=False)
    list_isi_persegi.insert(1,"red")
    list_isi_persegi.insert(2,"blue")
    list_isi_persegi.insert(3,"yellow")
    list_isi_persegi.insert(4,"magenta")
    list_isi_persegi.insert(5,"white")
    list_isi_persegi.grid(row=2,column=2,sticky='')

    
    
    btn_pp_ = tk.Button(
        master=frame1,text="continue",
        command=lambda:threading.Thread(
            target=persegi_plot(
                x_arr=[int(titik_persegi1.get()),int(titik_persegi2.get()),int(titik_persegi3.get()),int(titik_persegi4.get())],
                y_arr=[int(titik_persegi1_2.get()),int(titik_persegi2_2.get()),int(titik_persegi3_2.get()),int(titik_persegi4_2.get())],
                lw=int(lebar_garis_persegi.get()),
                color=list_warna_garis.get(list_warna_garis.curselection()),
                color2=list_isi_persegi.get(list_isi_persegi.curselection())
                )).start(),padx=25,pady=25).grid(row=6,column=3,sticky='')

def lingkaran_menu():
    
    for child in frame1.winfo_children():
        child.destroy()

    #frame config
    frame1.rowconfigure([1,2,3,4,5],weight=1)
    frame1.columnconfigure([1,2,3],weight=1)
    frame1.pack(ipadx=500,ipady=500,fill="both")

    #label
    lbl_krd_pst = tk.Label(master=frame1,text="Koordinat titik pusat").grid(row=1,column=1,sticky='w')
    lbl_pjg_jari = tk.Label(master=frame1,text="Panjang jari-jari").grid(row=2,column=1,sticky='w')
    lbl_lst_warna = tk.Label(master=frame1,text="Warna lingkaran").grid(row=3,column=1,sticky='w')
    
    #variabel
    ttk_lingkaran = tk.StringVar()
    ttk_lingkaran2 = tk.StringVar()
    pjg_lingkaran = tk.StringVar()

    #entry
    ent_krd_pst = tk.Entry(master=frame1,textvariable=ttk_lingkaran).grid(row=1,column=2,sticky='w',ipadx=65,ipady=0)
    ent_krd_pst2 = tk.Entry(master=frame1,textvariable=ttk_lingkaran2).grid(row=1,column=3,sticky='w',ipadx=65,ipady=0)
    ent_pjg_jari = tk.Entry(master=frame1,textvariable=pjg_lingkaran).grid(row=2,column=2,columnspan=2,sticky='w',ipadx=230,ipady=0)

    #list_box
    list_warna_lingkaran = tk.Listbox(master=frame1,selectmode="browse",activestyle='dotbox',exportselection=False)
    list_warna_lingkaran.insert(1,"red")
    list_warna_lingkaran.insert(2,"blue")
    list_warna_lingkaran.insert(3,"yellow")
    list_warna_lingkaran.insert(5,"white")
    list_warna_lingkaran.insert(4,"magenta")
    list_warna_lingkaran.grid(row=3,column=2,sticky='sn')

    #btn
    btn_lngkrn = tk.Button(
        master=frame1,text="Continue",
        command= lambda:threading.Thread(
            target=lingkaran_plot([int(ttk_lingkaran.get()),int(ttk_lingkaran2.get())],
            r=int(pjg_lingkaran.get()),
            color=list_warna_lingkaran.get(list_warna_lingkaran.curselection()))).start()).grid(row=5,column=1,columnspan=3,sticky='sew')
def main_menu():
    for i in frame1.winfo_children():
        i.destroy()
    frame1.rowconfigure([1,2,3,4,5],weight=1)
    frame1.columnconfigure([1,2,3],weight=1)
    frame1.pack(ipadx=500,ipady=500,fill="both")

    lbl_utama = tk.Label(master=frame1,text="Selamat Datang, di aplikasi...!!",font=("arial",32)).grid(row=1,column=1,columnspan=3)
    txt_utama = tk.Label(master=frame1,text="Klik opsi untuk memulai aplikasi",font=("arial",16))
    txt_utama.grid(row=3,column=1,columnspan=3)
    txt_pmb = tk.Label(master=frame1,text="@vxyzuc",font=("arial",8),fg="grey").grid(row=5,column=1,columnspan=3)
window = tk.Tk()
window.title("PEMVIS")
window.geometry("800x600")
window.resizable(height=True,width=True)
# Make menu
menubar = tk.Menu(window)
opsi = tk.Menu(menubar,tearoff=0,border=10)
menubar.add_cascade(label='opsi',menu=opsi)
opsi.add_command(label="garis",command=garis_menu)
opsi.add_command(label="persegi_panjang",command=persegi_panjang)
opsi.add_command(label="lingkaran",command=lingkaran_menu)
opsi.add_command(label="main",command=main_menu)
frame1 = tk.Frame(master=window)
frame1.rowconfigure([1,2,3,4,5],weight=1)
frame1.columnconfigure([1,2,3],weight=1)
frame1.pack(ipadx=500,ipady=500,fill="both")

lbl_utama = tk.Label(master=frame1,text="Selamat Datang, di aplikasi...!!",font=("arial",32)).grid(row=1,column=1,columnspan=3)
txt_utama = tk.Label(master=frame1,text="Klik opsi untuk memulai aplikasi",font=("arial",16))
txt_utama.grid(row=3,column=1,columnspan=3)
txt_pmb = tk.Label(master=frame1,text="@vxyzuc",font=("arial",8),fg="grey").grid(row=5,column=1,columnspan=3)
#function

window.config(menu=menubar)
window.mainloop()