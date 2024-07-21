import random as rd
import tkinter as tk
import tkinter.ttk as ttk
def start_game():
    pass


root = tk.Tk()
root.geometry("500x500")
root.maxsize(500,500)
root.minsize(500,500)
boss = tk.IntVar()
boss.set(100)

lbl1 = tk.Label(root,text="DEFEAT THE BOSS",foreground="red",font=("arial",18,"bold"))
lbl1.pack()

bar = ttk.Progressbar(root,variable=boss)
bar.pack()

def hit():
    boss.set(boss.get()-10)
btn = tk.Button(root,text="HIT",command=hit)
btn.pack()
root.mainloop()

