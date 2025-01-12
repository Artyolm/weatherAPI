import requests
from urllib.request import urlretrieve
import os

url = 'https://public.opendatasoft.com/api/explore/v2.1/%s'

class APIClient:
    def api_call(self):
        endpoint = 'catalog/datasets/weatherref-france-vigilance-meteo-departement/records'
        response = requests.get(url%endpoint)
        response.raise_for_status()
        print('data: ')
        return response.json()
    
    def get_data(self):
        endpoint = 'catalog/datasets/weatherref-france-vigilance-meteo-departement/exports/csv'
        response = requests.get(url%endpoint, stream=True)
        response.raise_for_status()
        
        if not os.path.exists('data'):
            os.makedirs('data')
        
        file_path = os.path.join('data', 'weather.csv')
        with open(file_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
        
        print('downloading data file..')

#catalog/datasets/weatherref-france-vigilance-meteo-departement/exports/csv
