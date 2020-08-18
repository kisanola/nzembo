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
    songs = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='song:songs-detail',
        lookup_field='slug'
    )

    class Meta:
        model = Category
        fields = ['id', 'category_name', 'date_added', 'songs']
        lookup_field = 'slug'
        extra_kwargs = {
            'songs': {'lookup_field': 'slug'}
        }


class AlbumSerializer(serializers.ModelSerializer):
    songs = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='song:songs-detail',
        lookup_field='slug'
    )

    class Meta:
        model = Album
        fields = ['id', 'album_name', 'artist', 'date_added', 'songs']


class ArtistSerializer(serializers.ModelSerializer):
    albums = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='song:albums-detail'
    )
    songs = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='song:songs-detail',
        lookup_field='slug'
    )

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
            'songs',
        ]


class SongSerializer(serializers.ModelSerializer):
    links = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    lyrics = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='song:lyrics-detail'
    )

    class Meta:
        model = Song
        fields = [
            'slug',
            'title',
            'category',
            'album',
            'artist',
            'date_published',
            'date_added',
            'links',
            'lyrics',
        ]


class SongLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = SongLink
        fields = ['id', 'provider', 'link', 'song', 'date_added']


class LanguageSerializer(serializers.ModelSerializer):
    translations = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='song:translations-detail'
    )
    lyric_requests = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='song:lyric-requests-detail'
    )
    lyrics = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='song:lyrics-detail'
    )

    class Meta:
        model = Language
        fields = [
            'id',
            'language',
            'translations',
            'lyric_requests',
            'lyrics',
            'date_added',
        ]


class LyricSerializer(serializers.ModelSerializer):
    translations = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='song:translations-detail'
    )
    user = serializers.ReadOnlyField(source='user.id')

    class Meta:
        model = Lyric
        fields = ['id', 'user', 'song', 'language', 'lyric', 'translations', 'date_added']


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
