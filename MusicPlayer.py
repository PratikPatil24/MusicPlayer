import os
from tkinter.filedialog import askopenfilename

import pygame
from mutagen.id3 import ID3
import tkinter

root = tkinter.Tk()
root.minsize(300, 300)
root.title('Music Player')

listofsongs = []          # songs list
realnames = []            # For song title
number = 0                # for song number
state = 1                 # for play and pause
stop = 0                  # for stop

v = tkinter.StringVar()                                         # for highlighting the current song
songlabel = tkinter.Label(root, textvariable=v, width=50)


def songchooser():
    file = askopenfilename()

    if file.endswith(".mp3"):
        realdir = os.path.realpath(file)
        audio = ID3(realdir)
        realnames.append(audio['TIT2'].text[0])
        listofsongs.append(file)

    if state == 1:
        pygame.mixer.init()
        pygame.mixer.music.load(listofsongs[0])
        pygame.mixer.music.play()


songchooser()

listbox = tkinter.Listbox(root)
listbox.pack()

realnames.reverse()
for items in realnames:
    listbox.insert(0, items)


def updatelabel():
    global number
    global songname
    v.set(realnames[number])
    return songname


def nextsong(event):
    global number
    number += 1
    pygame.mixer.music.load(listofsongs[number])
    pygame.mixer.music.play()
    updatelabel()


def prevsong(event):
    global number
    number -= 1
    pygame.mixer.music.load(listofsongs[number])
    pygame.mixer.music.play()
    updatelabel()


def stopsong(event):
    global stop
    stop = 1
    pygame.mixer.music.stop()
    v.set("")


def playsong(event):
    if stop == 1:
        pygame.mixer.music.load(listofsongs[number])
        pygame.mixer.music.play()

    pygame.mixer.music.unpause()



def pausesong(event):
    pygame.mixer.music.pause()


def addsong(event):
    file = askopenfilename()

    if file.endswith(".mp3"):
        realdir = os.path.realpath(file)
        audio = ID3(realdir)
        realnames.append(audio['TIT2'].text[0])
        listofsongs.append(file)

        listbox.delete(0, tkinter.END)          #deleting previous entries in listbox and adding all back
        for items in realnames:
            listbox.insert(0, items)


realnames.reverse()
addbutton = tkinter.Button(root, text='Add song')
addbutton.pack()

stopbutton = tkinter.Button(root, text='Stop')
stopbutton.pack()

playbutton = tkinter.Button(root, text='Play')
playbutton.pack()

pausebutton = tkinter.Button(root, text='Pause')
pausebutton.pack()

nextbutton = tkinter.Button(root, text='Next Song')
nextbutton.pack()

previousbutton = tkinter.Button(root, text='Previous Song')
previousbutton.pack()

addbutton.bind("<Button-1>", addsong)
stopbutton.bind("<Button-1>", stopsong)
playbutton.bind("<Button-1>", playsong)
pausebutton.bind("<Button-1>", pausesong)
nextbutton.bind("<Button-1>", nextsong)
previousbutton.bind("<Button-1>", prevsong)

songlabel.pack()

root.mainloop()
