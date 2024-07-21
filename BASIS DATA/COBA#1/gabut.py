import tkinter as tk
import string
import random as rd


def checker():
    for i in root.winfo_children():
        if "label" in i.winfo_name():
            i.destroy()
    a = ent1.get()
    strength = [0,0,0,0] #first for lower, second for upper, third for digit, last for symbol
    if len(a)>=8:
        for char in a:
            if char in string.ascii_lowercase:
                strength[0] += 1 
            if char in string.ascii_uppercase:
                strength[1] += 1
            if char in string.digits:
                strength[2] += 1
            if char in string.punctuation:
                strength[3] += 1
        if strength[0] != 0 and strength[1] != 0 and strength[2] != 0 and strength[3] != 0:
            # kode diatas dapat dipersingkat dengan 'if 0 not in strength:'
            lbl_scd = tk.Label(root,text="password is strong",foreground="green")
            lbl_scd.pack()
            print(a+" the password is meet the strong requirement")
        else:
            for i in range(len(strength)):
                if strength[i] == 0:
                    if i == 0:
                        lbl_l_case = tk.Label(root,text="Please use lower case",foreground="red").pack()
                        print("please use lower case")
                    if i == 1:
                        lbl_u_case = tk.Label(root,text="Please use Upper case",foreground="red").pack()
                        print("please use upper case")
                    if i == 2:
                        lbl_d_case = tk.Label(root,text="Please use digit",foreground="red").pack()
                        print("please use digits")
                    if i == 3:
                        lbl_s_case = tk.Label(root,text="Please use symbol",foreground="red").pack()
                        print("please use sysmbol")
    else:
        lbl_err = tk.Label(root,text="use 8 character",foreground="red")
        lbl_err.pack()
def random_generate():
    size = 8
    lower = rd.choice(string.ascii_lowercase)
    upper = rd.choice(string.ascii_uppercase)
    digits = rd.choice(string.digits)
    symbol = rd.choice(string.punctuation)
    combined = lower + upper + digits + symbol
    chars = string.ascii_lowercase+string.ascii_uppercase+string.digits+string.punctuation
    text = "".join(rd.choice(chars) for i in range(4))
    final = list(text+combined)
    rd.shuffle(final)
    f_text = "".join(final)
    ent1.delete(0,tk.END)
    ent1.insert(0,f_text)
    checker()
root = tk.Tk()
ent1 = tk.Entry(root,)
ent1.pack()
btn1 = tk.Button(root,text="check",command=checker)
btn1.pack()
btn2 = tk.Button(root,text="generate_pass",command=random_generate)
btn2.pack()
root.mainloop()


