import pytest

from django.urls import reverse

from rest_framework.status import (
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_204_NO_CONTENT,
    HTTP_403_FORBIDDEN,
)

from backend.song.models import Artist


pytestmark = pytest.mark.django_db


class TestCategoryView:

    def test_create_category(self, auth, create_category):

        assert create_category.status_code == HTTP_201_CREATED
        assert create_category
        assert create_category.data['id']
        assert create_category.data['category_name']
        assert create_category.data['date_added']

    def load_category_list(self, create_category, get):
        response = get(reverse('song:categories-list'))

        assert response.status_code == HTTP_200_OK
        assert response.data
        assert response.data['results'][0]
        assert response.data['results'][0]['id']
        assert response.data['results'][0]['category_name']
        assert response.data['results'][0]['date_added']
        assert response.data['results'][0]['songs']

    def test_load_category_list_filtered(self, create_category, get):
        response = get(f"{reverse('song:categories-list')}?category_name=rumba")

        assert response.status_code == HTTP_200_OK
        assert response.data['results'][0]['category_name'] == 'rumba'
        assert response.data['results']

    def test_load_category_detail(self, create_category, get):
        category_id = create_category.data['id']
        response = get(reverse('song:categories-detail', args=[category_id]))

        assert response.status_code == HTTP_200_OK
        assert response.data['category_name'] == 'rumba'

    def test_create_category_with_un_authorized_credentials(self, logout, create_category):

        assert create_category.status_code == HTTP_403_FORBIDDEN

    def test_update_category_put_request(self, auth, client, category):
        response = client.put(reverse('song:categories-detail', args=[category.id]), data={'category_name': 'ndombolo'}, format='json')

        assert response.status_code == HTTP_200_OK
        assert response.data['category_name'] == 'ndombolo'

    def test_delete_category_delete_request(self, category, delete):
        response = delete(reverse('song:categories-detail', args=[category.id]))

        assert response.status_code == HTTP_204_NO_CONTENT


class TestArtistsView:
    def test_creation_of_artist(self, create_artist):

        assert create_artist.status_code == HTTP_201_CREATED
        assert create_artist.data
        assert create_artist.data['first_name'] == 'ferre'
        assert create_artist.data['last_name']
        assert create_artist.data['is_still_alive']
        assert create_artist.data['image']
        assert create_artist.data['date_of_birth']
        assert not create_artist.data['date_of_death']

    def test_load_artist_list(self, create_artist, album, song, get):
        response = get(reverse('song:artists-list'))

        assert album
        assert song

        assert response.status_code == HTTP_200_OK
        assert response.data['results'][0]['last_name'] == create_artist.data['last_name']
        assert response.data['results']
        assert response.data['results'][0]['first_name']
        assert response.data['results'][0]['is_still_alive']
        assert response.data['results'][0]['image']
        assert response.data['results'][0]['date_of_birth'] == '1976-03-03'
        assert not response.data['results'][0]['date_of_death']
        assert not response.data['results'][0]['albums']
        assert not response.data['results'][0]['songs']

    def test_update_artist_put_request(self, create_artist, update):
        artist_id = create_artist.data['id']
        response = update(reverse('song:artists-detail', args=[artist_id]), {'first_name': 'wemba'})

        assert response.status_code == HTTP_200_OK
        assert response.data['first_name'] == 'wemba'

    def test_delete_artist_delete_request(self, create_artist, delete):
        artist_id = create_artist.data['id']
        response = delete(reverse('song:artists-detail', args=[artist_id]))

        assert response.status_code == HTTP_204_NO_CONTENT


class TestAlbumsView:
    def test_creation_of_album(self, artist, create_album):

        assert create_album.status_code == HTTP_201_CREATED
        assert create_album.data['album_name'] == 'tango to zalaki'
        assert create_album.data['id']
        assert create_album.data['date_added']

    def test_load_album_list(self, create_album, song, get):
        response = get(reverse('song:albums-list'))

        assert response.status_code == HTTP_200_OK
        assert response.data['results'][0]['album_name']
        assert not response.data['results'][0]['songs']
        assert response.data['results'][0]['artist']
        assert response.data['results'][0]['date_added']

    def test_load_album_detail(self, artist, create_album, get):
        album_id = create_album.data['id']
        response = get(reverse('song:albums-detail', args=[album_id]))

        assert response.status_code == HTTP_200_OK
        assert response.data['album_name'] == 'tango to zalaki'

    def test_load_album_list_filtered(self, artist, create_album, get):
        response = get(f"{reverse('song:albums-list')}?album_name=tango+to+zalaki&artist={artist.id}")

        assert response.status_code == HTTP_200_OK
        assert response.data['results'][0]['album_name'] == 'tango to zalaki'

    def test_update_album_patch_request(self, artist, album, update):
        response = update(reverse('song:albums-detail', args=[album.id]), {'album_name': 'droit chemin'})

        assert response.status_code == HTTP_200_OK
        assert response.data['album_name'] == 'droit chemin'

    def test_delete_album_delete_request(self, artist, album, delete):
        response = delete(reverse('song:albums-detail', args=[album.id]))

        assert response.status_code == HTTP_204_NO_CONTENT


class TestSongView:
    def test_creation_of_song(self, category, artist, album, create_song):

        assert album
        assert category
        assert artist

        assert create_song.status_code == HTTP_201_CREATED
        assert create_song.data['title'] == 'maboko pamba'
        assert create_song.data['artist'] == artist.id
        assert create_song.data['album'] == album.id

    def test_loads_songs_list(self, category, artist, album, create_song, get):
        response = get(reverse('song:songs-list'))

        assert response.status_code == HTTP_200_OK
        assert response.data['results'][0]['title'] == 'maboko pamba'
        assert len(response.data['results']) == 1
        assert not response.data['results'][0]['date_published']
        assert response.data['results'][0]['date_added']
        assert not response.data['results'][0]['links']
        assert not response.data['results'][0]['lyrics']

    def test_update_songs_patch_request(self, category, artist, album, create_song, update):
        response = update(reverse('song:songs-detail', kwargs={'slug': 'maboko-pamba'}), data={'title': 'malewa'})

        assert response.status_code == HTTP_200_OK
        assert response.data['title'] == 'malewa'

    def test_delete_songs_delete_request(self, category, artist, album, create_song, delete):
        response = delete(reverse('song:songs-detail', kwargs={'slug': 'maboko-pamba'}))
        
        assert response.status_code == HTTP_204_NO_CONTENT


class TestLanguageView:
    def test_creation_of_language(self, create_language):
        
        assert create_language.status_code == HTTP_201_CREATED
        assert create_language.data['language'] == 'french'

    def test_loads_languages_list(self, create_language, get):
        response = get(reverse('song:languages-list'))

        assert response.status_code == HTTP_200_OK
        assert response.data['results'][0]['language'] == 'french'
        assert len(response.data['results']) == 1
        assert response.data['results'][0]['id']
        assert not response.data['results'][0]['translations']
        assert not response.data['results'][0]['lyric_requests']
        assert not response.data['results'][0]['lyrics']
        assert response.data['results'][0]['date_added']

    def test_load_language_detail(self, create_language, get):
        language_id = create_language.data['id']
        response = get(reverse('song:languages-detail', args=[language_id]))

        assert response.status_code == HTTP_200_OK
        assert response.data['language'] == 'french'

    def test_load_language_list_filtered(self, create_language, get):
        response = get(f"{reverse('song:languages-list')}?language=french")

        assert response.status_code == HTTP_200_OK
        assert response.data['results'][0]['language'] == 'french'

    def test_update_language_patch_request(self, language, update):
        response = update(reverse('song:languages-detail', args=[language.id]), data={'language': 'english'})

        assert response.status_code == HTTP_200_OK
        assert response.data['language'] == 'english'

    def test_delete_language_delete_request(self, language, delete):
        response = delete(reverse('song:languages-detail', args=[language.id]))
        
        assert response.status_code == HTTP_204_NO_CONTENT


class TestLyricView:
    def test_creation_of_lyric(self, auth, language, song, create_lyric):
        
        assert create_lyric.status_code == HTTP_201_CREATED
        assert create_lyric.data
        assert create_lyric.data['lyric'] == 'Lorem Ipsum is simply dummy text of the printing'

    def test_loads_lyrics_list(self, auth, user, song, language, create_lyric, get):
        response = get(reverse('song:lyrics-list'))

        assert response.status_code == HTTP_200_OK
        assert response.data['results'][0]['lyric'] == 'Lorem Ipsum is simply dummy text of the printing'
        assert response.data['results'][0]['user'] == user.id
        assert len(response.data['results']) == 1
        assert response.data['results'][0]['id']
        assert response.data['results'][0]['song'] == song.id
        assert response.data['results'][0]['language'] == language.id
        assert not response.data['results'][0]['translations']
        assert response.data['results'][0]['date_added']

    def test_update_lyrics_put_request(self, auth, user, song, language, create_lyric, update):
        lyric_id = create_lyric.data['id']
        response = update(reverse('song:lyrics-detail', args=[lyric_id]), data={'lyric': 'this is my new lyric'})

        assert response.status_code == HTTP_200_OK
        assert response.data['lyric'] == 'this is my new lyric'
        assert response.data['user'] == user.id

    def test_delete_lyrics_delete_request(self, auth, user, language, song, create_lyric, delete):
        lyric_id = create_lyric.data['id']
        response = delete(reverse('song:lyrics-detail', args=[lyric_id]))
        
        assert response.status_code == HTTP_204_NO_CONTENT


class TestLyricRequestView:
    def test_creation_of_lyric_request(self, auth, user, language, song, create_lyric_request):
        
        assert create_lyric_request.status_code == HTTP_201_CREATED
        assert create_lyric_request.data['message'] == 'I need a lyric for this song'

    def test_loads_lyric_request_list(self, auth, user, language, song, create_lyric_request, get):
        response = get(reverse('song:lyric-requests-list'))

        assert response.status_code == HTTP_200_OK
        assert response.data['results'][0]['message'] == 'I need a lyric for this song'
        assert response.data['results'][0]['user'] == user.id
        assert response.data['results'][0]['id']
        assert response.data['results'][0]['song'] == song.id
        assert response.data['results'][0]['language'] == language.id
        assert response.data['results'][0]['date_added']

    def test_update_lyric_request_patch_request(self, auth, user, language, song, create_lyric_request, update):
        lyric_request_id = create_lyric_request.data['id']
        response = update(reverse('song:lyric-requests-detail', args=[lyric_request_id]), data={'message': 'my updated message'})

        assert response.status_code == HTTP_200_OK
        assert response.data['message'] == 'my updated message'
        assert response.data['user'] == user.id

    def delete_lyric_request_delete_request(self, auth, song, language, create_lyric_request, delete):
        lyric_request_id = create_lyric_request.data['id']
        response = delete(reverse('song:lyric-requests-detail', args=[lyric_request_id]))

        assert response.status_code == HTTP_204_NO_CONTENT


class TestTranslationView:
    def  test_creation_of_translation(self, auth, user, language, lyric, create_translation):

        assert create_translation.status_code == HTTP_201_CREATED
        assert create_translation.data['translation'] == 'My translation'
        assert create_translation.data['user'] == user.id
        assert create_translation.data['lyric'] == lyric.id

    def test_loads_translation_list(self, auth, user, language, lyric, create_translation, get):
        response = get(reverse('song:translations-list'))

        assert response.status_code == HTTP_200_OK
        assert response.data['results'][0]['translation'] == 'My translation'
        assert response.data['results'][0]['lyric'] == lyric.id
        assert response.data['results'][0]['user'] == user.id
        assert response.data['results'][0]['id']
        assert response.data['results'][0]['language'] == language.id
        assert response.data['results'][0]['date_added']

    def test_update_translation_put_request(self, auth, user, lyric, language, create_translation, update):
        translation_id = create_translation.data['id']
        response = update(reverse('song:translations-detail', args=[translation_id]),\
             data={'translation': 'My new translation'})

        assert response.status_code == HTTP_200_OK
        assert response.data['translation'] == 'My new translation'
        assert response.data['user'] == user.id

    def test_delete_translation_delete_request(self, auth, lyric, language, create_translation, delete):
        translation_id = create_translation.data['id']
        response = delete(reverse('song:translations-detail', args=[translation_id]))

        assert response.status_code == HTTP_204_NO_CONTENT
