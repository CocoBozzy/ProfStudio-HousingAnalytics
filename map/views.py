from django.shortcuts import render
from django.http import HttpResponse

import folium


# Create your views here.
def index(request):
    # Create Map Object
    m = folium.Map(location=[-33.8898, 151.2134],zoom_start=12)

    m = m._repr_html_()
    context = {
        'm': m,
    }
    return render(request, 'map/index.html',context)





