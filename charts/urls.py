from django.urls import path
from . import views

urlpatterns = [
    path('chart', views.ChartView.as_view()),
]