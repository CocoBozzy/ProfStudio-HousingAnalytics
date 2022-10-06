from django.urls import path
from . import views

urlpatterns=[
    path('', views.HomeView.as_view(), name='home'),
    path('contact/', views.contact, name = 'contact'),
    path('register/', views.register_page, name="register"),
	path('login/', views.login_page, name="login"),  
	path('logout/', views.logoutUser, name="logout"),

]


