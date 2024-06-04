# Intent Prediction Model for Novo Customer Feedback

## Project Structure

- `app/`: Contains the Flask application code
  - `__init__.py`: Flask application factory
  - `main.py`: Main Flask blueprint and routes
  - `model.py`: Intent classification model class
- `data/`: Contains the customer feedback data
  - `feedback.xlsx`: Excel file with customer feedback
- `models/`: Contains the trained model artifacts
  - `tfidf_vectorizer.pkl`: Trained TF-IDF vectorizer
  - `intent_classifier.pkl`: Trained intent classifier
  - `label_binarizer.pkl`: Label binarizer for intents
- `train_model.py`: Script to train the intent prediction model
- `run.py`: Entry point to run the Flask application
- `requirements.txt`: List of required Python packages
- `README.md`: Project documentation

## How to Run

1. Create a new conda environment and install dependencies:

    ```bash
    conda create -n novo_assignment python=3.9
    conda activate novo_assignment
    pip install -r requirements.txt
    ```

2. Train the model (if not already done):

    ```bash
    python train_model.py
    ```

3. Run the Flask application:

    ```bash
    python run.py
    ```

4. Use the `/predict` endpoint to predict intents for customer feedback.

## Notes

- Ensure `feedback.xlsx` is placed in the `data/` directory.
- The model files (`tfidf_vectorizer.pkl`, `intent_classifier.pkl`, `label_binarizer.pkl`) should be in the `models/` directory.

## Model Evaluation

- Evaluate the model using standard metrics like accuracy, precision, recall, and F1-score.
- Use a hold-out validation set or cross-validation for reliable performance estimates.

## Teaching New Intents

1. Collect new labeled data for the new intents.
2. Retrain the model using the updated dataset.
3. Save the updated model artifacts to the `models/` directory.

=======
