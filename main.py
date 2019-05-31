import config

import cv2

import logical


"""image = cv2.imread(config.car_image)

prediction = logical.predict_face(image)

print("prediction : ", prediction)"""

from tkinter import *
import cv2

from PIL import ImageTk

import os

import json

#img_default = PhotoImage(config.car_image)

def get_infos(userid):
    with open(config.database) as fp:
        data = json.load(fp)
    
    return data[userid.upper()]

def update_status(userid):
    with open(config.database) as fp:
        data = json.load(fp)
    status = data[userid.upper()][5]

    if status == "OUTDOOR":
        status = "INDOOR"
    else:
        status = "OUTDOOR"
    data[userid.upper()][5] = status

    data = json.dumps(data)

    with open(config.database, 'w') as fp:
        fp.write(data)



class UserInterface(Tk):
    TITLE = "INFORMATIONS"
    INFOS = [
        "MATRICULE",
        "NOM",
        "POST-NOM",
        "PRENOM",
        "GENRE",
        "STATUS"
    ]


    def __init__(self):
        Tk.__init__(self)
        
        self.canvas = Canvas(self, height=config.g_height,
                                width=config.g_width,
                                )#bg='blue')
        self.canvas.pack()
        
        self.titleid = self.canvas.create_text(
                                            config.t_x,
                                            config.t_y,
                                            text = self.TITLE
        )
        image_file = "C:\\Users\\RMB PC\\Documents\\PROJECTS\\Face-Identification\\samples\\gif.gif"#os.path.join(config.samples_folder, infos[0]+'.jpg')
        print(os.path.isfile(image_file))
        img = PhotoImage(file=image_file)
        
        self.textid = self.canvas.create_text(
                                            config.inf_x,
                                            config.inf_y,
                                            text="")
        #self.label = Label()
        #self.labelid = self.canvas.create_window(100, 100, window=self.label)
        self.change_view(userid=None)
    
    def change_view(self, userid=None):
        display_image = True
        if not userid:
            infos = ['...'] * len(self.INFOS)
            display_image = False
        
        else:
            update_status(userid=userid)
            infos = get_infos(userid=userid)
        
        infos_all = zip(self.INFOS, infos)

        funct = lambda tup_inf: f"{tup_inf[0]} : {tup_inf[1]}"

        infos_all = map(funct, infos_all)

        infos_all = list(infos_all)

        infos_str = "\n".join(infos_all)

        self.canvas.itemconfig(self.textid, text=infos_str)

        # image update
        if display_image:
            print("down")
            image_file = "C:\\Users\\RMB PC\\Documents\\PROJECTS\\Face-Identification\\samples\\Capture.png"#os.path.join(config.samples_folder, infos[0]+'.jpg')
            img = PhotoImage(file=image_file)
            
        

gui = UserInterface()
infos = ['16AM003', gui.INFOS[1:]]
gui.change_view(userid='16AM003')
gui.mainloop()


