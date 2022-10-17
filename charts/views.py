from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from .models import House
import pandas as pd
import json
from django.utils.safestring import mark_safe
from django.contrib.auth.decorators import login_required

# Create your views here.

#Class based Views
class ChartView(TemplateView):
    template_name = 'charts/chart.html' 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["qs"]= House.objects.all()
        return context


@login_required(login_url='login')
def chart_data(request):
    #Get CSV file
    data = pd.read_csv("data_sources/SydneyHousing.csv")

    #Convert columns to a list array
    labels=  list(data['Suburb'])
    datas = list(data['No.Sales'])

    #Return context as safe json 
    context = {"labels": mark_safe(json.dumps(labels)), "datas": mark_safe(json.dumps(datas))}

    return render(request, 'charts/deluxe_charts.html',context)





