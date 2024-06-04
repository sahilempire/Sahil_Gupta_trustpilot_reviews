from flask import Blueprint, request, jsonify
import joblib
import os

main = Blueprint('main', __name__)

model_path = os.path.join('models', 'intent_classifier.pkl')
vectorizer_path = os.path.join('models', 'tfidf_vectorizer.pkl')
label_binarizer_path = os.path.join('models', 'label_binarizer.pkl')

model = joblib.load(model_path)
vectorizer = joblib.load(vectorizer_path)
label_binarizer = joblib.load(label_binarizer_path)

@main.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    if 'text' not in data:
        return jsonify({'error': 'No text provided'}), 400
    
    text = data['text']
    X = vectorizer.transform([text])
    prediction = model.predict(X)
    label = label_binarizer.inverse_transform(prediction)
    return jsonify({'intent': label[0]})
