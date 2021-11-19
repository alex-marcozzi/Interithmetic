# Title: classifier.py
# Description: Contains the Classifier class for Interithmetic.
# Author: Alexander Marcozzi
# Date: 11/19/2021

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'  # hide log output
import tensorflow.keras
from PIL import Image, ImageOps
import numpy as np

class Classifier:
    """
    A class that manages (most of) the labels used by the game, allowing the
    engine to easily update the text and color of the UI.

    ...

    Attributes
    ----------
    saved_model : tensorflow keras model object
    
    Methods
    -------
    classify(image_path)
        Given a path to an image, classify it using the saved model
    """

    def __init__(self, model_path):
        """
        Parameters
        ----------
        model_path: string
            The path to the file containing the model
        """

        self.saved_model = tensorflow.keras.models.load_model(model_path)

    def classify(self, image_path):
        """
        Given a path to an image, classify it using the saved model.
        
        Parameters
        ----------
        image: string
            The path to the image file
        """

        data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
        image = Image.open(image_path)
        image = image.transpose(Image.FLIP_LEFT_RIGHT)
        size = (224, 224)
        image = ImageOps.fit(image, size, Image.ANTIALIAS)
        image_array = np.asarray(image)
        normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
        data[0] = normalized_image_array
        prediction = self.saved_model.predict(data)
        return np.argmax(prediction)