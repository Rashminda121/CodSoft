from tkinter import *
from PIL import Image,ImageTk # type: ignore
from random import randint


root = Tk()
root.title("Rock Paper Scissor Game")
root.configure(background="#5A639C")
root.geometry("920x450")
root.resizable(False, False) 



rock_img=ImageTk.PhotoImage(Image.open("rock.jpg").resize((210, 200), Image.LANCZOS))
paper_img=ImageTk.PhotoImage(Image.open("paper.jpg").resize((210, 200), Image.LANCZOS))
scissor_img=ImageTk.PhotoImage(Image.open("scissors.jpg").resize((210, 200), Image.LANCZOS))

user_label=Label(root,image=scissor_img)
comp_label=Label(root,image=scissor_img)
comp_label.grid(row=1, column=0,pady=10,padx=10)
user_label.grid(row=1, column=4,pady=10,padx=10)

#scores
playerScore=Label(root,text=0,font=100,bg="#5A639C",fg="white")
computerScore=Label(root,text=0,font=100,bg="#5A639C",fg="white")
computerScore.grid(row=1,column=1)
playerScore.grid(row=1,column=3)

#indicators
user_indicator=Label(root,font=50,text="USER",bg="#5A639C",fg="white")
comp_indicator=Label(root,font=50,text="COMPUTER",bg="#5A639C",fg="white")
user_indicator.grid(row=0,column=3,pady=10)
comp_indicator.grid(row=0,column=1,pady=10)


#messages
msg=Label(root,font=50,bg="#5A639C",fg="white",text="Welcome!!!")
msg.grid(row=3,column=2,pady=10)
msg2=Label(root,font=50,bg="#5A639C",fg="white",text="")
msg2.grid(row=4,column=2,pady=10)

#update message
def updateMessage(x):
    msg['text']= x

def updateMessage2(x):
    msg2['text']= x


reScore=0
matchWon = False

#update user score
def updateUserScore():
    global matchWon
    score= int(playerScore["text"])
    score +=1
    playerScore["text"]=str(score)
    if score==5:
        updateMessage("User Won!!!")
        updateMessage2("Play Again!")
        matchWon=True

    if matchWon==True:
        playerScore["text"]=str(reScore)
        computerScore["text"]=str(reScore)

    

#update computer score
def updateCompScore():
    global matchWon
    score= int(computerScore["text"])
    score +=1
    computerScore["text"]=str(score)
    if score==5:
        updateMessage("Computer Won!!!")
        updateMessage2("Play Again!")
        matchWon=True

    if matchWon==True:
        computerScore["text"]=str(reScore)
        playerScore["text"]=str(reScore)
        

#check winner
def checkWinner(player,computer):
    if player==computer:
        updateMessage("It's a Tie!!! ")
    elif player== "rock":
        if computer=="paper":
            updateMessage("You Loose!!!")
            updateCompScore()
        else:
            updateMessage("You Win!!!")
            updateUserScore()

    elif player=="paper":
        if computer=="scissor":
            updateMessage("You Loose!!!")
            updateCompScore()
        else:
            updateMessage("You Win!!!")
            updateUserScore()

    elif player=="scissor":
        if computer=="rock":
            updateMessage("You Loose!!!")
            updateCompScore()
        else:
            updateMessage("You Win!!!")
            updateUserScore()
    else:
        pass


choices=["rock","paper","scissor"]

def updateChoice(x):
    global matchWon
    matchWon=False
    updateMessage2("")

#computer
    compChoice=choices[randint(0,2)]

    if compChoice =="rock":
        comp_label.configure(image=rock_img)
    elif compChoice=="paper":
        comp_label.configure(image=paper_img)
    else:
        comp_label.configure(image=scissor_img)

#user 
    if x =="rock":
        user_label.configure(image=rock_img)
    elif x=="paper":
        user_label.configure(image=paper_img)
    else:
        user_label.configure(image=scissor_img)


    checkWinner(x,compChoice)   





rock=Button(root,width=20,height=2, text="ROCK", bg="#FF3E4D",command=lambda:updateChoice("rock")).grid(row=2,column=1,pady=10)
paper =Button(root,width=20,height=2, text="PAPER", bg="#FAD02E",command=lambda:updateChoice("paper")).grid(row=2,column=2)
scissor=Button(root,width=20,height=2, text="SCISSOR", bg="#0ABDE3",command=lambda:updateChoice("scissor")).grid(row=2,column=3)


root.mainloop()
