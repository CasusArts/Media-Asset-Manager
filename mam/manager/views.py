from django.template import loader
from django.shortcuts import render
from django.http import HttpResponse

from .models import Track, Artist, Label, Album


def index(request):
    all_tracks = Track.objects.order_by('track_year')
    context = {
        'all_tracks': all_tracks,
    }
    return render(request, 'manager/index.html', context)