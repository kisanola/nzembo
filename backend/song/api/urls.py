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
    path('categories/', CategoriesList.as_view()),
    path('categories/<int:pk>/', CategoriesDetail.as_view()),
    path('artists/', ArtistsList.as_view()),
    path('artists/<int:pk>/', ArtistsDetail.as_view()),
    path('albums/', AlbumsList.as_view()),
    path('albums/<int:pk>/', AlbumsDetail.as_view()),
    path('songs/', SongsList.as_view()),
    path('songs/<int:pk>/', SongsDetail.as_view()),
    path('languages/', LanguagesList.as_view()),
    path('languages/<int:pk>/', LanguagesDetail.as_view()),
    path('lyrics/', LyricsList.as_view()),
    path('lyrics/<int:pk>/', LyricsDetail.as_view()),
    path('lyric-requests/', LyricRequestsList.as_view()),
    path('lyric-requests/<int:pk>/', LyricRequestsDetail.as_view()),
    path('translations/', TranslationsList.as_view()),
    path('translations/<int:pk>/', TranslationsDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
