
#WAHAJ KHALIL

from tkinter import *

def callback(r,c):
    global winner
    global player
    if player == 'X' and states[r][c] == 0 and stop_game == False:
        b[r][c].configure(text = 'X' ,fg = "Blue",bg= 'White')
        states[r][c]='X'
        player = 'O'
        winner = "X"
    if player =='O' and states[r][c] ==0 and stop_game == False:
        b[r][c].configure(text = 'O',fg = "Orange",bg= 'Black')
        states[r][c]='O'
        player = 'X'
        winner = "O"
    check_for_winner()
    

def check_for_winner():
    global stop_game
    for i in range(3):
        if states[i][0]==states[i][1]==states[i][2]!=0:
            b[i][0].config(bg="Grey",fg='Red')
            b[i][1].config(bg="Grey",fg='Red') 
            b[i][2].config(bg="Grey",fg='Red')
            stop_game = True
            Label(window,text= "Player "+winner+" Win by rows",bg="Red").grid(row=6)
    for i in range(3):
        if states[0][i]==states[1][i]==states[2][i]!=0:
            b[0][i].config(bg="Grey")
            
            b[1][i].config(bg="Grey") 
            b[2][i].config(bg="Grey")
            stop_game = True
            Label(window,text= "Player "+winner+" Win by column ").grid(row =6)
            
            
        if states[0][0] ==states[1][1]==states[2][2]!=0:
            b[0][0].config(bg="Grey")
            b[1][1].config(bg="Grey")
            b[2][2].config(bg="Grey")
            stop_game = True
            Label(window,text= "PLayer "+winner+" Won Diagonally").grid(row=6)
        if states[2][0] ==states[1][1]==states[0][2]!=0:
            b[2][0].config(bg="Grey")
            b[1][1].config(bg="Grey")
            b[0][2].config(bg="Grey")
            Label(window,text="PLayer "+winner+" Won Diagonally",height=2,width=20,bg="Blue",fg="White").grid(row=6)
            stop_game = True
###################
info = Tk()
info.title("STRING")
info.geometry("300x300")
info.configure(background="Grey90")
info.resizable(0,0)


def Quit1():
   
    info.destroy()



def Rules():
    rules = Tk()
    rules.config(background="Grey90")
    rules.geometry("800x350")
    
    Label(rules, text="1. The game is played on a grid that's 3 squares by 3 squares",height = 2,bg ="Grey80").grid(sticky =W)#\n 2 : One player has X as his symbol and other players has O.\n 3 : First turn will be of Player X and the second turn will be of Player O and third turn will be of again of Player X and this sequence of turns will go on. \n 4 : The first player to get 3 of her marks in a row (up, down, across, or diagonally) is the winner./n 5 : When all 9 squares are marked, the game is over. If no player has 3 marks in a row, the game ends in a tie.").grid()
    Label(rules,text= "2 : One player has X as his symbol and other players has O.",height = 2,bg ="Grey80").grid(sticky = W)
    Label(rules,text= "3 : First turn will be of Player X and the second turn will be of Player O and third turn will be of again of Player X and this sequence of turns will go on.",height = 2,bg ="Grey80").grid(sticky = W)
    Label(rules,text= "4 : The first player to get 3 of her marks in a row (up, down, across, or diagonally) is the winner.",height  =2,bg ="Grey80").grid(sticky =W)
    Label(rules,text= "5 : When all 9 squares are marked, the game is over. If no player has 3 marks in a row, the game ends in a tie",height = 2,bg ="Grey80").grid(sticky = W)
    Label(rules,text ="TIP\n For quiting game at any moment, you can click EXIT or press Escape" ,bg ="Grey80").grid(column =0 ,sticky = W) 
    def Main_menu():
         rules.destroy()
    btn3 = Button(rules,text = "BACK TO MAIN MENU",command=Main_menu).grid(row = 7,pady = 20)
    
btn1= Button(info, text = "START GAME",command=Quit1,height = 4, width=15,bg="grey65",fg ="Black",font = ("Arial",10)).grid(row=1,column=0,padx=20,pady=10,sticky = NE)
btn2 = Button(info,text="INSTRUCTIONS",bg="Grey80",fg="Black",command=Rules,height = 4 ,width = 15,font=("Arial",10)).grid(row =2,column=0,padx =20 ,pady= 10,sticky=NE)
l1 =Label(info,text = "Welcome to Tic Tac Toe",font=("Times New Roman",15)).grid(row=0,padx = 10)
l2 =Label(info,text= "Created by Wahaj and Aiman",font=('Calibiri',10)).grid(sticky=W)



info.mainloop()
####################
window = Tk() #Progrossive Loop

window.title("Tic Tac Toe")


b = [[0,0,0],
     [0,0,0],
     [0,0,0]]


states = [[0,0,0],
          [0,0,0],
          [0,0,0]]

winner = 'X'

for i in range (3):
    for j in range (3):
        b[i][j] = Button(font=("Times New Roman",60),height =1
                         ,width = 5,bg = "SeaGreen1" ,
                         command = lambda r =i , c = j: callback(r,c))
        b[i][j].grid(row=i,column =j)



Label(window,text = "Player X",bg="Blue",fg="White",width = 15,height=2).grid(row=4,column=0)
Label(window,text = "Player O",bg="Black",fg="Orange",width=15,height=2).grid(row=4,column =2)



def Quit(event):    #for quiting whole game with escape key
    window.destroy()
def Quit2():
    window.destroy()  #for quittong with exit button


exit = Button(window,text="EXIT",bg = "Red",fg="Yellow",height =1, width =7,command= Quit2, font=("Times New Roman",20)).grid(row=5,column =1)

window.bind('<Escape>',Quit)
Label(window,text="No Winner Yet",bg="White" ,fg ="Red").grid(row=6)

player = 'X'

stop_game = False

mainloop()


