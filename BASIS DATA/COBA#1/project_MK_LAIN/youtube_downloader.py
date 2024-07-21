from pytube import YouTube
from pytube import Playlist
import customtkinter as ctk
import CTkMessagebox
import threading
from tkinter.filedialog import askdirectory
import urllib.request
from io import BytesIO
import loading_screen
from PIL import Image

class app:
    def __init__(self,window):
        self.root=window
        image_procces = Image.open('C:/Users/croco/OneDrive/Documents/BASIS DATA/COBA#1/project_MK_LAIN/download.png')
        self.frame = ctk.CTkFrame(master=self.root,border_width=3,corner_radius=13)
        self.frame.grid(row=0,rowspan=4,column=0,pady=30,padx=15)
        self.frm_content = ctk.CTkFrame(master=self.root,width=160,height=100)
        self.frm_content.rowconfigure(1,minsize=1)
        self.frm_content.grid(row=1,rowspan=3,column=1,columnspan=3,sticky="nsew",ipadx=5)
        self.img = ctk.CTkImage(image_procces,size=[120,120])
        self.lbl_image = ctk.CTkLabel(master=self.frame,image=self.img,text='',)
        self.lbl_image.grid(row=0,column=0,padx=15,pady=15)
        self.lbl_Judul = ctk.CTkLabel(master=self.root,text="Welcome to yt downloader",font=("arial",28))
        self.lbl_Judul.grid(row=0,column=1,columnspan=2,padx=85)
        self.lbl_teks = ctk.CTkLabel(master=self.frm_content,text="klik button disamping untuk untuk memulai",font=("arial",16))
        self.lbl_teks.grid(row=0,column=0,columnspan=2,padx=105,pady=15)
        self.lbl_teks2 = ctk.CTkLabel(master=self.frm_content,text="contact: @vxyzuc",font=("arial",12))
        self.lbl_teks2.grid(row=1,column=0,columnspan=2,rowspan=2,sticky='sew',pady=75)
        self.btn_vid = ctk.CTkButton(master=self.frame,text='video',corner_radius=12,command=self.video_menu)
        self.btn_vid.grid(row=1,column=0,padx=15,pady=15)
        self.btn_audio = ctk.CTkButton(master=self.frame,text='audio',corner_radius=12,command=self.audio_menu)
        self.btn_audio.grid(row=2,column=0,padx=15,pady=15)
        self.btn_playlist = ctk.CTkButton(master=self.frame,text='playlist',corner_radius=12,command=self.playlist_menu)
        self.btn_playlist.grid(row=3,column=0,padx=15,pady=15)
    def video_menu (self):
        for child in self.frm_content.winfo_children():
            child.destroy()
        self.frm_content.grid(row=1,rowspan=3,column=1,columnspan=3,sticky='n',ipadx=5)
        self.lbl_Judul.configure(1,text="video downloader")
        self.lbl_Judul.grid(row=0,column=1,columnspan=2,padx=125)
        self.lbl_video=ctk.CTkLabel(master=self.frm_content,text="link Video",font=('arial',14))
        self.lbl_video.pack(anchor='center',side="top",padx=215)
        self.link_var = ctk.StringVar()
        self.option_menu = ctk.StringVar()
        self.ent_lvid =ctk.CTkEntry(master=self.frm_content,textvariable=self.link_var)
        self.ent_lvid.pack(anchor = 'center',pady=25,ipadx=125)
        self.chck_bx = ctk.CTkComboBox(master=self.frm_content,values=["video only",'video & audio'])
        self.chck_bx.set("download option")
        self.chck_bx.pack(anchor='center')
        self.btn_vddwn = ctk.CTkButton(master=self.frm_content,text="DOWNLOAD",bg_color="transparent",command= lambda: threading.Thread(target=self.video_downloader).start())
        self.btn_vddwn.pack(anchor='center',ipadx=125,pady=15)

    def audio_menu(self):
        for child in self.frm_content.winfo_children():
            child.destroy()
        self.lbl_Judul.configure(1,text="audio downloader")
        self.lbl_Judul.grid(row=0,column=1,columnspan=2,padx=125)
        self.link_var = ctk.StringVar()
        self.frm_content.grid()
        self.lbl_video=ctk.CTkLabel(master=self.frm_content,text="link Video",font=('arial',14))
        self.lbl_video.pack(anchor='center',side="top",padx=215)
        self.ent_lvid =ctk.CTkEntry(master=self.frm_content,textvariable=self.link_var)
        self.ent_lvid.pack(anchor = 'center',pady=25,ipadx=125)
        self.chck_bx = ctk.CTkComboBox(master=self.frm_content,values=["MP4",'webm'])
        self.chck_bx.set("download option")
        self.chck_bx.pack(anchor='center')
        self.btn_auddwn = ctk.CTkButton(master=self.frm_content,text="DOWNLOAD",bg_color="transparent",command= lambda: threading.Thread(target=self.audio_downloader).start())
        self.btn_auddwn.pack(anchor='center',ipadx=125,pady=15)

    def playlist_menu(self):
        for child in self.frm_content.winfo_children():
            child.destroy()
        self.frm_content.grid(row=1,rowspan=3,column=1,columnspan=3,sticky='n',ipadx=5)
        self.lbl_Judul.configure(1,text="playlist downloader")
        self.lbl_Judul.grid(row=0,column=1,columnspan=2,padx=125)
        self.lbl_video=ctk.CTkLabel(master=self.frm_content,text="link Video",font=('arial',14))
        self.lbl_video.pack(anchor='center',side="top",padx=215)
        self.link_var = ctk.StringVar()
        self.option_menu = ctk.StringVar()
        self.ent_lvid =ctk.CTkEntry(master=self.frm_content,textvariable=self.link_var)
        self.ent_lvid.pack(anchor = 'center',pady=25,ipadx=125)
        self.chck_bx = ctk.CTkComboBox(master=self.frm_content,values=["video",'audio'])
        self.chck_bx.set("download option")
        self.chck_bx.pack(anchor='center')
        self.btn_vddwn = ctk.CTkButton(master=self.frm_content,text="DOWNLOAD",bg_color="transparent",command= lambda: threading.Thread(target=self.playlist_downloader).start())
        self.btn_vddwn.pack(anchor='center',ipadx=125,pady=15)


    def prog_bar(self,stream,chunk,bytes_remaining):
        progress = int(((stream.filesize-bytes_remaining)/stream.filesize)*100)
        self.progress_var.set(progress)
        self.p_bar.set(float(progress/100))
        self.lbl_dwn.configure(1,text="{},{}%".format(stream.title,progress))


    def on_complete(self,stream,file_path):
        CTkMessagebox.CTkMessagebox(title="download done",message="your donwload is succesfully complete",icon='check')
        self.lbl_dwn.destroy()
        self.p_bar.destroy()


    def video_downloader(self):
        link = self.link_var.get()
        self.progress_var = ctk.IntVar()
        self.progress_var.set(0)
        ct_chck_bx = self.chck_bx.get()
        if ct_chck_bx == "video only" and link is not None:
            youtube=YouTube(link,on_progress_callback=self.prog_bar,on_complete_callback=self.on_complete)
            CTkMessagebox.CTkMessagebox(master=self.root,title="video info",message="title: {}\nauthor: {}".format(youtube.title,youtube.author))
            u = urllib.request.urlopen(youtube.thumbnail_url)
            raw_data = u.read()
            u.close()
            im = Image.open(BytesIO(raw_data))
            pic_yt = ctk.CTkImage(im,size=[120,120])
            lbl_yt_thumbnail = ctk.CTkLabel(master=self.frm_content,text='',image=pic_yt)
            lbl_yt_thumbnail.pack(anchor='center')
            strm = youtube.streams.filter(adaptive=True,only_video=True).first()
            filename=askdirectory()
            if strm is not None:
                self.p_bar = ctk.CTkProgressBar(master=self.frm_content,orientation="horizontal",determinate_speed=1)
                self.p_bar.set(0)
                self.p_bar.pack(anchor="center",ipadx=125,pady=15)
                self.lbl_dwn = ctk.CTkLabel(master=self.frm_content,text="")
                self.lbl_dwn.pack(anchor='center')
                strm.download(filename)
            else:
                CTkMessagebox.CTkMessagebox(title="ERROR",message="There is some error please put the link correctly",option_1='ok',icon="cancel")
        elif ct_chck_bx == "video & audio" and link is not None:
            youtube=YouTube(link,on_progress_callback=self.prog_bar,on_complete_callback=self.on_complete)
            CTkMessagebox.CTkMessagebox(master=self.root,title="video info",message="title: {}\nauthor: {}".format(youtube.title,youtube.author))
            u = urllib.request.urlopen(youtube.thumbnail_url)
            raw_data = u.read()
            u.close()
            im = Image.open(BytesIO(raw_data))
            pic_yt = ctk.CTkImage(im,size=[120,120])
            lbl_yt_thumbnail = ctk.CTkLabel(master=self.frm_content,text='',image=pic_yt)
            lbl_yt_thumbnail.pack(anchor='center')
            strm = youtube.streams.get_highest_resolution()
            filename=askdirectory()
            if strm is not None:
                self.p_bar = ctk.CTkProgressBar(master=self.frm_content,orientation="horizontal",determinate_speed=1)
                self.p_bar.set(0)
                self.p_bar.pack(anchor="center",ipadx=125,pady=15)
                self.lbl_dwn = ctk.CTkLabel(master=self.frm_content,text="")
                self.lbl_dwn.pack(anchor='center')
                strm.download(str(filename))
            else:
                CTkMessagebox.CTkMessagebox(title="ERROR",message="There is some error please put the link correctly",option_1='ok',icon="cancel")
        else:
            CTkMessagebox.CTkMessagebox(master=self.root,title="error",message="please input all the requirement",option_1="ok",icon='cancel')
    
    def audio_downloader(self):
        link = self.link_var.get()
        self.progress_var = ctk.IntVar()
        self.progress_var.set(0)
        ct_chck_bx = self.chck_bx.get()
        if ct_chck_bx == "MP4" and link is not None:
            youtube=YouTube(link,on_progress_callback=self.prog_bar,on_complete_callback=self.on_complete)
            CTkMessagebox.CTkMessagebox(master=self.root,title="video info",message="title: {}\nauthor: {}".format(youtube.title,youtube.author))
            u = urllib.request.urlopen(youtube.thumbnail_url)
            raw_data = u.read()
            u.close()
            im = Image.open(BytesIO(raw_data))
            pic_yt = ctk.CTkImage(im,size=[120,120])
            lbl_yt_thumbnail = ctk.CTkLabel(master=self.frm_content,text='',image=pic_yt)
            lbl_yt_thumbnail.pack(anchor='center')
            strm = youtube.streams.get_audio_only()
            filename=askdirectory()
            if strm is not None:
                self.p_bar = ctk.CTkProgressBar(master=self.frm_content,orientation="horizontal",determinate_speed=1)
                self.p_bar.set(0)
                self.p_bar.pack(anchor="center",ipadx=125,pady=15)
                self.lbl_dwn = ctk.CTkLabel(master=self.frm_content,text="")
                self.lbl_dwn.pack(anchor='center')
                strm.download(filename)
            else:
                CTkMessagebox.CTkMessagebox(title="ERROR",message="There is some error please put the link correctly",option_1='ok',icon="cancel")
        elif ct_chck_bx == "webm" and link is not None:
            youtube=YouTube(link,on_progress_callback=self.prog_bar,on_complete_callback=self.on_complete)
            CTkMessagebox.CTkMessagebox(master=self.root,title="video info",message="title: {}\nauthor: {}".format(youtube.title,youtube.author))
            u = urllib.request.urlopen(youtube.thumbnail_url)
            raw_data = u.read()
            u.close()
            im = Image.open(BytesIO(raw_data))
            pic_yt = ctk.CTkImage(im,size=[120,120])
            lbl_yt_thumbnail = ctk.CTkLabel(master=self.frm_content,text='',image=pic_yt)
            lbl_yt_thumbnail.pack(anchor='center')
            strm = youtube.streams.filter(only_audio=True).last()
            filename=askdirectory()
            if strm is not None:
                self.p_bar = ctk.CTkProgressBar(master=self.frm_content,orientation="horizontal",determinate_speed=1)
                self.p_bar.set(0)
                self.p_bar.pack(anchor="center",ipadx=125,pady=15)
                self.lbl_dwn = ctk.CTkLabel(master=self.frm_content,text="")
                self.lbl_dwn.pack(anchor='center')
                strm.download(str(filename))
            else:
                CTkMessagebox.CTkMessagebox(title="ERROR",message="There is some error please put the link correctly",option_1='ok',icon="cancel")
        else:
            CTkMessagebox.CTkMessagebox(master=self.root,title="error",message="please input all the requirement",option_1="ok",icon='cancel')
    def playlist_downloader(self):
        link = self.link_var.get()
        self.progress_var = ctk.IntVar()
        self.progress_var.set(0)
        P_list = Playlist(link)
        ct_chck_bx = self.chck_bx.get()
        if ct_chck_bx == "video" and link is not None:
            filename=askdirectory()
            for video in P_list.video_urls:
                youtube=YouTube(video,on_progress_callback=self.prog_bar,on_complete_callback=self.on_complete)
                CTkMessagebox.CTkMessagebox(master=self.root,title="video info",message="title: {}\nauthor: {}".format(youtube.title,youtube.author))
                strm = youtube.streams.get_highest_resolution()
                if strm is not None:
                    self.p_bar = ctk.CTkProgressBar(master=self.frm_content,orientation="horizontal",determinate_speed=1)
                    self.p_bar.set(0)
                    self.p_bar.pack(anchor="center",ipadx=125,pady=15)
                    self.lbl_dwn = ctk.CTkLabel(master=self.frm_content,text="")
                    self.lbl_dwn.pack(anchor='center')
                    strm.download(filename)
                else:
                    CTkMessagebox.CTkMessagebox(title="ERROR",message="There is some error please put the link correctly",option_1='ok',icon="cancel")
        elif ct_chck_bx == "audio" and link is not None:
            filename=askdirectory()
            for video in P_list.video_urls:
                youtube=YouTube(video,on_progress_callback=self.prog_bar,on_complete_callback=self.on_complete)
                CTkMessagebox.CTkMessagebox(master=self.root,title="video info",message="title: {}\nauthor: {}".format(youtube.title,youtube.author))
                strm = youtube.streams.get_audio_only()
                if strm is not None:
                    self.p_bar = ctk.CTkProgressBar(master=self.frm_content,orientation="horizontal",determinate_speed=1)
                    self.p_bar.set(0)
                    self.p_bar.pack(anchor="center",ipadx=125,pady=15)
                    self.lbl_dwn = ctk.CTkLabel(master=self.frm_content,text="")
                    self.lbl_dwn.pack(anchor='center')
                    strm.download(str(filename))
                else:
                    CTkMessagebox.CTkMessagebox(title="ERROR",message="There is some error please put the link correctly",option_1='ok',icon="cancel")
        else:
            CTkMessagebox.CTkMessagebox(master=self.root,title="error",message="please input all the requirement",option_1="ok",icon='cancel')
window = ctk.CTk()
window.resizable(True,True)
window.geometry("720x400")
ctk.set_appearance_mode("dark")
APP = app(window)

window.mainloop()
