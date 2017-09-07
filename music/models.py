from django.db import models


class Album(models.Model):
    artist = models.CharField(max_length=255, name="artist")
    title = models.CharField(max_length=255, name="title")
    genre = models.CharField(max_length=255, name="genre")
    logo = models.TextField(name="logo")


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)