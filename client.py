import socket
import config

"""hote = "10.12.61.153"#"localhost"
port = 12800
"""
connexion_avec_serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connexion_avec_serveur.connect((config.host, config.port))
print("Connexion établie avec le serveur sur le port {}".format(config.port))

msg_a_envoyer = b""
while msg_a_envoyer != b"fin":
    try:
        msg_a_envoyer = input("> ")
        # Peut planter si vous tapez des caractères spéciaux
        msg_a_envoyer = msg_a_envoyer.encode()
        # On envoie le message
        connexion_avec_serveur.send(msg_a_envoyer)
        #msg_recu = connexion_avec_serveur.recv(1024)
        #print(msg_recu.decode()) # Là encore, peut planter s'il y a des accents

    except Exception as error:
        print(error)
        break
    
print("Fermeture de la connexion")
connexion_avec_serveur.close()