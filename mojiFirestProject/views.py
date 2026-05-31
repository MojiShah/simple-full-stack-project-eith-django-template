from django.shortcuts import render

def homePage(request):
    return render(request=request,template_name='home.html')

def aboutPage(request):
    context = {
        'name':'Javad',
        'profile' : {
            'job':'accountant',
            'age':29
        }
    }
    return render(request=request,template_name='about.html',context=context)