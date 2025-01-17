import folium
import webbrowser
class Visualizer:
    def __init__(self,df):
        print('Loading map..')
        self.df = df
        self.map_center = [self.df['latitude'].mean(), self.df['longitude'].mean()]
        
        
    def map(self):
        map = folium.Map(location=self.map_center, zoom_start=10)
        for i in range(0,len(self.df)):
            folium.Marker(
                location = [self.df.iloc[i]['latitude'],self.df.iloc[i]['longitude']],
                tooltip = "Click me!",
                popup = self.df.iloc[i]['2_metre_temperature'],
                icon = folium.Icon(color="red"),
            ).add_to(map)
        map.save('map.html')
        
        print('Opening file..')
        webbrowser.open_new_tab('map.html')