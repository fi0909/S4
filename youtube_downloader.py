#libary used in this project
import tkinter as tk
from pytube import YouTube
from tkinter.filedialog import askdirectory
import threading
import tkinter.messagebox
from pytube.cli import on_progress
from pytube import Playlist
from tkinter import  ttk

#to do list: - make progress bar
# Make Button function
def update_progressbar(stream,chunk,bytes_remaining):
    progress = int(((stream.filesize-bytes_remaining)/stream.filesize)*100)
    progress_var.set(progress)

def mix_downloader():
    try:
        link=user_input.get()
        youtube = YouTube(link,on_progress_callback=update_progressbar) 
        tkinter.messagebox.showinfo("info","title: "+youtube.title+"\nauthor: "+youtube.author)
        strm = youtube.streams.get_highest_resolution()
        filename=askdirectory()
        #make the progress bar
        progress_bar =ttk.Progressbar(master=main_content_frame,orient='horizontal',length=200,mode="determinate",variable=progress_var)
        progress_bar.grid(row=4,column=0,columnspan=3,sticky=tk.W+tk.E)
        if strm is not None : strm.download(str(filename))
        tkinter.messagebox.showinfo("","its done")
    except:
        tkinter.messagebox.showinfo("error","configuration failed")
        if user_input.get() == "":
            tkinter.messagebox.showinfo(None,"put link first")
def audio_downloader():
    try:
        link=user_input.get()
        youtube = YouTube(link,on_progress_callback=update_progressbar)
        tkinter.messagebox.showinfo("info","title: "+youtube.title+"\nauthor: "+youtube.author)
        strm = youtube.streams.get_audio_only()
        filename=askdirectory()
        #make the progress bar
        progress_bar =ttk.Progressbar(master=main_content_frame,orient='horizontal',length=200,mode="determinate",variable=progress_var)
        progress_bar.grid(row=4,column=0,columnspan=2,sticky=tk.W+tk.E)
        if  strm is not None: strm.download(str(filename))
        tkinter.messagebox.showinfo("","its done")
    except Exception as e:
        tkinter.messagebox.showinfo("error","configuration failed {}".format(str(e)))
        if user_input.get() == "":
            tkinter.messagebox.showinfo(None,"put link first")
def video_downloader():
    try:
        link=user_input.get()
        youtube = YouTube(link,on_progress_callback=update_progressbar)
        tkinter.messagebox.showinfo("info","title: "+youtube.title+"\nauthor: "+youtube.author)
        strm = youtube.streams.filter(adaptive=True,only_video=True).first()
        filename=askdirectory()
        #make the progress bar
        progress_bar =ttk.Progressbar(master=main_content_frame,orient='horizontal',length=200,mode='determinate',variable=progress_var)
        progress_bar.grid(row=4,column=0,columnspan=3,sticky='ew')
        if strm is not None: strm.download(str(filename))
        tkinter.messagebox.showinfo("","its done")
    except:
        tkinter.messagebox.showinfo("error","configuration failed")
        if user_input.get() == "":
            tkinter.messagebox.showinfo(None,"put link first")

def playlist_downloader():
    try:
        if playlist_con.get() == "yes":
            link = playlist_link.get()
            p = Playlist(link)
            filename = askdirectory()
            for video in p.video_urls:
                yt = YouTube(video,on_progress_callback=update_progressbar) #type: ignore
                yd = yt.streams.get_highest_resolution()
                #make the progress bar
                label_downloader = tk.Label(master=main_content_frame,textvariable=video,font=("arial", 14),bg='white')
                label_downloader.grid(row=4,column=3,sticky='ew')
                progress_bar =ttk.Progressbar(master=main_content_frame,orient='horizontal',length=200,mode="determinate",variable=progress_var)
                progress_bar.grid(row=4,column=0,columnspan=3,sticky=tk.W+tk.E)
                if yd is not None: yd.download(str(filename))
        elif playlist_con.get() == "no":
            link = playlist_link.get()
            p = Playlist(link)
            filename = askdirectory()
            for video in p.video_urls:
                print(video)
                yt = YouTube(video,on_progress_callback=update_progressbar)#type: ignore
                #make the progress bar
                yd = yt.streams.get_audio_only()
                label_downloader = tk.Label(master=main_content_frame,textvariable=video,font=("arial", 14),bg='white')
                label_downloader.grid(row=4,column=3,sticky='ew')
                progress_bar =ttk.Progressbar(master=main_content_frame,orient='horizontal',length=200,mode="determinate",variable=progress_var)
                progress_bar.grid(row=4,column=0,columnspan=3,sticky=tk.W+tk.E)
                if yd is not None: yd.download(str(filename))
        else:
            tkinter.messagebox.showerror("error","Please input video condition")
    except:
        tkinter.messagebox.showerror("erorr","the link you put is not recognized as youtube link or the video link is broken")

#MAKE THE GUI
window = tk.Tk()
window.title("youtube downloader")
window.resizable(width=True,height=True)
window.geometry("1280x720")

#user variable
user_input = tk.StringVar()
playlist_con = tk.StringVar()
playlist_link = tk.StringVar()
progress_var = tk.DoubleVar()
progress_var.set(0.0)

#Bagian atas
header_frame = tk.Frame(master=window,bg="white",height=100,width=100)
header_frame.rowconfigure([0,1,2],minsize=5,weight=0)
header_frame.columnconfigure([0,1,2],minsize=5,weight=0)
header_frame.pack(expand=True,fill=tk.BOTH,side=tk.TOP)
label1= tk.Label(master=header_frame,text="welcome to youtube downloader",background='white',font=("arial",28),fg='red')
label1.grid(row=1,column=1,sticky="ew")

#Bagian isi
main_content_frame = tk.Frame(master=window,bg="white",height=500,width=500)
main_content_frame.rowconfigure([0,1,2,3,4],minsize=100,weight=0)
main_content_frame.columnconfigure([0,1,2,3],minsize=100,weight=0)
main_content_frame.pack(fill=tk.BOTH,side=tk.TOP,expand=True)

#First downlaod the video and audio
label2 = tk.Label(master=main_content_frame,text="Auto Download The Highest Quality",font="arial")
label2.grid(row=0,column=0,sticky='ew')
button1 = tk.Button(master=main_content_frame,text="DOWNLOAD",font="arial",command=lambda: threading.Thread(target=mix_downloader).start())
button1.grid(row=3,column=0,sticky='ew')


#second download the audio
label3=tk.Label(master=main_content_frame,text="Auto Download The Highest Audio Quality",font="arial")
button2=tk.Button(master=main_content_frame,text="AUDIO DOWNLOAD",font="arial",command=lambda:threading.Thread(target=audio_downloader).start())
link_entry2=tk.Entry(master=main_content_frame,textvariable=user_input,width=25,justify='center')
txt_link = tk.Label(master=main_content_frame,text="please put link below:",font=("arial",18),justify="center")
txt_link.grid(row=1,column=1,sticky="ew")
label3.grid(row=0,column=1,sticky="ew")
link_entry2.grid(row=2,column=1,sticky="ew")
button2.grid(row=3,column=1,sticky="ew")

#third download only the video
label4=tk.Label(master=main_content_frame,text="Auto Download The Highest video Quality",font="arial")
button3=tk.Button(master=main_content_frame,text="Video DOWNLOAD",font="arial",command=lambda: threading.Thread(target=video_downloader).start())
label4.grid(row=0,column=2,sticky="ew")
button3.grid(row=3,column=2,sticky="ew")

#playlist downloader
playlist_lbl = tk.Label(master=main_content_frame,text="Auto download Playlist",font="arial",bg="white")
playlist_lbl.grid(row=0,column=3,sticky='ew')
playlist_frame = tk.Frame(master=main_content_frame,bg="white")
playlist_frame.rowconfigure([1,2,3,4],minsize=100,weight=0)
playlist_frame.columnconfigure([1],minsize=100,weight=0)
playlist_frame.grid(row=1,column=3,rowspan=2,sticky=tk.W+tk.E)
playlist_ent = tk.Entry(master=playlist_frame,textvariable=playlist_link,justify="center")
playlist_ent.grid(row=2,column=1,sticky='ew')
playlist_ent2 = tk.Entry(master=playlist_frame,textvariable=playlist_con,justify="center")
playlist_ent2.grid(row=4,column=1,sticky='ew')
Playlist_lbl2 = tk.Label(master=playlist_frame,text="Put the link below",font="arial")
Playlist_lbl2.grid(row=1,column=1,sticky='ew')
Playlist_lbl3 = tk.Label(master=playlist_frame,text="With video: yes/no",font="arial")
Playlist_lbl3.grid(row=3,column=1,sticky='ew')
playlist_button = tk.Button(master=main_content_frame,text="download playlist",font="arial",command=lambda: threading.Thread(target=playlist_downloader).start())
playlist_button.grid(row=3,column=3,sticky='ew')

#Bagian bawah
footer_frame = tk.Frame(master=window,bg="white")
footer_frame.rowconfigure([0,1,2],minsize=10,weight=0)
footer_frame.columnconfigure([0,1,2],minsize=10,weight=0)
footer_frame.pack(fill=tk.BOTH,side=tk.TOP,expand=True)
label5 = tk.Label(master=footer_frame,text="Thank you for using this application",bg='white',font=("arial",18),fg="gray")
label5.grid(row=1,column=1,sticky='ew')
label_dev = tk.Label(master=footer_frame,text="for bug contact: "+"@vxyzuc",font=("arial",14),fg="gray",background='white').grid(row=2,column=1,sticky='ew')

window.mainloop()

