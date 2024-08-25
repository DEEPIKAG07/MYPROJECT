from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
import joblib

# Assume we have a trained model saved
model = joblib.load('text_classifier_model.joblib')

def classify_text(text):
    # Predict the category
    category = model.predict([text])[0]
    return category

# For training (not used in production)
def train_classifier(X_train, y_train):
    pipeline = make_pipeline(
        TfidfVectorizer(),
        MultinomialNB()
    )
    pipeline.fit(X_train, y_train)
    joblib.dump(pipeline, 'text_classifier_model.joblib')
