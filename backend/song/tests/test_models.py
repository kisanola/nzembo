import pytest

from backend.song.models import (
    Category,
    Artist,
    Album,
    Lyric,
    LyricRequest,
    Song,
    SongLink,
    Language,
    Translation
)

pytestmark = pytest.mark.django_db

class TestModel:
    def test_check_category_creation(self, category):

        assert category.category_name == "religious"
        assert isinstance(category, (Category))

    def test_check_album_creation(self, album):

        assert album.album_name == "Droit chemin"
        assert isinstance(album, (Album))

    def test_check_artist_creation(self, artist):

        assert artist.last_name
        assert artist.first_name == "Fally"
        assert artist.is_still_alive
        assert isinstance(artist, (Artist))

    def test_check_dead_artist_creation(self, dead_artist):

        assert dead_artist.last_name == "Wembadio"
        assert dead_artist.first_name
        assert not dead_artist.is_still_alive
        assert isinstance(dead_artist, (Artist))

    def test_check_song_creation(self, song):

        assert song.title == 'ca bouge pas'
        assert song.slug == 'ca-bouge-pas'
        assert song.album
        assert song.artist
        assert song.category
        assert isinstance(song, (Song))

    def test_check_song_creation_for_dead_artist(self, song_for_dead_artist):

        assert song_for_dead_artist.category
        assert song_for_dead_artist.artist
        assert not song_for_dead_artist.artist.is_still_alive
        assert isinstance(song_for_dead_artist, (Song))

    def test_check_songLink_creation(self, song_link):

        assert song_link.provider == 'youtube'
        assert song_link.song
        assert song_link.link != 'https://youtube.com/s?v=HG68'
        assert isinstance(song_link, (SongLink))

    def test_check_language_creation(self, language):

        assert language.language
        assert isinstance(language, (Language))

    def test_check_lyric_creation(self, lyric):

        assert lyric.song
        assert lyric.user
        assert lyric.lyric
        assert isinstance(lyric, (Lyric))

    def test_check_lyric_request_creation(self, lyric_request):

        assert lyric_request.message == 'I need the lyric for this song'
        assert lyric_request.user
        assert lyric_request.song
        assert lyric_request.language
        assert isinstance(lyric_request, (LyricRequest))

    def test_check_translation_creation(self, translation):

        assert translation.user
        assert translation.lyric
        assert translation.translation
        assert translation.language
        assert isinstance(translation, (Translation))
