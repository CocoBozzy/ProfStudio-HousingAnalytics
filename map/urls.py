from django.urls import path
from . import views

urlpatterns = [
    path('map', views.new, name='map'),
    # path('map', views.map),
]
