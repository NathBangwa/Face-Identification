import os

cwd = os.getcwd()

model_file = os.path.join(cwd, 'model/model.onnx')

samples_folder = os.path.join(cwd, 'samples')
car_image = os.path.join(cwd, 'samples/car.jpg')
phone_image = os.path.join(cwd, 'samples/phone.jpg')

# server config
host = "192.168.43.95"
port = 12800

# database
database = "C:\\Users\\RMB PC\\Documents\\PROJECTS\\Face-Identification\\model\\database.json"#os.path.join(config.samples_folder, infos[0]+'.jpg')
        
# custom vision config
ENDPOINT = "https://westeurope.api.cognitive.microsoft.com"
projet_id = "0e64c081-ebcc-4d56-8afa-33e834453314"
prediction_key = "09ae11a1bede440db983495292d9f381"
Prediction_ressource_id = "/subscriptions/d8a42b2a-8c3f-4974-afbd-3a88ebcbfd92/resourceGroups/JPO-app-rg/providers/Microsoft.CognitiveServices/accounts/JPO-app-rg_prediction"
publish_iteration_name = "classifyModel"

# capture rectangle
x, y = 100, 100
width = x + 400
height = y + 300
rgb = (255, 0, 0)
thickness = 2

# GUI
g_height = 500
g_width = 500

# title
t_x = 100
t_y = 100

# image profil
img_x = 0
img_y = 0

# infos
inf_x = g_width // 2 + 50
inf_y = t_y + 120

