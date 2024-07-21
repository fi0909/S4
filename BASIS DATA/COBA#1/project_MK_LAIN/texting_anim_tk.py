from tkinter import *
import threading
import time
import pygame
root = Tk()

pygame.mixer.init()
def audio1():
    pygame.mixer.music.load("COBA#1/project_MK_LAIN/sound1.mp3")
    pygame.mixer.music.play(loops=0)
def audio2():
    pygame.mixer.music.load("COBA#1/project_MK_LAIN/sound2.mp3")
    pygame.mixer.music.play(loops=0)
def audio3():
    pygame.mixer.music.load("COBA#1/project_MK_LAIN/sound3.mp3")
    pygame.mixer.music.play(loops=0)

global con
global txt 
global index
global dict_info
global dict_name
global count
txt = ""
dict_name = dict(name = "luthfi", ig="@vxyzuc", youtube = "https://www.youtube.com/@vxyzuc")
dict_info = []
for x in dict_name.keys():
    dict_info.append(x)
count = 0
index = 0
con = True
def typed_text():
    global con
    global txt 
    global index
    global dict_info
    global dict_name
    global count
    if con is True:
        txt = dict_name[dict_info[count]]
        teks.set(txt[:index]+"|")
        index += 1
        if index >= len(txt):
            con = False
        else:
            pass

        root.after(100,typed)
    else:
        teks.set(txt[0:index]+"|")
        index -= 1
        if index <= 0:
            con = True
            index = 0
            count += 1
            if count > len(dict_info)-1:
                count = 0
        else:
            pass
        root.after(100,typed)
def typed():
    root.after(100,typed_text)
    

def condition_of_text(con,txt,number):
    if con is False:
        root.after(100,typed_text(con,txt,number))
    else:
        root.after(100,typed_text(con,txt,number))
        
root.geometry("800x100")
root.configure(background="green")
teks = StringVar()

label_nama = Label(root,textvariable=teks,font=("arial",32),background="green",fg="white")
label_nama.pack()
root.after(100,typed)



root.mainloop()
