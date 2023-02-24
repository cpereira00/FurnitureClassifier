from flask import Flask, request
import os
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array
from PIL import Image
import numpy as np

app = Flask(__name__)

model = load_model('saved_model/my_model.h5')
classes = ['bed', 'chair', 'sofa']
# preprocess image to have proper dims
def preprocess_image(image):
    image = image.resize((80, 80))
    image = img_to_array(image)
    # scale the pixel values to the range [0, 1]
    image = image / 255.0
    # add an extra dimension to the array to match the input shape of the model
    image = np.expand_dims(image, axis=0)
    # return the preprocessed image
    return image

@app.route("/predict", methods=['POST'])
def predict():

    # get the image
    image = '../Dataset/test/bed/Baxton Studio Adelaide Retro Modern Light Grey Fabric Upholstered Queen Size Platform Bed.jpg'
    image = request.files["image"]
    image = Image.open(image)

    image = preprocess_image(image)
    # make a prediction using the model
    predictions = model.predict(image)
    predicted_category = np.argmax(predictions, axis=1)[0]

    response = {'message': f'{classes[predicted_category]}'}

    return response

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=int(os.environ.get('PORT', 8080)))
