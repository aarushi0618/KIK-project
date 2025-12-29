from tkinter import *

root=Tk() #making a window
root.geometry("600x600")#window size
root.title("Tic Tac Toe")#title of window

frame1=Frame(root)#making a frame inside the window
frame1.pack()#packing thebframe to show it on the screen
titlelabel=Label(frame1,text="tic tac toe",font=("Arial", 30),fg="red",width=15) #giving a title to the frame1
titlelabel.grid(row=0,column=0)#ek hi frame mein grid and pack dono use nhi kar sakte
frame2=Frame(root)
frame2.pack()
turn="X"


board={1:" " ,2:" ",3:" ",
    4:" " ,5:" ",6:" ",
       7:" " ,8:" ",9:" "
       }#created a dictionary to store
def checkifwin(player):
  if(board[1]==board[2] and board[2]==board[3] and board[3]==player):
   return True
  elif(board[4]==board[5] and board[5]==board[6] and board[6]==player):
   return True
  elif(board[7]==board[8] and board[8]==board[9] and board[8]==player):
   return True
  elif(board[1]==board[5] and board[5]==board[9] and board[9]==player):
   return True
  elif(board[1]==board[4] and board[4]==board[7] and board[7]==player):
   return True
  elif(board[2]==board[5] and board[5]==board[8] and board[8]==player):
   return True
  elif(board[3]==board[6] and board[6]==board[9] and board[9]==player):
   return True
  elif(board[3]==board[5] and board[5]==board[7] and board[7]==player):
   return True
  else:
   return False
 
def minimax(board,isMaximizing):
  if checkifwin("o"):#if computer wins
    return 1
  if checkifwin("X"):#if user wins
    return -1
  if checkfordraw():#if computer wins
    return 0
  if isMaximizing:
    bestscore=-100# try to maximise so -1 theke kom likhbi as now computer is playing
  
    for keys in board.keys():
     if board[keys]==" ":
      board[keys]="o"#computer is playing as o
      score= minimax(board,False)#computer has already played now its user time to play so false dekhache and tai minimize korte parbe
      board[keys]=" "
      if score>bestscore:
        bestscore=score
    return bestscore
  else:
    bestscore=+100# try to minimise so +1 theke kom likhbi as now computer is playing
    
    for keys in board.keys():
     if board[keys]==" ":
      board[keys]="X"#computer is playing as o
      score= minimax(board,True)#computer has already played now its user time to play so false dekhache and tai minimize korte parbe
      board[keys]=" "
      if score<bestscore:
        bestscore=score
    return bestscore
 

def playComputer():
  bestscore=-100# try to maximise so -1 theke kom likhbi as now computer is playing
  bestmove=0
  for keys in board.keys():
    if board[keys]==" ":
      board[keys]="o"#computer is playing as o
      score= minimax(board,False)#computer has already played now its user time to play so false dekhache and tai minimize korte parbe
      board[keys]=" "
      if score>bestscore:
        bestscore=score
        bestmove=keys
  
  if bestmove!=0:
   board[bestmove]="o"
   buttons[bestmove-1].config(text="O")
   if checkifwin("o"):
            titlelabel.config(text="O wins the game", fg="green")
def restartgame():
  global turn
  turn = "X"#jate restart korar por x diye suru hoy
  for i in board.keys():
        board[i] = " "
  for button in buttons:
        button["text"] = " "
    # Reset the title label
  titlelabel.config(text="tic tac toe", fg="red")
def checkfordraw():
  for i in board.keys():
    if board[i] == " ":
      return False
  return True



def play(event):
    global turn#because we are changing the value of turn inside function permanently
    button =event.widget#identify which button was clicked i.e we extracted the button jisko click kiya and then uski property change kiya
    buttontext=str(button)
    clicked=buttontext[-1]#gives the last character of the string
    print(clicked)
    if(clicked=="n"):
       clicked=1
    else:
        clicked=int(clicked)

    if(button["text"]==" "):  #to avoid overwriting
       if turn=="X":
        button["text"]="X"
        board[clicked]=turn #updating the text inside the button
        output=checkifwin(turn)
        if(output ==True):
           titlelabel.config(text=f"{turn} wins the game", fg="green")
           
        if checkfordraw():
         titlelabel.config(text="It's a draw!", fg="orange")
         return
        turn="O"
        playComputer()
        turn="X"
       else:
        button["text"]="O"
        board[clicked]=turn
        output=checkifwin(turn)
        if(output ==True):
           titlelabel.config(text=f"{turn} wins the game", fg="green")
           return
        if checkfordraw():
         titlelabel.config(text="It's a draw!", fg="orange")
         print(board)
         return
        turn="X"
   
   
# tic tac toe board
button1=Button(frame2,text=" ",width=4,height=2,font={"Arial",30},bg="lightgrey",relief=RAISED,borderwidth=8)#making buttons inside frame2
button1.grid(row=0,column=0)
button1.bind("<Button-1>",play)
#The basic structure looks like this: button1.bind(event, function)

# Event: This is a string that describes what the user does (e.g., "<Button-1>" for a left-click, or "<Enter>" for moving the mouse over the button).

# Function: This is the name of the function (the "callback") that should execute when that event happens.

button2=Button(frame2,text=" ",width=4,height=2,font={"Arial",30},bg="lightgrey",relief=RAISED,borderwidth=8)#making buttons inside frame2
button2.grid(row=0,column=1)
button2.bind("<Button-1>",play)

button3=Button(frame2,text=" ",width=4,height=2,font={"Arial",30},bg="lightgrey",relief=RAISED,borderwidth=8)#making buttons inside frame2
button3.grid(row=0,column=2)
button3.bind("<Button-1>",play)

button4=Button(frame2,text=" ",width=4,height=2,font={"Arial",30},bg="lightgrey",relief=RAISED,borderwidth=8)#making buttons inside frame2
button4.grid(row=1,column=0)
button4.bind("<Button-1>",play)

button5=Button(frame2,text=" ",width=4,height=2,font={"Arial",30},bg="lightgrey",relief=RAISED,borderwidth=8)#making buttons inside frame2
button5.grid(row=1,column=1)
button5.bind("<Button-1>",play)

button6=Button(frame2,text=" ",width=4,height=2,font={"Arial",30},bg="lightgrey",relief=RAISED,borderwidth=8)#making buttons inside frame2
button6.grid(row=1,column=2)
button6.bind("<Button-1>",play)

button7=Button(frame2,text=" ",width=4,height=2,font={"Arial",30},bg="lightgrey",relief=RAISED,borderwidth=8)#making buttons inside frame2
button7.grid(row=2,column=0)
button7.bind("<Button-1>",play)

button8=Button(frame2,text=" ",width=4,height=2,font={"Arial",30},bg="lightgrey",relief=RAISED,borderwidth=8)#making buttons inside frame2
button8.grid(row=2,column=1)
button8.bind("<Button-1>",play)

button9=Button(frame2,text=" ",width=4,height=2,font={"Arial",30},bg="lightgrey",relief=RAISED,borderwidth=8)#making buttons inside frame2
button9.grid(row=2,column=2)
button9.bind("<Button-1>",play)

restartbutton=Button(frame1,text="Restart ",width=10,height=2,font={"Arial",30},bg="lightgrey",relief=RAISED,borderwidth=8,command=restartgame)#making buttons inside frame2
restartbutton.grid(row=1,column=0,columnspan=3,pady=10)
#command=restartgame calls the function
buttons=[button1,button2,button3,button4,button5,button6,button7,button8,button9] #list of buttons

root.mainloop()
