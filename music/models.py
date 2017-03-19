from django.db import models
from django.core.urlresolvers import reverse  # After user submit redirects user


# A foreign_key links to some primary_key
# If some album hava a primary_key of 1


# Every new model needs to inherit from models.Model
class Album(models.Model):
    # Variables below represents columns on the database table
    artist = models.CharField(max_length=250)
    album_title = models.CharField(max_length=500)
    genre = models.CharField(max_length=100)
    album_logo = models.FileField()

    # This is the 'success' URL
    def get_absolute_url(self):
        # Reverse means redirect user
        return reverse('music:detail', kwargs={'pk': self.pk})  # kwargs (keyword args)

    # string representation that will be displayed when an object instance of that class is printed
    def __str__(self):
        return f"{self.artist} - {self.album_title}"


class Song(models.Model):
    # Sets a relationship field with model Album
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    # Cascade here will delete all songs with the same foreign_key

    file_type = models.CharField(max_length=10)
    song_title = models.CharField(max_length=250)
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.song_title


'''
on_delete=models.CASCADE | Deletes in cascade
Django emulates the behavior of the SQL constraint ON DELETE CASCADE
and also deletes the object containing the ForeignKey
'''
