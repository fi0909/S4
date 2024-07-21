import customtkinter as ctk
import tkinter as tk

root = ctk.CTk()
root.geometry("1280x720")
root.title("test side menu")
#making scroll bar frames
frm_scroll1=ctk.CTkScrollableFrame(master=root,fg_color="transparent",height=300,orientation="horizontal")
frm_scroll1.place(relx=0.1,y=235,relwidth=0.88)


# making layout
frm_side = ctk.CTkFrame(master=root,fg_color="light blue",width=125)
frm_side.place(x=25,y=25,relheight=0.9,relwidth=0.07)

frm_title = ctk.CTkFrame(master=root,fg_color="light green",height=200)
frm_title.place(relx=0.1,y=25,relwidth=0.88)

for x in range(10):
    jarak = 5
    frm_content = ctk.CTkFrame(master=frm_scroll1,fg_color="pink",height=200,width=200)
    frm_content.pack(side="left",padx=jarak,expand=1)
    jarak += 10

frm_content2 = ctk.CTkFrame(master=root,fg_color="#FFD580")
frm_content2.place(relx=0.545,y=535,relwidth=0.435)

frm_content3 = ctk.CTkFrame(master=root,fg_color="#ff99ff")
frm_content3.place(relx=0.1,y=845,relwidth=0.575)

frm_content4 = ctk.CTkFrame(master=root,fg_color="#3366ff")
frm_content4.place(relx=0.685,y=845,relwidth=0.295)

btn_img = ctk.CTkButton(master=frm_side,text="ICON",width=25,height=25)
btn_img.place(relx="0.2",rely='0.05')
ctk.set_appearance_mode("dark")
root.mainloop()