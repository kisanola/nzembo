import factory

from factory.django import DjangoModelFactory
from backend.song.models import (
    Category,
    Artist,
    Album,
    Song,
    SongLink,
    Lyric,
    LyricRequest,
    Language,
    Translation
)
from backend.users.tests.factories import UserFactory

class CategoryFactory(DjangoModelFactory):
    class Meta:
        model = Category
    category_name = factory.Faker('word')


class ArtistFactory(DjangoModelFactory):
    class Meta:
        model = Artist
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    is_still_alive = factory.Iterator([True, False])


class AlbumFactory(DjangoModelFactory):
    class Meta:
        model = Album
    album_name = factory.Faker('sentence', nb_words=5)
    artist = factory.SubFactory(ArtistFactory)


class SongFactory(DjangoModelFactory):
    class Meta:
        model = Song
    title = factory.Faker('sentence', nb_words=3)
    slug = factory.Faker('slug', value=title)
    category = factory.SubFactory(CategoryFactory)
    album = factory.SubFactory(AlbumFactory)
    artist = factory.SubFactory(ArtistFactory)


class SongLinkFactory(DjangoModelFactory):
    class Meta:
        model = SongLink
    provider = factory.Faker('word')
    link = factory.Faker('url')
    song = factory.SubFactory(SongFactory)


class LanguageFactory(DjangoModelFactory):
    class Meta:
        model = Language

    language = factory.Faker('language_name')


class LyricFactory(DjangoModelFactory):
    class Meta:
        model = Lyric
    user = factory.SubFactory(UserFactory)
    song = factory.SubFactory(SongFactory)
    language = factory.SubFactory(LanguageFactory)
    lyric = factory.Faker('text', max_nb_chars=200)


class LyricRequestFactory(DjangoModelFactory):
    class Meta:
        model = LyricRequest
    user = factory.SubFactory(UserFactory)
    song = factory.SubFactory(SongFactory)
    language = factory.SubFactory(LanguageFactory)
    message = factory.Faker('text', max_nb_chars=100)


class TranslationFactory(DjangoModelFactory):
    class Meta:
        model = Translation
    user = factory.SubFactory(UserFactory)
    lyric = factory.SubFactory(LyricFactory)
    language = factory.SubFactory(LanguageFactory)
    translation = factory.Faker('text', max_nb_chars=200)
