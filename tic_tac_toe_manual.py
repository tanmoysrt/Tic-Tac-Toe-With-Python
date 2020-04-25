# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 09:54:12 2020

@author: Tanmoy
"""
from tkinter import *
import tkinter.messagebox
player_no=0 # 0 for player1 & 1 for player2
count=0
def play(i):
    global player_no,count
    if i['text']==' ':
        if player_no==0:
            i['text']='O'
            player_no=1
            label['text']="Active Player: {}".format(getPlayerName())
            checkWin()
        elif player_no==1:
            i['text']='X'
            player_no=0
            label['text']="Active Player: {}".format(getPlayerName())
            checkWin()
        count+=1
    else:
        tkinter.messagebox.showinfo("Tic Tac Toe in Python",'Button is Already Clicked')
    

def checkWin():
    if (button1['text']==button2['text']==button3['text']=='X' or
        button4['text']==button5['text']==button6['text']=='X' or
        button7['text']==button8['text']==button9['text']=='X' or
        button1['text']==button4['text']==button7['text']=='X' or
        button2['text']==button5['text']==button8['text']=='X' or
        button3['text']==button6['text']==button9['text']=='X' or
        button1['text']==button5['text']==button9['text']=='X' or
        button3['text']==button5['text']==button7['text']=='X'):
        tkinter.messagebox.showinfo("Tic Tac Toe in Python",'Player2 Wins')
        restart()
    elif(button1['text']==button2['text']==button3['text']=='O' or
        button4['text']==button5['text']==button6['text']=='O' or
        button7['text']==button8['text']==button9['text']=='O' or
        button1['text']==button4['text']==button7['text']=='O' or
        button2['text']==button5['text']==button8['text']=='O' or
        button3['text']==button6['text']==button9['text']=='O' or
        button1['text']==button5['text']==button9['text']=='O' or
        button3['text']==button5['text']==button7['text']=='O'):
        tkinter.messagebox.showinfo("Tic Tac Toe in Python",'Player1 Wins')
        restart()
    
    elif count==8:
        tkinter.messagebox.showinfo("Tic Tac Toe in Python",'Game Ties')
        restart()

def restart():
    global count,player_no
    button1['text']= button2['text']= button3['text']= button4['text']= button5['text']= button6['text']= button7['text']= button8['text']= button9['text']=' '
    count=0
    player_no=0
    label['text']="Let's Start : Player1"

def getPlayerName():
    global player_no
    if player_no==0:
        return 'Player1'
    elif player_no==1:
        return 'Player2'
screen=Tk()
screen.title("Tic Tac Toe in Python")
label = Label(screen, 
		 text="Let's Start : Player1",
		 fg = "orange",
		 bg = "yellow",
		 font = "Times 16 bold italic")
label.grid(row=0,columnspan=3)
button1 = Button(screen, text=' ', font='Times 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: play(button1))
button2 = Button(screen, text=' ', font='Times 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: play(button2))
button3 = Button(screen, text=' ', font='Times 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: play(button3))
button4 = Button(screen, text=' ', font='Times 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: play(button4))
button5 = Button(screen, text=' ', font='Times 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: play(button5))
button6 = Button(screen, text=' ', font='Times 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: play(button6))
button7 = Button(screen, text=' ', font='Times 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: play(button7))
button8 = Button(screen, text=' ', font='Times 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: play(button8))
button9 = Button(screen, text=' ', font='Times 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: play(button9))
button1.grid(row=1, column=0)
button2.grid(row=1, column=1)
button3.grid(row=1, column=2)
button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)
button7.grid(row=3, column=0)
button8.grid(row=3, column=1)
button9.grid(row=3, column=2)
screen.mainloop()