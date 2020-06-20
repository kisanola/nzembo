from django.db import models
from backend.users.models import User
from django.utils.text import slugify


class Category(models.Model):
    category_name = models.CharField(max_length=50, unique=True)
    date_added = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.category_name


class Album(models.Model):
    album_name = models.CharField(max_length=50, unique=True)
    date_added = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.album_name


class Artist(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    is_still_alive = models.BooleanField(default=False)
    image = models.CharField(max_length=100, null=True)
    date_of_birth = models.DateField(null=True)
    date_of_death = models.DateField(null=True)
    date_added = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{ self.first_name }, { self.last_name }, { self.is_still_alive }"


class Song(models.Model):
    title = models.CharField(max_length=100)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    album = models.ForeignKey('Album', on_delete=models.CASCADE)
    artist = models.ForeignKey('Artist', on_delete=models.CASCADE)
    date_published = models.DateField(null=True)
    slug = models.SlugField(default='', editable=False, max_length=100, unique=True)
    date_added = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Song, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class SongLink(models.Model):
    provider = models.CharField(max_length=50)
    link = models.TextField()
    song = models.ForeignKey('Song', on_delete=models.CASCADE)
    dete_added = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{ self.provider }, { self.link }"


class Language(models.Model):
    language = models.CharField(max_length=30, unique=True)
    date_added = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.language


class Lyric(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    song = models.ForeignKey('Song', on_delete=models.CASCADE)
    language = models.ForeignKey('Language', on_delete=models.CASCADE)
    lyric = models.TextField()
    date_added = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.date_added


class LyricRequest(models.Model):
    lyric = models.ForeignKey('Lyric', on_delete=models.CASCADE)
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    language = models.ForeignKey('Language', on_delete=models.CASCADE)
    message = models.CharField(max_length=200, null=True)
    date_requested = models.DateTimeField(auto_now=True)


class Translation(models.Model):
    lyric = models.ForeignKey('Lyric', on_delete=models.CASCADE)
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    language = models.ForeignKey('Language', on_delete=models.CASCADE)
    translation = models.TextField()
    date_added = models.DateTimeField(auto_now=True)
