import folium
from folium.plugins import MarkerCluster
import webbrowser
class Visualizer:
    def __init__(self,df):
        print('Loading map..')
        self.df = df
        self.map_center = [self.df['latitude'].mean(), self.df['longitude'].mean()]
        
        
    def map(self):
        map = folium.Map(location=self.map_center, zoom_start=10)
        marker_cluster = MarkerCluster().add_to(map)
        for i in range(0,len(self.df)):
            popup = f"""
            <strong>Forecast: </h3>{self.df.iloc[i]['forecast']}
            <strong>Temperature: </strong> {self.df.iloc[i]['2_metre_temperature']} °C<br>
            <strong>Position: </strong> {self.df.iloc[i]['position']}<br>
            <strong>Humidity: </strong> {self.df.iloc[i]['2_metre_relative_humidity']}%<br>
            <strong>Wind Speed: </strong> {self.df.iloc[i]['10m_wind_speed']} m/s<br>
            <strong>Latest update: </strong>{self.df.iloc[i]['timestamp']}
            """
            folium.Marker(
                location = [self.df.iloc[i]['latitude'],self.df.iloc[i]['longitude']],
                tooltip = "Click me!",
                popup = folium.Popup(popup),
                icon = folium.Icon(color="red"),
            ).add_to(marker_cluster)
        map.save('map.html')
        
        print('Opening file..')
        webbrowser.open_new_tab('map.html')