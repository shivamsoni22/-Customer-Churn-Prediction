from src.data_preprocessing import load_data
from src.model_training import train_model
from src.model_evaluation import evaluate_model

def main():
    # Load the dataset
    data = load_data('D:\\-Customer-Churn-Prediction\\Data\\customer_churn_data.csv')  # Updated file path

    # Train the model
    model, X_test, y_test = train_model(data)  # Get the model and test data

    # Evaluate the model
    evaluate_model(model, X_test, y_test)

if __name__ == "__main__":
    main()
