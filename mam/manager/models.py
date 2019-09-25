from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.db import models
from django.urls import reverse
from django_countries.fields import CountryField


class Artist(models.Model):
    artist_name = models.CharField(max_length=120, blank=False)
    artist_label = models.CharField(max_length=120)
    artist_country = CountryField(default="DE")

    class Meta:
        verbose_name = "Artist"
        verbose_name_plural = verbose_name + "s"

    def __str__(self):
        return self.artist_name

    def get_absolute_url(self):
        return reverse("artist_detail", kwargs={"pk": self.pk})


class Album(models.Model):
    album_title = models.CharField(max_length=120, default="Unknown Album")
    album_artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    album_year = models.IntegerField()
    album_genre = models.CharField(max_length=120)

    class Meta:
        verbose_name = "Album"
        verbose_name_plural = "Albums"

    def get_absolute_url(self):
        return reverse("album_detail", kwargs={"pk": self.pk})


class Label(models.Model):
    label_name = models.CharField(max_length=120)
    label_address = models.TextField(max_length=120)
    label_genre = models.CharField(max_length=120)
    label_country = CountryField(default='DE')

    class Meta:
        verbose_name = "Label"
        verbose_name_plural = verbose_name + "s"

    def get_absolute_url(self):
        return reverse("label_detail", kwargs={"pk": self.pk})


class Track(models.Model):
    track_title = models.CharField(max_length=120, default="Unknown Track")
    # track_artist = models.CharField(max_length=120, default="Unknown Artist")
    track_artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    track_album = models.CharField(max_length=120, default="Unknown Album")
    track_genre = models.CharField(max_length=100)
    track_year = models.IntegerField()
    track_comment = models.TextField()

    class Meta:
        verbose_name = "Track"
        verbose_name_plural = verbose_name + "s"

    def __str__(self):
        return f"{self.track_artist} - {self.track_title}"
