from django.urls import path

from rest_framework.urlpatterns import format_suffix_patterns

from backend.song.api.views import (
    CategoriesList,
    CategoriesDetail,
    ArtistsList,
    ArtistsDetail,
    AlbumsList,
    AlbumsDetail,
    SongsList,
    SongsDetail,
    LanguagesList,
    LanguagesDetail,
    LyricsList,
    LyricsDetail,
    LyricRequestsList,
    LyricRequestsDetail,
    TranslationsList,
    TranslationsDetail
)

app_name = 'song'

urlpatterns = [
    path('categories/', CategoriesList.as_view(), name='categories-list'),
    path('categories/<int:pk>/', CategoriesDetail.as_view(), name='categories-detail'),
    path('artists/', ArtistsList.as_view(), name='artists-list'),
    path('artists/<int:pk>/', ArtistsDetail.as_view(), name='artists-detail'),
    path('albums/', AlbumsList.as_view(), name='albums-list'),
    path('albums/<int:pk>/', AlbumsDetail.as_view(), name='albums-detail'),
    path('songs/', SongsList.as_view(), name='songs-list'),
    path('songs/<int:pk>/', SongsDetail.as_view(), name='songs-detail'),
    path('languages/', LanguagesList.as_view(), name='languages-list'),
    path('languages/<int:pk>/', LanguagesDetail.as_view(), name='languages-detail'),
    path('lyrics/', LyricsList.as_view(), name='lyrics-list'),
    path('lyrics/<int:pk>/', LyricsDetail.as_view(), name='lyrics-detail'),
    path('lyric-requests/', LyricRequestsList.as_view(), name='lyric-requests-list'),
    path('lyric-requests/<int:pk>/', LyricRequestsDetail.as_view(), name='lyric-requests-detail'),
    path('translations/', TranslationsList.as_view(), name='translations-list'),
    path('translations/<int:pk>/', TranslationsDetail.as_view(), name='translations-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
