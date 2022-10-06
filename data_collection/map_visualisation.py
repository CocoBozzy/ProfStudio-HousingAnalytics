import folium


def create_folium_map():
    # initialize the map and store it in a m object
    m = folium.Map(location=[40, -95],
                   zoom_start=4)

    # show the map
    m.save('my_map.html')

# template_name = 'map/index.html'
#     # Create Map Object
#     m = folium.Map(location=[-33.8898, 151.2134], zoom_start=12)
#     m = m._repr_html_()
#     context = {'m': m,}
#     extra_context = context

if __name__ == "__main__":
    create_folium_map()
