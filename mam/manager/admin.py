from django.contrib import admin

from .models import (
    Track, Album, Label, Artist
)

admin.site.register(Track)
admin.site.register(Album)
admin.site.register(Label)
admin.site.register(Artist)