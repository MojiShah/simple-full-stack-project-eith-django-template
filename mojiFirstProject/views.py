from django.shortcuts import render
from . import models

def homePage(request):
    return render(request=request,template_name='home.html')

def aboutPage(request):
    persons = models.Person.objects.all()

    context = {
        'name':'Javad',
        'profile' : {
            'job':'accountant',
            'age':29
        },
        'people':persons
    }
    return render(request=request,template_name='about.html',context=context)