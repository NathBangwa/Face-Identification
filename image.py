from tkinter import *

import os
from PIL import ImageTk


def change_interface(canv):

    image_file = "C:\\Users\\RMB PC\\Documents\\PROJECTS\\Face-Identification\\samples\\capture.png"#os.path.join(config.samples_folder, infos[0]+'.jpg')
    print(os.path.isfile(image_file))
    img = ImageTk.PhotoImage(file=image_file)
    window = Label(image=img)
    #window.config(image=img)
    imageid=canv.create_window(0,0, window=window, anchor='nw')

root = Tk()
can = Canvas(width=500, height=500, bg='red')
can.pack()
image_file = "C:\\Users\\RMB PC\\Documents\\PROJECTS\\Face-Identification\\samples\\gif.gif"#os.path.join(config.samples_folder, infos[0]+'.jpg')
print(os.path.isfile(image_file))
img = ImageTk.PhotoImage(file=image_file)
window = Label(image=img)
#paned.add(window)
#imageid=can.create_window(0,0, window=window, anchor='nw')
can.create_image(0,0, image=img)
#change_interface(can)
root.mainloop()