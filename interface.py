import matplotlib.pyplot as plt
import config
import PIL
import cv2

class UserInterface:
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
        self.fig, (self.inter_1, self.inter_2) = plt.subplots(1,2)
        self.change_view()

    def change_view(self, infos=None):
        #plt.clf()
        self.inter_1.set_title("Photo")
        self.inter_2.set_title("Informations")
        set_img = True
        if not infos:
            infos = ['...'] * len(self.INFOS)
            set_img = False
        
        infos_all = zip(self.INFOS, infos)

        funct = lambda tup_inf: f"{tup_inf[0]} : {tup_inf[1]}"

        infos_all = map(funct, infos_all)

        infos_all = list(infos_all)

        infos_str = "\n".join(infos_all)
        
        
        # image update
        if set_img:
            print("image")
            image = cv2.imread(config.car_image)
            print(image.shape)
            self.inter_1.imshow(image)
        
        #plt.show()

gui = UserInterface()
inf = ["tag"] * len(gui.INFOS)
gui.change_view(inf)