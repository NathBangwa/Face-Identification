import os

cwd = os.getcwd()

model_file = os.path.join(cwd, 'model/model.onnx')

car_image = os.path.join(cwd, 'samples/car.jpg')
phone_image = os.path.join(cwd, 'samples/phone.jpg')