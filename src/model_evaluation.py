from src.model_training import train_model  # Import the train_model function
import pandas as pd
from sklearn.metrics import classification_report, confusion_matrix

def evaluate_model(model, X_test, y_test):
    """Evaluate the trained model."""
    y_pred = model.predict(X_test)
    print(confusion_matrix(y_test, y_pred))
    print(classification_report(y_test, y_pred))

if __name__ == "__main__":
    # Load data and train the model
    data = pd.read_csv(r'D:\Customer-Churn-Prediction\Data\customer_churn_data.csv')
    model, X_test, y_test = train_model(data)  # Get the model and test data
    evaluate_model(model, X_test, y_test)
