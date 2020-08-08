from django.db import models
from backend.users.models import User

class Base(models.Model):
    date_added = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(Base):
    category_name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.category_name


class Artist(Base):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    is_still_alive = models.BooleanField(default=True)
    image = models.URLField(max_length=255, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{ self.first_name }, { self.last_name }, { self.is_still_alive }"


class Album(Base):
    album_name = models.CharField(max_length=50, unique=True)
    artist = models.ForeignKey('Artist', related_name='albums', on_delete=models.CASCADE)

    def __str__(self):
        return self.album_name


class Song(Base):
    title = models.CharField(max_length=100, unique=True)
    category = models.ForeignKey('Category', related_name='category_songs', on_delete=models.CASCADE)
    album = models.ForeignKey('Album', related_name='album_songs', on_delete=models.CASCADE)
    artist = models.ForeignKey('Artist', related_name='artist_songs', on_delete=models.CASCADE)
    date_published = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title


class SongLink(Base):
    provider = models.CharField(max_length=50)
    link = models.TextField()
    song = models.ForeignKey('Song', related_name='links', on_delete=models.CASCADE)

    def __str__(self):
        return f"{ self.provider }, { self.link }"


class Language(Base):
    language = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.language


class Lyric(Base):
    user = models.ForeignKey('users.User', related_name='user_lyrics', on_delete=models.CASCADE)
    song = models.ForeignKey('Song', related_name='song_lyrics', on_delete=models.CASCADE)
    language = models.ForeignKey('Language', related_name='language_lyric', on_delete=models.CASCADE)
    lyric = models.TextField(null=False, blank=False)

    def __str__(self):
        return self.date_added


class LyricRequest(Base):
    song = models.ForeignKey('Song', related_name='song_lyric_requests', on_delete=models.CASCADE)
    user = models.ForeignKey('users.User', related_name='user_lyric_requests', on_delete=models.CASCADE)
    language = models.ForeignKey('Language', related_name='language_lyric_requests', on_delete=models.CASCADE)
    message = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.id


class Translation(Base):
    lyric = models.ForeignKey('Lyric', related_name='lyric_translations', on_delete=models.CASCADE)
    user = models.ForeignKey('users.User', related_name='user_translations', on_delete=models.CASCADE)
    language = models.ForeignKey('Language', related_name='language_translations', on_delete=models.CASCADE)
    translation = models.TextField()

    def __str__(self):
        return self.id
