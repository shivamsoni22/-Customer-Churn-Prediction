import pandas as pd

def load_data():
    """Load the dataset from a csv file."""
    # Directly using the specified file path
    filepath = r'D:\-Customer-Churn-Prediction\Data\customer_churn_data.csv'  # Use raw string to avoid escape issues
    return pd.read_csv(filepath)

def clean_data(data):
    """Clean the data by handling missing values and encoding categorical features."""
    data = data.dropna()  # Example: drop rows with missing values
    data = pd.get_dummies(data, drop_first=True)  # One-hot encoding for categorical features
    return data

if __name__ == "__main__":
    # Example usage
    data = load_data()
    cleaned_data = clean_data(data)
    print(cleaned_data.head())
