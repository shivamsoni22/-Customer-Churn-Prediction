from src.data_preprocessing import load_data, clean_data
from src.model_training import train_model
from src.model_evaluation import evaluate_model

def main():
    # Load and clean data
    data = load_data('D:\-Customer-Churn-Prediction\Data\customer_churn_data.csv')
    clean_data_df = clean_data(data)

    # Train the model
    model, X_test, y_test = train_model(clean_data_df)

    # Evaluate the model
    evaluate_model(model, X_test, y_test)

if __name__ == "__main__":
    main()

