from rest_framework import serializers

from backend.song.models import (
    Category,
    Album,
    Artist,
    Song,
    SongLink,
    Language,
    Lyric,
    LyricRequest,
    Translation
)


class CategorySerializer(serializers.ModelSerializer):
    category_songs = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'category_name', 'date_added', 'category_songs']


class AlbumSerializer(serializers.ModelSerializer):
    album_songs = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Album
        fields = ['id', 'album_name', 'artist', 'date_added', 'album_songs']


class ArtistSerializer(serializers.ModelSerializer):
    albums = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    artist_songs = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Artist
        fields = [
            'id',
            'first_name',
            'last_name',
            'is_still_alive',
            'image',
            'date_of_birth',
            'date_of_death',
            'date_added',
            'albums',
            'artist_songs',
        ]


class SongSerializer(serializers.ModelSerializer):
    links = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    song_lyrics = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Song
        fields = [
            'id',
            'title',
            'category',
            'album',
            'artist',
            'date_published',
            'date_added',
            'links',
            'song_lyrics',
        ]


class SongLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = SongLink
        fields = ['id', 'provider', 'link', 'song', 'dete_added']


class LanguageSerializer(serializers.ModelSerializer):
    language_translations = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    language_lyric_requests = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    language_lyric = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Language
        fields = [
            'id',
            'language',
            'language_translations',
            'language_lyric_requests',
            'language_lyric',
            'date_added',
        ]


class LyricSerializer(serializers.ModelSerializer):
    lyric_translations = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    user = serializers.ReadOnlyField(source='user.id')

    class Meta:
        model = Lyric
        fields = ['id', 'user', 'song', 'language', 'lyric', 'lyric_translations', 'date_added']


class LyricRequestSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.id')
    class Meta:
        model = LyricRequest
        fields = ['id', 'user', 'song', 'language', 'message', 'date_added']


class TranslationSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.id')
    class Meta:
        model = Translation
        fields = ['id', 'lyric', 'user', 'language', 'translation', 'date_added']
