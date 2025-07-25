import pandas as pd
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier
import pickle
import json

def train(input_csv, model_path, metrics_path, target='default'):
    df = pd.read_csv(input_csv)
    X = df.drop(target, axis=1)
    y = df[target]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    model = XGBClassifier().fit(X_train, y_train)
    acc = model.score(X_test, y_test)
    pickle.dump(model, open(model_path, "wb"))
    metrics = {"accuracy": acc}
    with open(metrics_path, "w") as f:
        json.dump(metrics, f)
    pd.DataFrame({"truth": y_test, "pred": model.predict(X_test)}).to_csv("predictions.csv", index=False)

if __name__ == "__main__":
    train("selected.csv", "model.pkl", "metrics.json")
