import random as rd
# dice versus game
person1 = []
person2 = []
player1 = 0
player2 = 0 
current_dice = []
dice_list = [1,2,3,4,5,6]
dice_value = 0
def rolling_dice(a):
    return rd.choices(a)
def change_player_con(confirm,player1,player2):
    if confirm == "1":
        player1 = 1
        player2 = 0
        return player1,player2
    elif confirm =="2":
        player1 = 0
        player2 = 1
        return player1,player2
    return 0
def player(p1,p2,confirm,dv,dl):
    dice_get = []
    if confirm == "1" and p1 == 0:
        for i in range (dv):
            dice = rolling_dice(dl)
            dice_get.append(dice)
        return current_dice.extend(dice_get)
    elif confirm == "2" and p2==0:
        for i in range (dv):
            dice = rolling_dice(dl)
            dice_get.append(dice)
        return current_dice.extend(dice_get)
    elif confirm == "x":
        exit()
    elif confirm == "1" or confirm == "2":
        if p1 == 1 or p2 == 1:
            print("Change The Player !!!")
    else:
        print("type was not recognized")
def calculate(arr):
    jumlah = 0
    for i, in arr:
        jumlah = jumlah + i
    return (jumlah)
print("welcome to dice versus game !!!!!!")
print("1 vs 1 player model")
print("test your luck in this game")
print("the first one to go to 100 point is the winner")
dice_value = int(input("how much dice you want to use?"))
print("NOTE:\n"+"start>>> frist type this to start the game\n"+"p1>>>type p1 to start the player1\n"+"p2>>>>type this to start dice on p2\n"+"x>>>type this to exit\n")
start = input("type start to start: ")
while start == "start":
    confirm = input("player1/2(input 1/2): ")
    player(p1=player1,p2=player2,confirm=confirm,dv=dice_value,dl=dice_list)
    player1, player2 = change_player_con(confirm,player1,player2) # type: ignore 
    if player1 == 1:
        player2 = False
        print("you rolled up",current_dice)
        print("point it get:",calculate(current_dice))
        person1.extend(current_dice)
        current_dice = []
        print("your total point",calculate(person1))
    elif player2 == 1 :
        print("you rolled up:",current_dice)
        print("point it get",current_dice)
        person2.extend(current_dice)
        current_dice = []
        print("total point: ",calculate(person2))
    value1 = int(calculate(person1))
    value2 = int(calculate(person2))
    if value1 >= 100:
        print("the winner is player 1")
        print("dice rolled: ",person1)
        print("the total dice rolled:",len(person1))
        break
    elif value2 >= 100:
        print("the winner is player2")
        print("dice rolled: ",person2)
        print("the total dice rolled:",len(person1))
        break
    
# status : done
# next : fight with dice ?
