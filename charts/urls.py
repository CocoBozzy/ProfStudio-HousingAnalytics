from django.urls import path
from . import views

urlpatterns = [
    path('charts', views.ChartView.as_view(), name='charts'),
    path('deluxe_charts', views.chart_data, name='premium_charts'),
]