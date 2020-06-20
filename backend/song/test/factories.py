import factory

from backend.song import models
from backend.users.tests.factories import UserFactory

class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Category
    category_name = factory.Faker('word')


class AlbumFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Album
    album_name = factory.Faker('sentence', nb_words=5)


class ArtistFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Artist
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    is_still_alive = factory.Iterator([True, False])


class SongFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Song
    title = factory.Faker('sentence', nb_words=3)
    category = factory.SubFactory(CategoryFactory)
    album = factory.SubFactory(AlbumFactory)
    artist = factory.SubFactory(ArtistFactory)
    slug = factory.Faker('slug', value=title)


class SongLinkFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.SongLink
    provider = factory.Faker('word')
    link = factory.Faker('url')
    song = factory.SubFactory(SongFactory)


class LanguageFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Language

    language = factory.Faker('language_name')


class LyricFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Lyric
    user = factory.SubFactory(UserFactory)
    song = factory.SubFactory(SongFactory)
    language = factory.SubFactory(LanguageFactory)
    lyric = factory.Faker('text', max_nb_chars=200)
