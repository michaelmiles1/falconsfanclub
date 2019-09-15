from django.shortcuts import render
from roster.models import Roster

def roster_index(request):
    players = Roster.objects.all().order_by('number')
    context = {
        'roster': players
    }
    return render(request, 'roster_index.html', context)
