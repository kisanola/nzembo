import pytest

pytestmark = pytest.mark.django_db

class TestModel:
    def test_check_category_creation(self, category):

        assert category.category_name == "rumba"

    def test_check_album_creation(self, album):

        assert album.album_name == "Droit chemin"

    def test_check_artist_creation(self, artist):

        assert artist.last_name
        assert artist.first_name == "Fally"
        assert artist.is_still_alive

    def test_check_dead_artist_creation(self, dead_artist):

        assert dead_artist.last_name == "Wembadio"
        assert dead_artist.first_name
        assert not dead_artist.is_still_alive

    def test_check_song_creation(self, song):

        assert song.title == 'ca bouge pas'
        assert song.slug == 'ca-bouge-pas'
        assert song.album
        assert song.artist
        assert song.category

    def test_check_song_creation_for_dead_artist(self, song_for_dead_artist):

        assert song_for_dead_artist.slug == 'ca-ne-bouge-pas'
        assert song_for_dead_artist.category
        assert song_for_dead_artist.artist

    def test_check_songLink_creation(self, song_link):

        assert song_link.provider == 'youtube'
        assert song_link.song
        assert song_link.link != 'https://youtube.com/s?v=HG68'

    def test_check_language_creation(self, language):

        assert language.language

    def test_check_lyric_creation(self, lyric):

        assert lyric.song
        assert lyric.user
        assert lyric.lyric

    def test_check_lyric_request_creation(self, lyric_request):

        assert lyric_request.message == 'need the lyric for this song'
        assert lyric_request.user
        assert lyric_request.lyric
        assert lyric_request.language

    def test_check_translation_creation(self, translation):

        assert translation.user
        assert translation.lyric
        assert translation.translation
        assert translation.language
