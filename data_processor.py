import pandas as pa

class DataProcessor:
    def __init__(self,path):
        self.path= path
        self.df=None

    def clean_data(self):
        df = pa.read_csv(self.path,delimiter=";")
        print('Cleaning data..')
        df = df.dropna()
        df['forecast'] = pa.to_datetime(df['forecast'])
        df = df.loc[df.groupby(['position'])['forecast'].idxmax()].reset_index(drop=True)
        df[['latitude', 'longitude']] = df['position'].str.split(',', expand=True).astype(float)
        return df
        