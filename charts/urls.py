from django.urls import path
from . import views

urlpatterns = [
    path('charts', views.ChartView.as_view(), name='charts'),
]