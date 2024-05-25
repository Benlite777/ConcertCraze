from django.db import models
from django.contrib.auth.models import User

class Artist(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200, default="No description provided.")
    image = models.ImageField(upload_to='artist_images', null=True, blank=True)  # ImageField added
    
    def __str__(self):
        return self.name

class Song(models.Model):
    title = models.CharField(max_length=100)
    artist = models.ForeignKey(Artist, related_name='songs', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title

class Concert(models.Model):
    artists = models.ManyToManyField(Artist, related_name='concerts')  
    place = models.CharField(max_length=100)
    date = models.DateField()
    
    def __str__(self):
        artists_names = ", ".join(str(artist) for artist in self.artists.all())
        return f"{artists_names}'s Concert at {self.place} on {self.date}"
