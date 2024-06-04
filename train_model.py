import pandas as pd
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
from sklearn.preprocessing import LabelBinarizer
import joblib

# Load data
data = pd.read_excel(os.path.join('data', 'feedback.xlsx'))

# Print column names to debug
print("Columns in the dataset:", data.columns)

# Check if the necessary columns exist
if 'rating' not in data.columns or 'rating_processed' not in data.columns:
    raise KeyError("The necessary columns 'rating' or 'rating_processed' are missing from the dataset.")

# Verify the content of the 'rating' column
print("Sample data from 'rating' column:", data['rating'].head())

texts = data['rating'].tolist()
labels = data['rating_processed'].tolist()

# Filter out empty texts
valid_texts = [text for text in texts if isinstance(text, str) and text.strip()]
valid_labels = [labels[i] for i in range(len(labels)) if isinstance(texts[i], str) and texts[i].strip()]

if not valid_texts:
    raise ValueError("No valid texts available for training.")

# Debug the counts of valid texts and labels
print(f"Number of valid texts: {len(valid_texts)}")
print(f"Number of valid labels: {len(valid_labels)}")

# Vectorize the text data
vectorizer = TfidfVectorizer(stop_words='english', max_features=1000)
X = vectorizer.fit_transform(valid_texts)

# Debug the shape of X
print(f"Shape of X: {X.shape}")

# Binarize the labels
label_binarizer = LabelBinarizer()
y = label_binarizer.fit_transform(valid_labels)

# Debug the shape of y and the classes
print(f"Shape of y: {y.shape}")
print(f"Classes: {label_binarizer.classes_}")

if len(label_binarizer.classes_) < 2:
    raise ValueError("This solver needs samples of at least 2 classes in the data, but the data contains only one class.")

# Train the classifier
classifier = LinearSVC(dual='auto')
classifier.fit(X, y)

# Save the models
os.makedirs('models', exist_ok=True)
joblib.dump(vectorizer, os.path.join('models', 'tfidf_vectorizer.pkl'))
joblib.dump(classifier, os.path.join('models', 'intent_classifier.pkl'))
joblib.dump(label_binarizer, os.path.join('models', 'label_binarizer.pkl'))

print("Training completed and models saved.")