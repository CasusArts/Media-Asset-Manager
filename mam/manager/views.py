from django.shortcuts import render, get_object_or_404

from .models import Track, Artist, Label, Album


def index(request):
    context = {'home_page': 'active'}
    return render(request, 'manager/index.html', context)


def list_all_tracks(request):
    all_tracks = Track.objects.order_by('track_year')
    context = {
        'all_tracks': all_tracks,
        'tracks_page': 'active'
    }
    return render(request, 'manager/tracks.html', context)


def track_details(request, track_id):
    track = get_object_or_404(Track, pk=track_id)
    context = {'track': track}

    return render(request, 'manager/track_detail.html', context)