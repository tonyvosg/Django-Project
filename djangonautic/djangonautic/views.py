from django.http import HttpResponse
from django.shortcuts import render
def about(request):
    #return HttpResponse('About');
    return render(request, 'pyhomepage.html')
def home(request):
    #return HttpResponse('Homepage');
    return render(request, 'about.html')