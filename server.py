import socket
import logical
import config


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
            print("Access accepted")
        else:
            print("Access Denied")

        connexion_avec_client.send(b"5 / 5")
        # warning mobile
        connexion_avec_client.close()

    except Exception as error:
        print(error)
        break
    

print("Fermeture de la connexion")
connexion_avec_client.close()
connexion_principale.close()