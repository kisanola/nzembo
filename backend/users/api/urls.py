from django.urls import path

from backend.users.api.views import (
    UserTranslationsView,
    UserLyricsView,
    UserLyricRequestView
)

app_name = "users"

urlpatterns = [
    path(
        "<str:username>/translations/",
        view=UserTranslationsView.as_view({'get': 'list'}),
        name="translation-list"
    ),
    path(
        "<str:username>/lyrics/",
        view=UserLyricsView.as_view({'get': 'list'}),
        name="lyric-list"
    ),
    path(
        "<str:username>/lyric-requests/",
        view=UserLyricRequestView.as_view({'get': 'list'}),
        name="lyric-request-list"
    )
]