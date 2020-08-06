from rest_framework import generics

from backend.song.models import (
    Category,
    Artist,
    Album,
    Song,
    Language,
    Lyric,
    LyricRequest,
    Translation
)
from backend.song.permissions import IsOwnerOrReadOnly
from backend.song.api.serializers import (
    CategorySerializer,
    AlbumSerializer,
    LanguageSerializer,
    LyricSerializer,
    ArtistSerializer,
    LyricRequestSerializer,
    SongSerializer,
    TranslationSerializer
)


class CategoriesList(generics.ListCreateAPIView):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filterset_fields = ['category_name',]


class CategoryList(generics.RetrieveUpdateDestroyAPIView):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ArtistsList(generics.ListCreateAPIView):

    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    filterset_fields = ['first_name', 'last_name', 'is_still_alive',]


class ArtistList(generics.RetrieveUpdateDestroyAPIView):

    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer


class AlbumsList(generics.ListCreateAPIView):

    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    filterset_fields = ['album_name', 'artist',]


class AlbumList(generics.RetrieveUpdateDestroyAPIView):

    queryset = Album.objects.all()
    serializer_class = AlbumSerializer


class SongsList(generics.ListCreateAPIView):

    queryset = Song.objects.all()
    serializer_class = SongSerializer
    filterset_fields = ['title', 'category', 'album', 'artist',]


class SongList(generics.RetrieveUpdateDestroyAPIView):

    queryset = Song.objects.all()
    serializer_class = SongSerializer


class LanguagesList(generics.ListCreateAPIView):

    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
    filterset_fields = ['language',]


class LanguageList(generics.RetrieveUpdateDestroyAPIView):

    queryset = Language.objects.all()
    serializer_class = LanguageSerializer


class LyricsList(generics.ListCreateAPIView):

    queryset = Lyric.objects.all()
    serializer_class = LyricSerializer
    filterset_fields = ['user', 'song', 'language',]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class LyricList(generics.RetrieveUpdateDestroyAPIView):

    queryset = Lyric.objects.all()
    serializer_class = LyricSerializer
    permission_classes = [IsOwnerOrReadOnly]


class LyricRequestsList(generics.ListCreateAPIView):

    queryset = LyricRequest.objects.all()
    serializer_class = LyricRequestSerializer
    filterset_fields = ['user', 'language',]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class LyricRequestList(generics.RetrieveUpdateDestroyAPIView):

    queryset = LyricRequest.objects.all()
    serializer_class = LyricRequestSerializer
    permission_classes = [IsOwnerOrReadOnly]


class TranslationsList(generics.ListCreateAPIView):

    queryset = Translation.objects.all()
    serializer_class = TranslationSerializer
    filterset_fields = ['lyric', 'user', 'language',]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TranslationList(generics.RetrieveUpdateDestroyAPIView):

    queryset = Translation.objects.all()
    serializer_class = TranslationSerializer
    permission_classes = [IsOwnerOrReadOnly]
