# Import the PIL and tkinter modules
from PIL import Image, ImageTk
import tkinter

# Open the JPEG image using PIL
image = Image.open("circleIcon.jpg")

# Convert the image to a PhotoImage object
photo = ImageTk.PhotoImage(image)

# Create a top-level window
root = tkinter.Tk()

# Add the image to the window using a label widget
label = tkinter.Label(root, image=photo)
label.pack()

# Start the event loop
root.mainloop()




''''
#Tkinter File Browser and selection

from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image



root = Tk()
root.title("File Browser")
root.geometry("500x400")

#create a variable to store an image
my_image = None


def open():
    global my_image
    root.filename = filedialog.askopenfilename(initialdir="C:/Users/James/Desktop/Code/MusicPlayer", title="Select A File", filetypes=(("png Files", "*.png"), ("jpg Files", "*.jpg")))
    my_label = Label(root, text=root.filename).pack()
    #set my_image to the image
    my_image = Image.open(root.filename)
    my_image_label = Label(image=my_image).pack()

def convert():
    global my_image
    my_image = my_image.convert('RGB')
    my_image.save('C:/Users/James/Desktop/Code/MusicPlayer/Assets/stopButton.png', 'png')

my_btn = Button(root, text="Open File", command=open).pack()
convert_btn = Button(root, text="Convert to PNG", command=convert).pack()

root.mainloop()
'''