import pandas as pd

def load_data(filepath):
    """Load the dataset from a csv file."""
    return pd.read_csv('D:\-Customer-Churn-Prediction\Data\customer_churn_data.csv')

def clean_data(data):
    """Clean the data by handling missing values and encoding categorical features."""
    data = data.dropna()  # Example: drop rows with missing values
    data = pd.get_dummies(data, drop_first=True)  # One-hot encoding for categorical features
    return data

if __name__ == "__main__":
    # Example usage
    data = load_data('../data/customer_churn_data.csv')
    clean_data = clean_data(data)
    print(clean_data.head())
