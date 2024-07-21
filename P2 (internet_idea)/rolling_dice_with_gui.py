#libary used
import random as rd
import tkinter as tk
import threading
from tkinter import Text, messagebox as msgbx
from tkinter.ttk import Style

#variabel
total_pointget1 = 0
total_pointget2 = 0
temp_point1 = 0
temp_point2 = 0
current_dice = []
player1_dice =[]
player2_dice =[]
dice_list = [1,2,3,4,5,6]
using_dice = 2
player1_con = 0
player2_con = 0
#function
def rolling_dice(dl):
    return rd.choices(dl)

def change_player1():
    global player1_con
    global player2_con
    player1_con = 1
    player2_con = 0
    return player1_con,player2_con
def change_player2():
    global player1_con
    global player2_con
    player2_con = 1
    player1_con = 0
    return current_dice,player2_con,player1_con
def button_pressed1(player1_con):
    global current_dice
    global player1_dice
    temp_dice = []
    current_dice = []
    if player1_con == 1:
        msgbx.showerror("error","Please change the player")
        return 0
    for i in range (using_dice):
        dice = rolling_dice(dice_list)
        temp_dice.append(dice)
    current_dice.extend(temp_dice)
    player1_dice.extend(current_dice)
    temp_point1 = calculate(current_dice)
    total_pointget1 = calculate(player1_dice)
    player1.set("point get from rolled: {}".format(str(temp_point1)))
    player1_point.set("total point : {}".format(str(total_pointget1)))
    change_player1()
    if total_pointget1 >= 100:
        msgbx.showinfo("WINNER","CONGRATS you win player 1\ntotal point you get: {}".format(total_pointget1))
        exit()
    return player1_dice, current_dice,temp_point1,total_pointget1

def button_pressed2(player2_con):
    temp_dice = []
    current_dice = []
    if player2_con == 1:
        msgbx.showerror("error","Please change the player")
        return 0
    for i in range (using_dice):
        dice = rolling_dice(dice_list)
        temp_dice.append(dice)
    current_dice.extend(temp_dice)
    player2_dice.extend(current_dice)
    temp_point2 = calculate(current_dice)
    total_pointget2 = calculate(player2_dice)
    player2.set("Point get from rolled {}".format(str(temp_point2)))
    player2_point.set("total point: {}".format(str(total_pointget2)))
    change_player2()
    if total_pointget2 == 100:
        msgbx.showinfo("WINNER","CONGRATS you win player 2\ntotal point you get: {}".format(total_pointget2))
        exit()
    return player2_dice, current_dice,temp_point2,total_pointget2    

def main1():
    button_pressed1(player1_con)
def main2():
    button_pressed2(player2_con)
def calculate(arr):
    jum = 0
    for i, in arr:
        jum += i
    return (jum)
def see_dice():
    if player1_con == 1:
        msgbx.showinfo("dice rolled","your dice rolled: {}\noverall dice rolled: {}".format(current_dice,player1_dice))
    else:
        msgbx.showerror("error","you must roll first")
    return 0
#window
window = tk.Tk()
window.title("ROLLING DICE GAME")
window.resizable(height=True,width=True)
window.geometry("1000x1000")
window.columnconfigure([1,2],minsize=5,weight=1)
window.rowconfigure([1,2],minsize=5,weight=1)
window.grid()

#player1 variable
player1 = tk.StringVar()
player1.set("point get from rolled: {}".format(str(temp_point1)))
player1_point= tk.StringVar()
player1_point.set("Total point: {}".format(str(total_pointget1)))

#player2 variable
player2 = tk.StringVar()
player2.set("Point get from rolled: {}".format(str(temp_point2)))
player2_point= tk.StringVar()
player2_point.set("total point get: {}".format(str(total_pointget2)))
#header
header_label = tk.Label(master=window,text="Welcome to dice rolling game\nthe first one to get 100 point is the winner",font=("arial",18))
header_label.grid(row=1,column=1,columnspan=2,sticky=tk.W+tk.E)

#player1_content
frame1 = tk.Frame(master=window)
frame1.rowconfigure([1,2,3],minsize=5,weight=1)
frame1.columnconfigure([1,2],minsize=5,weight=1)
frame1.grid(row=2,column=1,sticky='ew')
player1_label = tk.Label(master=frame1,bg="white",text="player1",font=("arial",28),justify="left")
player1_label.grid(row=1,column=1,columnspan=2,sticky=tk.W+tk.E)
label1 = tk.Label(master=frame1,textvariable=player1,font=("arial",18),justify="left")
label1.grid(row=2,column=1)
total_point1 = tk.Label(master=frame1,textvariable=player1_point,font=("arial",18),justify="right")
total_point1.grid(row=2,column=2)
player1_button = tk.Button(master=frame1,justify="center",text="roll",command= lambda: threading.Thread(target=main1).start()) 
player1_button.grid(row=3,column=1,sticky='ew')
player1_button2 = tk.Button(master=frame1,justify="center",text="see collected dice",command=lambda: threading.Thread(target=see_dice).start())
player1_button2.grid(row=3,column=2,sticky='ew')


#player2_content
frame2 = tk.Frame(master=window)
frame2.rowconfigure([1,2,3],minsize=5,weight=1)
frame2.columnconfigure([1,2],minsize=5,weight=1)
frame2.grid(row=2,column=2,sticky='ew')
player2_label = tk.Label(master=frame2,bg="white",text="player2",font=("arial",28),justify="left")
player2_label.grid(row=1,column=1,columnspan=2,sticky=tk.W+tk.E)
label2 = tk.Label(master=frame2,textvariable=player2,font=("arial",18),justify="left")
label2.grid(row=2,column=1)
total_point2 = tk.Label(master=frame2,textvariable=player2_point,font=("arial",18),justify="right")
total_point2.grid(row=2,column=2)
player2_button = tk.Button(master=frame2,justify="center",text="roll",command= lambda: threading.Thread(target=main2).start())
player2_button.grid(row=3,column=1,sticky='ew')
player2_button = tk.Button(master=frame2,justify="center",text="see collected dice")
player2_button.grid(row=3,column=2,sticky='ew')


#execute
window.mainloop()


#status : complete