from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

# def home(request):
#     return render(request,'home/welcome.html',{})

# @login_required(login_url = '/admin')
# def authorized(request):
#     return render(request, 'home/authorized.html',{})




#Class based Views
class HomeView(TemplateView):
    template_name = 'home/welcome.html' 
    extra_context = {'today': datetime.today()}

class AuthorizedView(LoginRequiredMixin, TemplateView):
    template_name = 'home/authorized.html'
    login_url = '/admin'



def contact(request):
    """View function for home page of site."""
    # Render the HTML template index.html with the data in the context variable
    return render(request, 'home/contact.html')




