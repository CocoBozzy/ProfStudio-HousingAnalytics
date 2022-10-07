from django.urls import path
from . import views

urlpatterns = [
    # path('map', views.MapView.as_view(), name='map'),
    path('map', views.build_map, name='map'),
    path('suburb_data', views.build_suburb_view, name='suburb_data'),
]

