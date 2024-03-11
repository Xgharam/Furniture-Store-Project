from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Items,ItemDetails

# LightingDecor
def LightingDecor(request):
    template=loader.get_template('LightingDecor.html')
    furniture=ItemDetails.objects.select_related('itemsid')
    return HttpResponse(template.render({'furniture':furniture,'request':request}))

# Details
def ShowDetails(request,id):
    template=loader.get_template('ShowDetails.html')
    furniture=ItemDetails.objects.select_related('itemsid').filter(id=id)
    context={
        'furniture':furniture,
        'request':request
    }
    return HttpResponse(template.render(context))