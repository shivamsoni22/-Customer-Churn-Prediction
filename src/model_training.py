import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

def load_data():
    """Load the dataset from a csv file."""
    filepath = r'D:\-Customer-Churn-Prediction\Data\customer_churn_data.csv'
    data = pd.read_csv(filepath)
    print("Columns in the dataset:", data.columns)
    print("First 5 rows of the dataset:\n", data.head())
    return data

def clean_data(data):
    """Clean the data by handling missing values and encoding categorical features."""
    # Drop non-numeric column 'customerID'
    data = data.drop(columns=['customerID'])
    
    # Handle missing values in TotalCharges
    data['TotalCharges'] = pd.to_numeric(data['TotalCharges'], errors='coerce')
    data = data.dropna()  # Drop rows with missing values after conversion
    
    # Convert categorical columns to numeric using one-hot encoding
    data = pd.get_dummies(data, drop_first=True)
    return data

def train_model(data):
    """Train a machine learning model."""
    X = data.drop('Churn_Yes', axis=1)  # Features
    y = data['Churn_Yes']  # Target variable
    
    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Initialize and train the model
    print("Training the model...")
    model = RandomForestClassifier()
    model.fit(X_train, y_train)
    print("Model training completed.")
    
    # Make predictions
    y_pred = model.predict(X_test)
    
    # Calculate accuracy
    accuracy = accuracy_score(y_test, y_pred)
    print(f'Model Accuracy: {accuracy * 100:.2f}%')  # Display accuracy
    
    return model, X_test, y_test

if __name__ == "__main__":
    data = load_data()
    data = clean_data(data)  # Clean the data
    model, X_test, y_test = train_model(data)
