from django.urls import path
from . import views

urlpatterns = [
    # path('map', views.MapView.as_view(), name='map'),
    path('map', views.build_map, name='map'),
]
