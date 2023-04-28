from keras.models import load_model
from flask import Flask, render_template, request, jsonify
from tensorflow.keras.preprocessing.image import img_to_array
import numpy as np
import json
from PIL import Image
import io
import os

# Creating the app
app = Flask(__name__)

# Loading the model
model = load_model("skin_disorder_classifier_EfficientNetB2.h5")

# Loading the json file with the skin disorders
def get_treatment(path):
    with open(path) as f:
        return json.load(f)
treatment_dict = get_treatment("skin_disorder.json")

# function to check if the file is an allowed image type
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in {'png', 'jpg', 'jpeg'}


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get the image from the request
    file = request.files['file']

    # check if the file is an image
    if not file or not allowed_file(file.filename):
        return render_template('error.html', error='Only image files are allowed')
   

    # Open the image using PIL
    image = Image.open(file)

    # Preprocess the image
    img = image.resize((300,300))
    img_array = img_to_array(img)
    img = img_array / 255.0
    image = np.expand_dims(img, axis=0)

    # Make prediction
    pred = model.predict(image)
    class_idx = np.argmax(pred)

    # Classes
    classes = ["Acne", "Basal cell carcinoma", "Benign Keratosis-like Lesions (BKL)", "Atopic dermatitis(Eczema)",
           "Actinic keratosis(AK)", "Melanoma", "Psoriasis","Tinea(Ringworm)"]
    
    # Predicted class
    pred_class = classes[class_idx]

    # treatment options
    treatments = treatment_dict.get(pred_class, [])

    return render_template('results.html', prediction=pred_class, treatments=treatments)

    
if __name__ == '__main__':
    app.run(debug=True)
