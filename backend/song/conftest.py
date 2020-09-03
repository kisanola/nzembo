from datetime import date

import os
import pytest
import config

from django.urls import reverse

from rest_framework.test import APIClient

from config.settings.base import BASE_DIR

from backend.song.tests.factories import (
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

from backend.users.tests.factories import UserFactory

# tells pytest to conntect the existing sqlitedb instead of postgres
@pytest.fixture(scope='session')
def django_db_setup():
    config.settings.base.DATABASES['default'] = {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }


client_ = APIClient()


@pytest.fixture
def client():
    return client_

@pytest.fixture
def category():
    return CategoryFactory(category_name="religious")

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
    return SongFactory(title='ca ne bouge pas', artist=ArtistFactory(is_still_alive=False))

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
    return LyricRequestFactory(message='I need the lyric for this song')

@pytest.fixture
def translation():
    return TranslationFactory()

@pytest.fixture
def user():
    return UserFactory()

@pytest.fixture
def auth(user):
    client_.force_authenticate(user=user)

@pytest.fixture
def logout():
    client_.logout()

@pytest.fixture
def create_category():
    category_data = {
        'category_name': 'rumba'
    }
    return client_.post(reverse('song:categories-list'), data=category_data, format='json')

@pytest.fixture
def create_artist():
    artist_ = {
        'first_name': 'ferre',
        'last_name': 'gola',
        'is_still_alive': True,
        'date_of_birth': date(1976, 3, 3),
        'image': 'https://lastfm.freetls.fastly.net/i/u/arO/7de29a9d31b55e3ee367cecf152c0052'
    }
    return client_.post(reverse('song:artists-list'), data=artist_, format='json')

@pytest.fixture
def create_album(artist):
    album_ = {
        'album_name': 'tango to zalaki',
        'artist': artist.id
    }
    return client_.post(reverse('song:albums-list'), data=album_, format='json')

@pytest.fixture
def create_language():
    language_ = {
        'language': 'french'
    }
    return client_.post(reverse('song:languages-list'), data=language_, format='json')

@pytest.fixture
def create_song(category, album, artist):
    song_ = {
        'title': 'maboko pamba',
        'category': category.id,
        'album': album.id,
        'artist': artist.id
    }
    return client_.post(reverse('song:songs-list'), data=song_, format='json')

@pytest.fixture
def create_lyric(song, language):
    lyric_ = {
        'lyric': "Lorem Ipsum is simply dummy text of the printing",
        'song': song.id,
        'language': language.id
    }
    return client_.post(reverse('song:lyrics-list'), data=lyric_, format='json')

@pytest.fixture
def create_lyric_request(song, language):
    lyric_request_ = {
        'song': song.id,
        'language': language.id,
        'message': "I need a lyric for this song"
    }
    return client_.post(reverse('song:lyric-requests-list'), data=lyric_request_, format='json')

@pytest.fixture
def create_translation(lyric, language):
    translation_ = {
        'lyric': lyric.id,
        'language': language.id,
        'translation': "My translation"
    }
    return client_.post(reverse('song:translations-list'), data=translation_, format='json')

@pytest.fixture
def delete():
    def generic_delete_requtest(url):
        return client_.delete(url)

    return generic_delete_requtest

@pytest.fixture
def get():
    def generic_get_requtest(url):
        return client_.get(url)

    return generic_get_requtest

@pytest.fixture
def update():
    def generic_update_requtest(url, data):
        return client_.patch(url, data=data, format='json')

    return generic_update_requtest
