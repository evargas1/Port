from django.shortcuts import render
from projects.models import Project
# Create your views here.

def index(request):
    context = {}
    return render(request, 'projects/index.html', context)