from api_client import APIClient
from data_processor import DataProcessor
from visualizer import Visualizer

api_client = APIClient()
data_processor = DataProcessor('data/weather.csv')

def main():
    print("Starting..")
    api_client.get_data()
    cleaned_data = data_processor.clean_data()
    #print(cleaned_data)
    visualizer = Visualizer(cleaned_data)
    visualizer.map() 
    
if __name__ == "__main__":
    main()