import numpy as np
import onnx
import caffe2.python.onnx.backend as backend
import config


def predict_face(image:list):
    """
        permet de predire lidentité de l'etudiant
    """
    # Load the ONNX model
    model = onnx.load(config.model_file)

    # Run the ONNX model with Caffe2
    outputs = backend.run_model(model, [image])
