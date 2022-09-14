from django.shortcuts import render
import folium
import pandas as pd
from .models import SearchCriteria

from .forms import SearchCriteriaForm
import data_collection.domain_dev_data as ddd


# Create your views here.
def build_map(request):
    m = folium.Map(location=[-33.8898, 151.2134], zoom_start=14)
    m = m._repr_html_()
    context = {'m': m}

    if request.method == "POST":
        suburb = request.POST.get('suburb')
        bedrooms = request.POST.get('bedrooms')
        bathrooms = request.POST.get('bathrooms')
        cars = request.POST.get('cars')
        print(suburb, bedrooms, bathrooms, cars)

        token = ddd.get_access_token()
        dicts = ddd.get_agencies_listings(token, suburb, bedrooms, bathrooms, cars)
        df = ddd.convert_to_df.convert_dict_to_df(dicts)

        # visualisations
        locations = df[['Latitude', 'Longitude']]
        location_list = locations.values.tolist()

        m = folium.Map(location=location_list[0], zoom_start=15)
        try:
            for point in range(0, len(location_list)):
                folium.Marker(location_list[point], popup=df['ListingType'][point]).add_to(m)
        except:
            print('')

        m = m._repr_html_()
        context = {'m': m}
        return render(request, "map/index.html", context)

    else:
        form = SearchCriteriaForm()

    return render(request, "map/index.html", context)
