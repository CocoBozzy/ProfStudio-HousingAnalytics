from django.urls import path
from . import views

urlpatterns = [
    # path('map', views.MapView.as_view(), name='map'),
    path('map', views.build_map, name='map'),
    # path('suburb_data', views.build_get_suburb_view, name='get_suburb_data'),
    # path('suburb_data_graph', views.build_suburb_view_graph, name='suburb_data_graph'),
]

