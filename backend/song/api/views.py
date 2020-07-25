from rest_framework import generics

from backend.song import models
from backend.song.permissions import IsOwnerOrReadOnly
from backend.song.api import serializers


class CategoriesList(generics.ListCreateAPIView):

    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer
    filterset_fields = ['category_name',]


class CategoryList(generics.RetrieveUpdateDestroyAPIView):

    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer


class ArtistsList(generics.ListCreateAPIView):

    queryset = models.Artist.objects.all()
    serializer_class = serializers.ArtistSerializer
    filterset_fields = ['first_name', 'last_name', 'is_still_alive',]


class ArtistList(generics.RetrieveUpdateDestroyAPIView):

    queryset = models.Artist.objects.all()
    serializer_class = serializers.ArtistSerializer


class AlbumsList(generics.ListCreateAPIView):

    queryset = models.Album.objects.all()
    serializer_class = serializers.AlbumSerializer
    filterset_fields = ['album_name', 'artist',]


class AlbumList(generics.RetrieveUpdateDestroyAPIView):

    queryset = models.Album.objects.all()
    serializer_class = serializers.AlbumSerializer


class SongsList(generics.ListCreateAPIView):

    queryset = models.Song.objects.all()
    serializer_class = serializers.SongSerializer
    filterset_fields = ['title', 'category', 'album', 'artist',]


class SongList(generics.RetrieveUpdateDestroyAPIView):

    queryset = models.Song.objects.all()
    serializer_class = serializers.SongSerializer


class LanguagesList(generics.ListCreateAPIView):

    queryset = models.Language.objects.all()
    serializer_class = serializers.LanguageSerializer
    filterset_fields = ['language',]


class LanguageList(generics.RetrieveUpdateDestroyAPIView):

    queryset = models.Language.objects.all()
    serializer_class = serializers.LanguageSerializer


class LyricsList(generics.ListCreateAPIView):

    queryset = models.Lyric.objects.all()
    serializer_class = serializers.LyricSerializer
    filterset_fields = ['user', 'song', 'language',]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class LyricList(generics.RetrieveUpdateDestroyAPIView):

    queryset = models.Lyric.objects.all()
    serializer_class = serializers.LyricSerializer
    permission_classes = [IsOwnerOrReadOnly]


class LyricRequestsList(generics.ListCreateAPIView):

    queryset = models.LyricRequest.objects.all()
    serializer_class = serializers.LyricRequestSerializer
    filterset_fields = ['user', 'language',]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class LyricRequestList(generics.RetrieveUpdateDestroyAPIView):

    queryset = models.LyricRequest.objects.all()
    serializer_class = serializers.LyricRequestSerializer
    permission_classes = [IsOwnerOrReadOnly]


class TranslationsList(generics.ListCreateAPIView):

    queryset = models.Translation.objects.all()
    serializer_class = serializers.TranslationSerializer
    filterset_fields = ['lyric', 'user', 'language',]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TranslationList(generics.RetrieveUpdateDestroyAPIView):

    queryset = models.Translation.objects.all()
    serializer_class = serializers.TranslationSerializer
    permission_classes = [IsOwnerOrReadOnly]
