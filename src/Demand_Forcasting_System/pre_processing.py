import pandas as pd
from Demand_Forcasting_System.exception import DemandForcastingException

class DemandForecasting:
    def __init__(self, csv_file):
        self.csv_file = csv_file

    def preprocess_data(self):
        try:
            df = pd.read_csv(self.csv_file)

            df['date'] = pd.to_datetime(df['date'])
            df['year'] = df['date'].dt.year
            df['month'] = df['date'].dt.month
            df['day'] = df['date'].dt.day
            df['date'] = pd.to_datetime(df['date'])
            df['day_of_week'] = df['date'].dt.dayofweek
            df['month_name'] = df['date'].dt.strftime('%B')
            df.set_index('date', inplace=True)
            month_map = {'January': 1, 'February': 2, 'March': 3, 'April': 4, 'May': 5, 'June': 6, 'July': 7, 'August': 8, 'September': 9, 'October': 10, 'November': 11, 'December': 12}
            df['month_num'] = df['month_name'].map(month_map)
            df.drop(columns = ['month_name'], inplace = True)
            df.to_csv('preprocessed_datasets/pre_processed_test.csv', index=False)

        except Exception as e:
            raise DemandForcastingException(error_message=e, error_detail=sys)

# csv_file = 'preprocessed_datasets/pre_processed_test.csv'
# demand_forecasting = DemandForecasting(csv_file)
# demand_forecasting.preprocess_data()
