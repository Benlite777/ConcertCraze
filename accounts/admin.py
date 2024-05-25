from django.contrib import admin
from .models import Artist, Song, Concert# Importing Artist, Song, and Playlist from the current module

# Register your models here.
admin.site.register(Artist)
admin.site.register(Song)
admin.site.register(Concert)

