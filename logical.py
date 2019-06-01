import numpy as np
import config
import cv2
from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
import copy


def predict_face(image:list):
    """
        permet de predire lidentité de l'etudiant
    """
    # Byte 
    image_contents = cv2.imencode('.jpg', image)[1].tostring()

    # Now there is a trained endpoint that can be used to make a prediction
    predictor = CustomVisionPredictionClient(config.prediction_key, endpoint=config.ENDPOINT)

    #with open(base_image_url + "images/Test/test_image.jpg", "rb") as image_contents:
    results = predictor.classify_image(config.project_id, config.publish_iteration_name, image_contents)

    # hight probability
    prediction = results.predictions[0]
    """for prediction in results.predictions:
        if prediction.probability > prob:
            tag_name = prediction.tag_name
            prob = prediction.probability

        print ("\t" + prediction.tag_name + ": {0:.2f}%".format(prediction.probability * 100))
    """
    return prediction

def take_capture():
    response = list

    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

    cap = cv2.VideoCapture(0)

    try:
        while(True):
            if not cap.isOpened():
                cap.open()
            # Capture frame-by-frame
            ret, frame = cap.read()

            if ret: # correctly frame
                # Our operations on the frame come here
                img = copy.deepcopy(frame)
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                img = cv2.rectangle(img,(config.x,config.y),(config.width, config.height),config.rgb,config.thickness)
                # Display the resulting frame
                cv2.imshow('frame',img)

                #return frame
                response = frame

            key = cv2.waitKey(1) & 0xFF

            if key == ord('q'):
                break
            
            elif key == ord('v') or key == ord('V'):
                return frame

    except Exception as error:
        print(error)
        
    finally:
        # When everything done, release the capture
        cap.release()
        cv2.destroyAllWindows()
# Load an color image in grayscale
#array = cv2.imread(config.phone_image,1)
#array = take_capture()
#prediction = predict_face(array)
#print(prediction.tag_name, prediction.probability)