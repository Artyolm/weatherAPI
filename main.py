from api_client import APIClient
from data_processor import DataProcessor
from visualizer import Visualizer

api_client = APIClient()
data_processor = DataProcessor()
visualizer = Visualizer()

def main():
    api_client.get_data()
    visualizer.create_histogram(cleaned_data)