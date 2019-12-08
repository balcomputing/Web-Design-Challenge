import pandas as pd

columns = ['City', 'Latitude', 'Temperature', 'Humidity', 'Clouds', 'Wind Speed']

df = pd.read_csv(r"WebVisualizations\Web_HW\weather.csv")
df.to_html("WebVisualizations\Web_HW\weather.html")
