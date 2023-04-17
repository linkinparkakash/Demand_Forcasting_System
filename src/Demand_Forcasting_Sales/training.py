import pandas as pd
import xgboost as xgb
from sklearn.metrics import mean_squared_error
import joblib
from Demand_Forcasting_System.exception import DemandForcastingException

class XGBoostTrainer:
    def __init__(self, data_path, model_path):
        self.data_path = data_path
        self.model_path = model_path
        self.df = pd.read_csv(data_path)
        try:    
            def train_model(self):
                # Prepare data
                X = self.df.drop("sales", axis=1)
                y = self.df["sales"]

                # Split data into training and testing sets
                train_size = int(len(X) * 0.8)
                X_train, X_test = X[:train_size], X[train_size:]
                y_train, y_test = y[:train_size], y[train_size:]

                # Define model
                model = xgb.XGBRegressor(objective="reg:squarederror", n_estimators=100, learning_rate=0.1, max_depth=5)

                # Train model
                model.fit(X_train, y_train)

                # Make predictions
                y_pred = model.predict(X_test)

                # Calculate root mean squared error (RMSE)
                rmse = mean_squared_error(y_test, y_pred, squared=False)
                print("RMSE:", rmse)

                # Export model
                joblib.dump(model, self.model_path)
                
                # Return trained model
                return model
        except Exception as e:
            raise DemandForcastingException(error_message=e, error_detail=sys)
    
"""
trainer = XGBoostTrainer("C:\Users\HP\Demand_Forcasting_System_Store_Sales\Demand_Forcasting_System\src\Demand_Forcasting_System\datasets/train.csv", "C:\Users\HP\Demand_Forcasting_System_Store_Sales\Demand_Forcasting_System\xgboost_sales_forcasting.joblib")
trained_model = trainer.train_model()

"""