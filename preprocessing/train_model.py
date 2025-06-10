import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
import joblib
import os
def train_flood_model(data_path, model_output_path):
    # Load the data
    df = pd.read_csv(data_path)
    X = df[["rainfall", "elevation"]]
    y = df["flood_risk"]
    # Split into training and test set (80/20)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    # Train Random Forest
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    # Evaluate
    y_pred = model.predict(X_test)
    print("✅ Model Evaluation:")
    print(confusion_matrix(y_test, y_pred))
    print(classification_report(y_test, y_pred))
    # Save the model
    os.makedirs(os.path.dirname(model_output_path), exist_ok=True)
    joblib.dump(model, model_output_path)
    print(f"✅ Model saved to: {model_output_path}")
if __name__ == "__main__":
    data_path = "processed/training_data.csv"
    model_output_path = "processed/flood_model.pkl"
    train_flood_model(data_path, model_output_path)