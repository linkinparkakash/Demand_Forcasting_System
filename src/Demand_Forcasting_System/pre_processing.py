import pandas as pd
import logging

class DemandForecasting:
    def __init__(self, csv_file):
        self.csv_file = csv_file
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)

        # create file handler which logs even debug messages
        fh = logging.FileHandler('logs.txt')
        fh.setLevel(logging.INFO)

        # create formatter and add it to the handlers
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)

        # add the handlers to the logger
        self.logger.addHandler(fh)

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
            monthly_data = df[['sales']].resample('M').sum()
            month_map = {'January': 1, 'February': 2, 'March': 3, 'April': 4, 'May': 5, 'June': 6, 'July': 7, 'August': 8, 'September': 9, 'October': 10, 'November': 11, 'December': 12}
            df['month_num'] = df['month_name'].map(month_map)
            df.drop(columns = ['month_name'], inplace = True)
            df.to_csv('pre_processed_test', index=False)

        except Exception as e:
            self.logger.error(f"Error occurred while preprocessing data: {e}")

csv_file = 'pre_processed_test.csv'
demand_forecasting = DemandForecasting(csv_file)
demand_forecasting.preprocess_data()
