from rest_framework import status
from rest_framework.test import APITestCase
from  rest_framework.reverse import reverse

from backend.users.models import User

from backend.song import models


class BaseTestSetUp(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="test",
            email="test@nzembo.msc",
            name="test user",
            password="strongP@sswor2"
        )

        self.authenticate()

        self.artistInfo = {
            'first_name': 'Jules',
            'last_name': 'Shungu',
            'is_still_alive': False,
            'image': 'https://lastfm.freetls.fastly.net/i/u/arO/7de29a9d31b55e3ee367cecf152c0052'
        }
        self.artist = models.Artist.objects.create(**self.artistInfo)

        self.albumInfo = {
            'album_name': 'tango to zalaki',
            'artist': self.artist.id
        }

        self.language = {
            'language': 'french'
        }

        self.song = {
            'title': 'maboko pamba',
            'category': 1,
            'album': 1,
            'artist': self.artist.id
        }

        self.lyric = {
            'lyric': "What is Lorem Ipsum Lorem Ipsum is simply dummy text of the printing",
            'song': 1,
            'language': 1
        }

        self.lyric_request = {
            'song': 1,
            'language': 1,
            'message': "I need a lyric for this song"
        }

        self.translation = {
            'lyric': 1,
            'language': 1,
            'translation': "My translation"
        }

    def authenticate(self):
        self.client.force_authenticate(user=self.user)

    def logout(self):
        self.client.logout()

    def send_a_single_category_post_request(self):
        return self.client.post('/api/v1/categories/', data={'category_name': 'rumba'}, format='json')

    def send_a_single_album_post_request(self):
        return self.client.post('/api/v1/albums/', data=self.albumInfo, format='json')

    def send_a_single_language_post_request(self):
        return self.client.post('/api/v1/languages/', data=self.language, format='json')

    def send_a_single_song_post_request(self):
        return self.client.post('/api/v1/songs/', data=self.song, format='json')

    def send_a_single_lyrirc_post_request(self):
        return self.client.post('/api/v1/lyrics/', data=self.lyric, format='json')

    def send_a_single_lyric_request_post_request(self):
        return self.client.post('/api/v1/lyric-requests/', data=self.lyric_request, format='json')

    def send_a_single_translation_post_request(self):
        return self.client.post('/api/v1/translations/', data=self.translation, format='json')

    def generic_get_request(self, url):
        return self.client.get(url)

    def generic_delete_test(self, **kwords):
        self.client.post(kwords['post_url'], data=kwords['post_data'], format='json')
        response = self.client.delete(kwords['delete_url'])

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def generic_post_test(self, **kwords):
        response = self.client.post(kwords['post_url'], data=kwords['post_data'], format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data[kwords['test_field']], kwords['expected_value'])


class CategoryTestCase(BaseTestSetUp):

    def test_create_category(self):
        self.generic_post_test(
            post_url='/api/v1/categories/',
            post_data={'category_name': 'rumba'},
            test_field='category_name',
            expected_value='rumba'
        )

    def test_load_category_list(self):
        self.send_a_single_category_post_request()
        response = self.generic_get_request('/api/v1/categories/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsNotNone(response.data)
        self.assertNotEqual(response.data['results'], [])

    def test_load_category_list_filtered(self):
        self.send_a_single_category_post_request()
        response = self.generic_get_request('/api/v1/categories/?category_name=rumba')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['results'][0]['category_name'], 'rumba')
        self.assertNotEqual(response.data['results'], [])

    def test_load_category_detail(self):
        self.send_a_single_category_post_request()
        response = self.generic_get_request('/api/v1/categories/1/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['category_name'], 'rumba')

    def test_create_category_with_un_authorized_credentials(self):
        self.logout()
        response = self.send_a_single_category_post_request()
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_category_put_request(self):
        self.send_a_single_category_post_request()
        response = self.client.put('/api/v1/categories/1/', data={'category_name': 'ndombolo'}, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['category_name'], 'ndombolo')

    def test_delete_category_delete_request(self):
        self.generic_delete_test(
            post_url='/api/v1/categories/',
            post_data={'category_name': 'rumba'},
            delete_url='/api/v1/categories/1/'
        )


class ArtistsTestCase(BaseTestSetUp):
    def test_creation_of_artist(self):
        self.generic_post_test(
            post_url='/api/v1/artists/',
            post_data=self.artistInfo,
            test_field='last_name',
            expected_value=self.artistInfo['last_name']
        )

    def test_loads_artist_list(self):
        response = self.generic_get_request('/api/v1/artists/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['results'][0]['last_name'], self.artistInfo['last_name'])
        self.assertEqual(len(response.data['results']), 1)

    def test_update_artist_put_request(self):
        self.artistInfo['first_name'] = 'wemba'
        response = self.client.put('/api/v1/artists/1/', data=self.artistInfo, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['first_name'], 'wemba')

    def test_delete_artist_delete_request(self):
        self.generic_delete_test(
            post_url='/api/v1/artists/',
            post_data=self.artistInfo,
            delete_url='/api/v1/artists/1/'
        )


class AlbumsTestCase(BaseTestSetUp):
    def test_creation_of_album(self):
        self.generic_post_test(
            post_url='/api/v1/albums/',
            post_data=self.albumInfo,
            test_field='album_name',
            expected_value='tango to zalaki'
        )

    def test_load_album_list(self):
        self.send_a_single_album_post_request()
        response = self.generic_get_request('/api/v1/albums/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['results'][0]['album_name'], 'tango to zalaki')

    def test_load_album_detail(self):
        self.send_a_single_album_post_request()
        response = self.generic_get_request('/api/v1/albums/1/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['album_name'], 'tango to zalaki')

    def test_load_album_list_filtered(self):
        self.send_a_single_album_post_request()
        response = self.generic_get_request('/api/v1/albums/?album_name=tango+to+zalaki&artist=1')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['results'][0]['album_name'], 'tango to zalaki')

    def test_update_album_patch_request(self):
        self.send_a_single_album_post_request()
        response = self.client.patch('/api/v1/albums/1/', data={'album_name': 'droit chemin'}, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['album_name'], 'droit chemin')

    def test_delete_album_delete_request(self):
        self.generic_delete_test(
            post_url='/api/v1/albums/',
            post_data=self.albumInfo,
            delete_url='/api/v1/albums/1/'
        )

class SongTestCase(BaseTestSetUp):
    def __song_request_helper(self):
        self.send_a_single_category_post_request()
        self.send_a_single_album_post_request()

    def test_creation_of_song(self):
        self.__song_request_helper()
        self.generic_post_test(
            post_url='/api/v1/songs/',
            post_data=self.song,
            test_field='title',
            expected_value='maboko pamba'
        )

    def test_loads_songs_list(self):
        self.__song_request_helper()
        self.send_a_single_song_post_request()
        response = self.generic_get_request('/api/v1/songs/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['results'][0]['title'], self.song['title'])
        self.assertEqual(len(response.data['results']), 1)

    def test_update_songs_patch_request(self):
        self.__song_request_helper()
        self.song['title'] = 'malewa'
        self.send_a_single_song_post_request()
        response = self.client.put('/api/v1/songs/1/', data=self.song, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'malewa')

    def test_delete_songs_delete_request(self):
        self.__song_request_helper()
        self.generic_delete_test(
            post_url='/api/v1/songs/',
            post_data=self.song,
            delete_url='/api/v1/songs/1/'
        )


class LanguageTestCase(BaseTestSetUp):
    def test_creation_of_language(self):
        self.generic_post_test(
            post_url='/api/v1/languages/',
            post_data={'language': 'french'},
            test_field='language',
            expected_value='french'
        )

    def test_loads_languages_list(self):
        self.send_a_single_language_post_request()
        response = self.generic_get_request('/api/v1/languages/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['results'][0]['language'], self.language['language'])
        self.assertEqual(len(response.data['results']), 1)

    def test_load_album_detail(self):
        self.send_a_single_language_post_request()
        response = self.generic_get_request('/api/v1/languages/1/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['language'], 'french')

    def test_load_album_list_filtered(self):
        self.send_a_single_language_post_request()
        response = self.generic_get_request('/api/v1/languages/?language=french')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['results'][0]['language'], 'french')

    def test_update_language_patch_request(self):
        self.send_a_single_language_post_request()
        self.language['language'] = 'english'
        response = self.client.put('/api/v1/languages/1/', data=self.language, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['language'], 'english')

    def test_delete_language_delete_request(self):
        self.generic_delete_test(
            post_url='/api/v1/languages/',
            post_data=self.language,
            delete_url='/api/v1/languages/1/'
        )


class LyricTestCase(BaseTestSetUp):
    def __lyric_request_helper(self):
        self.send_a_single_category_post_request()
        self.send_a_single_album_post_request()
        self.send_a_single_language_post_request()
        self.send_a_single_song_post_request()

    def test_creation_of_lyric(self):
        self.__lyric_request_helper()
        self.generic_post_test(
            post_url='/api/v1/lyrics/',
            post_data=self.lyric,
            test_field='lyric',
            expected_value=self.lyric['lyric']
        )

    def test_loads_lyrics_list(self):
        self.__lyric_request_helper()
        self.send_a_single_lyrirc_post_request()
        response = self.generic_get_request('/api/v1/lyrics/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['results'][0]['lyric'], self.lyric['lyric'])
        self.assertEqual(response.data['results'][0]['user'], self.user.id)
        self.assertEqual(len(response.data['results']), 1)

    def test_update_lyrics_put_request(self):
        self.__lyric_request_helper()
        self.send_a_single_lyrirc_post_request()
        self.lyric['lyric'] = 'this is my new lyric'
        response = self.client.put('/api/v1/lyrics/1/', data=self.lyric, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['lyric'], 'this is my new lyric')

    def test_delete_lyrics_delete_request(self):
        self.__lyric_request_helper()
        self.generic_delete_test(
            post_url='/api/v1/lyrics/',
            post_data=self.lyric,
            delete_url='/api/v1/lyrics/1/'
        )


class LyricRequestTestCase(BaseTestSetUp):
    def __lyric_request_request_helper(self):
        self.send_a_single_album_post_request()
        self.send_a_single_category_post_request()
        self.send_a_single_language_post_request()
        self.send_a_single_song_post_request()

    def  test_creation_of_lyric(self):
        self.__lyric_request_request_helper()
        self.generic_post_test(
            post_url='/api/v1/lyric-requests/',
            post_data=self.lyric_request,
            test_field='message',
            expected_value=self.lyric_request['message']
        )

    def test_loads_lyric_request_list(self):
        self.__lyric_request_request_helper()
        self.send_a_single_lyric_request_post_request()
        response = self.generic_get_request('/api/v1/lyric-requests/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['results'][0]['message'], self.lyric_request['message'])
        self.assertEqual(response.data['results'][0]['user'], self.user.id)

    def test_update_lyric_request_patch_request(self):
        self.__lyric_request_request_helper()
        self.send_a_single_lyric_request_post_request()
        self.lyric_request['message'] = 'my updated message'
        response = self.client.put('/api/v1/lyric-requests/1/', data=self.lyric_request, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['message'], 'my updated message')
        self.assertEqual(response.data['user'], self.user.id)

    def delete_lyric_request_delete_request(self):
        self.__lyric_request_request_helper()
        self.generic_delete_test(
            post_url='/api/v1/lyric-requests/',
            post_data=self.lyric_request,
            delete_url='/api/v1/lyric-requests/1/'
        )


class TranslationTestCase(BaseTestSetUp):
    def __translation_request_helper(self):
        self.send_a_single_album_post_request()
        self.send_a_single_category_post_request()
        self.send_a_single_language_post_request()
        self.send_a_single_song_post_request()
        self.send_a_single_lyrirc_post_request()

    def  test_creation_of_translation(self):
        self.__translation_request_helper()
        self.generic_post_test(
            post_url='/api/v1/translations/',
            post_data=self.translation,
            test_field='translation',
            expected_value=self.translation['translation']
        )

    def test_loads_translation_list(self):
        self.__translation_request_helper()
        self.send_a_single_translation_post_request()
        response = self.generic_get_request('/api/v1/translations/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['results'][0]['translation'], self.translation['translation'])
        self.assertEqual(response.data['results'][0]['lyric'], 1)

    def update_translation_put_request(self):
        self.__translation_request_helper()
        self.send_a_single_translation_post_request()
        self.translation['translation'] = 'My new translation'
        response = self.client.put('/api/v1/translations/1/', data=self.translation, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['translation'], 'My new translation')
        self.assertEqual(response.data['user'], self.user.id)

    def test_delete_translation_delete_request(self):
        self.__translation_request_helper()
        self.generic_delete_test(
            post_url='/api/v1/translations/',
            post_data=self.translation,
            delete_url='/api/v1/translations/1/'
        )
