from django.shortcuts import render
import folium
import pandas as pd
from .models import SearchCriteria
import os

from .forms import SearchCriteriaForm
import data_collection.domain_dev_data as ddd


# Create your views here.
def build_map(request):
    m = folium.Map(location=[-33.8898, 151.2134], zoom_start=14)
    m = m._repr_html_()
    context = {'m': m}

    if request.method == "POST":
        # Get user input
        suburb = request.POST.get('suburb')
        bedrooms = request.POST.get('bedrooms')
        bathrooms = request.POST.get('bathrooms')
        cars = request.POST.get('cars')
        print(suburb, bedrooms, bathrooms, cars)

        # Get Domain API Response data
        token = ddd.get_access_token()
        dicts = ddd.get_agencies_listings(token, suburb, bedrooms, bathrooms, cars)
        df = ddd.convert_to_df.convert_dict_to_df(dicts)
        locations = df[['Latitude', 'Longitude']]
        location_list = locations.values.tolist()

        # Get school data
        df_schools = pd.read_csv('data_sources/school-locations-clean.csv')
        df_schools = df_schools[df_schools['suburb'] == suburb]
        school_locations = df_schools[['latitude', 'longitude']]
        school_locations_list = school_locations.values.tolist()

        # Build map
        m = folium.Map(location=location_list[0], zoom_start=15)
        try:
            # visualise properties
            for point in range(0, len(location_list)):
                tooltip = "<b>Bedrooms:</b> {} <br><b>Bathrooms:</b> {} <br><b>Carspaces:</b> {}".format(
                    df['Bedrooms'][point], df['Bathrooms'][point], df['Carspaces'][point])
                folium.Marker(location_list[point], tooltip=tooltip).add_to(m)

            # visualise schools
            for point in range(0, len(school_locations_list)):
                tooltip = "<b>{}</b> <br>School Level: {}".format(df_schools['school_name'].values[point],
                                                                  df_schools['level_of_schooling'].values[point])
                folium.Marker(school_locations_list[point], tooltip=tooltip,
                              icon=folium.Icon(icon='fa-leanpub', prefix='fa', color='red')).add_to(m)

        except:
            print('')

        # Return map in html format
        m = m._repr_html_()
        context = {'m': m}
        return render(request, "map/index.html", context)

    else:
        form = SearchCriteriaForm()

    return render(request, "map/index.html", context)
