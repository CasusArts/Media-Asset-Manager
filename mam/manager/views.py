from django.http import HttpResponse
from django.shortcuts import render

from .models import Track, Artist, Label, Album


def index(request):
    return render(request, 'manager/index.html')


def all_tracks(request):
    all_tracks = Track.objects.order_by('track_year')
    context = {
        'all_tracks': all_tracks,
    }
    return render(request, 'manager/tracks.html', context)


