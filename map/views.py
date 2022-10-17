from multiprocessing import context
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from charts.models import House
from django.template.response import TemplateResponse
from django.template.context_processors import request
import json
from django.contrib import messages
# from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# from datetime import datetime
# from django.views.generic import TemplateView
# from django.contrib.auth.mixins import LoginRequiredMixin
# from .forms import SearchCriteriaForm
# import DataCollection.domain_dev_data as ddd
# from .models import SearchCriteria
# import folium
# import pandas as pd

import folium
import pandas as pd
from .models import SearchCriteria
import os

from .forms import SearchCriteriaForm
import data_collection.domain_dev_data as ddd
import callumdomaintest as suburbInfo


# Create your views here.

@login_required(login_url='login')
def build_map(request):
    m = folium.Map(location=[-33.8898, 151.2134], zoom_start=14)
    m = m._repr_html_()
    context = {'m': m}
    map_error_message = ''
    graph_error_message = ''

    if request.method == "POST":

        # Get user input
        suburb = request.POST.get('suburb')
        bedrooms = request.POST.get('bedrooms')
        bathrooms = request.POST.get('bathrooms')
        cars = request.POST.get('cars')
        postcode = request.POST.get('postcode')
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
        try:
            m = folium.Map(location=location_list[0], zoom_start=15)
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

            m = m._repr_html_()

        except:
            m = folium.Map(location=[-33.8898, 151.2134], zoom_start=14)
            m = m._repr_html_()
            map_error_message = 'There are no properties for sale that meet the criteria.'

        # Build graph
        try:
            token2 = suburbInfo.get_access_token()
            suburbSalesData = suburbInfo.get_sales_per_suburb_per_year(token2, suburb, postcode, bedrooms)

            suburbSalesDataYearList = list(suburbSalesData)
            suburbSalesDataSoldList = list(suburbSalesData.values())
            request.session['suburbSalesDataYearList'] = suburbSalesDataYearList
            request.session['suburbSalesDataSoldList'] = suburbSalesDataSoldList
            request.session['suburb'] = suburb.capitalize()

            if isinstance(suburbSalesData, dict):
                messages.error(request, "Error: This is the sample error Flash message.")

            labels = json.dumps(request.session['suburbSalesDataYearList'])
            print(labels)
            data = json.dumps(request.session['suburbSalesDataSoldList'])
            suburb = request.session['suburb']

        except:
            graph_error_message = 'There are no historical values for sales in this suburb.'
            labels = []
            data = []
            suburb = suburb

        # Build context with map and graph
        context = {
            'm': m,
            'map_error_message': map_error_message,
            'graph_error_message': graph_error_message,
            'labels': labels,
            'data': data,
            'suburb': suburb
        }

        return render(request, "map/index.html", context)

    else:
        form = SearchCriteriaForm()

    return render(request, "map/index.html", context)
