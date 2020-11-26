import webbrowser
import tkinter as tk 
from tkinter import *
import os
import json
import time
import sys
import random
import clipboard

with open("adres.json", "r") as jsonfile:
    ZOOM = json.load(jsonfile)

with open("sekme.json", "r") as jsonfile1:
    sekme = json.load(jsonfile1)
sekme = int(sekme)
root = Tk() 
reklamnumara = random.randint(1,3) 


    

# this is the function called when the button is clicked
def btnClickFunction():
    for count in range(sekme):
             time. sleep(1)
             webbrowser.open(ZOOM, new=0, autoraise=False)
             count =+ 1
             

def btnClickFunctionRESET():
    count = 0           

def siteac():
     webbrowser.open('takipsizad0.itch.io/zoom-spammer', new=0, autoraise=False)    
           

         
def btnClickFunctionSTOP():
    root.destroy()
    sys.exit
    exit()

def pixargonac():
    clipboard.copy("play.pixargon.net")  
    Label(root, text='linki kopyalandı 1.8 ile girebilirsiniz', bg='#F0F8FF', font=('arial', 12, 'normal')).place(x=90, y=225)


def kanalac():  
    webbrowser.open('https://www.youtube.com/channel/UCFQR58n1gs8cxmRWNNsCdGQ?view_as=subscriber', new=0, autoraise=False)      

if reklamnumara == 1:
     Button(root, text='linki kopyala ', bg='#F0F8FF', font=('arial', 12, 'normal'), command=pixargonac).place(x=200, y=245)
     Label(root, text='pixargonda uzay skyblock gibi özel ', bg='#F0F8FF', font=('arial', 12, 'normal')).place(x=90, y=280)
     Label(root, text=' oyun modları bulabilirsiniz', bg='#F0F8FF', font=('arial', 12, 'normal')).place(x=90, y=301)
 
if reklamnumara == 2:
     Button(root, text='kanalımı aç ', bg='#F0F8FF', font=('arial', 12, 'normal'), command=kanalac).place(x=200, y=245)
     Label(root, text='yapımcımın youtube kanalı ', bg='#F0F8FF', font=('arial', 12, 'normal')).place(x=90, y=280)

# This is the section of code which creates the main window
root.geometry('372x327')
root.configure(background='#F0F8FF')
root.title('ZOOM SPAMMER')


# This is the section of code which creates a button
Button(root, text='başla ', bg='#F0F8FF', font=('arial', 12, 'normal'), command=btnClickFunction).place(x=7, y=250)
Button(root, text='çıkış', bg='#F0F8FF', font=('arial', 12, 'normal'), command=btnClickFunctionSTOP).place(x=7, y=220)
Button(root, text='sıfırla ', bg='#F0F8FF', font=('arial', 12, 'normal'), command=btnClickFunctionRESET).place(x=7, y=282)
Label(root, text='yapımcım takipsizad', bg='#F0F8FF', font=('arial', 12, 'normal')).place(x=40, y=10)
Button(root, text='güncelle', bg='#F0F8FF', font=('arial', 12, 'normal'), command=siteac).place(x=7, y=100)
Label(root, text='sadece takipsizad0.itch.io da', bg='#F0F8FF', font=('arial', 12, 'normal')).place(x=90, y=100)


root.mainloop()



