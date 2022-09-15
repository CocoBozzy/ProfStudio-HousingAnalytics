from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.core.exceptions import *


def search(request):
    return render(request, 'form.html')

    # if request.method == 'POST':
    #     search_id = request.POST.get('textfield', None)
    #     try:
    #         user = Person.objects.get(name = search_id)
    #         #do something with user
    #         html = ("<H1>%s</H1>", user)
    #         return HttpResponse(html)
    #     except Person.DoesNotExist:
    #         return HttpResponse("no such user")
    # else:
    #     return render(request, 'form.html')
