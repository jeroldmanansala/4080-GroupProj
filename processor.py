import cv2
import numpy as np
from tensorflow.keras.models import load_model

def process_and_predict(image_path):
    model = load_model("emotion_model.h5")
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img, (64, 64))  
    img = img.reshape(1, 64, 64, 1) / 255.0
    prediction = model.predict(img)
    return ["Happy", "Sad", "Mad"][np.argmax(prediction)]
