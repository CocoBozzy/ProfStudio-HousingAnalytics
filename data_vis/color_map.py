import pandas as pd
import folium

syd = folium.Map(location=[-33.8898, 151.2134])

syd.save('sydney.html')

import geopandas

# The URL we will read our data from
url = 'https://en.wikipedia.org/wiki/List_of_countries_by_meat_consumption'
# read_html returns a list of tables from the URL
tables = pd.read_html(url)
# The data is in the first table - this changes from time to time - wikipedia is updated all the time.
table = tables[0]
# Read the geopandas dataset
world = geopandas.read_file(geopandas.datasets.get_path('naturalearth_lowres'))

print(world)
# Merge the two DataFrames together
table = world.merge(table, how="left", left_on=['name'], right_on=['Country'])
# # Clean data: remove rows with no data
table = table.dropna(subset=['kg/person (2002)[9][note 1]'])

print(table)


# Create a map
my_map = folium.Map(location=[48, -102], zoom_start=3)
# Add the data
folium.Choropleth(geo_data=table,name='choropleth',data=table,columns=['Country', 'kg/person (2002)[9][note 1]'],key_on='feature.properties.name',fill_color='OrRd',fill_opacity=0.7,line_opacity=0.2,legend_name='Meat consumption in kg/person').add_to(my_map)
my_map.save('meat1.html')













# url = (
#     "https://raw.githubusercontent.com/python-visualization/folium/master/examples/data"
# )
# state_geo = f"{url}/us-states.json"
# state_unemployment = f"{url}/US_Unemployment_Oct2012.csv"
# state_data = pd.read_csv(state_unemployment)

# m = folium.Map(location=[48, -102], zoom_start=3)

# folium.Choropleth(
#     geo_data=state_geo,
#     name="choropleth",
#     data=state_data,
#     columns=["State", "Unemployment"],
#     key_on="feature.id",
#     fill_color="YlGn",
#     fill_opacity=0.7,
#     line_opacity=0.2,
#     legend_name="Unemployment Rate (%)",
# ).add_to(m)

# folium.LayerControl().add_to(m)

# m.save('map.html')

# m
