from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')

    
def fale_conosco(request):
    return render(request, 'fale_conosco.html')
