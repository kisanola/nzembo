import os
import pytest
import config

from django.test import RequestFactory
from config.settings.base import BASE_DIR
from backend.users.models import User
from backend.users.tests.factories import UserFactory

from backend.song.test.factories import (
    CategoryFactory,
    AlbumFactory,
    ArtistFactory,
    SongFactory,
    SongLinkFactory,
    LanguageFactory,
    LyricFactory
)

@pytest.fixture(autouse=True)
def media_storage(settings, tmpdir):
    settings.MEDIA_ROOT = tmpdir.strpath


@pytest.fixture
def user() -> User:
    return UserFactory()


@pytest.fixture
def request_factory() -> RequestFactory:
    return RequestFactory()

# tells pytest to conntect the existing sqlitedb instead of postgres
@pytest.fixture(scope='session')
def django_db_setup():
    config.settings.base.DATABASES['default'] = {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }

@pytest.fixture
def category():
    return CategoryFactory(category_name="rumba")

@pytest.fixture
def album():
    return AlbumFactory(album_name="Droit chemin")

@pytest.fixture
def artist():
    return ArtistFactory(first_name="Fally", is_still_alive=True)

@pytest.fixture
def dead_artist():
    return ArtistFactory(last_name="Wembadio", is_still_alive=False)

@pytest.fixture
def song(category, album, artist):
    return SongFactory(title='ca bouge pas', category=category, album=album, artist=artist)

@pytest.fixture
def song_for_dead_artist(dead_artist, category):
    return SongFactory(title='ca ne bouge pas', artist=dead_artist, category=category)

@pytest.fixture
def song_link(song):
    return SongLinkFactory(provider='youtube', song=song)

@pytest.fixture
def language():
    return LanguageFactory()

@pytest.fixture
def lyric():
    return LyricFactory()
