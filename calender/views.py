from django.shortcuts import render
from .models import celenderEvent as ce

# Create your views here.

def index(request):
    event=ce.objects.values()
    params={'events':event}
    return(render(request, 'index.html',params))
