from tkinter import *
import time

def clicked():
    global current_text
    global delete_index
    global is_typing
    text_to_type = username.get()
    if not is_typing:
        is_typing = True
        current_text = text_to_type
        delete_index = len(text_to_type)
        type_and_delete()

def type_and_delete():
    global delete_index
    global current_text
    global is_typing
    if delete_index >= 0:
        tkstring.set(current_text[:delete_index])
        delete_index -= 1
        window.after(100, type_and_delete)
    else:
        is_typing = False
        window.after(1000, type_text)

def type_text():
    global current_text
    global is_typing
    if current_text:
        char = current_text[0]
        tkstring.set(tkstring.get() + char)
        current_text = current_text[1:]
        window.after(100, type_text)
    else:
        window.after(1000, clicked)

def clear():
    global is_typing
    is_typing = False
    for i in window.winfo_children():
        if "label" in str(i).lower():
            i.destroy()
    button_hello.config(state=NORMAL)

window = Tk()

window.geometry("800x600")
username = StringVar()
tkstring = StringVar()
label = Label(window,text="hello world",textvariable=username).pack()
label_txt = Label(window,textvariable=tkstring).pack(pady=5)
entry = Entry(window,textvariable=username).pack(pady=5)
button_hello = Button(window,text="click me",command=clicked)
button_hello.pack(pady=5)
button_clear = Button(window,text="clear_text",command=clear)
button_clear.pack(pady=5)

is_typing = False
current_text = ""
delete_index = 0

window.mainloop()
