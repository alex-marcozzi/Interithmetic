import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import tensorflow.keras
from PIL import Image, ImageOps
import numpy as np

class Classifier:
    def __init__(self, model_path):
        self.saved_model = tensorflow.keras.models.load_model(model_path)

    def classify(self, image_path):
        data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
        image = Image.open(image_path)
        size = (224, 224)
        image = ImageOps.fit(image, size, Image.ANTIALIAS)
        image_array = np.asarray(image)
        normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
        data[0] = normalized_image_array
        prediction = self.saved_model.predict(data)
        return np.argmax(prediction) + 1

# test = Classifier('./assets/converted_keras/model.h5')
# print("GO")
# print(test.classify('./assets/images/test_image2.jpg'))
# print(test.classify('./assets/images/test_image1.jpg'))
# print(test.classify('./assets/images/test_image1.jpg'))
# print(test.classify('./assets/images/test_image2.jpg'))
# print(test.classify('./assets/images/test_image2.jpg'))