import pytest

from django.urls import reverse

from rest_framework.status import (
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_204_NO_CONTENT,
    HTTP_403_FORBIDDEN,
)
from rest_framework.test import APIClient

from backend.song.models import Artist


pytestmark = pytest.mark.django_db


class TestCategory:

    def generic_get_request(self, url):
        client = APIClient()
        return client.get(url)

    def test_create_category(self, auth, create_category):

        assert create_category.status_code == HTTP_201_CREATED
        assert create_category != {}

    def load_category_list(self, create_category):
        response = self.generic_get_request(reverse('song:categories-list'))

        assert response.status_code == HTTP_200_OK
        assert response.data
        assert response.data['results'] != []

    def test_load_category_list_filtered(self, create_category):
        response = self.generic_get_request(f"{reverse('song:categories-list')}?category_name=rumba")

        assert response.status_code == HTTP_200_OK
        assert response.data['results'][0]['category_name'] == 'rumba'
        assert response.data['results'] != []

    def test_load_category_detail(self, create_category):
        response = self.generic_get_request(reverse('song:categories-detail', args=[1]))

        assert response.status_code == HTTP_200_OK
        assert response.data['category_name'] == 'rumba'

    def test_create_category_with_un_authorized_credentials(self, logout, create_category):

        assert create_category.status_code == HTTP_403_FORBIDDEN

    def test_update_category_put_request(self, auth, client, create_category):
        response = client.put(reverse('song:categories-detail', args=[1]), data={'category_name': 'ndombolo'}, format='json')

        assert response.status_code == HTTP_200_OK
        assert response.data['category_name'] == 'ndombolo'

    def test_delete_category_delete_request(self, create_category, delete):
        response = delete(reverse('song:categories-detail', args=[1]))

        assert response.status_code == HTTP_204_NO_CONTENT


class TestArtistsView:
    def test_creation_of_artist(self, create_artist):

        assert create_artist.status_code == HTTP_201_CREATED
        assert create_artist.data != {}
        assert create_artist.data['first_name'] == 'ferre'

    def test_loads_artist_list(self, create_artist, get):
        response = get(reverse('song:artists-list'))

        assert response.status_code == HTTP_200_OK
        assert response.data['results'][0]['last_name'] == 'gola'
        assert len(response.data['results']) == 1

    def test_update_artist_put_request(self, create_artist, update):
        id = create_artist.data['id']
        response = update(reverse('song:artists-detail', args=[id]), {'first_name': 'wemba'})

        assert response.status_code == HTTP_200_OK
        assert response.data['first_name'] == 'wemba'

    def test_delete_artist_delete_request(self, create_artist, delete):
        id = create_artist.data['id']
        response = delete(reverse('song:artists-detail', args=[id]))

        assert response.status_code == HTTP_204_NO_CONTENT


class TestAlbums:
    def test_creation_of_album(self, artist, create_album):

        assert create_album.status_code == HTTP_201_CREATED
        assert create_album.data['album_name'] == 'tango to zalaki'

    def test_load_album_list(self, create_artist, create_album, get):
        response = get(reverse('song:albums-list'))

        assert response.status_code == HTTP_200_OK
        assert response.data['results'][0]['album_name'] == 'tango to zalaki'

    def test_load_album_detail(self, create_artist, create_album, get):
        response = get(reverse('song:albums-detail', args=[1]))

        assert response.status_code == HTTP_200_OK
        assert response.data['album_name'] == 'tango to zalaki'

    def test_load_album_list_filtered(self, create_artist, create_album, get):
        response = get(f"{reverse('song:albums-list')}?album_name=tango+to+zalaki&artist=1")

        assert response.status_code == HTTP_200_OK
        assert response.data['results'][0]['album_name'] == 'tango to zalaki'

    def test_update_album_patch_request(self, create_artist, create_album, update):
        response = update(reverse('song:albums-detail', args=[1]), {'album_name': 'droit chemin'})

        assert response.status_code == HTTP_200_OK
        assert response.data['album_name'] == 'droit chemin'

    def test_delete_album_delete_request(self, create_artist, create_album, delete):
        response = delete(reverse('song:albums-detail', args=[1]))

        assert response.status_code == HTTP_204_NO_CONTENT


class TestSong:
    def test_creation_of_song(self, category, artist, album, create_song):

        assert album != {}
        assert category != {}
        assert artist != {}

        assert create_song.status_code == HTTP_201_CREATED
        assert create_song.data['title'] == 'maboko pamba'
        assert create_song.data['artist'] == artist.id

    def test_loads_songs_list(self, category, artist, album, create_song, get):
        response = get(reverse('song:songs-list'))

        assert response.status_code == HTTP_200_OK
        assert response.data['results'][0]['title'] == 'maboko pamba'
        assert len(response.data['results']) == 1

    def test_update_songs_patch_request(self, category, artist, album, create_song, update):
        response = update(reverse('song:songs-detail', args=[1]), data={'title': 'malewa'})

        assert response.status_code == HTTP_200_OK
        assert response.data['title'] == 'malewa'

    def test_delete_songs_delete_request(self, category, artist, album, create_song, delete):
        response = delete(reverse('song:songs-detail', args=[1]))
        
        assert response.status_code == HTTP_204_NO_CONTENT


class TestLanguage:
    def test_creation_of_language(self, create_language):
        
        assert create_language.status_code == HTTP_201_CREATED
        assert create_language.data['language'] == 'french'

    def test_loads_languages_list(self, create_language, get):
        response = get(reverse('song:languages-list'))

        assert response.status_code == HTTP_200_OK
        assert response.data['results'][0]['language'] == 'french'
        assert len(response.data['results']) == 1

    def test_load_album_detail(self, create_language, get):
        response = get(reverse('song:languages-detail', args=[1]))

        assert response.status_code == HTTP_200_OK
        assert response.data['language'] == 'french'

    def test_load_album_list_filtered(self, create_language, get):
        response = get(f"{reverse('song:languages-list')}?language=french")

        assert response.status_code == HTTP_200_OK
        assert response.data['results'][0]['language'] == 'french'

    def test_update_language_patch_request(self, create_language, update):
        response = update(reverse('song:languages-detail', args=[1]), data={'language': 'english'})

        assert response.status_code == HTTP_200_OK
        assert response.data['language'] == 'english'

    def test_delete_language_delete_request(self, create_language, delete):
        response = delete(reverse('song:languages-detail', args=[1]))
        
        assert response.status_code == HTTP_204_NO_CONTENT


class TestLyric():
    def test_creation_of_lyric(self, user, language, song, create_lyric):
        
        assert create_lyric.status_code == HTTP_201_CREATED
        assert create_lyric.data != {}
        assert create_lyric.data['lyric'] == 'Lorem Ipsum is simply dummy text of the printing'

    def test_loads_lyrics_list(self, user, song, create_language, create_lyric, get):
        response = get(reverse('song:lyrics-list'))

        assert response.status_code == HTTP_200_OK
        assert response.data['results'][0]['lyric'] == 'Lorem Ipsum is simply dummy text of the printing'
        assert response.data['results'][0]['user'] == user.id
        assert len(response.data['results']) == 1

    def test_update_lyrics_put_request(self, user, song, language, create_lyric, update):
        response = update(reverse('song:lyrics-detail', args=[1]), data={'lyric': 'this is my new lyric'})

        assert response.status_code == HTTP_200_OK
        assert response.data['lyric'] == 'this is my new lyric'
        assert response.data['user'] == user.id

    def test_delete_lyrics_delete_request(self, user, language, song, create_lyric, delete):
        response = delete(reverse('song:lyrics-detail', args=[1]))
        
        assert response.status_code == HTTP_204_NO_CONTENT


class TestLyricRequest():
    def  test_creation_of_lyric(self, user, language, song, create_lyric_request):
        
        assert create_lyric_request.status_code == HTTP_201_CREATED
        assert create_lyric_request.data['message'] == 'I need a lyric for this song'

    def test_loads_lyric_request_list(self, user, language, song, create_lyric_request, get):
        response = get(reverse('song:lyric-requests-list'))

        assert response.status_code == HTTP_200_OK
        assert response.data['results'][0]['message'] == 'I need a lyric for this song'
        assert response.data['results'][0]['user'] == user.id

    def test_update_lyric_request_patch_request(self, user, language, song, create_lyric_request, update):
        response = update(reverse('song:lyric-requests-detail', args=[1]), data={'message': 'my updated message'})

        assert response.status_code == HTTP_200_OK
        assert response.data['message'] == 'my updated message'
        assert response.data['user'] == user.id

    def delete_lyric_request_delete_request(self, user, song, language, create_lyric_request, delete):
        response = delete(reverse('song:lyric-requests-detail'))
    
        assert response.status_code == HTTP_204_NO_CONTENT


class TranslationTestCase():
    def  test_creation_of_translation(self, user, language, lyric, create_translation):

        assert create_transaltion.status_code == HTTP_201_CREATED
        assert create_translation.data['translation'] == 'My translation'
        assert create_translation.data['user'] == user.id
        assert response.data['lyric'] == lyric.id

    def test_loads_translation_list(self, user, language, lyric, create_transaltion, get):
        response = get(reverse('song:translations-list'))

        assert response.status_code == HTTP_200_OK
        assert response.data['results'][0]['translation'] == 'My translation'
        assert response.data['results'][0]['lyric'] == lyric.id
        assert response.data['results'][0]['user'] == user.id

    def test_update_translation_put_request(self, user, lyric, language, create_transaltion, update):
        response = update(reverse('song:translations-detail', args=[1]), data={'translation': 'My new translation'})

        assert response.status_code == HTTP_200_OK
        assert response.data['translation'] == 'My new translation'
        assert response.data['user'] == user.id

    def test_delete_translation_delete_request(self, user, lyric, language, create_transaltion, delete):
        response = delete(reverse('song:translations-detail', args=[1]))

        assert response.status_code == HTTP_204_NO_CONTENT
