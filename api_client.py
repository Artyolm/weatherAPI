import requests
import os

url = 'https://public.opendatasoft.com/api/explore/v2.1/%s'

class APIClient:
    # def api_call(self):
    #     endpoint = 'catalog/datasets/arome-0025-sp1_sp2_paris/records'
    #     response = requests.get(url%endpoint)
    #     response.raise_for_status()
    #     print('data: ')
    #     return response.json()
    
    def get_data(self):
        endpoint = 'catalog/datasets/arome-0025-sp1_sp2_paris/exports/csv'
        response = requests.get(url%endpoint, stream=True)
        response.raise_for_status()
        
        if not os.path.exists('data'):
            os.makedirs('data')
        
        file_path = os.path.join('data', 'weather.csv')
        with open(file_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
        
        print('Downloading data file..')

#catalog/datasets/arome-0025-sp1_sp2_paris/exports/csv
