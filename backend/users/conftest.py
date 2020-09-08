import pytest

from rest_framework.test import APIRequestFactory, force_authenticate

from django.test import RequestFactory
from django.urls import reverse

from backend.users.models import User
from backend.users.tests.factories import UserFactory

from backend.song.tests.factories import (
    TranslationFactory,
    LyricFactory,
    LyricRequestFactory
)

@pytest.fixture(autouse=True)
def media_storage(settings, tmpdir):
    settings.MEDIA_ROOT = tmpdir.strpath


@pytest.fixture
def user() -> User:
    return UserFactory()


@pytest.fixture
def request_factory() -> RequestFactory:
    return RequestFactory()


@pytest.fixture()
def api_request_factory() -> APIRequestFactory:
    return APIRequestFactory()


@pytest.fixture
def translation(user) -> TranslationFactory:
    return TranslationFactory(user=user)


@pytest.fixture
def diff_translation() -> TranslationFactory:
    return TranslationFactory(user=UserFactory())


@pytest.fixture
def lyric(user) -> LyricFactory:
    return LyricFactory(user=user)


@pytest.fixture
def lyric_request(user) -> LyricRequestFactory:
    return LyricRequestFactory(user=user)


@pytest.fixture
def get(user, api_request_factory):
    def generic_get_request(url, view):
        request = api_request_factory.get(reverse(url, kwargs={"username": user.username}))
        force_authenticate(request, user=user)

        return view(request)

    return generic_get_request
