from tkinter import *
from tkinter.ttk import Progressbar
from tkinter.ttk import Style


# progress work : DONE
class load_scr:
    def __init__(self,root) :
        self.root = root
        self.root.title("loading screen")
        self.root.geometry("800x600")
        self.root.maxsize(800,600)
        # ========== frame loading screeen ================#
        self.frm_load_scrn = Frame(self.root)
        self.frm_load_scrn.configure(background="#666666")
        self.frm_load_scrn.place(relx=0,rely=0,relwidth=1,relheight=1)
        self.s = Style(self.frm_load_scrn)
        self.s.theme_use("default")
        self.s.configure("custom.Horizontal.TProgressbar", troughcolor='grey',background='white')

        #========================== variabel that can be change =====================#
        self.str = StringVar()
        self.x0 = 0
        self.x1 = 0
        self.y0 = 0
        self.y1 = 0
        self.index = 0

        # ========================== canvas -ciricle =============== #
        self.canvas = Canvas(master=self.frm_load_scrn,bg="grey")
        self.canvas.place(relheight=1,relwidth=1)
    
        self.lbl_load_scrn = Label(self.frm_load_scrn,textvariable=self.str,fg="black",bg='white',justify="center",font=("arial",18,"bold",))
        self.lbl_load_scrn.place(relx=0.4,rely=0.25)

        self.condition = False
        self.text = "nama_aplikasi"
        # ======================================== progbar =========================================#
        self.progbar = Progressbar(master=self.frm_load_scrn,style="custom.Horizontal.TProgressbar",orient="horizontal")
        self.progbar.place(relx=0.1,rely=0.8,height=30,relwidth=0.8)
        self.progbar["value"] = 0

        #========================== call function =====================#
        self.text_anim()
    
    def text_anim(self):
        self.delay = 100
        if self.condition is False: #adding the text anim
            char = (self.text[:self.index]+"|")
            self.str.set(char)
            self.index += 1
            self.progbar["value"] += 1
            self.delay_task = self.frm_load_scrn.after(self.delay,self.text_anim) # looping the anim with the delay
            self.cirlce_size()
            #self.prog_bar_updt()
            if self.index >= len(self.text):
                self.condition = True
            if self.progbar['value'] >= 100:
                self.frm_load_scrn.after_cancel(self.delay_task) #stop the looping 
                self.delay_task = None #change the delay teks variable to stop
                self.root.destroy()
        else: # deleteting the text
            char = (self.text[0:self.index]+"|")
            self.str.set(char)
            self.index -= 1
            self.progbar["value"] += 1
            self.delay_task = self.frm_load_scrn.after(self.delay,self.text_anim)
            #self.prog_bar_updt()
            if self.index <= 0:
                self.index = 0
                self.condition = False
            if self.progbar['value'] >= 100:
                self.frm_load_scrn.after_cancel(self.delay_task)
                self.delay_task = None
                self.root.destroy()
    def prog_bar_updt(self):
        self.prog_value = self.progbar['value']
        if self.prog_value >= 100:
            pass
    def menu_utama(self):
        for i in self.frm_load_scrn.winfo_children():
            i.destroy()
        self.lbl_utama = Label(master=self.frm_load_scrn,text="welcome to app").pack()
    
    def cirlce_size(self):
        self.canvas.create_oval(self.x0,self.y0,self.x1,self.y1,fill="white",outline="white")
        self.y1 += 20
        self.x1 -= 20
        self.x0 += 20
        self.y0 -= 20
win = Tk()
tk = load_scr(win)

win.mainloop()