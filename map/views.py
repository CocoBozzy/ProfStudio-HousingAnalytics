
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

import folium
import pandas as pd


# Create your views here.
# def index(request):
#     # Create Map Object
#     m = folium.Map(location=[-33.8898, 151.2134],zoom_start=12)

#     m = m._repr_html_()
#     context = {
#         'm': m,
#     }
#     return render(request, 'map/index.html',context)

#get Saved locations
locations = pd.read_csv("map/templates/map/saved_locations.csv", index_col=0)
#print(locations)
location_list = locations.values.tolist()
# len(location_list)
# print(location_list[0])

#Class based Views
class MapView(TemplateView):
    template_name = 'map/index.html' 

    # Create Map Object
    #Rachel Map Code
    m = folium.Map(location=location_list[0], zoom_start=14)
    for point in range(0, len(location_list)):
        folium.Marker(location_list[point]).add_to(m)
    m = m._repr_html_()
    context = {'m': m,}
    extra_context = context


    #m = folium.Map(location=[-33.8898, 151.2134],zoom_start=12)




