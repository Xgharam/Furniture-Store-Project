from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Items,ItemDetails

# Bedrooms
def Bedrooms(request):
    template=loader.get_template('Bedrooms.html')
    furniture=ItemDetails.objects.select_related('itemsid')
    return HttpResponse(template.render({'furniture':furniture,'request':request}))

# Details
def BedroomsDetails(request,id):
    template=loader.get_template('BedroomsDetails.html')
    furniture=ItemDetails.objects.select_related('itemsid').filter(id=id)
    context={
        'furniture':furniture,
        'request':request
    }
    return HttpResponse(template.render(context))