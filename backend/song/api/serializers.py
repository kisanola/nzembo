from rest_framework import serializers

from backend.song.models import(
    Category,
    Album,
    Artist,
    Song,
    SongLink,
    Language,
    Lyric
)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'category_name', 'date_added']


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ['id', 'album_name', 'date_added']


class ArtistSerializer(serializers.ModelSerializer):
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
            'date_added'
        ]


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = [
            'id',
            'title',
            'category',
            'album',
            'artist',
            'date_published',
            'slug',
            'date_added'
        ]


class SongLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = SongLink
        fields = ['id', 'provider', 'link', 'song', 'dete_added']


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ['id', 'language', 'date_added']


class LyricSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lyric
        fields = ['id', 'user', 'song', 'language', 'content', 'date_added']
