from flask import flask, render_template, request
from Demand_Forcasting_System.data_validation import DataValidator
from Demand_Forcasting_System.pre_processing import DemandForecasting
import joblib
import pandas as pd
from Demand_Forcasting_System.exception import DemandForcastingException

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def predict():
            try:
                if request.method == 'POST':
                    # Get the file path from the form
                    file = request.form['csvfile']

                    # Check if the data is valid
                    validator = DataValidator(file)
                    if validator.is_valid():
                        # Preprocess the data
                        df = DemandForecasting(file)
                        df.preprocess_data()

                        # Load the trained model
                        model = joblib.load('xgboost_sales_forcasting.joblib')

                        # Generate predictions
                        test_data = pd.read_csv('preprocessed_datasets/pre_processed_test.csv')
                        predictions = model.predict(test_data)

                        # Save predictions to a CSV file
                        output_file = 'predictions.csv'
                        predictions_df = pd.DataFrame({'predictions': predictions})
                        predictions_df.to_csv(output_file, index=False)

                        # Return a message that the predictions have been generated
                        return f'Predictions have been generated for {file}'

                    else:
                        return 'Invalid data'
            except Exception as e:
                 raise DemandForcastingException(error_message=e, error_detail=sys)
