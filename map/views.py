
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

import folium


# Create your views here.
# def index(request):
#     # Create Map Object
#     m = folium.Map(location=[-33.8898, 151.2134],zoom_start=12)

#     m = m._repr_html_()
#     context = {
#         'm': m,
#     }
#     return render(request, 'map/index.html',context)


#Class based Views
class MapView(TemplateView):
    template_name = 'map/index.html' 
    # Create Map Object
    m = folium.Map(location=[-33.8898, 151.2134],zoom_start=12)
    m = m._repr_html_()
    context = {'m': m,}
    extra_context = context





