from sklearn.dummy import DummyClassifier
import joblib

model = DummyClassifier(strategy="most_frequent")
model.fit([[0], [1], [2]], ["positive", "positive", "positive"])

joblib.dump(model, "model/sentiment_model.joblib")
