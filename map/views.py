
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

import folium
import pandas as pd

from .forms import SearchCriteriaForm
import DataCollection.domain_dev_data as ddd

from .models import SearchCriteria

def map(request):
    m = folium.Map(location=[-33.8898, 151.2134], zoom_start=14)
    m = m._repr_html_()
    context = {'m': m,}

    if request.method == "POST":
        suburb = request.POST.get('search')
        print(suburb)

        token = ddd.get_access_token()
        dicts = ddd.get_agencies_listings(token, suburb)
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
        context = {'m': m,}
        extra_context = context
        return render(request, "map/index.html", context)

    else:
        form = SearchCriteriaForm()

    return render(request, "map/index.html",context)


# Create your views here.
# def index(request):
#     # Create Map Object
#     m = folium.Map(location=[-33.8898, 151.2134],zoom_start=12)

#     m = m._repr_html_()
#     context = {
#         'm': m,
#     }
#     return render(request, 'map/index.html',context)


#JOELS STUFF 
# #get Saved locations
# locations = pd.read_csv("map/templates/map/saved_locations.csv", index_col=0)
# #print(locations)
# location_list = locations.values.tolist()
# # len(location_list)
# # print(location_list[0])

# #Class based Views
# class MapView(TemplateView):
#     template_name = 'map/index.html' 

#     # Create Map Object
#     #Rachel Map Code
#     m = folium.Map(location=location_list[0], zoom_start=14)
#     for point in range(0, len(location_list)):
#         folium.Marker(location_list[point]).add_to(m)
#     m = m._repr_html_()
#     context = {'m': m,}
#     extra_context = context


#     #m = folium.Map(location=[-33.8898, 151.2134],zoom_start=12)




