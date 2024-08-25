from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import train_test_split
import joblib
import pandas as pd

# Sample data loading
data = pd.read_csv('grievances.csv')  # Assumed CSV with 'text' and 'category' columns
X = data['text']
y = data['category']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Training
pipeline = make_pipeline(
    TfidfVectorizer(),
    MultinomialNB()
)
pipeline.fit(X_train, y_train)

# Saving model
joblib.dump(pipeline, 'text_classifier_model.joblib')

