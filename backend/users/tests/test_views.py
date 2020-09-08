import pytest

from rest_framework.status import HTTP_200_OK

from backend.users.views import UserRedirectView, UserUpdateView
from backend.users.api.views import UserTranslationsView, UserLyricRequestView, UserLyricsView


pytestmark = pytest.mark.django_db


class TestUserUpdateView:
    """
    TODO:
        extracting view initialization code as class-scoped fixture
        would be great if only pytest-django supported non-function-scoped
        fixture db access -- this is a work-in-progress for now:
        https://github.com/pytest-dev/pytest-django/pull/258
    """

    def test_get_success_url(self, user, request_factory):
        view = UserUpdateView()
        request = request_factory.get("/fake-url/")
        request.user = user

        view.request = request

        assert view.get_success_url() == f"/users/{user.username}/"

    def test_get_object(self, user, request_factory):
        view = UserUpdateView()
        request = request_factory.get("/fake-url/")
        request.user = user

        view.request = request

        assert view.get_object() == user


class TestUserRedirectView:
    def test_get_redirect_url(self, user, request_factory):
        view = UserRedirectView()
        request = request_factory.get("/fake-url")
        request.user = user

        view.request = request

        assert view.get_redirect_url() == f"/users/{user.username}/"


class TestUserActivities:
    def test_get_user_translations(self, translation, user, get):
        response = get("users_api:translation-list", UserTranslationsView.as_view({'get': 'list'}))

        assert translation
        assert response.status_code == HTTP_200_OK
        assert response.data["results"]
        assert response.data["results"][0]["user"] == user.id

    def test_get_user_lyrics(self, lyric, user, get):
        response = get("users_api:translation-list", UserLyricsView.as_view({"get": "list"}))

        assert lyric
        assert response.status_code == HTTP_200_OK
        assert response.data["results"]
        assert response.data["results"][0]["user"] == user.id

    def test_get_user_lyricRequests(self, lyric_request, user, get):
        response = get("users_api:translation-list", UserLyricRequestView.as_view({"get": "list"}))

        assert lyric_request
        assert response.status_code == HTTP_200_OK
        assert response.data["results"]
        assert response.data["results"][0]["user"] == user.id

    def test_try_to_get_non_belonging_translations(self, diff_translation, get):
        response = get("users_api:translation-list", UserTranslationsView.as_view({'get': 'list'}))

        assert diff_translation
        assert response.status_code == HTTP_200_OK
        assert not response.data["results"]
