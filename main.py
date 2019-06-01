
from tkinter import *
import config
import os
from PIL import ImageTk, Image
import socket
import logical

import json
from threading import Thread

#img_default = PhotoImage(config.car_image)

def pointer(event):
    chaine.configure(text = f"clic X = {event.x} Y = {event.y}")
    ui.change_infos('16AM003', False)
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


class Server:
    def __init__(self, ui):
        self.ui = ui
        connexion_principale = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        connexion_principale.bind((config.host, config.port))
        connexion_principale.listen(5)
        print("Le serveur {} écoute à présent sur le port {}".format(config.host, config.port))
        msg_recu = b""
        while msg_recu != b"fin":
            try:
                connexion_avec_client, infos_connexion = connexion_principale.accept()
                msg_recu = connexion_avec_client.recv(1024)
                
                idCard = msg_recu.decode('utf-8')
                idCard = idCard.strip().upper()

                image = logical.take_capture()

                prediction = logical.predict_face(image)

                idPredict = prediction.tag_name
                probability = prediction.probability
                idPredict = idPredict.strip().upper()
                
                msg = (f"IdCard : {idCard}, IdPredict : {idPredict}, Probability : {probability}")
                
                print(msg)

                if idCard == idPredict:
                    self.ui.change_infos(userid=idCard, iscorrect=True)
                else:
                    self.ui.change_infos(userid='16AM003', iscorrect=False)

                connexion_avec_client.send(b"5 / 5")
                # warning mobile
                connexion_avec_client.close()

            except Exception as error:
                print(error)
                break
            

        print("Fermeture de la connexion")
        connexion_avec_client.close()
        connexion_principale.close()

class UI:
    TITLE = "INFORMATIONS"
    INFOS = [
        "MATRICULE",
        "NOM",
        "POST-NOM",
        "PRENOM",
        "GENRE",
        "STATUS"
    ]
    def __init__(self, parent):
        self.root = root
        self.init_interface()
    
    def init_interface(self):
        #self.title = Label(self.root, text="TITLE")
        self.canvas = Canvas(self.root, 
                            width=config.g_width,
                            height=config.g_height, bg=config.g_bg)
        
        self.title = self.canvas.create_text(
            config.t_x, config.t_y,
            text=config.t_text,
            fill=config.t_fill,
            font=config.t_font
        )
        self.canvas.bind("<Button-1>", pointer)

        self.infos = self.canvas.create_text(
            config.inf_x,
            config.inf_y, text="...",
            fill=config.inf_fill,
            font=config.inf_font,
            state='normal',
            anchor='nw'
        )
        canvas = Canvas(self.canvas, 
                        width=config.img_w,
                        height=config.img_h,
                        bg=config.g_bg)

        self.canvas.create_window(
                config.img_x,
                config.img_y,window=canvas,
                anchor='nw'
            )

        self.message = self.canvas.create_text(
            config.msg_x,
            config.msg_y, text="",
            fill=config.inf_fill,
            font=config.msg_font,
            state='normal',
            anchor='nw'
        )
        self.canvas.pack()
        self.change_infos()
    
    def change_infos(self, userid=None, iscorrect=None):
        display_image = True
        if not userid:
            infos = ['None'] * len(self.INFOS)
            display_image = False
        
        else:
            infos = get_infos(userid=userid)
        
        if iscorrect:
            update_status(userid=userid)
            msg = config.message['accepted']
        else:
            msg = config.message['denied']

        self.canvas.itemconfig(self.message, text=msg['text'],
                        fill=msg['fill'])


        
        
        infos_all = zip(self.INFOS, infos)

        funct = lambda tup_inf: f"{tup_inf[0]} : {tup_inf[1]}"

        infos_all = map(funct, infos_all)

        infos_all = list(infos_all)

        infos_str = config.inf_join.join(infos_all)

        self.canvas.itemconfig(self.infos, text=infos_str)

        # image update
        if display_image:
            image = self.load_image(uid=userid)

            canvas = Canvas(self.canvas, 
                        width=config.img_w,
                        height=config.img_h,
                        bg=config.g_bg)
            
            canvas.image = image

            canvas.create_image(0,0, image = canvas.image,
            anchor='nw')

            self.canvas.create_window(
                config.img_x,
                config.img_y,window=canvas,
                anchor='nw'
            )
            
    def load_image(self, uid=None):
        if not uid:
            uid = 'gif.gif'
        
        else:
            uid += '.png'
        
        image_file = os.path.join(
            config.samples_folder,
            uid
        )
        image = Image.open(image_file)

        image = ImageTk.PhotoImage(image=image)
        return image



if __name__ == "__main__":
    root = Tk()
    ui = UI(root)

    chaine = Label(root, fg='blue', font='Andalus 10 bold')
    chaine.pack()
    server = Thread(target=Server, args=(ui,))

    server.start()
    root.mainloop()
    server.join()
