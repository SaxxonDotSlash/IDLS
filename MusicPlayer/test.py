from tkinter import *

test = Tk()

img = PhotoImage(file='MusicPlayer\Assets\stopButton.png')
testbutton = Button(test, image=img, borderwidth=0, command=print("stopped")).pack()

test.mainloop()