from django.http import HttpResponse
from django.shortcuts import render


#######################################################################
def about(request):
    #return HttpResponse('Hello there - <a href="/david">Davids page</a>')
    return render(request, 'about.html')

#######################################################################
def home(request):
    vbls = {'pagename': "the main homepage"}
    return render(request, 'home.html', vbls)

#######################################################################
def david(request):
    vbls = {'pagename': "David's page"}
    return render(request, 'home.html', vbls)
