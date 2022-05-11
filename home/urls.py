from django.urls import path
from . import views

urlpatterns=[
    path('', views.HomeView.as_view(), name='home'),
    path('authorized', views.AuthorizedView.as_view()),
    path('contact/', views.contact, name = 'contact'),
]