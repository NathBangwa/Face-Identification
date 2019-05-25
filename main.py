import config

import cv2

import logical


image = cv2.imread(config.car_image)

prediction = logical.predict_face(image)

print("prediction : ", prediction)



