
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import SearchCriteriaForm
import DataCollection.domain_dev_data as ddd
from .models import SearchCriteria
import folium
import pandas as pd


def map(request):
    m = folium.Map(location=[-33.8898, 151.2134], zoom_start=14)
    m = m._repr_html_()
    context = {'m': m,}

    if request.method == "POST":
        suburb = request.POST.get('search')
        # print(suburb)

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




