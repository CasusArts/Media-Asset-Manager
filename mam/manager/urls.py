from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('tracks/', views.list_all_tracks, name='tracks'),
    path('tracks/<int:track_id>/', views.track_details, name='track_details'),
]
