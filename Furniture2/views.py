from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Items,ItemDetails

# Sofas
def Sofas(request):
    template=loader.get_template('Sofas.html')
    furniture=ItemDetails.objects.select_related('itemsid')
    return HttpResponse(template.render({'furniture':furniture,'request':request}))

# Details
def SofasDetails(request,id):
    template=loader.get_template('SofasDetails.html')
    furniture=ItemDetails.objects.select_related('itemsid').filter(id=id)
    context={
        'furniture':furniture,
        'request':request
    }
    return HttpResponse(template.render(context))