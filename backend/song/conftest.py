import os
import pytest
import config

from config.settings.base import BASE_DIR

from backend.song.test.factories import (
    CategoryFactory,
    AlbumFactory,
    ArtistFactory,
    SongFactory,
    SongLinkFactory,
    LanguageFactory,
    LyricFactory,
    LyricRequestFactory,
    TranslationFactory
)

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
def song():
    return SongFactory(title='ca bouge pas')

@pytest.fixture
def song_for_dead_artist():
    return SongFactory(title='ca ne bouge pas')

@pytest.fixture
def song_link():
    return SongLinkFactory(provider='youtube')

@pytest.fixture
def language():
    return LanguageFactory()

@pytest.fixture
def lyric():
    return LyricFactory()

@pytest.fixture
def lyric_request():
    return LyricRequestFactory(message='need the lyric for this song')

@pytest.fixture
def translation():
    return TranslationFactory()
