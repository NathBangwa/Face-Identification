import os
import json
cwd = os.getcwd()

samples_folder = os.path.join(cwd, 'samples')
model_folder = os.path.join(cwd, 'model')

# config
config_file = os.path.join(model_folder, 'config.json')
with open(config_file) as fp:
    config = json.load(fp)

#DATABASE
database = os.path.join(model_folder, config['database'])
# server config
host = config['server']['host']
port = config['server']['port']

# custom vision config
ENDPOINT = config['api']['endpoint']#"https://westeurope.api.cognitive.microsoft.com"
project_id = config['api']['project_id']#"0e64c081-ebcc-4d56-8afa-33e834453314"
prediction_key = config['api']['prediction_key']#"09ae11a1bede440db983495292d9f381"
Prediction_ressource_id = config['api']['Prediction_ressource_id']#"/subscriptions/d8a42b2a-8c3f-4974-afbd-3a88ebcbfd92/resourceGroups/JPO-app-rg/providers/Microsoft.CognitiveServices/accounts/JPO-app-rg_prediction"
publish_iteration_name = config['api']['publish_iteration_name']#"classifyModel"

# capture rectangle
opencv = config['opencv']
x = opencv['rectangle']['x']
y = opencv['rectangle']['y']
width = x + opencv['rectangle']['w']
height = y + opencv['rectangle']['h']
rgb = opencv['rectangle']['rgb']
thickness = opencv['rectangle']['tickness']

# GUI
ui = config['ui']
g_height = ui['canvas']['h']
g_width = ui['canvas']['w']
g_bg = ui['canvas']['bg']

# title
t_x = ui['title']['x']
t_y = ui['title']['y']
t_fill = ui['title']['fill']
t_font = ui['title']['font']
t_text = ui['title']['text']

# image profil
img_x = ui['image']['x']
img_y = ui['image']['y']
img_w = ui['image']['c_x']
img_h = ui['image']['c_y']

# infos
inf_x = ui['infos']['x']
inf_y = ui['infos']['y']
inf_fill = ui['infos']['fill']
inf_font = ui['infos']['font']
inf_join = ui['infos']['joinchar']

# message
message = ui['message']
msg_x = message['x']
msg_y = message['y']
msg_font = message['font']


