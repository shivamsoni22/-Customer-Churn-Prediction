import pandas as pd

def load_data():
    """Load the dataset from a CSV file."""
    filepath = r'D:\Customer-Churn-Prediction\Data\customer_churn_data.csv'  # Use raw string to avoid escape issues
    data = pd.read_csv(filepath)
    print("Loaded data with columns:", data.columns)
    return data

def clean_data(data):
    """Clean the data by handling missing values and encoding categorical features."""
    # Drop non-numeric column 'customerID'
    if 'customerID' in data.columns:
        data = data.drop(columns=['customerID'])

    # Handle missing values in 'TotalCharges'
    data['TotalCharges'] = pd.to_numeric(data['TotalCharges'], errors='coerce')
    data = data.dropna()  # Drop rows with missing values after conversion

    # Convert categorical columns to numeric using one-hot encoding
    data = pd.get_dummies(data, drop_first=True)
    return data

if __name__ == "__main__":
    # Example usage
    data = load_data()
    cleaned_data = clean_data(data)
    print(cleaned_data.head())
