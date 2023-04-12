import pandas as pd
from Demand_Forcasting_System.exception import DemandForcastingException

class DataValidator:
    def __init__(self, file_path):
        self.file_path = file_path
        self.expected_columns = ['id', 'date', 'store', 'item']
        self.expected_dtypes = {'id': 'int64', 'date': 'object', 'store': 'int64', 'item': 'int64'}

    try:
        logging.info(f"Exporting collection data as pandas dataframe")    
        def is_valid(self):
            # read the CSV file into a pandas dataframe
            df = pd.read_csv(self.file_path)
            
            # check if the dataframe contains all expected columns with the expected dtypes
            if not set(self.expected_columns) == set(df.columns) and self.expected_dtypes == dict(df.dtypes):
                return False
            
            # if all checks pass, the dataset is valid
            return True
    except Exception as e:
            raise DemandForcastingException(error_message=e, error_detail=sys)

"""
from data_validation import DataValidator

# create a DataValidator object with the file path of your CSV
validator = DataValidator('your_csv_file.csv')

# check if the data is valid
if validator.is_valid():
    print('Data is valid')
else:
    print('Data is not valid')

"""