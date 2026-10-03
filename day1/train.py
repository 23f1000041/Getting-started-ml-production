import os
import joblib
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression

X, y = load_iris(return_X_y=True)
model = LogisticRegression(max_iter=200)
model.fit(X, y)

path = os.path.join(os.path.dirname(__file__), "model.pkl")
joblib.dump(model, path)
print("Saved model.pkl | accuracy:", model.score(X, y))
