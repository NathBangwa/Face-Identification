from tkinter import *

import os



def change_interface():
    global Canvas, window


    image_file = "C:\\Users\\RMB PC\\Documents\\PROJECTS\\Face-Identification\\samples\\capture.png"#os.path.join(config.samples_folder, infos[0]+'.jpg')
    print(os.path.isfile(image_file))
    img = PhotoImage(file=image_file)
    can.create_window(0,0, window=window, anchor='nw')
    
root = Tk()
can = Canvas(width=500, height=500, bg='red')
can.pack()
image_file = "C:\\Users\\RMB PC\\Documents\\PROJECTS\\Face-Identification\\samples\\capture.png"#os.path.join(config.samples_folder, infos[0]+'.jpg')
print(os.path.isfile(image_file))
img = PhotoImage(file=image_file)
window = Label(image=img)
imageid=can.create_window(0,0, window=window, anchor='nw')
change_interface()
root.mainloop()