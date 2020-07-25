from django.urls import path

from rest_framework.urlpatterns import format_suffix_patterns

from backend.song.api import views
app_name = 'song'

urlpatterns = [
    path('categories/', views.CategoriesList.as_view()),
    path('categories/<int:pk>/', views.CategoryList.as_view()),
    path('artists/', views.ArtistsList.as_view()),
    path('artists/<int:pk>/', views.ArtistList.as_view()),
    path('albums/', views.AlbumsList.as_view()),
    path('albums/<int:pk>/', views.AlbumList.as_view()),
    path('songs/', views.SongsList.as_view()),
    path('songs/<int:pk>/', views.SongList.as_view()),
    path('languages/', views.LanguagesList.as_view()),
    path('languages/<int:pk>/', views.LanguageList.as_view()),
    path('lyrics/', views.LyricsList.as_view()),
    path('lyrics/<int:pk>/', views.LyricList.as_view()),
    path('lyric-requests/', views.LyricRequestsList.as_view()),
    path('lyric-requests/<int:pk>/', views.LyricRequestList.as_view()),
    path('translations/', views.TranslationsList.as_view()),
    path('translations/<int:pk>/', views.TranslationList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
