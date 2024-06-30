import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
from tensorflow.keras.models import load_model
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Muat model
model = load_model('DTRModel.h5')

# Fungsi untuk mempersiapkan data
def preprocess_input(data):
    label_encoders = {
        'Gender': LabelEncoder(),
        'Area': LabelEncoder(),
        'AreaType': LabelEncoder(),
        'HouseType': LabelEncoder(),
        'District': LabelEncoder()
    }

    for column in ['Gender', 'Area', 'AreaType', 'HouseType', 'District']:
        data[column] = label_encoders[column].fit_transform(data[column])

    X = data[['Gender', 'Age', 'NS1', 'IgG', 'IgM', 'Area', 'AreaType', 'HouseType', 'District']]
    scaler = StandardScaler()
    X = scaler.fit_transform(X)
    return X

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Ambil data dari form
    data = request.form.to_dict()
    
    # Buat DataFrame dari data form
    input_data = pd.DataFrame([data])

    # Preproses data
    processed_data = preprocess_input(input_data)

    # Prediksi
    prediction = model.predict(processed_data)
    output = (prediction > 0.5).astype(int)[0][0]

    # Render hasil prediksi ke template
    return render_template('index.html', output=output)

if __name__ == '__main__':
    app.run(debug=True, port=5001)
