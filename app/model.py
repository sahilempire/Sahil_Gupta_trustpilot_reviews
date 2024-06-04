import joblib
import os

class IntentClassifier:
    def __init__(self):
        self.vectorizer = joblib.load(os.path.join('models', 'tfidf_vectorizer.pkl'))
        self.classifier = joblib.load(os.path.join('models', 'intent_classifier.pkl'))
        self.label_binarizer = joblib.load(os.path.join('models', 'label_binarizer.pkl'))

    def predict(self, text):
        X = self.vectorizer.transform([text])
        prediction = self.classifier.predict(X)
        label = self.label_binarizer.inverse_transform(prediction)
        return label[0]
