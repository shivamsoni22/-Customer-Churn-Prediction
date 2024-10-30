import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

def train_model(data):
    X = data.drop('churn', axis=1)  # Feature columns
    y = data['churn']  # Target column

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = RandomForestClassifier()  # Example model
    model.fit(X_train, y_train)

    return model, X_test, y_test  # Return model and test data

if __name__ == "__main__":
    # Load your data here
    data = pd.read_csv('D:\-Customer-Churn-Prediction\Data\customer_churn_data.csv')
    model, X_test, y_test = train_model(data)
