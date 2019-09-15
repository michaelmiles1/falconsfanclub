from django.shortcuts import render
from home.models import Home

def home_index(request):
    home = Home.objects.all()
    context = {
        "home": home
    }
    return render(request, "home_index.html", context)
