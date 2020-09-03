from django.db import models
from django.utils.text import slugify

from backend.users.models import User

class Base(models.Model):
    date_added = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(Base):
    category_name = models.CharField(max_length=50, unique=True)


class Artist(Base):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    is_still_alive = models.BooleanField(default=True)
    image = models.URLField(max_length=255, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField(null=True, blank=True)


class Album(Base):
    album_name = models.CharField(max_length=255, unique=True)
    artist = models.ForeignKey('Artist', related_name='albums', on_delete=models.CASCADE)


class Song(Base):
    title = models.CharField(max_length=100, unique=True)
    category = models.ForeignKey('Category', related_name='songs', on_delete=models.CASCADE)
    album = models.ForeignKey('Album', related_name='songs', on_delete=models.CASCADE)
    artist = models.ForeignKey('Artist', related_name='songs', on_delete=models.CASCADE)
    date_published = models.DateField(null=True, blank=True)
    slug = models.SlugField(default='', editable=False, max_length=100, unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Song, self).save(*args, **kwargs)


class SongLink(Base):
    provider = models.CharField(max_length=50)
    link = models.TextField()
    song = models.ForeignKey('Song', related_name='links', on_delete=models.CASCADE)


class Language(Base):
    language = models.CharField(max_length=30, unique=True)


class Lyric(Base):
    user = models.ForeignKey('users.User', related_name='lyrics', on_delete=models.CASCADE)
    song = models.ForeignKey('Song', related_name='lyrics', on_delete=models.CASCADE)
    language = models.ForeignKey('Language', related_name='lyrics', on_delete=models.CASCADE)
    lyric = models.TextField(null=False, blank=False)


class LyricRequest(Base):
    song = models.ForeignKey('Song', related_name='lyric_requests', on_delete=models.CASCADE)
    user = models.ForeignKey('users.User', related_name='lyric_requests', on_delete=models.CASCADE)
    language = models.ForeignKey('Language', related_name='lyric_requests', on_delete=models.CASCADE)
    message = models.CharField(max_length=200, null=True, blank=True)


class Translation(Base):
    lyric = models.ForeignKey('Lyric', related_name='translations', on_delete=models.CASCADE)
    user = models.ForeignKey('users.User', related_name='translations', on_delete=models.CASCADE)
    language = models.ForeignKey('Language', related_name='translations', on_delete=models.CASCADE)
    translation = models.TextField()
