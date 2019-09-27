from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('tracks/', views.list_all_tracks, name='tracks'),
]
