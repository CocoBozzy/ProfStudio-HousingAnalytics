from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from .models import House

# Create your views here.

#Class based Views
class ChartView(TemplateView):
    template_name = 'charts/chart.html' 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["qs"]= House.objects.all()
        return context



